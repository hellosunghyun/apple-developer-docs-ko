---
title: "MLRegressorMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlregressormetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.139233+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlregressormetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLRegressorMetrics

struct

MLRegressorMetrics
==================

regressor의 성능을 평가할 때 사용하는 metric입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    struct MLRegressorMetrics

[언급된 문서](https://developer.apple.com/documentation/createml/mlregressormetrics#mentions)

-----------------------------------------------------------------------------------------------

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[개요](https://developer.apple.com/documentation/createml/mlregressormetrics#overview)

-------------------------------------------------------------------------------------------

regressor에서 기대할 수 있는 성능을 이해하려면 먼저 [`maximumError`](https://developer.apple.com/documentation/createml/mlregressormetrics/maximumerror)
를 살펴봅니다. 이 high-level metric은 model의 최악의 경우 성능을 나타냅니다. model이 평균적으로 어떻게 동작하는지 파악하려면 [`rootMeanSquaredError`](https://developer.apple.com/documentation/createml/mlregressormetrics/rootmeansquarederror)
를 확인합니다. 두 경우 모두 값을 최소화해 error를 줄이는 것이 목표입니다.

[주제](https://developer.apple.com/documentation/createml/mlregressormetrics#topics)

---------------------------------------------------------------------------------------

### [Understanding the model](https://developer.apple.com/documentation/createml/mlregressormetrics#Understanding-the-model)

[`var maximumError: Double`](https://developer.apple.com/documentation/createml/mlregressormetrics/maximumerror)

testing 또는 training 중 기대값과 model 예측값 사이의 절대 차이 중 가장 큰 값입니다.

[`var rootMeanSquaredError: Double`](https://developer.apple.com/documentation/createml/mlregressormetrics/rootmeansquarederror)

정답값과 예측값 사이의 편차를 판단할 때 자주 사용하는 metric입니다.

### [Handling errors](https://developer.apple.com/documentation/createml/mlregressormetrics#Handling-errors)

[`var isValid: Bool`](https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid)

regressor model이 metric을 계산할 수 있었는지 나타내는 Boolean value입니다.

[`var error: (any Error)?`](https://developer.apple.com/documentation/createml/mlregressormetrics/error)

metric이 유효하지 않을 때 존재하는 underlying error입니다.

### [Creating metrics](https://developer.apple.com/documentation/createml/mlregressormetrics#Creating-metrics)

[`init(maximumError: Double, rootMeanSquaredError: Double)`](https://developer.apple.com/documentation/createml/mlregressormetrics/init(maximumerror:rootmeansquarederror:))

model의 품질을 설명하는 regressor metric을 생성합니다.

### [Describing metrics](https://developer.apple.com/documentation/createml/mlregressormetrics#Describing-metrics)

[`var description: String`](https://developer.apple.com/documentation/createml/mlregressormetrics/description)

regressor metric의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlregressormetrics/debugdescription)

debugging 중 출력하기에 적합한 regressor metric의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlregressormetrics/playgrounddescription)

playground에 표시되는 regressor metric의 설명입니다.

### [Default Implementations](https://developer.apple.com/documentation/createml/mlregressormetrics#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlregressormetrics/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlregressormetrics/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlregressormetrics/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlregressormetrics#relationships)

-----------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlregressormetrics#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlregressormetrics#see-also)

-------------------------------------------------------------------------------------------

### [Model accuracy](https://developer.apple.com/documentation/createml/mlregressormetrics#Model-accuracy)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

metric을 사용해 machine learning model의 성능을 조정합니다.

[`struct MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)

classifier의 성능을 평가할 때 사용하는 metric입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger의 성능을 평가할 때 사용하는 metric입니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender의 성능을 평가할 때 사용하는 metric입니다.

[`struct MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)

object detector의 성능을 평가할 때 사용하는 metric입니다.

현재 페이지: MLRegressorMetrics
