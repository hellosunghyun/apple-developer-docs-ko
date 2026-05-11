---
title: "phase | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mljob/phase"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.145074+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mljob/phase#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLJob](https://developer.apple.com/documentation/createml/mljob)
    
*   phase

instance property

phase
=====

phase publisher입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 16.0+visionOS 1.0+

    final var phase: AnyPublisher<MLPhase, Never> { get }

[같이 보기](https://developer.apple.com/documentation/createml/mljob/phase#see-also)

------------------------------------------------------------------------------------

### [progress update 받기](https://developer.apple.com/documentation/createml/mljob/phase#Receiving-progress-updates)

[`var checkpoints: AnyPublisher<MLCheckpoint, Never>`](https://developer.apple.com/documentation/createml/mljob/checkpoints)

session의 각 checkpoint interval마다 checkpoint를 보내는 publisher입니다.

[`var result: AnyPublisher<Result, any Error>`](https://developer.apple.com/documentation/createml/mljob/result)

training session이 끝나면 result를 제공하는 publisher입니다.

현재 페이지: phase
