---
title: "metrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcheckpoint/metrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148026+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcheckpoint/metrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCheckpoint](https://developer.apple.com/documentation/createml/mlcheckpoint)
    
*   metrics

instance property

metrics
=======

session이 checkpoint를 저장했을 때 model 성능을 나타내는 측정값입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    var metrics: [MLProgress.Metric : Any] { get set }

[같이 보기](https://developer.apple.com/documentation/createml/mlcheckpoint/metrics#see-also)

---------------------------------------------------------------------------------------------

### [Assessing a checkpoint](https://developer.apple.com/documentation/createml/mlcheckpoint/metrics#Assessing-a-checkpoint)

[`enum Metric`](https://developer.apple.com/documentation/createml/mlprogress/metric)

training session 동안 model 성능을 평가할 때 사용하는 metric입니다.

현재 페이지: metrics
