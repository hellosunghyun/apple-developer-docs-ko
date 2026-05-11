---
title: "evaluation(on:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133145+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTextClassifier](https://developer.apple.com/documentation/createml/mltextclassifier)
    
*   evaluation(on:)

instance method

evaluation(on:)
===============

evaluation metric을 계산합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+visionOS 1.0+

    func evaluation(on labeledTexts: MLTextClassifier.DataSource) -> MLClassifierMetrics

Show all declarations

[Parameters](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)#parameters)

-------------------------------------------------------------------------------------------------------------

`labeledTexts`

평가할 labeled text data source입니다.

[Return Value](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)#return-value)

-----------------------------------------------------------------------------------------------------------------

classifier metric입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)#see-also)

---------------------------------------------------------------------------------------------------------

### [Evaluating a text classifier](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)#Evaluating-a-text-classifier)

[`func evaluation(on:textColumn:labelColumn:)`](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:textcolumn:labelcolumn:))

evaluation metric을 계산합니다.

[`let trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mltextclassifier/trainingmetrics)

training data set에서 classifier 성능을 나타내는 측정값입니다.

[`let validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mltextclassifier/validationmetrics)

validation data set에서 classifier 성능을 나타내는 측정값입니다.

현재 페이지: evaluation(on:)
