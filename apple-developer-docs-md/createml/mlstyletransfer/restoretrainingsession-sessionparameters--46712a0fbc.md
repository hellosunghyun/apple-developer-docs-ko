---
title: "restoreTrainingSession(sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137122+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   restoreTrainingSession(sessionParameters:)

type method

restoreTrainingSession(sessionParameters:)
==========================================

기존 training session의 state를 parameter에서 복원해 style transfer model용 비동기 training session을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>

[parameter](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------

`sessionParameters`

The [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance you used to create the training session using [`makeTrainingSession(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:))
.

[Return Value](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:)#return-value)

-------------------------------------------------------------------------------------------------------------------------------------------

An [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
 that represents the style transfer model-training session.

[관련 항목](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------

### [style transfer model 비동기 training](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:)#Training-a-style-transfer-model-asynchronously)

[`static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:))

비동기 style transfer model training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:))

style transfer model용 비동기 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:))

비동기 style transfer model training session을 시작하거나 이어서 진행합니다.

현재 페이지는 restoreTrainingSession(sessionParameters:)
