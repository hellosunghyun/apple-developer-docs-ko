---
title: "phase | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcheckpoint/phase"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142265+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcheckpoint/phase#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCheckpoint](https://developer.apple.com/documentation/createml/mlcheckpoint)
    
*   phase

instance property

phase
=====

checkpoint를 만들었을 때의 training session phase입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    var phase: MLPhase

[같이 보기](https://developer.apple.com/documentation/createml/mlcheckpoint/phase#see-also)

-------------------------------------------------------------------------------------------

### [checkpoint 확인하기](https://developer.apple.com/documentation/createml/mlcheckpoint/phase#Inspecting-a-checkpoint)

[`var iteration: Int`](https://developer.apple.com/documentation/createml/mlcheckpoint/iteration)

checkpoint를 만들었을 때 training session phase의 iteration 번호입니다.

[`var date: Date`](https://developer.apple.com/documentation/createml/mlcheckpoint/date)

training session이 checkpoint를 만든 시각입니다.

[`var url: URL`](https://developer.apple.com/documentation/createml/mlcheckpoint/url)

file system에서 checkpoint의 위치입니다.

현재 페이지: phase
