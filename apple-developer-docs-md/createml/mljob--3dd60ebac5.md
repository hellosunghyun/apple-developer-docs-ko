---
title: "MLJob | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mljob"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.141959+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mljob#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLJob

class

MLJob
=====

session 진행 상황을 모니터링하거나 실행을 종료하는 데 사용하는 model의 asynchronous training session 표현입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    final class MLJob<Result>

[주제](https://developer.apple.com/documentation/createml/mljob#topics)

--------------------------------------------------------------------------

### [Receiving progress updates](https://developer.apple.com/documentation/createml/mljob#Receiving-progress-updates)

[`var checkpoints: AnyPublisher<MLCheckpoint, Never>`](https://developer.apple.com/documentation/createml/mljob/checkpoints)

session의 각 checkpoint interval마다 checkpoint를 보내는 publisher입니다.

[`var result: AnyPublisher<Result, any Error>`](https://developer.apple.com/documentation/createml/mljob/result)

training session이 끝나면 result를 제공하는 publisher입니다.

[`var phase: AnyPublisher<MLPhase, Never>`](https://developer.apple.com/documentation/createml/mljob/phase)

phase publisher입니다.

### [Managing a job](https://developer.apple.com/documentation/createml/mljob#Managing-a-job)

[`func cancel()`](https://developer.apple.com/documentation/createml/mljob/cancel())

training session 실행을 중지합니다.

[`var isCanceled: Bool`](https://developer.apple.com/documentation/createml/mljob/iscanceled)

job을 취소했는지 나타내는 Boolean 값입니다.

### [Inspecting a job](https://developer.apple.com/documentation/createml/mljob#Inspecting-a-job)

[`let startDate: Date`](https://developer.apple.com/documentation/createml/mljob/startdate)

training session이 시작한 날짜와 시간입니다.

[`let progress: Progress`](https://developer.apple.com/documentation/createml/mljob/progress)

training session의 현재 진행 상태입니다.

[`struct MLProgress`](https://developer.apple.com/documentation/createml/mlprogress)

training session progress 정보를 노출하는 convenience type입니다.

[관계](https://developer.apple.com/documentation/createml/mljob#relationships)

----------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mljob#conforms-to)

*   [`Cancellable`](https://developer.apple.com/documentation/Combine/Cancellable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mljob#see-also)

------------------------------------------------------------------------------

### [Model training Control](https://developer.apple.com/documentation/createml/mljob#Model-training-Control)

[`class MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)

model의 asynchronous training session 현재 상태입니다.

[`struct MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)

training session의 configuration 설정입니다.

[`struct MLCheckpoint`](https://developer.apple.com/documentation/createml/mlcheckpoint)

feature extraction 또는 training phase 중 특정 시점의 model asynchronous training session 상태입니다.

현재 페이지는 MLJob입니다
