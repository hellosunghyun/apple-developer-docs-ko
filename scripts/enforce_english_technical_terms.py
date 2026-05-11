#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "apple-developer-docs-md"

REPLACEMENTS = {
    "프레임워크": "framework",
    "프로퍼티": "property",
    "메서드": "method",
    "클래스": "class",
    "구조체": "struct",
    "열거형": "enum",
    "프로토콜": "protocol",
    "객체": "object",
    "인스턴스": "instance",
    "타입": "type",
    "매개변수": "parameter",
    "모델": "model",
    "데이터": "data",
    "샘플": "sample",
    "상수": "constant",
    "서비스": "service",
    "카테고리": "category",
    "함수": "function",
}


def main() -> None:
    changed_count = 0
    for path in DOC_ROOT.rglob("*.md"):
        original = path.read_text(encoding="utf-8")
        updated = original
        for korean, english in REPLACEMENTS.items():
            updated = updated.replace(korean, english)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_count += 1
    print(f"technical_term_normalized_files={changed_count}")


if __name__ == "__main__":
    main()
