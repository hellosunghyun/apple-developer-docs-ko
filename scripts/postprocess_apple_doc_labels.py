#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "apple-developer-docs-md"

LINE_REPLACEMENTS = {
    "Framework": "framework",
    "Class": "class",
    "Structure": "struct",
    "Enumeration": "enum",
    "Protocol": "protocol",
    "Type Alias": "type alias",
    "Associated Type": "associated type",
    "Instance Property": "인스턴스 property",
    "Type Property": "타입 property",
    "Instance Method": "인스턴스 method",
    "Type Method": "타입 method",
    "Initializer": "initializer",
    "Instance Subscript": "인스턴스 subscript",
    "Type Subscript": "타입 subscript",
    "Operator": "operator",
}

LINK_LABEL_REPLACEMENTS = {
    "Skip Navigation": "탐색 건너뛰기",
    "Overview": "개요",
    "Topics": "주제",
    "Discussion": "논의",
    "Relationships": "관계",
    "See Also": "같이 보기",
    "Mentioned in": "언급된 문서",
    "Mentions": "언급된 문서",
    "Beta": "beta",
    "Constants": "상수",
    "Initializers": "initializer",
    "Instance Properties": "인스턴스 property",
    "Type Properties": "타입 property",
    "Instance Methods": "인스턴스 method",
    "Type Methods": "타입 method",
    "Instance Subscripts": "인스턴스 subscript",
    "Type Subscripts": "타입 subscript",
    "Operators": "operator",
    "Relationships": "관계",
    "Conforms To": "준수하는 protocol",
    "Inherits From": "상속 대상",
    "Inherited By": "상속하는 type",
    "See Also": "같이 보기",
}


def replace_link_labels(text: str) -> str:
    for old, new in LINK_LABEL_REPLACEMENTS.items():
        text = re.sub(rf"\[{re.escape(old)}\]\(([^)]+)\)", rf"[{new}](\1)", text)
    return text


def replace_standalone_lines(text: str) -> str:
    lines = text.splitlines()
    changed = []
    for line in lines:
        stripped = line.strip()
        if stripped in LINE_REPLACEMENTS and line == stripped:
            changed.append(LINE_REPLACEMENTS[stripped])
        else:
            changed.append(line)
    return "\n".join(changed) + ("\n" if text.endswith("\n") else "")


def replace_current_page(text: str) -> str:
    return re.sub(r"^Current page is (.+)$", r"현재 페이지: \1", text, flags=re.MULTILINE)


def main() -> None:
    changed_count = 0
    for path in DOC_ROOT.rglob("*.md"):
        original = path.read_text(encoding="utf-8")
        updated = replace_link_labels(original)
        updated = replace_standalone_lines(updated)
        updated = replace_current_page(updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_count += 1
    print(f"postprocessed_files={changed_count}")


if __name__ == "__main__":
    main()
