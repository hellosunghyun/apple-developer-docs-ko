---
title: "resume(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137259+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   resume(\_:)

type method

resume(\_:)
===========

비동기 style transfer model-training session을 시작하거나 이어서 진행합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func resume(_ session: MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>

[Parameters](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:)#parameters)

-------------------------------------------------------------------------------------------------------

`session`

training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
 instance입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:)#return-value)

-----------------------------------------------------------------------------------------------------------

style transfer model-training session을 나타내는 [`MLJob`](https://developer.apple.com/documentation/createml/mljob)
입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:)#see-also)

---------------------------------------------------------------------------------------------------

### [비동기로 style transfer model training하기](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:)#Training-a-style-transfer-model-asynchronously)

[`static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:))

비동기 style transfer model-training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:))

style transfer model용 비동기 training session을 생성합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:))

기존 training session의 state를 parameters에서 복원해 style transfer model용 비동기 training session을 생성합니다.

현재 페이지는 resume(\_:)입니다
