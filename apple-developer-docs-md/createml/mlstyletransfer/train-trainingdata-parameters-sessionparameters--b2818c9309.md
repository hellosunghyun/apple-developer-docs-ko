---
title: "train(trainingData:parameters:sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137580+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   train(trainingData:parameters:sessionParameters:)

type method

train(trainingData:parameters:sessionParameters:)
=================================================

asynchronous style transfer model training session을 시작합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func train(
        trainingData: MLStyleTransfer.DataSource,
        parameters: MLStyleTransfer.ModelParameters = .init(),
        sessionParameters: MLTrainingSessionParameters = .init()
    ) throws -> MLJob<MLStyleTransfer>

[parameter](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------------

`trainingData`

style image와 content image를 data source로 표현한 값입니다.

`parameters`

training session용 model을 구성할 때 사용하는 [`MLStyleTransfer.ModelParameters`](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters)
 instance입니다.

`sessionParameters`

training session을 구성할 때 사용하는 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:)#return-value)

--------------------------------------------------------------------------------------------------------------------------------------------------

style transfer model training session을 나타내는 [`MLJob`](https://developer.apple.com/documentation/createml/mljob)
 입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------

### [style transfer model을 비동기로 training하기](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:)#Training-a-style-transfer-model-asynchronously)

[`static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:))

style transfer model용 asynchronous training session을 만듭니다.

[`static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:))

asynchronous style transfer model training session을 시작하거나 계속합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:))

기존 training session의 state를 parameter에서 복원해 style transfer model용 asynchronous training session을 만듭니다.

현재 페이지: train(trainingData:parameters:sessionParameters:)
