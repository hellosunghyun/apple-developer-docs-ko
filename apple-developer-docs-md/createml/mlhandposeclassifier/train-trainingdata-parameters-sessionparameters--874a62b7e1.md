---
title: "train(trainingData:parameters:sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.141461+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   train(trainingData:parameters:sessionParameters:)

type method

train(trainingData:parameters:sessionParameters:)
=================================================

비동기 hand pose classifier training session을 시작합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    static func train(
        trainingData: MLHandPoseClassifier.DataSource,
        parameters: MLHandPoseClassifier.ModelParameters = ModelParameters(),
        sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters
    ) throws -> MLJob<MLHandPoseClassifier>

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------------------

`trainingData`

[`MLHandPoseClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource)
 instance입니다.

`parameters`

training session용 model을 구성하는 데 사용하는 [`MLHandPoseClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct)
 instance입니다.

`sessionParameters`

training session을 구성하는 데 사용하는 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:)#return-value)

-------------------------------------------------------------------------------------------------------------------------------------------------------

hand pose classifier의 training session을 나타내는 [`MLJob`](https://developer.apple.com/documentation/createml/mljob)
입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------------

### [비동기 hand pose classifier training하기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:)#Training-a-hand-pose-classifier-asynchronously)

[`static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

비동기 hand pose classifier training session을 생성합니다.

[`static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:))

비동기 hand pose classifier training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:))

file system에 저장된 상태를 복원해 비동기 hand pose classifier training session을 다시 만듭니다.

현재 페이지: train(trainingData:parameters:sessionParameters:)
