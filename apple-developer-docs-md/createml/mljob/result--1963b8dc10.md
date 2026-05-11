---
title: "result | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mljob/result"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.143566+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mljob/result#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLJob](https://developer.apple.com/documentation/createml/mljob)
    
*   result

instance property

result
======

training session이 끝났을 때 result를 제공하는 publisher입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    final var result: AnyPublisher<Result, any Error> { get }

[같이 보기](https://developer.apple.com/documentation/createml/mljob/result#see-also)

-------------------------------------------------------------------------------------

### [Progress Update 받기](https://developer.apple.com/documentation/createml/mljob/result#Receiving-progress-updates)

[`var checkpoints: AnyPublisher<MLCheckpoint, Never>`](https://developer.apple.com/documentation/createml/mljob/checkpoints)

session의 각 checkpoint interval마다 checkpoint를 보내는 publisher입니다.

[`var phase: AnyPublisher<MLPhase, Never>`](https://developer.apple.com/documentation/createml/mljob/phase)

phase publisher입니다.

현재 페이지: result
