---
title: "MLRecommenderMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlrecommendermetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.141758+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlrecommendermetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLRecommenderMetrics

struct

MLRecommenderMetrics
====================

recommender의 성능을 평가할 때 사용하는 metric입니다.

macOS 10.15+

    struct MLRecommenderMetrics

[주제](https://developer.apple.com/documentation/createml/mlrecommendermetrics#topics)

-----------------------------------------------------------------------------------------

### [model 평가하기](https://developer.apple.com/documentation/createml/mlrecommendermetrics#Assessing-the-model)

[`let excludingObserved: Bool`](https://developer.apple.com/documentation/createml/mlrecommendermetrics/excludingobserved)

recommender가 recommendation에서 training data를 제외했는지 나타내는 Boolean 값입니다.

[`var precisionRecall: MLDataTable`](https://developer.apple.com/documentation/createml/mlrecommendermetrics/precisionrecall)

각 item의 recall과 precision이 들어 있는 data table입니다.

Deprecated

[`var precisionRecallDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlrecommendermetrics/precisionrecalldataframe)

각 item의 recall과 precision이 들어 있는 data table입니다.

### [error 처리하기](https://developer.apple.com/documentation/createml/mlrecommendermetrics#Handling-errors)

[`var isValid: Bool`](https://developer.apple.com/documentation/createml/mlrecommendermetrics/isvalid)

recommender model이 metric을 계산할 수 있었는지 나타내는 Boolean 값입니다.

[`let error: (any Error)?`](https://developer.apple.com/documentation/createml/mlrecommendermetrics/error)

metric이 유효하지 않을 때 존재하는 기반 error입니다.

### [metric 만들기](https://developer.apple.com/documentation/createml/mlrecommendermetrics#Creating-metrics)

[`init(precisionRecall: MLDataTable, excludingObserved: Bool)`](https://developer.apple.com/documentation/createml/mlrecommendermetrics/init(precisionrecall:excludingobserved:))

precision과 recall metric column이 들어 있는 data table과 recommender가 training data를 제외했는지 여부를 받아 recommender용 metric을 만듭니다.

Deprecated

[같이 보기](https://developer.apple.com/documentation/createml/mlrecommendermetrics#see-also)

---------------------------------------------------------------------------------------------

### [Model accuracy](https://developer.apple.com/documentation/createml/mlrecommendermetrics#Model-accuracy)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

metric을 사용해 machine learning model의 성능을 조정합니다.

[`struct MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)

classifier의 성능을 평가할 때 사용하는 metric입니다.

[`struct MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)

regressor의 성능을 평가할 때 사용하는 metric입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger의 성능을 평가할 때 사용하는 metric입니다.

[`struct MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)

object detector의 성능을 평가할 때 사용하는 metric입니다.

현재 페이지: MLRecommenderMetrics
