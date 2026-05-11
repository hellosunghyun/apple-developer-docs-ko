---
title: "MLProgress | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlprogress"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.156690+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlprogress#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLProgress

struct

MLProgress
==========

training session 진행 상황 정보를 노출하는 convenience type입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    struct MLProgress

[개요](https://developer.apple.com/documentation/createml/mlprogress#overview)

-----------------------------------------------------------------------------------

Create ML은 _Progress_ instance 안의 특정 값을 property로 노출할 때 이 type을 사용합니다.

[주제](https://developer.apple.com/documentation/createml/mlprogress#topics)

-------------------------------------------------------------------------------

### [Creating a training progress update](https://developer.apple.com/documentation/createml/mlprogress#Creating-a-training-progress-update)

[`init(phase: MLPhase)`](https://developer.apple.com/documentation/createml/mlprogress/init(phase:))

training phase에서 training session progress instance를 생성합니다.

[`init?(progress: Progress)`](https://developer.apple.com/documentation/createml/mlprogress/init(progress:))

foundation progress object에서 training session progress instance를 생성합니다.

### [Inspecting a session’s progress](https://developer.apple.com/documentation/createml/mlprogress#Inspecting-a-sessions-progress)

[`var elapsedTime: TimeInterval`](https://developer.apple.com/documentation/createml/mlprogress/elapsedtime)

training session이 시작된 뒤 경과한 시간(초)입니다.

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mlprogress/phase)

training session의 현재 phase입니다.

[`var itemCount: Int`](https://developer.apple.com/documentation/createml/mlprogress/itemcount)

feature extraction phase 동안 처리한 현재 file 수 또는 training phase 동안 완료한 iteration 수입니다.

[`var totalItemCount: Int?`](https://developer.apple.com/documentation/createml/mlprogress/totalitemcount)

feature extraction phase의 전체 file 수 또는 training phase의 전체 iteration 수입니다.

[`var metrics: [MLProgress.Metric : Any]`](https://developer.apple.com/documentation/createml/mlprogress/metrics)

training session의 training 또는 evaluation phase 동안 model 성능을 나타내는 측정값입니다.

[`enum Metric`](https://developer.apple.com/documentation/createml/mlprogress/metric)

training session 동안 model 성능을 평가할 때 사용하는 metric입니다.

### [Accessing general information](https://developer.apple.com/documentation/createml/mlprogress#Accessing-general-information)

[`static let elapsedTimeKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/elapsedtimekey)

elapsed time 값에 접근하는 key입니다.

[`static let phaseKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/phasekey)

현재 phase 값에 접근하는 key입니다.

[`static let itemCountKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/itemcountkey)

현재 item count 값에 접근하는 key입니다.

[`static let totalItemCountKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/totalitemcountkey)

전체 item count 값에 접근하는 key입니다.

### [Accessing assessment metrics](https://developer.apple.com/documentation/createml/mlprogress#Accessing-assessment-metrics)

[`static let accuracyKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/accuracykey)

training accuracy 값에 접근하는 key입니다.

[`static let lossKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/losskey)

training loss 값에 접근하는 key입니다.

[`static let validationAccuracyKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/validationaccuracykey)

validation accuracy 값에 접근하는 key입니다.

[`static let validationLossKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/validationlosskey)

validation loss 값에 접근하는 key입니다.

### [Accessing style transfer metrics](https://developer.apple.com/documentation/createml/mlprogress#Accessing-style-transfer-metrics)

[`static let contentLossKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/contentlosskey)

content image loss 값에 접근하는 key입니다.

[`static let styleLossKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/stylelosskey)

style image loss 값에 접근하는 key입니다.

[`static let stylizedImageKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/stylizedimagekey)

stylized image 값에 접근하는 key입니다.

### [Accessing error information](https://developer.apple.com/documentation/createml/mlprogress#Accessing-error-information)

[`static let maximumErrorKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/maximumerrorkey)

maximum error 값에 접근하는 key입니다.

[`static let rootMeanSquaredErrorKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/rootmeansquarederrorkey)

root-mean-squared error 값에 접근하는 key입니다.

[`static let validationMaximumErrorKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/validationmaximumerrorkey)

validation maximum error 값에 접근하는 key입니다.

[`static let validationRootMeanSquaredErrorKey: ProgressUserInfoKey`](https://developer.apple.com/documentation/createml/mlprogress/validationrootmeansquarederrorkey)

validation root-mean-squared error 값에 접근하는 key입니다.

### [Encoding and decoding a session’s progress](https://developer.apple.com/documentation/createml/mlprogress#Encoding-and-decoding-a-sessions-progress)

[`func encode(to: any Encoder) throws`](https://developer.apple.com/documentation/createml/mlprogress/encode(to:))

progress 값을 지정한 encoder에 인코딩합니다.

[`init(from: any Decoder) throws`](https://developer.apple.com/documentation/createml/mlprogress/init(from:))

지정한 decoder에서 decoding해 progress instance를 생성합니다.

[관계](https://developer.apple.com/documentation/createml/mlprogress#relationships)

---------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlprogress#conforms-to)

*   [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable)
    
*   [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlprogress#see-also)

-----------------------------------------------------------------------------------

### [Inspecting a job](https://developer.apple.com/documentation/createml/mlprogress#Inspecting-a-job)

[`let startDate: Date`](https://developer.apple.com/documentation/createml/mljob/startdate)

training session이 시작된 날짜와 시간입니다.

[`let progress: Progress`](https://developer.apple.com/documentation/createml/mljob/progress)

training session의 현재 progress입니다.

현재 페이지: MLProgress
