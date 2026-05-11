---
title: "MLCheckpoint | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcheckpoint"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.145598+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcheckpoint#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLCheckpoint

struct

MLCheckpoint
============

feature extraction 또는 training 단계 중 특정 시점에서의 model async training session 상태입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    struct MLCheckpoint

[주제](https://developer.apple.com/documentation/createml/mlcheckpoint#topics)

---------------------------------------------------------------------------------

### [Inspecting a checkpoint](https://developer.apple.com/documentation/createml/mlcheckpoint#Inspecting-a-checkpoint)

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mlcheckpoint/phase)

training session이 checkpoint를 만들었을 때의 phase입니다.

[`var iteration: Int`](https://developer.apple.com/documentation/createml/mlcheckpoint/iteration)

training session의 phase에서 checkpoint를 만들었을 때의 iteration 번호입니다.

[`var date: Date`](https://developer.apple.com/documentation/createml/mlcheckpoint/date)

training session이 checkpoint를 만든 시각입니다.

[`var url: URL`](https://developer.apple.com/documentation/createml/mlcheckpoint/url)

file system에서 checkpoint의 위치입니다.

### [Assessing a checkpoint](https://developer.apple.com/documentation/createml/mlcheckpoint#Assessing-a-checkpoint)

[`var metrics: [MLProgress.Metric : Any]`](https://developer.apple.com/documentation/createml/mlcheckpoint/metrics)

session이 checkpoint를 저장했을 당시 model 성능의 measurement입니다.

[`enum Metric`](https://developer.apple.com/documentation/createml/mlprogress/metric)

training session 중 model 성능을 평가할 때 사용하는 metric입니다.

### [Encoding and decoding a checkpoint](https://developer.apple.com/documentation/createml/mlcheckpoint#Encoding-and-decoding-a-checkpoint)

[`func encode(to: any Encoder) throws`](https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:))

checkpoint를 encoder에 인코딩합니다.

[`init(from: any Decoder) throws`](https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:))

decoder에서 디코딩해 새 checkpoint를 만듭니다.

[관계](https://developer.apple.com/documentation/createml/mlcheckpoint#relationships)

-----------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlcheckpoint#conforms-to)

*   [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable)
    
*   [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlcheckpoint#see-also)

-------------------------------------------------------------------------------------

### [Model training Control](https://developer.apple.com/documentation/createml/mlcheckpoint#Model-training-Control)

[`class MLJob`](https://developer.apple.com/documentation/createml/mljob)

session 진행 상황을 모니터링하거나 실행을 종료할 때 사용하는 model async training session 표현입니다.

[`class MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)

model async training session의 현재 상태입니다.

[`struct MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)

training session의 configuration setting입니다.

현재 페이지: MLCheckpoint
