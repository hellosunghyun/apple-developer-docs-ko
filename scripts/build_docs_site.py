#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse

import markdown
import yaml


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "apple-developer-docs-md"
SITE_ROOT = ROOT / "site"
ASSET_DIR = SITE_ROOT / "assets"
ASSET_VERSION = "20260511-code-external-link-mark"

SECTION_ORDER = ["Core Motion", "SensorKit", "Create ML"]
SECTION_SLUGS = {
    "Core Motion": "coremotion",
    "SensorKit": "sensorkit",
    "Create ML": "createml",
}


@dataclass(frozen=True)
class Doc:
    rel_md: str
    md_path: Path
    out_path: Path
    source_url: str
    title: str
    display_title: str
    section: str
    summary: str
    order: int


@dataclass(frozen=True)
class TopicLink:
    label: str
    summary: str
    href: str
    doc: Doc | None


@dataclass(frozen=True)
class TopicGroup:
    title: str
    links: list[TopicLink]


def clean_title(title: str) -> str:
    return title.replace(" | Apple Developer Documentation", "").strip() or "Documentation"


def body_title(body: str, fallback: str) -> str:
    lines = body.splitlines()
    for idx, raw in enumerate(lines[:-1]):
        title = raw.strip()
        underline = lines[idx + 1].strip()
        if title and re.fullmatch(r"=+", underline):
            return title
    for raw in lines:
        match = re.match(r"^#\s+(.+)$", raw.strip())
        if match:
            return match.group(1).strip()
    return fallback


