---
title: "metrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlprogress/metrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.160956+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlprogress/metrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLProgress](https://developer.apple.com/documentation/createml/mlprogress)
    
*   metrics

instance property

metrics
=======

training session의 training 또는 evaluation 단계에서 model 성능을 측정한 값입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    var metrics: [MLProgress.Metric : Any]

[관련 항목](https://developer.apple.com/documentation/createml/mlprogress/metrics#see-also)

-------------------------------------------------------------------------------------------

### [session progress 확인](https://developer.apple.com/documentation/createml/mlprogress/metrics#Inspecting-a-sessions-progress)

[`var elapsedTime: TimeInterval`](https://developer.apple.com/documentation/createml/mlprogress/elapsedtime)

training session이 시작된 이후 경과한 시간(초)입니다.

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mlprogress/phase)

현재 training session 단계입니다.

[`var itemCount: Int`](https://developer.apple.com/documentation/createml/mlprogress/itemcount)

feature extraction 단계에서 현재 처리한 파일 수 또는 training 단계에서 완료한 iteration 수입니다.

[`var totalItemCount: Int?`](https://developer.apple.com/documentation/createml/mlprogress/totalitemcount)

feature extraction 단계의 전체 파일 수 또는 training 단계의 전체 iteration 수입니다.

[`enum Metric`](https://developer.apple.com/documentation/createml/mlprogress/metric)

training session 동안 model 성능을 평가할 때 사용하는 metric입니다.

현재 페이지는 metrics입니다
