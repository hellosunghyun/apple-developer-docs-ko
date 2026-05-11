---
title: "trainingMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133644+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLActionClassifier](https://developer.apple.com/documentation/createml/mlactionclassifier)
    
*   trainingMetrics

instance property

trainingMetrics
===============

action classifier가 training dataset에서 보인 성능 측정값입니다.

macOS 11.0+

    var trainingMetrics: MLClassifierMetrics { get }

[관련 항목](https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics#see-also)

-----------------------------------------------------------------------------------------------------------

### [action classifier 평가](https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics#Evaluating-an-action-classifier)

[`func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/evaluation(on:))

data source로 표현된 label된 video에 대한 action classifier의 성능을 설명하는 metrics를 생성합니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics)

action classifier가 validation dataset에서 보인 성능 측정값입니다.

현재 페이지: trainingMetrics
