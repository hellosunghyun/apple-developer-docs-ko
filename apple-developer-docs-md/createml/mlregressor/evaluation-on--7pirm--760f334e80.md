---
title: "evaluation(on:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142052+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLRegressor](https://developer.apple.com/documentation/createml/mlregressor)
    
*   *   [MLRegressor](https://developer.apple.com/documentation/createml/mlregressor)
        
*   evaluation(on:) Deprecated

instance method

evaluation(on:)
===============

제공한 labeled data로 classifier를 평가합니다.

macOS 10.14–13.0Deprecated

    func evaluation(on labeledData: MLDataTable) -> MLRegressorMetrics

모든 선언 보기

[parameter](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm#parameters)

--------------------------------------------------------------------------------------------------------------

`labeledData`

training된 model을 평가할 `MLDataTable`입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm#return-value)

------------------------------------------------------------------------------------------------------------------

최대 error([`maximumError`](https://developer.apple.com/documentation/createml/mlregressormetrics/maximumerror)
) 또는 평균 error([`rootMeanSquaredError`](https://developer.apple.com/documentation/createml/mlregressormetrics/rootmeansquarederror)
)를 설명하는 metrics입니다.

[설명](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm#discussion)

--------------------------------------------------------------------------------------------------------------

evaluation은 model이 training 또는 validation data set에서 보지 않은 testing data set으로 수행해야 합니다. 이 data에는 training data와 이름과 type이 같은 feature column이 있어야 하며, labels column 이름도 같아야 합니다.

현재 페이지는 evaluation(on:)
