---
title: "resume(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.138650+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   resume(\_:)

type method

resume(\_:)
===========

비동기 hand pose classifier의 training session을 시작하거나 계속 진행합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    static func resume(_ session: MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:)#parameters)

------------------------------------------------------------------------------------------------------------

`session`

training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
 instance입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:)#return-value)

----------------------------------------------------------------------------------------------------------------

hand pose training session을 나타내는 [`MLJob`](https://developer.apple.com/documentation/createml/mljob)
 입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:)#see-also)

--------------------------------------------------------------------------------------------------------

### [Training a hand pose classifier asynchronously](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:)#Training-a-hand-pose-classifier-asynchronously)

[`static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:))

비동기 hand pose classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

비동기 hand pose classifier training session을 생성합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:))

file system에 저장된 state를 복원해 비동기 hand pose classifier training session을 다시 만듭니다.

현재 페이지: resume(\_:)
