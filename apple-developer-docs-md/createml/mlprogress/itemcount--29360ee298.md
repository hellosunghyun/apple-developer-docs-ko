---
title: "itemCount | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlprogress/itemcount"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.160770+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlprogress/itemcount#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLProgress](https://developer.apple.com/documentation/createml/mlprogress)
    
*   itemCount

instance property

itemCount
=========

feature extraction phase에서 현재 처리한 file 수 또는 training phase에서 완료한 iteration 수입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    var itemCount: Int

[관련 항목](https://developer.apple.com/documentation/createml/mlprogress/itemcount#see-also)

---------------------------------------------------------------------------------------------

### [session 진행 상황 확인](https://developer.apple.com/documentation/createml/mlprogress/itemcount#Inspecting-a-sessions-progress)

[`var elapsedTime: TimeInterval`](https://developer.apple.com/documentation/createml/mlprogress/elapsedtime)

training session이 시작된 이후 경과한 시간(초)입니다.

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mlprogress/phase)

training session의 현재 phase입니다.

[`var totalItemCount: Int?`](https://developer.apple.com/documentation/createml/mlprogress/totalitemcount)

feature extraction phase의 전체 file 수 또는 training phase의 전체 iteration 수입니다.

[`var metrics: [MLProgress.Metric : Any]`](https://developer.apple.com/documentation/createml/mlprogress/metrics)

training session의 training 또는 evaluation phase 동안 model 성능 측정값입니다.

[`enum Metric`](https://developer.apple.com/documentation/createml/mlprogress/metric)

training session 동안 model 성능을 평가할 때 사용하는 metrics입니다.

현재 페이지는 itemCount
