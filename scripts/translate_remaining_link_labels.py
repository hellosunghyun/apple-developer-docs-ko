#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = ROOT / "apple-developer-docs-md"

LABELS = {
    "API ReferenceCustomDebugStringConvertible Implementations": "API Reference: CustomDebugStringConvertible implementation",
    "API ReferenceCustomNSError Implementations": "API Reference: CustomNSError implementation",
    "API ReferenceCustomPlaygroundDisplayConvertible Implementations": "API Reference: CustomPlaygroundDisplayConvertible implementation",
    "API ReferenceCustomStringConvertible Implementations": "API Reference: CustomStringConvertible implementation",
    "API ReferenceData visualizations": "API Reference: data visualization",
    "API ReferenceEquatable Implementations": "API Reference: Equatable implementation",
    "API ReferenceLocalizedError Implementations": "API Reference: LocalizedError implementation",
    "Accessing submersion data": "submersion data 접근하기",
    "Adhering to the movement disorder data collection requirements": "movement disorder data collection requirement 준수하기",
    "Building an Action Classifier Data Source": "Action Classifier Data Source 만들기",
    "Building an object detector data source": "object detector data source 만들기",
    "Configuring your project for sensor reading": "sensor reading을 위해 project 구성하기",
    "Creating a model from tabular data": "tabular data에서 model 만들기",
    "Creating a text classifier model": "text classifier model 만들기",
    "Creating a word tagger model": "word tagger model 만들기",
    "Creating an Action Classifier Model": "Action Classifier Model 만들기",
    "Creating an Image Classifier Model": "Image Classifier Model 만들기",
    "Detecting human actions in a live video feed": "live video feed에서 human action 감지하기",
    "Event Handling Guide for UIKit Apps": "UIKit app용 event handling guide",
    "Gathering Training Videos for an Action Classifier": "Action Classifier용 training video 모으기",
    "Getting motion-activity data from headphones": "headphone에서 motion-activity data 가져오기",
    "Getting movement disorder symptom data": "movement disorder symptom data 가져오기",
    "Getting processed device-motion data": "processed device-motion data 가져오기",
    "Getting raw accelerometer events": "raw accelerometer event 가져오기",
    "Getting raw gyroscope events": "raw gyroscope event 가져오기",
    "Improving Your Model’s Accuracy": "model accuracy 개선하기",
    "Movement disorder algorithm changelog": "movement disorder algorithm 변경 내역",
}


def main() -> None:
    changed_count = 0
    for path in DOC_ROOT.rglob("*.md"):
        original = path.read_text(encoding="utf-8")
        updated = original
        for old, new in LABELS.items():
            updated = re.sub(rf"\[{re.escape(old)}\]\(([^)]+)\)", rf"[{new}](\1)", updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_count += 1
    print(f"link_label_translated_files={changed_count}")


if __name__ == "__main__":
    main()
