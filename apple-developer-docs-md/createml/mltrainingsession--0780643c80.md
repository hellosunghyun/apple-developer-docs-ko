---
title: "MLTrainingSession | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsession"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142151+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsession#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLTrainingSession

class

MLTrainingSession
=================

model의 asynchronous training session 현재 상태입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    final class MLTrainingSession<Task>

[주제](https://developer.apple.com/documentation/createml/mltrainingsession#topics)

--------------------------------------------------------------------------------------

### [training session 진행 상태 확인](https://developer.apple.com/documentation/createml/mltrainingsession#Checking-a-training-sessions-progress)

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mltrainingsession/phase)

training session의 현재 상태입니다.

[`enum MLPhase`](https://developer.apple.com/documentation/createml/mlphase)

training session이 가질 수 있는 상태입니다.

[`var iteration: Int`](https://developer.apple.com/documentation/createml/mltrainingsession/iteration)

training session phase의 iteration 번호입니다.

[`var checkpoints: [MLCheckpoint]`](https://developer.apple.com/documentation/createml/mltrainingsession/checkpoints)

지금까지 training session이 생성한 checkpoint array입니다.

### [checkpoint 제거](https://developer.apple.com/documentation/createml/mltrainingsession#Removing-checkpoints)

[`func removeCheckpoints((MLCheckpoint) -> Bool) throws`](https://developer.apple.com/documentation/createml/mltrainingsession/removecheckpoints(_:))

closure를 만족하는 checkpoint를 training session에서 제거합니다.

### [이전 session의 feature 재사용](https://developer.apple.com/documentation/createml/mltrainingsession#Reusing-features-from-a-previous-session)

[`func reuseExtractedFeatures(from: MLTrainingSession<Task>) throws`](https://developer.apple.com/documentation/createml/mltrainingsession/reuseextractedfeatures(from:))

다른 session이 dataset에서 이미 추출한 feature를 사용합니다.

### [session 검사](https://developer.apple.com/documentation/createml/mltrainingsession#Inspecting-a-session)

[`var date: Date`](https://developer.apple.com/documentation/createml/mltrainingsession/date)

이 training session을 생성한 시각입니다.

[`let parameters: MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsession/parameters)

training session 생성에 사용한 parameter입니다.

[관계](https://developer.apple.com/documentation/createml/mltrainingsession#relationships)

----------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mltrainingsession#conforms-to)

*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/createml/mltrainingsession#see-also)

------------------------------------------------------------------------------------------

### [Model training Control](https://developer.apple.com/documentation/createml/mltrainingsession#Model-training-Control)

[`class MLJob`](https://developer.apple.com/documentation/createml/mljob)

session 진행 상황을 모니터링하거나 실행을 종료할 때 사용하는 model의 asynchronous training session 표현입니다.

[`struct MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)

training session용 configuration setting입니다.

[`struct MLCheckpoint`](https://developer.apple.com/documentation/createml/mlcheckpoint)

feature extraction 또는 training phase의 특정 시점에서 model asynchronous training session 상태입니다.

현재 페이지: MLTrainingSession
