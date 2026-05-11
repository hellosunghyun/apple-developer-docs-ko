---
title: "makeTrainingSession(trainingData:parameters:sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.141355+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   makeTrainingSession(trainingData:parameters:sessionParameters:)

type method

makeTrainingSession(trainingData:parameters:sessionParameters:)
===============================================================

async hand pose classifier의 training session을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    static func makeTrainingSession(
        trainingData: MLHandPoseClassifier.DataSource,
        parameters: MLHandPoseClassifier.ModelParameters = .init(),
        sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters
    ) throws -> MLTrainingSession<MLHandPoseClassifier>

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

`trainingData`

[`MLHandPoseClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource)
instance입니다.

`parameters`

training session용 model을 구성할 때 사용하는 [`MLHandPoseClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct)
instance입니다.

`sessionParameters`

training session을 구성할 때 사용하는 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
instance입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#return-value)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

action classifier training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Training a hand pose classifier asynchronously](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#Training-a-hand-pose-classifier-asynchronously)

[`static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:))

async hand pose classifier의 training session을 시작합니다.

[`static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:))

async hand pose classifier의 training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:))

저장된 state를 file system에서 복원해 async hand pose classifier의 training session을 다시 만듭니다.

현재 페이지: makeTrainingSession(trainingData:parameters:sessionParameters:)
