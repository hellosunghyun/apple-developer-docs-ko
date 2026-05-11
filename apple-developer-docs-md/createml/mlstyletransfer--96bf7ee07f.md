---
title: "MLStyleTransfer | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130798+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLStyleTransfer

struct

MLStyleTransfer
===============

image의 style을 다른 image나 video에 적용하도록 training하는 model입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    struct MLStyleTransfer

[주제](https://developer.apple.com/documentation/createml/mlstyletransfer#topics)

------------------------------------------------------------------------------------

### [style transfer model 비동기 training](https://developer.apple.com/documentation/createml/mlstyletransfer#Training-a-style-transfer-model-asynchronously)

[`static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:))

비동기 style transfer model-training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:))

style transfer model을 위한 비동기 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:))

비동기 style transfer model-training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>`](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:))

기존 training session 상태를 parameter에서 복원해 style transfer model용 비동기 training session을 생성합니다.

### [checkpoint에서 style transfer model 생성하기](https://developer.apple.com/documentation/createml/mlstyletransfer#Creating-a-style-transfer-model-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/init(checkpoint:))

training session checkpoint에서 style transfer model을 생성합니다.

### [style transfer model 동기 training](https://developer.apple.com/documentation/createml/mlstyletransfer#Training-a-style-transfer-model-synchronously)

[`init(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/init(trainingdata:parameters:))

data source로 표현된 training dataset으로 style transfer model을 생성합니다.

### [image 스타일 적용하기](https://developer.apple.com/documentation/createml/mlstyletransfer#Stylizing-an-image)

[`func stylize(image: CGImage) throws -> CGImage?`](https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:))

model이 학습한 style을 image에 적용합니다.

### [style transfer model 저장하기](https://developer.apple.com/documentation/createml/mlstyletransfer#Saving-a-style-transfer-model)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:))

style transfer model을 file system의 위치에 Core ML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:))

style transfer model을 file path에 Core ML model file로 내보냅니다.

### [model asset 다운로드하기](https://developer.apple.com/documentation/createml/mlstyletransfer#Downloading-model-assets)

[`static func downloadAssets() throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/downloadassets())

Style Transfer training에 필요한 mlmodel asset 다운로드를 시작합니다. 필요할 때 training 시 자동으로 수행되지만, training 전에 독립적으로 실행할 수도 있습니다.

### [style transfer model 설명하기](https://developer.apple.com/documentation/createml/mlstyletransfer#Describing-a-style-transfer-model)

[`var description: String`](https://developer.apple.com/documentation/createml/mlstyletransfer/description)

style transfer model의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlstyletransfer/debugdescription)

debugging 출력에 적합한 style transfer model의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlstyletransfer/playgrounddescription)

playground에 표시되는 style transfer model 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlstyletransfer#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlstyletransfer/datasource)

style transfer model용 data source입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters)

style transfer model의 training process에 영향을 주는 parameter입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlstyletransfer#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlstyletransfer/customdebugstringconvertible-implementations)

[API Reference: CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlstyletransfer/customplaygrounddisplayconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlstyletransfer/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlstyletransfer#relationships)

--------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlstyletransfer#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlstyletransfer#see-also)

----------------------------------------------------------------------------------------

### [Video model](https://developer.apple.com/documentation/createml/mlstyletransfer#Video-models)

[Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)

사람의 body movement를 인식하는 machine learning model을 training합니다.

[실시간 video feed에서 human action 감지하기](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed)

video frame series의 pose data를 action-classification model로 보내 body movement를 식별합니다.

[`struct MLActionClassifier`](https://developer.apple.com/documentation/createml/mlactionclassifier)

video로 사람의 body movement를 분류하도록 training하는 model입니다.

[`struct MLHandActionClassifier`](https://developer.apple.com/documentation/createml/mlhandactionclassifier)

제공한 사람 손동작 video로 training해 hand action classification model을 만드는 task입니다.

현재 페이지: MLStyleTransfer
