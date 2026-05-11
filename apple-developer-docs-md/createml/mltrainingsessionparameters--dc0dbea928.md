---
title: "MLTrainingSessionParameters | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsessionparameters"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.145371+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLTrainingSessionParameters

struct

MLTrainingSessionParameters
===========================

training session의 configuration 설정입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    struct MLTrainingSessionParameters

[주제](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#topics)

------------------------------------------------------------------------------------------------

### [session parameters 만들기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#Creating-a-sessions-parameters)

[`init(sessionDirectory: URL?, reportInterval: Int, checkpointInterval: Int, iterations: Int)`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/init(sessiondirectory:reportinterval:checkpointinterval:iterations:))

training session용 parameter 집합을 생성합니다.

### [session parameters 구성하기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#Configuring-the-sessions-parameters)

[`let sessionDirectory: URL?`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory)

session이 진행 상황을 저장하는 file system 위치입니다.

[`var reportInterval: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/reportinterval)

session이 진행 상황을 보고하기 전에 완료하는 iteration 수입니다.

[`var checkpointInterval: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/checkpointinterval)

session이 checkpoint를 저장하기 전에 완료하는 iteration 수입니다.

[`var iterations: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations)

training session의 최대 iteration 수입니다.

[관계](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#relationships)

--------------------------------------------------------------------------------------------------------------

### [준수 대상](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#conforms-to)

*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#see-also)

----------------------------------------------------------------------------------------------------

### [model training control](https://developer.apple.com/documentation/createml/mltrainingsessionparameters#Model-training-Control)

[`class MLJob`](https://developer.apple.com/documentation/createml/mljob)

session의 진행 상황을 모니터링하거나 실행을 종료하는 데 사용하는 model의 asynchronous training session 표현입니다.

[`class MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)

model의 asynchronous training session의 현재 상태입니다.

[`struct MLCheckpoint`](https://developer.apple.com/documentation/createml/mlcheckpoint)

feature extraction 또는 training 단계 중 특정 시점의 model asynchronous training session 상태입니다.

현재 페이지는 MLTrainingSessionParameters입니다
