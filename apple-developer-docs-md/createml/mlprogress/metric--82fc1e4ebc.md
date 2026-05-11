---
title: "MLProgress.Metric | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlprogress/metric"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.149259+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlprogress/metric#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLProgress](https://developer.apple.com/documentation/createml/mlprogress)
    
*   MLProgress.Metric

enum

MLProgress.Metric
=================

training session 동안 model 성능을 평가할 때 사용하는 metric입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    enum Metric

[주제](https://developer.apple.com/documentation/createml/mlprogress/metric#topics)

--------------------------------------------------------------------------------------

### [metric key 가져오기](https://developer.apple.com/documentation/createml/mlprogress/metric#Retrieving-metric-keys)

[`case accuracy`](https://developer.apple.com/documentation/createml/mlprogress/metric/accuracy)

model accuracy용 metric입니다.

[`case contentLoss`](https://developer.apple.com/documentation/createml/mlprogress/metric/contentloss)

style transfer model의 content loss용 metric입니다.

[`case loss`](https://developer.apple.com/documentation/createml/mlprogress/metric/loss)

model loss용 metric입니다.

[`case maximumError`](https://developer.apple.com/documentation/createml/mlprogress/metric/maximumerror)

model maximum error용 metric입니다.

[`case rootMeanSquaredError`](https://developer.apple.com/documentation/createml/mlprogress/metric/rootmeansquarederror)

model root mean squared error(RMSE)용 metric입니다.

[`case styleLoss`](https://developer.apple.com/documentation/createml/mlprogress/metric/styleloss)

style transfer model의 style loss용 metric입니다.

[`case stylizedImageURL`](https://developer.apple.com/documentation/createml/mlprogress/metric/stylizedimageurl)

file system에서 stylized image content의 위치입니다.

[`case validationAccuracy`](https://developer.apple.com/documentation/createml/mlprogress/metric/validationaccuracy)

model validation accuracy용 metric입니다.

[`case validationLoss`](https://developer.apple.com/documentation/createml/mlprogress/metric/validationloss)

model validation loss용 metric입니다.

[`case validationMaximumError`](https://developer.apple.com/documentation/createml/mlprogress/metric/validationmaximumerror)

model validation maximum error용 metric입니다.

[`case validationRootMeanSquaredError`](https://developer.apple.com/documentation/createml/mlprogress/metric/validationrootmeansquarederror)

model validation root mean squared error(RMSE)용 metric입니다.

[관계](https://developer.apple.com/documentation/createml/mlprogress/metric#relationships)

----------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlprogress/metric#conforms-to)

*   [`CaseIterable`](https://developer.apple.com/documentation/Swift/CaseIterable)
    
*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable)
    
*   [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/createml/mlprogress/metric#see-also)

------------------------------------------------------------------------------------------

### [checkpoint 평가](https://developer.apple.com/documentation/createml/mlprogress/metric#Assessing-a-checkpoint)

[`var metrics: [MLProgress.Metric : Any]`](https://developer.apple.com/documentation/createml/mlcheckpoint/metrics)

session이 checkpoint를 저장했을 당시 model 성능 측정값입니다.

현재 페이지: MLProgress.Metric
