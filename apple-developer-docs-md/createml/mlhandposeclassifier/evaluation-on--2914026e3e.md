---
title: "evaluation(on:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137928+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   evaluation(on:)

instance method

evaluation(on:)
===============

label이 지정된 image dataset으로 hand pose classifier의 성능을 설명하는 metric을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    func evaluation(on annotatedImages: MLHandPoseClassifier.DataSource) throws -> MLClassifierMetrics

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:)#parameters)

-----------------------------------------------------------------------------------------------------------------

`annotatedImages`

[`MLHandPoseClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource)
 instance입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:)#see-also)

-------------------------------------------------------------------------------------------------------------

### [Evaluating a hand pose classifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:)#Evaluating-a-hand-pose-classifier)

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics)

training dataset에서 hand pose classifier의 성능을 나타내는 측정값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/validationmetrics)

validation dataset에서 hand pose classifier의 성능을 나타내는 측정값입니다.

현재 페이지는 evaluation(on:)입니다
