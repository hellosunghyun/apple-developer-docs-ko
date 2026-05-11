---
title: "restoreTrainingSession(sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.138553+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   restoreTrainingSession(sessionParameters:)

type method

restoreTrainingSession(sessionParameters:)
==========================================

저장된 state를 file system에서 복원해 asynchronous hand pose classifier의 training session을 다시 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>

[parameter](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------

`sessionParameters`

기존 training session을 만들 때 사용한 것과 동일한 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:)#return-value)

------------------------------------------------------------------------------------------------------------------------------------------------

hand pose classifier training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
 입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------

### [hand pose classifier를 비동기로 training하기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:)#Training-a-hand-pose-classifier-asynchronously)

[`static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:))

asynchronous hand pose classifier의 training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

asynchronous hand pose classifier의 training session을 만듭니다.

[`static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:))

asynchronous hand pose classifier의 training session을 시작하거나 계속합니다.

현재 페이지: restoreTrainingSession(sessionParameters:)
