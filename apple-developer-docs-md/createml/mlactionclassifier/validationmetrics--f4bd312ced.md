---
title: "validationMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133541+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLActionClassifier](https://developer.apple.com/documentation/createml/mlactionclassifier)
    
*   validationMetrics

instance property

validationMetrics
=================

validation dataset에서 action classifier 성능을 나타내는 측정값입니다.

macOS 11.0+

    var validationMetrics: MLClassifierMetrics { get }

[같이 보기](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics#see-also)

-------------------------------------------------------------------------------------------------------------

### [action classifier 평가하기](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics#Evaluating-an-action-classifier)

[`func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/evaluation(on:))

data source로 표현한 labeled video에서 action classifier의 성능을 설명하는 metrics를 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics)

training dataset에서 action classifier 성능을 나타내는 측정값입니다.

현재 페이지: validationMetrics
