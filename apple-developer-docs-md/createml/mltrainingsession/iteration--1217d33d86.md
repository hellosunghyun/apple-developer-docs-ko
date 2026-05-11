---
title: "iteration | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsession/iteration"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.143790+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsession/iteration#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTrainingSession](https://developer.apple.com/documentation/createml/mltrainingsession)
    
*   iteration

instance property

iteration
=========

training session phase의 iteration 번호입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    final var iteration: Int { get }

[같이 보기](https://developer.apple.com/documentation/createml/mltrainingsession/iteration#see-also)

----------------------------------------------------------------------------------------------------

### [training session progress 확인하기](https://developer.apple.com/documentation/createml/mltrainingsession/iteration#Checking-a-training-sessions-progress)

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mltrainingsession/phase)

training session의 현재 상태입니다.

[`enum MLPhase`](https://developer.apple.com/documentation/createml/mlphase)

training session의 가능한 상태입니다.

[`var checkpoints: [MLCheckpoint]`](https://developer.apple.com/documentation/createml/mltrainingsession/checkpoints)

training session이 지금까지 생성한 checkpoint array입니다.

현재 페이지: iteration
