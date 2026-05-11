---
title: "validationMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/validationmetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.140970+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/validationmetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   validationMetrics

instance property

validationMetrics
=================

validation dataset에서 image classifier 성능을 측정한 값입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    var validationMetrics: MLClassifierMetrics { get }

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/validationmetrics#see-also)

------------------------------------------------------------------------------------------------------------

### [sound classifier 평가하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/validationmetrics#Evaluating-a-sound-classifier)

[`func evaluation(on:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:))

data source로 표현된 dataset에서 sound classifier의 성능을 평가해 metric을 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlsoundclassifier/trainingmetrics)

training dataset에서 classifier 성능을 측정한 값입니다.

현재 페이지: validationMetrics
