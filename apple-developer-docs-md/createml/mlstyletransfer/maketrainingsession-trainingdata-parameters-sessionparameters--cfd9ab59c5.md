---
title: "makeTrainingSession(trainingData:parameters:sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137458+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   makeTrainingSession(trainingData:parameters:sessionParameters:)

type method

makeTrainingSession(trainingData:parameters:sessionParameters:)
===============================================================

style transfer model용 비동기 training session을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func makeTrainingSession(
        trainingData: MLStyleTransfer.DataSource,
        parameters: MLStyleTransfer.ModelParameters = .init(),
        sessionParameters: MLTrainingSessionParameters = .init()
    ) throws -> MLTrainingSession<MLStyleTransfer>

[Parameters](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------------------------------

`trainingData`

data source로 표현되는 style image와 content image입니다.

`parameters`

training session용 model을 구성할 때 사용하는 [`MLStyleTransfer.ModelParameters`](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters)
 instance입니다.

`sessionParameters`

training session을 구성할 때 사용하는 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:)#return-value)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

style transfer model training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:)#see-also)

--------------------------------------------------------------------------------------------------------------------------------------------------------

### [style transfer model 비동기 training하기](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:)#Training-a-style-transfer-model-asynchronously)

[`static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:))

비동기 style transfer model training session을 시작합니다.

[`static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:))

비동기 style transfer model training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:))

기존 training session의 상태를 parameter에서 복원해 style transfer model용 비동기 training session을 생성합니다.

현재 페이지: makeTrainingSession(trainingData:parameters:sessionParameters:)