def parse_markdown(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, front, body = text.split("---", 2)
        meta = yaml.safe_load(front) or {}
        return meta, body.lstrip("\n")
    return {}, text


def clean_body(body: str) -> str:
    lines = body.splitlines()
    cleaned: list[str] = []
    idx = 0
    while idx < len(lines):
        stripped = lines[idx].strip()
        if re.match(r"^\[탐색 건너뛰기\]\([^)]+\)$", stripped):
            idx += 1
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            # Apple breadcrumbs are scraped as a leading bullet list. Render
            # our own chrome instead of showing those as document content.
            if idx < len(lines) and lines[idx].lstrip().startswith("*"):
                while idx < len(lines):
                    next_line = lines[idx]
                    next_stripped = next_line.strip()
                    if not next_stripped:
                        idx += 1
                        continue
                    if next_line.lstrip().startswith("*"):
                        idx += 1
                        continue
                    break
            continue
        if stripped.startswith("현재 페이지:") or stripped.startswith("현재 페이지는 "):
            idx += 1
            continue
        cleaned.append(normalize_availability_line(lines[idx]))
        idx += 1
    return "\n".join(cleaned).strip() + "\n"


def promote_inpage_heading_links(body: str) -> str:
    lines = body.splitlines()
    output: list[str] = []
    idx = 0
    while idx < len(lines):
        current = lines[idx].strip()
        link = markdown_link_parts(current)
        next_idx = idx + 1
        while next_idx < len(lines) and not lines[next_idx].strip():
            next_idx += 1
        if (
            link
            and next_idx < len(lines)
            and re.fullmatch(r"-{8,}", lines[next_idx].strip())
            and "#" in link[1]
        ):
            output.append(f"## {link[0]}")
            idx = next_idx + 1
            continue
        output.append(lines[idx])
        idx += 1
    return "\n".join(output).strip() + "\n"


def normalize_availability_line(line: str) -> str:
    stripped = line.strip()
    platforms = ("iOS", "iPadOS", "Mac Catalyst", "macOS", "visionOS", "watchOS", "tvOS")
    if not stripped.startswith(platforms):
        return line
    if sum(1 for platform in platforms if platform in stripped) < 2:
        return line
    value = re.sub(r"(?<!^)(?=(iPadOS|Mac Catalyst|macOS|visionOS|watchOS|tvOS)\s)", " | ", stripped)
    indent = line[: len(line) - len(line.lstrip())]
    return indent + value


def normalize_apple_doc_url(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc.lower() != "developer.apple.com":
        return None
    path = unquote(parsed.path).rstrip("/")
    if not path.lower().startswith("/documentation/"):
        return None
    return f"https://developer.apple.com{path.lower()}"


def split_url_fragment(url: str) -> tuple[str, str]:
    if "#" not in url:
        return url, ""
    base, frag = url.split("#", 1)
    return base, f"#{frag}"


def local_fragment(fragment: str) -> str:
    if not fragment:
        return ""
    return "#" + fragment[1:].lower()


def output_path_for(rel_md: str) -> Path:
    rel = Path(rel_md)
    return SITE_ROOT / "docs" / rel.with_suffix(".html")


def rel_href(from_file: Path, to_file: Path) -> str:
    rel = os.path.relpath(to_file, start=from_file.parent)
    return rel.replace(os.sep, "/")


def site_root_prefix(from_file: Path) -> str:
    rel = os.path.relpath(SITE_ROOT, start=from_file.parent).replace(os.sep, "/")
    return "." if rel == "." else rel


def html_to_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value).strip()


def first_summary(body: str) -> str:
    body = clean_body(body)
    lines = body.splitlines()
    first_heading_end = 0
    for idx, raw in enumerate(lines[:-1]):
        if raw.strip() and re.fullmatch(r"=+", lines[idx + 1].strip()):
            first_heading_end = idx + 2
            break
    for raw in lines[first_heading_end:]:
        line = raw.strip()
        if not line:
            continue
        if re.fullmatch(r"[-=]{3,}", line):
            continue
        if line.startswith(("#", "[", "*", "`", "!", "---")):
            continue
        if re.match(r"^[A-Za-z0-9 .:+_(){}<>,/|?;'\"-]+$", line):
            continue
        if re.match(r"^(iOS|iPadOS|macOS|watchOS|tvOS|visionOS|Mac Catalyst)", line):
            continue
        return re.sub(r"\s+", " ", line)[:180]
    return ""


def load_docs() -> list[Doc]:
    docs: list[Doc] = []
    order = 0
    manifest_files = [DOC_ROOT / SECTION_SLUGS[section] / "_manifest.jsonl" for section in SECTION_ORDER]
    seen: set[str] = set()
    for manifest_file in manifest_files:
        if not manifest_file.exists():
            continue
        for line in manifest_file.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            rel_md = item["file"]
            path = DOC_ROOT / rel_md
            if not path.exists() or rel_md in seen:
                continue
            seen.add(rel_md)
            meta, body = parse_markdown(path)
            title = str(meta.get("title") or item.get("title") or clean_title(path.stem))
            display_title = body_title(body, clean_title(title))
            section = str(meta.get("section") or "")
            source_url = str(meta.get("source_url") or item.get("source_url") or "")
            docs.append(
                Doc(
                    rel_md=rel_md,
                    md_path=path,
                    out_path=output_path_for(rel_md),
                    source_url=source_url,
                    title=title,
                    display_title=display_title,
                    section=section,
                    summary=first_summary(body),
                    order=order,
                )
            )
            order += 1
    for path in sorted(DOC_ROOT.rglob("*.md")):
        rel_md = path.relative_to(DOC_ROOT).as_posix()
        if rel_md in seen:
            continue
        meta, body = parse_markdown(path)
        title = str(meta.get("title") or clean_title(path.stem))
        display_title = body_title(body, clean_title(title))
        docs.append(
            Doc(
                rel_md=rel_md,
                md_path=path,
                out_path=output_path_for(rel_md),
                source_url=str(meta.get("source_url") or ""),
                title=title,
                display_title=display_title,
                section=str(meta.get("section") or ""),
                summary=first_summary(body),
                order=order,
            )
        )
        order += 1
    return docs


def build_url_map(docs: Iterable[Doc]) -> dict[str, Doc]:
    mapping: dict[str, Doc] = {}
    for doc in docs:
        normalized = normalize_apple_doc_url(doc.source_url)
        if normalized:
            mapping[normalized] = doc
    return mapping


def markdown_link_parts(line: str) -> tuple[str, str] | None:
    match = re.match(r"^\s*\[(`?[^]]+?`?)\]\(([^)]+)\)\s*$", line)
    if not match:
        return None
    label = match.group(1).strip()
    label = re.sub(r"^`|`$", "", label)
    return label, match.group(2).strip()


def href_for_url(url: str, out_file: Path, url_map: dict[str, Doc]) -> tuple[str, Doc | None]:
    base, fragment = split_url_fragment(url)
    normalized = normalize_apple_doc_url(base)
    if normalized and normalized in url_map:
        doc = url_map[normalized]
        return rel_href(out_file, doc.out_path) + local_fragment(fragment), doc
    return url, None


def build_topic_groups(index_doc: Doc, out_file: Path, url_map: dict[str, Doc]) -> list[TopicGroup]:
    _, raw_body = parse_markdown(index_doc.md_path)
    lines = raw_body.splitlines()
    groups: list[TopicGroup] = []
    current_title: str | None = None
    current_links: list[TopicLink] = []
    idx = 0

    def flush() -> None:
        nonlocal current_title, current_links
        if current_title and current_links:
            groups.append(TopicGroup(current_title, current_links))
        current_title = None
        current_links = []

    while idx < len(lines):
        line = lines[idx].strip()
        heading = re.match(r"^###\s+\[([^]]+)\]\([^)]+\)", line)
        if heading:
            flush()
            current_title = heading.group(1).strip()
            idx += 1
            continue
        if current_title:
            parts = markdown_link_parts(line)
            if parts:
                label, url = parts
                if label in {"개요", "주제"}:
                    idx += 1
                    continue
                summary = ""
                scan = idx + 1
                while scan < len(lines):
                    candidate = lines[scan].strip()
                    if not candidate:
                        scan += 1
                        continue
                    if candidate.startswith("[") or candidate.startswith("###") or candidate.startswith("`"):
                        break
                    if candidate in {"Deprecated"}:
                        scan += 1
                        continue
                    summary = candidate
                    break
                href, target_doc = href_for_url(url, out_file, url_map)
                current_links.append(TopicLink(label=label, summary=summary, href=href, doc=target_doc))
        idx += 1
    flush()
    return groups


def rewrite_html_links(rendered: str, current: Path, url_map: dict[str, Doc]) -> str:
    def replace(match: re.Match[str]) -> str:
        attr = match.group(1)
        value = html.unescape(match.group(2))
        if attr != "href":
            return match.group(0)
        if value.startswith("#"):
            return f'{attr}="{html.escape(local_fragment(value), quote=True)}"'
        if value.startswith(("mailto:", "tel:", "javascript:")):
            return f'{attr}="{html.escape(value, quote=True)}"'
        base, fragment = split_url_fragment(value)
        normalized = normalize_apple_doc_url(base)
        if normalized and normalized in url_map:
            target = rel_href(current, url_map[normalized].out_path) + local_fragment(fragment)
            return f'{attr}="{html.escape(target, quote=True)}"'
        return f'{attr}="{html.escape(value, quote=True)}" target="_blank" rel="noopener"'

    return re.sub(r'(href|src)="([^"]+)"', replace, rendered)


def render_markdown(body: str) -> str:
    return markdown.markdown(
        body,
        extensions=["extra", "toc", "sane_lists", "tables"],
        extension_configs={"toc": {"permalink": False}},
        output_format="html5",
    )


def extract_toc(rendered: str) -> list[tuple[int, str, str]]:
    toc: list[tuple[int, str, str]] = []
    for match in re.finditer(r"<h([23]) id=\"([^\"]+)\">(.*?)</h[23]>", rendered, flags=re.S):
        level = int(match.group(1))
        anchor = html.unescape(match.group(2))
        label = html_to_text(match.group(3))
        if label:
            toc.append((level, anchor, label))
    return toc


def group_docs(docs: list[Doc]) -> dict[str, list[Doc]]:
    grouped = {section: [] for section in SECTION_ORDER}
    for doc in docs:
        grouped.setdefault(doc.section, []).append(doc)
    for items in grouped.values():
        items.sort(key=lambda item: (0 if item.rel_md.endswith("/index.md") else 1, item.display_title.lower(), item.order))
    return grouped


def sidebar_html(current: Doc | None, out_file: Path, grouped: dict[str, list[Doc]], url_map: dict[str, Doc]) -> str:
    framework_links = []
    for section in SECTION_ORDER:
        index_doc = next((doc for doc in grouped.get(section, []) if doc.rel_md.endswith("/index.md")), None)
        href = rel_href(out_file, index_doc.out_path) if index_doc else "#"
        active = " is-active" if current and current.section == section else ""
        framework_links.append(f'<a class="framework-link{active}" href="{href}">{html.escape(section)}</a>')

    current_section = current.section if current else ""
    topic_markup = ""
    if current_section:
        index_doc = next((doc for doc in grouped.get(current_section, []) if doc.rel_md.endswith("/index.md")), None)
        topic_groups = build_topic_groups(index_doc, out_file, url_map) if index_doc else []
        groups_html = []
        for group in topic_groups:
            links_html = []
            group_has_current = False
            for item in group.links:
                active = ""
                if current and item.doc and item.doc.rel_md == current.rel_md:
                    active = " is-current"
                    group_has_current = True
                summary = f'<span>{html.escape(item.summary)}</span>' if item.summary else ""
                external = ' target="_blank" rel="noopener"' if item.doc is None and item.href.startswith("http") else ""
                data_title = html.escape(f"{item.label} {item.summary}".lower(), quote=True)
                links_html.append(
                    f'<a class="topic-link{active}" href="{html.escape(item.href, quote=True)}" data-title="{data_title}"{external}>'
                    f'<strong>{html.escape(item.label)}</strong>{summary}</a>'
                )
            open_attr = " open" if group_has_current or len(groups_html) < 4 else ""
            groups_html.append(
                f'<details class="topic-group"{open_attr}><summary>{html.escape(group.title)}</summary>'
                f'<div class="topic-links">{"".join(links_html)}</div></details>'
            )
        topic_markup = f"""
  <div class="sidebar-section navigator-section">
    <div class="sidebar-label">Topics</div>
    <input class="navigator-filter" id="navigator-filter" type="search" placeholder="Topic 필터" autocomplete="off">
    <div class="topic-list" id="navigator-list">
      {''.join(groups_html)}
    </div>
  </div>
"""

    return f"""
<aside class="sidebar" id="site-sidebar" aria-label="Documentation navigator">
  <div class="sidebar-section">
    <div class="sidebar-label">Frameworks</div>
    <div class="framework-list">
      {''.join(framework_links)}
    </div>
  </div>
  {topic_markup}
</aside>
"""


def toc_html(toc: list[tuple[int, str, str]]) -> str:
    if not toc:
        return '<aside class="toc-rail" aria-label="On this page"><div class="toc-title">On This Page</div><p class="toc-empty">Section 없음</p></aside>'
    links = []
    for level, anchor, label in toc[:24]:
        links.append(f'<a class="toc-link level-{level}" href="#{html.escape(anchor, quote=True)}">{html.escape(label)}</a>')
    return f"""
<aside class="toc-rail" aria-label="On this page">
  <div class="toc-title">On This Page</div>
  <nav>{''.join(links)}</nav>
</aside>
"""


def shell(
    *,
    out_file: Path,
    title: str,
    body_class: str,
    sidebar: str,
    main: str,
    toc: str = "",
) -> str:
    root_prefix = site_root_prefix(out_file)
    css_href = rel_href(out_file, ASSET_DIR / "site.css")
    js_href = rel_href(out_file, ASSET_DIR / "site.js")
    home_href = rel_href(out_file, SITE_ROOT / "index.html")
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="docsite-root" content="{html.escape(root_prefix, quote=True)}">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{css_href}?v={ASSET_VERSION}">
</head>
<body class="{body_class}">
  <header class="globalbar">
    <a class="brand" href="{home_href}" aria-label="Home">
      <span class="brand-title">Developer</span>
    </a>
    <nav class="topnav" aria-label="Top navigation">
      <a href="https://developer.apple.com/get-started/" target="_blank" rel="noopener">Get Started</a>
      <a href="https://developer.apple.com/platforms/" target="_blank" rel="noopener">Platforms</a>
      <a href="https://developer.apple.com/technologies/" target="_blank" rel="noopener">Technologies</a>
      <a href="https://developer.apple.com/community/" target="_blank" rel="noopener">Community</a>
      <a href="{home_href}">Documentation</a>
      <a href="https://developer.apple.com/download/" target="_blank" rel="noopener">Downloads</a>
      <a href="https://developer.apple.com/support/" target="_blank" rel="noopener">Support</a>
    </nav>
    <button class="global-icon-button global-search-icon" type="button" data-open-search aria-label="Search">Search</button>
  </header>
  <header class="localbar">
    <button class="icon-button nav-toggle" type="button" aria-label="Documentation Navigator 열기" aria-controls="site-sidebar"><span class="navigator-glyph"></span></button>
    <a class="local-title" href="{home_href}">Documentation</a>
    <span class="unofficial-badge">비공식 한국어 아카이브</span>
  </header>
  <div class="mobile-scrim" data-close-nav></div>
  <div class="page-shell">
    {sidebar}
    <main class="main-column" id="app-main">
      {main}
    </main>
    {toc}
  </div>
  <div class="search-modal" id="search-modal" aria-hidden="true">
    <div class="search-card" role="dialog" aria-modal="true" aria-label="문서 검색">
      <div class="search-card-header">
        <input id="global-search-input" type="search" placeholder="Search documentation" autocomplete="off">
        <button class="icon-button" type="button" data-close-search aria-label="검색 닫기">×</button>
      </div>
      <div class="search-results" id="global-search-results"></div>
    </div>
  </div>
  <script>window.DOCSITE_ROOT = {json.dumps(root_prefix)};</script>
  <script src="{js_href}?v={ASSET_VERSION}"></script>
</body>
</html>
"""


def render_doc_page(doc: Doc, docs: list[Doc], grouped: dict[str, list[Doc]], url_map: dict[str, Doc]) -> None:
    meta, body = parse_markdown(doc.md_path)
    body = clean_body(body)
    body = promote_inpage_heading_links(body)
    rendered = render_markdown(body)
    rendered = re.sub(
        r"(<pre><code>)(class|struct|protocol|enum)(\s)",
        r'\1<span class="syntax-keyword">\2</span>\3',
        rendered,
    )
    rendered = rewrite_html_links(rendered, doc.out_path, url_map)
    toc = extract_toc(rendered)
    section_index = next((item for item in grouped.get(doc.section, []) if item.rel_md.endswith("/index.md")), None)
    section_href = rel_href(doc.out_path, section_index.out_path) if section_index else "#"
    main = f"""
<article class="doc-article">
  <div class="doc-toolbar">
    <nav class="breadcrumbs" aria-label="Breadcrumbs">
      <a href="{html.escape(section_href, quote=True)}">{html.escape(doc.section)}</a>
      <span>/</span>
      <span>{html.escape(doc.display_title)}</span>
    </nav>
  </div>
  <div class="markdown-body">
    {rendered}
  </div>
</article>
"""
    html_page = shell(
        out_file=doc.out_path,
        title=f"{doc.display_title} | Korean Apple Developer Documentation",
        body_class="doc-page",
        sidebar=sidebar_html(doc, doc.out_path, grouped, url_map),
        main=main,
        toc=toc_html(toc),
    )
    doc.out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.out_path.write_text(html_page, encoding="utf-8")


def render_home(docs: list[Doc], grouped: dict[str, list[Doc]], url_map: dict[str, Doc]) -> None:
    out_file = SITE_ROOT / "index.html"
    cards = []
    for section in SECTION_ORDER:
        index_doc = next((doc for doc in grouped.get(section, []) if doc.rel_md.endswith("/index.md")), None)
        count = len(grouped.get(section, []))
        href = rel_href(out_file, index_doc.out_path) if index_doc else "#"
        summary = html.escape(index_doc.summary if index_doc else "")
        cards.append(
            f"""
<a class="home-card" href="{href}">
  <span class="home-card-kind">Framework</span>
  <strong>{html.escape(section)}</strong>
  <span>{count}개 문서</span>
  <p>{summary}</p>
</a>
"""
        )
    recent_links = []
    for doc in docs[:18]:
        recent_links.append(
            f'<a href="{rel_href(out_file, doc.out_path)}"><span>{html.escape(doc.section)}</span>{html.escape(doc.display_title)}</a>'
        )
    main = f"""
<section class="home-hero">
  <div class="home-kicker">Apple Developer Documentation</div>
  <h1>Core Motion, SensorKit, Create ML</h1>
  <p>크롤링한 Apple Developer 문서를 한국어로 읽고 탐색할 수 있는 정적 문서 사이트입니다.</p>
  <div class="home-search-wrap">
    <button class="home-search" type="button" data-open-search>Search documentation</button>
  </div>
</section>
<section class="home-section">
  <h2>Frameworks</h2>
  <div class="home-grid">{''.join(cards)}</div>
</section>
<section class="home-section">
  <h2>Documentation</h2>
  <div class="home-list">{''.join(recent_links)}</div>
</section>
"""
    page = shell(
        out_file=out_file,
        title="Korean Apple Developer Documentation",
        body_class="home-page",
        sidebar=sidebar_html(None, out_file, grouped, url_map),
        main=main,
        toc="",
    )
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(page, encoding="utf-8")


def render_404(grouped: dict[str, list[Doc]], url_map: dict[str, Doc]) -> None:
    out_file = SITE_ROOT / "404.html"
    main = """
<section class="not-found">
  <h1>문서를 찾을 수 없습니다.</h1>
  <p>검색을 사용하거나 framework navigator에서 문서를 다시 선택하세요.</p>
  <button class="search-button prominent" type="button" data-open-search>Search documentation</button>
</section>
"""
    page = shell(
        out_file=out_file,
        title="Not Found | Korean Apple Developer Documentation",
        body_class="home-page",
        sidebar=sidebar_html(None, out_file, grouped, url_map),
        main=main,
        toc="",
    )
    out_file.write_text(page, encoding="utf-8")


def write_search_index(docs: list[Doc]) -> None:
    items = []
    for doc in docs:
        items.append(
            {
                "title": doc.display_title,
                "section": doc.section,
                "summary": doc.summary,
                "href": doc.out_path.relative_to(SITE_ROOT).as_posix(),
                "sourceUrl": doc.source_url,
            }
        )
    (SITE_ROOT / "search-index.json").write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def write_assets() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    (ASSET_DIR / "site.css").write_text(CSS, encoding="utf-8")
    (ASSET_DIR / "site.js").write_text(JS, encoding="utf-8")
    (SITE_ROOT / ".nojekyll").write_text("", encoding="utf-8")


def build() -> None:
    docs = load_docs()
    if SITE_ROOT.exists():
        shutil.rmtree(SITE_ROOT)
    SITE_ROOT.mkdir(parents=True)
    grouped = group_docs(docs)
    url_map = build_url_map(docs)
    write_assets()
    render_home(docs, grouped, url_map)
    for doc in docs:
        render_doc_page(doc, docs, grouped, url_map)
    render_404(grouped, url_map)
    write_search_index(docs)
    print(f"built_site={SITE_ROOT}")
    print(f"documents={len(docs)}")


CSS = r"""
:root {
  color-scheme: dark;
  --bg: #000;
  --chrome: #161617;
  --text: #f5f5f7;
  --muted: #a1a1a6;
  --subtle: #6e6e73;
  --line: #424245;
  --soft-line: #2c2c2e;
  --fill: #1d1d1f;
  --fill-2: #080808;
  --hover: #1c1c1e;
  --selected: #1f3754;
  --blue: #2997ff;
  --blue-hover: #66b1ff;
  --code-bg: #2d2d2f;
  --pink: #ff7ab2;
  --nav-width: 298px;
  --toc-width: 238px;
  --globalbar-height: 44px;
  --localbar-height: 52px;
  --chrome-height: calc(var(--globalbar-height) + var(--localbar-height));
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.47059;
  letter-spacing: 0;
}

a { color: var(--blue); text-decoration: none; }
a:hover { color: var(--blue-hover); text-decoration: underline; }

.globalbar {
  position: sticky;
  top: 0;
  z-index: 40;
  height: var(--globalbar-height);
  display: flex;
  align-items: center;
  gap: 26px;
  padding: 0 22px;
  border-bottom: 1px solid #242426;
  background: rgba(22, 22, 23, 0.92);
  backdrop-filter: saturate(180%) blur(20px);
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  flex: 0 0 auto;
  min-width: max-content;
  color: var(--text);
  font-size: 18px;
  font-weight: 600;
  white-space: nowrap;
}

.brand:hover { color: var(--text); text-decoration: none; }
.brand-title { overflow: visible; text-overflow: clip; }

.topnav {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-left: 6px;
  font-size: 12px;
}

.topnav a { color: #d2d2d7; }
.topnav a:hover { color: #fff; text-decoration: none; }

.global-icon-button {
  position: relative;
  min-width: 30px;
  height: 30px;
  border: 0;
  background: transparent;
  color: #d2d2d7;
  font: inherit;
  font-size: 12px;
  cursor: pointer;
}

.global-icon-button:hover { color: #fff; }
.global-search-icon { margin-left: auto; font-size: 0; }
.global-search-icon::before {
  content: "";
  position: absolute;
  left: 9px;
  top: 8px;
  width: 10px;
  height: 10px;
  border: 1.6px solid currentColor;
  border-radius: 50%;
}

.global-search-icon::after {
  content: "";
  position: absolute;
  left: 19px;
  top: 19px;
  width: 7px;
  border-top: 1.6px solid currentColor;
  transform: rotate(45deg);
  transform-origin: left center;
}

.localbar {
  position: sticky;
  top: var(--globalbar-height);
  z-index: 39;
  height: var(--localbar-height);
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid #242426;
  background: rgba(0, 0, 0, 0.92);
  padding: 0 22px;
  backdrop-filter: saturate(180%) blur(20px);
}

.local-title {
  color: #fff;
  font-size: 21px;
  font-weight: 600;
  line-height: 1;
}

.local-title:hover { color: #fff; text-decoration: none; }

.unofficial-badge {
  color: var(--muted);
  font-size: 12px;
  line-height: 1;
  margin-left: auto;
  white-space: nowrap;
}

.icon-button:hover { background: #1d1d1f; }

.search-button,
.home-search {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 32px;
  border: 1px solid var(--line);
  border-radius: 980px;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 12px;
  padding: 5px 13px;
  cursor: pointer;
}

.search-button:hover,
.home-search:hover {
  background: var(--hover);
  color: var(--text);
  text-decoration: none;
}

.icon-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 18px;
  cursor: pointer;
}

.nav-toggle { display: none; }

.navigator-glyph {
  width: 17px;
  height: 14px;
  display: inline-block;
  border: 1.5px solid currentColor;
  border-radius: 2px;
  position: relative;
}

.navigator-glyph::before {
  content: "";
  position: absolute;
  top: -1.5px;
  bottom: -1.5px;
  left: 5px;
  border-left: 1.5px solid currentColor;
}

.page-shell {
  display: grid;
  grid-template-columns: var(--nav-width) minmax(0, 1fr) var(--toc-width);
  align-items: start;
  min-height: calc(100vh - var(--chrome-height));
}

.home-page .page-shell { grid-template-columns: var(--nav-width) minmax(0, 1fr); }

.sidebar {
  position: sticky;
  top: var(--chrome-height);
  height: calc(100vh - var(--chrome-height));
  overflow: auto;
  border-right: 1px solid var(--soft-line);
  background: var(--fill-2);
  padding: 22px 18px 28px;
}

.sidebar-label {
  margin: 0 0 8px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 600;
}

.sidebar-section + .sidebar-section { margin-top: 28px; }

.framework-list,
.navigator-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.framework-link,
.navigator-link {
  display: block;
  border-radius: 8px;
  color: #d2d2d7;
  font-size: 13px;
  line-height: 1.3;
  padding: 7px 9px;
}

.framework-link:hover,
.navigator-link:hover {
  background: var(--hover);
  color: var(--text);
  text-decoration: none;
}

.framework-link.is-active,
.navigator-link.is-current {
  background: var(--selected);
  color: var(--blue);
  font-weight: 600;
}

.topic-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.topic-group {
  border-top: 1px solid var(--soft-line);
  padding-top: 10px;
}

.topic-group:first-child {
  border-top: 0;
  padding-top: 0;
}

.topic-group summary {
  min-height: 34px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  border-radius: 8px;
  color: var(--text);
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  line-height: 1.3;
  list-style: none;
  padding: 8px 9px;
}

.topic-group summary::-webkit-details-marker { display: none; }

.topic-group summary::after {
  content: "›";
  flex: 0 0 auto;
  color: var(--muted);
  font-size: 16px;
  transform: rotate(90deg);
  transition: transform 120ms ease;
}

.topic-group:not([open]) summary::after { transform: rotate(0deg); }

.topic-group summary:hover {
  background: var(--hover);
}

.topic-links {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 4px 0 10px;
}

.topic-link {
  display: block;
  min-height: 42px;
  border-radius: 9px;
  color: #d2d2d7;
  padding: 9px 10px;
}

.topic-link:hover {
  background: var(--hover);
  color: var(--text);
  text-decoration: none;
}

.topic-link strong {
  display: block;
  font-size: 13px;
  font-weight: 500;
  line-height: 1.25;
}

.topic-link[target="_blank"] strong::after {
  content: "↗";
  display: inline-block;
  margin-left: 6px;
  color: var(--blue);
  font-size: 11px;
  font-weight: 600;
  line-height: 1;
  transform: translateY(-1px);
}

.topic-link[target="_blank"]:hover strong::after {
  color: var(--blue-hover);
}

.topic-link span {
  display: block;
  margin-top: 3px;
  color: var(--muted);
  font-size: 11px;
  line-height: 1.32;
}

.topic-link.is-current {
  background: var(--selected);
  color: var(--blue);
}

.topic-link.is-current strong { font-weight: 600; }
.topic-link.is-current span { color: #b9d7ff; }

.navigator-filter {
  width: 100%;
  height: 34px;
  margin: 0 0 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #111;
  color: var(--text);
  font: inherit;
  font-size: 13px;
  padding: 0 10px;
}

.main-column {
  min-width: 0;
  padding: 0 34px 88px;
}

.doc-article {
  max-width: 660px;
  margin: 0 auto;
  padding-top: 44px;
}

.doc-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
  color: var(--muted);
  font-size: 13px;
}

.breadcrumbs {
  display: flex;
  align-items: center;
  min-width: 0;
  gap: 7px;
  color: #d2d2d7;
}

.breadcrumbs a { color: #d2d2d7; text-decoration: underline; text-underline-offset: 2px; }
.breadcrumbs span:last-child { color: #f5f5f7; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.toc-rail {
  position: sticky;
  top: var(--chrome-height);
  height: calc(100vh - var(--chrome-height));
  overflow: auto;
  border-left: 1px solid var(--soft-line);
  padding: 34px 22px 40px;
}

.toc-title {
  margin-bottom: 10px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 600;
}

.toc-link {
  display: block;
  color: #a1a1a6;
  font-size: 12px;
  line-height: 1.35;
  padding: 5px 0;
}

.toc-link.level-3 { padding-left: 12px; }
.toc-empty { color: var(--subtle); font-size: 12px; }

.markdown-body {
  color: var(--text);
  font-size: 17px;
  line-height: 1.52947;
}

.markdown-body > :first-child { margin-top: 0; }
.markdown-body > p:first-child {
  color: #86868b;
  font-size: 21px;
  font-weight: 600;
  line-height: 1.19048;
  margin: 0 0 14px;
  text-transform: capitalize;
}

.markdown-body h1 {
  margin: 0 0 12px;
  font-size: 40px;
  line-height: 1.08349;
  font-weight: 600;
  letter-spacing: -0.003em;
}

.markdown-body h1 + p {
  color: #f5f5f7;
  font-size: 21px;
  line-height: 1.381;
  margin: 0 0 16px;
}

.markdown-body h1 + p + p {
  color: #d2d2d7;
  font-size: 14px;
  line-height: 1.42859;
  margin: 0 0 28px;
}

.markdown-body h2 {
  margin: 42px 0 16px;
  padding-top: 38px;
  border-top: 1px solid var(--soft-line);
  font-size: 32px;
  line-height: 1.125;
  font-weight: 600;
  scroll-margin-top: calc(var(--chrome-height) + 22px);
}

.markdown-body h3 {
  margin: 34px 0 12px;
  font-size: 24px;
  line-height: 1.25;
  font-weight: 600;
  scroll-margin-top: calc(var(--chrome-height) + 22px);
}

.markdown-body h4 {
  margin: 28px 0 10px;
  font-size: 18px;
}

.markdown-body a[target="_blank"]::after {
  content: "↗";
  display: inline-block;
  margin-left: 0.18em;
  color: var(--blue);
  font-size: 0.78em;
  line-height: 1;
  text-decoration: none;
  transform: translateY(-0.08em);
}

.markdown-body a[target="_blank"]:hover::after {
  color: var(--blue-hover);
}

.markdown-body a[target="_blank"]:has(> code)::after {
  content: none;
}

.markdown-body a[target="_blank"] > code::after {
  content: " ↗";
  color: var(--blue);
  font-size: 0.8em;
  font-weight: 600;
}

.markdown-body a[target="_blank"]:hover > code::after {
  color: var(--blue-hover);
}

.markdown-body p,
.markdown-body ul,
.markdown-body ol {
  margin: 12px 0;
}

.markdown-body ul,
.markdown-body ol { padding-left: 1.35em; }

.markdown-body li { margin: 5px 0; }

.markdown-body code {
  border-radius: 5px;
  background: var(--code-bg);
  font-family: "SF Mono", SFMono-Regular, ui-monospace, Menlo, Consolas, monospace;
  color: #a8c7fa;
  font-size: 0.88em;
  padding: 0.12em 0.32em;
}

.markdown-body pre {
  overflow: auto;
  border: 0;
  border-radius: 22px;
  background: var(--code-bg);
  margin: 36px 0 40px;
  padding: 16px 20px;
}

.markdown-body pre code {
  background: transparent;
  color: #f5f5f7;
  padding: 0;
  font-size: 14px;
  line-height: 1.55;
}

.syntax-keyword { color: var(--pink); }

.markdown-body img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 22px 0;
  border: 1px solid var(--soft-line);
  border-radius: 12px;
  background: #111;
}

.markdown-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 22px 0;
  font-size: 14px;
}

.markdown-body th,
.markdown-body td {
  border-bottom: 1px solid var(--soft-line);
  padding: 10px 12px;
  text-align: left;
  vertical-align: top;
}

.markdown-body hr {
  border: 0;
  border-top: 1px solid var(--soft-line);
  margin: 18px 0 24px;
}

.markdown-body blockquote {
  margin: 18px 0;
  border-left: 4px solid var(--line);
  color: var(--muted);
  padding-left: 16px;
}

.home-hero {
  max-width: 980px;
  margin: 0 auto;
  padding: 72px 0 48px;
}

.home-kicker {
  color: var(--muted);
  font-size: 17px;
  font-weight: 600;
}

.home-hero h1 {
  max-width: 760px;
  margin: 10px 0 14px;
  font-size: clamp(42px, 6vw, 72px);
  line-height: 1.02;
}

.home-hero p {
  max-width: 680px;
  color: var(--muted);
  font-size: 21px;
  line-height: 1.38;
}

.home-search-wrap { margin-top: 26px; }
.home-search {
  width: min(100%, 520px);
  justify-content: flex-start;
  min-height: 44px;
  color: var(--muted);
  background: var(--fill);
}

.home-section {
  max-width: 980px;
  margin: 0 auto;
  padding: 32px 0;
  border-top: 1px solid var(--soft-line);
}

.home-section h2 {
  margin: 0 0 18px;
  font-size: 28px;
}

.home-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.home-card {
  min-height: 210px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  border: 1px solid var(--soft-line);
  border-radius: 10px;
  background: #111;
  color: var(--text);
  padding: 20px;
}

.home-card:hover {
  border-color: #515154;
  box-shadow: 0 10px 30px rgba(255, 255, 255, 0.08);
  text-decoration: none;
}

.home-card-kind,
.home-card span {
  color: var(--muted);
  font-size: 13px;
}

.home-card strong {
  font-size: 26px;
  line-height: 1.15;
}

.home-card p {
  margin: auto 0 0;
  color: var(--muted);
  font-size: 14px;
}

.home-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0 28px;
}

.home-list a {
  display: flex;
  gap: 12px;
  border-top: 1px solid var(--soft-line);
  color: var(--text);
  font-size: 14px;
  padding: 13px 0;
}

.home-list a:hover { text-decoration: none; color: var(--blue); }
.home-list span { width: 90px; flex: 0 0 auto; color: var(--muted); font-size: 12px; }

.not-found {
  max-width: 720px;
  margin: 0 auto;
  padding: 80px 0;
}

.not-found h1 { font-size: 44px; margin: 0 0 12px; }
.not-found p { color: var(--muted); font-size: 19px; }
.prominent { min-height: 40px; margin-top: 12px; }

.search-modal {
  position: fixed;
  inset: 0;
  z-index: 40;
  display: none;
  background: rgba(0, 0, 0, 0.58);
  padding: 76px 18px 24px;
}

.search-modal.is-open { display: block; }

.search-card {
  max-width: 760px;
  max-height: min(760px, calc(100vh - 110px));
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border-radius: 14px;
  background: #1d1d1f;
  box-shadow: 0 22px 80px rgba(0, 0, 0, 0.5);
}

.search-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  border-bottom: 1px solid var(--soft-line);
  padding: 12px;
}

#global-search-input {
  width: 100%;
  height: 42px;
  border: 0;
  outline: 0;
  background: #111;
  border-radius: 10px;
  color: var(--text);
  font: inherit;
  font-size: 16px;
  padding: 0 13px;
}

.search-results {
  overflow: auto;
  padding: 8px;
}

.search-result {
  display: block;
  border-radius: 10px;
  color: var(--text);
  padding: 12px;
}

.search-result:hover {
  background: #2d2d2f;
  text-decoration: none;
}

.search-result strong { display: block; font-size: 15px; }
.search-result span { color: var(--muted); font-size: 12px; }
.search-result p { margin: 5px 0 0; color: var(--muted); font-size: 13px; }

.mobile-scrim { display: none; }

@media (max-width: 1180px) {
  .page-shell,
  .home-page .page-shell { grid-template-columns: var(--nav-width) minmax(0, 1fr); }
  .toc-rail { display: none; }
}

@media (max-width: 1068px) {
  .globalbar { gap: 18px; padding: 0 22px; }
  .nav-toggle { display: inline-flex; }
  .topnav { margin-left: auto; }
  .brand-title { max-width: 56vw; }
  .page-shell,
  .home-page .page-shell { display: block; }
  .sidebar {
    position: fixed;
    z-index: 32;
    inset: var(--chrome-height) auto 0 0;
    width: min(86vw, 320px);
    transform: translateX(-100%);
    transition: transform 180ms ease;
    box-shadow: 20px 0 50px rgba(0, 0, 0, 0.18);
  }
  body.nav-open .sidebar { transform: translateX(0); }
  body.nav-open .mobile-scrim {
    display: block;
    position: fixed;
    z-index: 31;
    inset: var(--chrome-height) 0 0;
    background: rgba(0, 0, 0, 0.46);
  }
  .main-column { padding: 0 28px 64px; }
  .doc-article { margin-left: auto; margin-right: auto; padding-top: 44px; }
  .doc-toolbar { align-items: flex-start; flex-direction: column; }
}

@media (max-width: 735px) {
  .globalbar { padding: 0 16px; }
  .topnav { display: none; }
  .global-icon-button { margin-left: auto; }
  .localbar { padding: 0 16px; }
  .main-column { padding: 0 20px 64px; }
  .markdown-body { font-size: 16px; }
  .markdown-body h1 { font-size: 36px; }
  .markdown-body h2 { font-size: 24px; }
  .home-hero { padding: 44px 0 32px; }
  .home-hero h1 { font-size: 44px; }
  .home-hero p { font-size: 18px; }
  .home-grid,
  .home-list { grid-template-columns: 1fr; }
  .home-card { min-height: 170px; }
}
"""


JS = r"""
(() => {
  const root = window.DOCSITE_ROOT || ".";
  const resolve = (href) => new URL(`${root}/${href}`.replace(/\/+/g, "/"), window.location.href).href;
  const body = document.body;
  const navToggle = document.querySelector(".nav-toggle");
  const closeNav = document.querySelector("[data-close-nav]");
  const sidebar = document.querySelector("#site-sidebar");
  const filter = document.querySelector("#navigator-filter");
  const modal = document.querySelector("#search-modal");
  const searchInput = document.querySelector("#global-search-input");
  const results = document.querySelector("#global-search-results");
  let searchIndex = null;

  function scrollToHashTarget() {
    if (!window.location.hash) return;
    const raw = decodeURIComponent(window.location.hash.slice(1));
    if (!raw) return;
    const target = document.getElementById(raw) || document.getElementById(raw.toLowerCase());
    if (!target) return;
    if (target.id !== raw) {
      history.replaceState(null, "", `${window.location.pathname}${window.location.search}#${target.id}`);
    }
    const styles = getComputedStyle(document.documentElement);
    const globalHeight = parseFloat(styles.getPropertyValue("--globalbar-height")) || 0;
    const localHeight = parseFloat(styles.getPropertyValue("--localbar-height")) || 0;
    const top = target.getBoundingClientRect().top + window.scrollY - globalHeight - localHeight - 22;
    window.scrollTo({ top, behavior: "auto" });
  }

  requestAnimationFrame(scrollToHashTarget);
  window.addEventListener("hashchange", scrollToHashTarget);

  navToggle?.addEventListener("click", () => body.classList.toggle("nav-open"));
  closeNav?.addEventListener("click", () => body.classList.remove("nav-open"));
  sidebar?.addEventListener("click", (event) => {
    if (event.target.closest("a")) body.classList.remove("nav-open");
  });

  filter?.addEventListener("input", () => {
    const query = filter.value.trim().toLowerCase();
    document.querySelectorAll(".navigator-link, .topic-link").forEach((link) => {
      const title = link.dataset.title || link.textContent.toLowerCase();
      const hit = !query || title.includes(query);
      link.style.display = hit ? "" : "none";
    });
    document.querySelectorAll(".topic-group").forEach((group) => {
      const links = Array.from(group.querySelectorAll(".topic-link"));
      const hasVisibleLink = links.some((link) => link.style.display !== "none");
      group.style.display = !query || hasVisibleLink ? "" : "none";
      if (query && hasVisibleLink) group.open = true;
    });
  });

  async function loadSearch() {
    if (searchIndex) return searchIndex;
    const response = await fetch(resolve("search-index.json"));
    searchIndex = await response.json();
    return searchIndex;
  }

  function renderResults(items, query) {
    if (!results) return;
    if (!query) {
      results.innerHTML = '<div class="search-result"><span>검색어를 입력하세요.</span></div>';
      return;
    }
    if (!items.length) {
      results.innerHTML = '<div class="search-result"><strong>결과 없음</strong><p>다른 API 이름이나 framework 이름으로 검색해 보세요.</p></div>';
      return;
    }
    results.innerHTML = items.slice(0, 40).map((item) => {
      const href = resolve(item.href);
      const summary = item.summary ? `<p>${escapeHtml(item.summary)}</p>` : "";
      return `<a class="search-result" href="${href}"><span>${escapeHtml(item.section)}</span><strong>${escapeHtml(item.title)}</strong>${summary}</a>`;
    }).join("");
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    }[char]));
  }

  async function runSearch() {
    const query = searchInput.value.trim().toLowerCase();
    const index = await loadSearch();
    const words = query.split(/\s+/).filter(Boolean);
    const scored = index.map((item) => {
      const haystack = `${item.title} ${item.section} ${item.summary} ${item.sourceUrl}`.toLowerCase();
      let score = 0;
      for (const word of words) {
        if (item.title.toLowerCase().includes(word)) score += 6;
        if (haystack.includes(word)) score += 1;
      }
      return { item, score };
    }).filter((entry) => entry.score > 0).sort((a, b) => b.score - a.score).map((entry) => entry.item);
    renderResults(scored, query);
  }

  async function openSearch() {
    modal?.classList.add("is-open");
    modal?.setAttribute("aria-hidden", "false");
    await loadSearch();
    searchInput?.focus();
    renderResults([], searchInput?.value.trim() || "");
  }

  function closeSearch() {
    modal?.classList.remove("is-open");
    modal?.setAttribute("aria-hidden", "true");
  }

  document.querySelectorAll("[data-open-search]").forEach((button) => button.addEventListener("click", openSearch));
  document.querySelectorAll("[data-close-search]").forEach((button) => button.addEventListener("click", closeSearch));
  modal?.addEventListener("click", (event) => {
    if (event.target === modal) closeSearch();
  });
  searchInput?.addEventListener("input", runSearch);
  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openSearch();
    }
    if (event.key === "Escape") {
      closeSearch();
      body.classList.remove("nav-open");
    }
  });
})();
"""


if __name__ == "__main__":
    build()
