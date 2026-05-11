---
title: "init(maximumError:rootMeanSquaredError:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlregressormetrics/init(maximumerror:rootmeansquarederror:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.140520+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlregressormetrics/init(maximumerror:rootmeansquarederror:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLRegressorMetrics](https://developer.apple.com/documentation/createml/mlregressormetrics)
    
*   init(maximumError:rootMeanSquaredError:)

이니셜라이저

init(maximumError:rootMeanSquaredError:)
========================================

model의 품질을 설명하는 regressor metric을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    init(
        maximumError: Double,
        rootMeanSquaredError: Double
    )

[파라미터](https://developer.apple.com/documentation/createml/mlregressormetrics/init(maximumerror:rootmeansquarederror:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------

`maximumError`

training data에 대한 model의 최대 error입니다.

`rootMeanSquaredError`

training data에 대한 model의 root mean squared error입니다.

[설명](https://developer.apple.com/documentation/createml/mlregressormetrics/init(maximumerror:rootmeansquarederror:)#discussion)

----------------------------------------------------------------------------------------------------------------------------------------

보통 metric을 직접 초기화하지는 않습니다. 대신 training 후 model의 metric을 가져옵니다. 예를 들어 [`MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)
를 training하면 [`trainingMetrics`](https://developer.apple.com/documentation/createml/mlregressor/trainingmetrics)
와 [`validationMetrics`](https://developer.apple.com/documentation/createml/mlregressor/validationmetrics)
 property를 확인할 수 있습니다. 추가로 [`evaluation(on:)`](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm)
 method로 test set에서의 성능을 확인할 수 있습니다.

현재 페이지는 init(maximumError:rootMeanSquaredError:)입니다
