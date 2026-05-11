---
title: "evaluation(on:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142472+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   evaluation(on:)

instance method

evaluation(on:)
===============

data source로 표현된 dataset에서 sound classifier 성능을 평가해 metric을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func evaluation(on testingData: MLSoundClassifier.DataSource) -> MLClassifierMetrics

Show all declarations

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)#parameters)

--------------------------------------------------------------------------------------------------------------

`testingData`

[`MLSoundClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
로 표현된 label audio file collection입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)#return-value)

------------------------------------------------------------------------------------------------------------------

평가 결과를 담은 [`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
instance입니다.

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)#see-also)

----------------------------------------------------------------------------------------------------------

### [sound classifier 평가하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)#Evaluating-a-sound-classifier)

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlsoundclassifier/trainingmetrics)

training dataset에서 classifier 성능을 측정한 값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlsoundclassifier/validationmetrics)

validation dataset에서 image classifier 성능을 측정한 값입니다.

현재 페이지: evaluation(on:)
