#!/usr/bin/env python3
import json
import hashlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API_BASE = "http://localhost:3002"
OUT_DIR = Path(__file__).resolve().parents[1] / "apple-developer-docs-md"
POLL_SECONDS = 30

TARGETS = [
    {
        "name": "coremotion",
        "label": "Core Motion",
        "url": "https://developer.apple.com/documentation/coremotion",
        "include": r"^https://developer\.apple\.com/documentation/coremotion(?:/.*)?$",
    },
    {
        "name": "sensorkit",
        "label": "SensorKit",
        "url": "https://developer.apple.com/documentation/sensorkit",
        "include": r"^https://developer\.apple\.com/documentation/sensorkit(?:/.*)?$",
    },
    {
        "name": "createml",
        "label": "Create ML",
        "url": "https://developer.apple.com/documentation/createml",
        "include": r"^https://developer\.apple\.com/documentation/createml(?:/.*)?$",
    },
]


def request_json(method, url, payload=None, timeout=90, retries=4):
    body = None
    headers = {"Content-Type": "application/json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")

    last_error = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as response:
                raw = response.read()
            if not raw:
                return {}
            return json.loads(raw.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"HTTP {exc.code} {url}: {raw[:1000]}")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = exc

        if attempt < retries:
            time.sleep(min(2 * attempt, 10))

    raise last_error


def yaml_scalar(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def sanitize_segment(segment):
    segment = urllib.parse.unquote(segment)
    segment = re.sub(r"[^A-Za-z0-9._-]+", "-", segment).strip("-")
    return segment or "index"


def page_path(section_name, source_url):
    url_hash = hashlib.sha1(source_url.encode("utf-8")).hexdigest()[:10]
    parsed = urllib.parse.urlparse(source_url)
    parts = [part for part in parsed.path.split("/") if part]
    prefix = ["documentation", section_name]
    if parts[:2] == prefix:
        parts = parts[2:]

    if not parts:
        return OUT_DIR / section_name / "index.md"

    safe_parts = [sanitize_segment(part) for part in parts]
    safe_parts[-1] = f"{safe_parts[-1]}--{url_hash}"
    return OUT_DIR / section_name / Path(*safe_parts[:-1], f"{safe_parts[-1]}.md")


def doc_key(doc):
    metadata = doc.get("metadata") or {}
    return metadata.get("sourceURL") or metadata.get("url") or ""


def write_markdown(section, doc):
    metadata = doc.get("metadata") or {}
    source_url = doc_key(doc)
    markdown = doc.get("markdown") or ""
    if not source_url or not markdown.strip():
        return None

    title = metadata.get("title")
    if isinstance(title, list):
        title = " | ".join(str(item) for item in title)

    path = page_path(section["name"], source_url)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(
        [
            "---",
            f"title: {yaml_scalar(title)}",
            f"source_url: {yaml_scalar(source_url)}",
            f"section: {yaml_scalar(section['label'])}",
            f"scraped_at: {yaml_scalar(datetime.now(timezone.utc).isoformat())}",
            "---",
            "",
            markdown.rstrip(),
            "",
        ]
    )
    path.write_text(content, encoding="utf-8")
    return path


def append_jsonl(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def fetch_status_pages(status_url):
    seen_next = set()
    next_url = status_url
    while next_url:
        if next_url.startswith("/"):
            next_url = API_BASE + next_url
        if next_url in seen_next:
            break
        seen_next.add(next_url)
        status = request_json("GET", next_url, timeout=120)
        yield status
        next_url = status.get("next")


def collect_status(status_url):
    merged = {"data": []}
    for page in fetch_status_pages(status_url):
        merged.update({k: v for k, v in page.items() if k != "data"})
        merged["data"].extend(page.get("data") or [])
    return merged


def start_crawl(section):
    payload = {
        "url": section["url"],
        "includePaths": [section["include"]],
        "regexOnFullURL": True,
        "ignoreQueryParameters": True,
        "limit": 10000,
        "maxConcurrency": 2,
        "sitemap": "include",
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True,
            "removeBase64Images": True,
            "waitFor": 1200,
            "timeout": 60000,
        },
    }
    response = request_json("POST", f"{API_BASE}/v2/crawl", payload=payload, timeout=120)
    if not response.get("success"):
        raise RuntimeError(f"Failed to start crawl for {section['name']}: {response}")
    return response["id"], response["url"]


def scrape_url(url, timeout_ms=180000):
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,
        "removeBase64Images": True,
        "waitFor": 2000,
        "timeout": timeout_ms,
    }
    response = request_json("POST", f"{API_BASE}/v2/scrape", payload=payload, timeout=(timeout_ms / 1000) + 30)
    if not response.get("success"):
        raise RuntimeError(f"Scrape failed for {url}: {response}")
    return response["data"]


