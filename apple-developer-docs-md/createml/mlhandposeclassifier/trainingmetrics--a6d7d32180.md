---
title: "trainingMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137814+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   trainingMetrics

instance property

trainingMetrics
===============

training dataset에서 hand pose classifier 성능을 측정한 값입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    var trainingMetrics: MLClassifierMetrics

[관련 항목](https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics#see-also)

-------------------------------------------------------------------------------------------------------------

### [hand pose classifier 평가하기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics#Evaluating-a-hand-pose-classifier)

[`func evaluation(on: MLHandPoseClassifier.DataSource) throws -> MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:))

label된 image dataset으로 hand pose classifier 성능을 설명하는 metric을 생성합니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/validationmetrics)

validation dataset에서 hand pose classifier 성능을 측정한 값입니다.

현재 페이지: trainingMetrics
