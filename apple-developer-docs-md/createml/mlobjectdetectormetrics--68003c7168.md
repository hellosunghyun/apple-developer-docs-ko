---
title: "MLObjectDetectorMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlobjectdetectormetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.141855+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLObjectDetectorMetrics

struct

MLObjectDetectorMetrics
=======================

object detector 성능을 평가할 때 사용하는 metric입니다.

macOS 10.15+

    struct MLObjectDetectorMetrics

[개요](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#overview)

------------------------------------------------------------------------------------------------

object detector는 intersection-over-union(IoU) metric을 생성합니다. 이는 두 bounding box의 유사도를 측정하는 방법입니다. IoU metric은 겹치는 영역을 bounding box union의 전체 영역으로 나눈 값입니다.

예를 들어 두 bounding box가 완전히 겹치면 overlap 영역이 union과 같으므로 IoU는 `1.0`입니다. 두 bounding box가 전혀 겹치지 않으면 IoU는 `0.0`입니다. `0.0`과 `1.0` 사이 값은 두 bounding box가 부분적으로 겹치거나 한 box가 다른 box를 완전히 감싸는 경우를 의미합니다.

[주제](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#topics)

--------------------------------------------------------------------------------------------

### [Creating metrics](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#Creating-metrics)

[`init(averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double]), meanAveragePrecision: (variedIoU: Double, IoU50: Double))`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/init(averageprecision:meanaverageprecision:))

average precision과 mean average precision으로 object detector metric을 생성합니다.

### [Assessing the model](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#Assessing-the-model)

[`var averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double])`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision)

서로 다른 threshold에서 계산한 average precision dictionary 두 개입니다.

[`var meanAveragePrecision: (variedIoU: Double, IoU50: Double)`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/meanaverageprecision)

서로 다른 threshold에서 계산한 mean average precision 두 개입니다.

### [Handling errors](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#Handling-errors)

[`var isValid: Bool`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/isvalid)

object detector model이 metric을 계산할 수 있었는지 나타내는 Boolean 값입니다.

[`var error: (any Error)?`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/error)

metric이 유효하지 않을 때 포함되는 underlying error입니다.

### [Describing metrics](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#Describing-metrics)

[`var description: String`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/description)

object detector metric의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/debugdescription)

debugging 중 output에 적합한 object detector metric의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/playgrounddescription)

playground에 표시하는 object detector metric 설명입니다.

### [Default Implementations](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#relationships)

----------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#see-also)

------------------------------------------------------------------------------------------------

### [Model accuracy](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics#Model-accuracy)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

metric을 사용해 machine learning model의 성능을 조정합니다.

[`struct MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)

classifier 성능을 평가할 때 사용하는 metric입니다.

[`struct MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)

regressor 성능을 평가할 때 사용하는 metric입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger 성능을 평가할 때 사용하는 metric입니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender 성능을 평가할 때 사용하는 metric입니다.

현재 페이지: MLObjectDetectorMetrics