def crawl_section(section):
    section_dir = OUT_DIR / section["name"]
    section_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = section_dir / "_manifest.jsonl"
    failures_path = section_dir / "_failures.jsonl"
    summary_path = section_dir / "_summary.json"

    crawl_id, status_url = start_crawl(section)
    print(f"[{section['name']}] started crawl_id={crawl_id}", flush=True)

    saved = {}
    last_completed = -1
    started_at = datetime.now(timezone.utc).isoformat()

    while True:
        status = collect_status(status_url)
        docs = status.get("data") or []

        for doc in docs:
            source_url = doc_key(doc)
            if not source_url or source_url in saved:
                continue
            written_path = write_markdown(section, doc)
            metadata = doc.get("metadata") or {}
            if written_path is None:
                append_jsonl(
                    failures_path,
                    {
                        "crawl_id": crawl_id,
                        "source_url": source_url,
                        "status_code": metadata.get("statusCode"),
                        "error": metadata.get("error") or doc.get("error") or "empty markdown",
                    },
                )
                continue
            saved[source_url] = str(written_path.relative_to(OUT_DIR))
            append_jsonl(
                manifest_path,
                {
                    "crawl_id": crawl_id,
                    "source_url": source_url,
                    "file": saved[source_url],
                    "title": metadata.get("title"),
                    "status_code": metadata.get("statusCode"),
                },
            )

        completed = status.get("completed", 0)
        total = status.get("total", 0)
        crawl_status = status.get("status")
        if completed != last_completed or crawl_status != "scraping":
            print(
                f"[{section['name']}] status={crawl_status} completed={completed}/{total} saved={len(saved)}",
                flush=True,
            )
            last_completed = completed

        summary = {
            "section": section["label"],
            "root_url": section["url"],
            "crawl_id": crawl_id,
            "status": crawl_status,
            "total": total,
            "completed": completed,
            "saved_markdown_files": len(saved),
            "started_at": started_at,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        if crawl_status in {"completed", "failed", "cancelled"}:
            try:
                errors = request_json("GET", f"{API_BASE}/v2/crawl/{crawl_id}/errors", timeout=120)
                (section_dir / "_errors.json").write_text(
                    json.dumps(errors, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
            except Exception as exc:
                append_jsonl(failures_path, {"crawl_id": crawl_id, "error": f"failed to fetch crawl errors: {exc}"})

            if crawl_status != "completed":
                raise RuntimeError(f"Crawl did not complete for {section['name']}: {summary}")
            return summary

        time.sleep(POLL_SECONDS)


def clean_export_files(section_dir):
    for markdown_file in section_dir.rglob("*.md"):
        markdown_file.unlink()
    for generated_file in [
        section_dir / "_manifest.jsonl",
        section_dir / "_failures.jsonl",
    ]:
        if generated_file.exists():
            generated_file.unlink()


def reexport_from_summary():
    root_summary_path = OUT_DIR / "_summary.json"
    root_summary = json.loads(root_summary_path.read_text(encoding="utf-8"))
    by_name = {section["name"]: section for section in TARGETS}
    summaries = []

    for old_summary in root_summary["sections"]:
        root_url = old_summary["root_url"]
        section = next(item for item in by_name.values() if item["url"] == root_url)
        section_dir = OUT_DIR / section["name"]
        section_dir.mkdir(parents=True, exist_ok=True)
        clean_export_files(section_dir)

        manifest_path = section_dir / "_manifest.jsonl"
        failures_path = section_dir / "_failures.jsonl"
        crawl_id = old_summary["crawl_id"]
        status_url = f"{API_BASE}/v2/crawl/{crawl_id}"
        status = collect_status(status_url)
        saved = {}

        for doc in status.get("data") or []:
            source_url = doc_key(doc)
            written_path = write_markdown(section, doc)
            metadata = doc.get("metadata") or {}
            if written_path is None:
                append_jsonl(
                    failures_path,
                    {
                        "crawl_id": crawl_id,
                        "source_url": source_url,
                        "status_code": metadata.get("statusCode"),
                        "error": metadata.get("error") or doc.get("error") or "empty markdown",
                    },
                )
                continue
            saved[source_url] = str(written_path.relative_to(OUT_DIR))
            append_jsonl(
                manifest_path,
                {
                    "crawl_id": crawl_id,
                    "source_url": source_url,
                    "file": saved[source_url],
                    "title": metadata.get("title"),
                    "status_code": metadata.get("statusCode"),
                },
            )

        try:
            errors = request_json("GET", f"{API_BASE}/v2/crawl/{crawl_id}/errors", timeout=120)
            (section_dir / "_errors.json").write_text(
                json.dumps(errors, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except Exception as exc:
            append_jsonl(failures_path, {"crawl_id": crawl_id, "error": f"failed to fetch crawl errors: {exc}"})

        new_summary = {
            **old_summary,
            "saved_markdown_files": len(saved),
            "reexported_at": datetime.now(timezone.utc).isoformat(),
        }
        (section_dir / "_summary.json").write_text(
            json.dumps(new_summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        summaries.append(new_summary)
        print(f"[{section['name']}] reexported saved={len(saved)}", flush=True)

    root_summary["sections"] = summaries
    root_summary["reexported_at"] = datetime.now(timezone.utc).isoformat()
    root_summary_path.write_text(json.dumps(root_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(root_summary, ensure_ascii=False, indent=2), flush=True)


def retry_errors():
    root_summary_path = OUT_DIR / "_summary.json"
    root_summary = json.loads(root_summary_path.read_text(encoding="utf-8"))
    by_url = {section["url"]: section for section in TARGETS}

    for section_summary in root_summary["sections"]:
        section = by_url[section_summary["root_url"]]
        section_dir = OUT_DIR / section["name"]
        errors_path = section_dir / "_errors.json"
        if not errors_path.exists():
            continue

        errors_payload = json.loads(errors_path.read_text(encoding="utf-8"))
        errors = errors_payload.get("errors") or []
        retried = 0
        retry_failures = section_dir / "_retry_failures.jsonl"
        if retry_failures.exists():
            retry_failures.unlink()

        for item in errors:
            url = item.get("url")
            if not url:
                continue
            try:
                doc = scrape_url(url)
                written_path = write_markdown(section, doc)
                if written_path is None:
                    raise RuntimeError("empty markdown")
                metadata = doc.get("metadata") or {}
                append_jsonl(
                    section_dir / "_manifest.jsonl",
                    {
                        "crawl_id": section_summary["crawl_id"],
                        "retry": True,
                        "source_url": doc_key(doc) or url,
                        "file": str(written_path.relative_to(OUT_DIR)),
                        "title": metadata.get("title"),
                        "status_code": metadata.get("statusCode"),
                    },
                )
                retried += 1
                print(f"[{section['name']}] retry saved {url}", flush=True)
            except Exception as exc:
                append_jsonl(
                    retry_failures,
                    {
                        "source_url": url,
                        "original_code": item.get("code"),
                        "retry_error": str(exc),
                    },
                )
                print(f"[{section['name']}] retry failed {url}: {exc}", flush=True)

        if retried:
            current_files = len(list(section_dir.rglob("*.md")))
            section_summary["saved_markdown_files"] = current_files
            section_summary["retried_error_markdown_files"] = retried
            section_summary["retry_updated_at"] = datetime.now(timezone.utc).isoformat()
            (section_dir / "_summary.json").write_text(
                json.dumps(section_summary, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    root_summary["retry_updated_at"] = datetime.now(timezone.utc).isoformat()
    root_summary_path.write_text(json.dumps(root_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(root_summary, ensure_ascii=False, indent=2), flush=True)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--reexport-from-summary":
        reexport_from_summary()
        return
    if len(sys.argv) > 1 and sys.argv[1] == "--retry-errors":
        retry_errors()
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    all_summaries = []
    for section in TARGETS:
        all_summaries.append(crawl_section(section))

    root_summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "api_base": API_BASE,
        "output_dir": str(OUT_DIR),
        "sections": all_summaries,
    }
    (OUT_DIR / "_summary.json").write_text(
        json.dumps(root_summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(root_summary, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
