---
title: "MLWordTaggerMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordtaggermetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.139334+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLWordTaggerMetrics

struct

MLWordTaggerMetrics
===================

word tagger 성능을 평가할 때 사용하는 metrics입니다.

macOS 10.14+

    struct MLWordTaggerMetrics

[언급 항목](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#mentions)

------------------------------------------------------------------------------------------------

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

[주제](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#topics)

----------------------------------------------------------------------------------------

### [tagger 성능 분석](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#Analyzing-the-taggers-performance)

[`var taggingError: Double`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/taggingerror)

잘못 tag된 example의 비율입니다.

[`var precisionRecall: MLDataTable`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecall)

각 category의 precision과 recall 비율을 나열한 data table입니다.

Deprecated

[`var confusion: MLDataTable`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/confusion)

각 tagging category의 actual label과 predicted label을 비교한 table입니다.

Deprecated

### [error 처리](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#Handling-errors)

[`var isValid: Bool`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/isvalid)

metrics가 계산되었는지 나타내는 Boolean value입니다.

[`var error: (any Error)?`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/error)

metrics가 올바르지 않을 때 존재하는 underlying error입니다.

### [metrics 설명](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#Describing-metrics)

[`var description: String`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/description)

word tagger metrics의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/debugdescription)

debugging 중 output에 적합한 word tagger metrics의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/playgrounddescription)

playground에 표시되는 word tagger metrics 설명입니다.

[`var confusionDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/confusiondataframe)

각 class의 actual label과 predicted label을 비교한 data frame입니다.

[`var precisionRecallDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecalldataframe)

각 class의 precision과 recall 비율을 나열한 data frame입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#relationships)

------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#see-also)

--------------------------------------------------------------------------------------------

### [Model 정확도](https://developer.apple.com/documentation/createml/mlwordtaggermetrics#Model-accuracy)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

machine learning model의 성능을 조정할 때 metrics를 사용합니다.

[`struct MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)

classifier 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)

regressor 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)

object detector 성능을 평가할 때 사용하는 metrics입니다.

현재 페이지는 MLWordTaggerMetrics
