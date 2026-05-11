---
title: "MLClassifierMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlclassifiermetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132669+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlclassifiermetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLClassifierMetrics

구조

MLClassifierMetrics
===================

classifier 성능을 평가할 때 사용하는 metrics입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    struct MLClassifierMetrics

[언급 문서](https://developer.apple.com/documentation/createml/mlclassifiermetrics#mentions)

------------------------------------------------------------------------------------------------

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

[Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[개요](https://developer.apple.com/documentation/createml/mlclassifiermetrics#overview)

--------------------------------------------------------------------------------------------

[`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
를 사용해 data를 분류할 때 model이 서로 다른 category를 구분하는 능력을 평가합니다.

[`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
 metric으로 model accuracy를 확인할 수 있습니다. model이 특정 category를 잘못 label하거나 놓치는 방식을 보려면 [`precisionRecall`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)
 metric을 사용합니다. model이 한 label을 다른 label로 혼동하는 구체적인 경우를 확인하려면 [`confusion`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)
 property를 사용합니다.

unbalanced data를 사용하면 accuracy는 오해를 부를 수 있습니다. 이는 일부 category의 example 수가 다른 category보다 훨씬 많다는 뜻입니다. 이런 경우에는 [`precisionRecall`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)
 또는 [`confusion`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)
을 사용합니다.

[주제](https://developer.apple.com/documentation/createml/mlclassifiermetrics#topics)

----------------------------------------------------------------------------------------

### [model 이해하기](https://developer.apple.com/documentation/createml/mlclassifiermetrics#Understanding-the-model)

[`var classificationError: Double`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)

잘못 label된 example의 비율입니다.

[`var precisionRecall: MLDataTable`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)

각 class의 precision 및 recall 백분율을 나열한 data table입니다.

[`var confusion: MLDataTable`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)

각 classification category의 실제 label과 예측 label을 비교하는 table입니다.

[`var confusionDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe)

각 class의 실제 label과 예측 label을 비교하는 data frame입니다.

[`var precisionRecallDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecalldataframe)

각 class의 precision 및 recall 백분율을 나열한 data frame입니다.

### [error 처리](https://developer.apple.com/documentation/createml/mlclassifiermetrics#Handling-errors)

[`var isValid: Bool`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/isvalid)

classifier model이 metrics를 계산할 수 있었는지 나타내는 Boolean 값입니다.

[`var error: (any Error)?`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/error)

metrics가 유효하지 않을 때의 underlying error입니다.

### [metrics 만들기](https://developer.apple.com/documentation/createml/mlclassifiermetrics#Creating-metrics)

[`init(classificationError: Double, confusion: MLDataTable, precisionRecall: MLDataTable)`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/init(classificationerror:confusion:precisionrecall:))

빈 classifier metrics를 만듭니다.

### [metrics 설명](https://developer.apple.com/documentation/createml/mlclassifiermetrics#Describing-metrics)

[`var description: String`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/description)

classifier metrics의 텍스트 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/debugdescription)

debugging 중 출력하기에 적합한 classifier metrics의 텍스트 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/playgrounddescription)

playground에 표시되는 classifier metrics 설명입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlclassifiermetrics#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlclassifiermetrics/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlclassifiermetrics/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlclassifiermetrics/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlclassifiermetrics#relationships)

------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlclassifiermetrics#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlclassifiermetrics#see-also)

--------------------------------------------------------------------------------------------

### [Model 정확도](https://developer.apple.com/documentation/createml/mlclassifiermetrics#Model-accuracy)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

metrics를 사용해 machine learning model 성능을 조정합니다.

[`struct MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)

regressor 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)

object detector 성능을 평가할 때 사용하는 metrics입니다.

현재 페이지: MLClassifierMetrics
