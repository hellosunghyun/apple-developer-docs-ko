---
title: "MLHandActionClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandactionclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131219+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandactionclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLHandActionClassifier

struct

MLHandActionClassifier
======================

제공한 사람 손동작 video로 training해 hand action classification model을 만드는 task입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    struct MLHandActionClassifier

[주제](https://developer.apple.com/documentation/createml/mlhandactionclassifier#topics)

-------------------------------------------------------------------------------------------

### [Training a hand action classifier asynchronously](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Training-a-hand-action-classifier-asynchronously)

[`static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/train(trainingdata:parameters:sessionparameters:))

async hand action classifier의 training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

async hand action classifier의 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/resume(_:))

async hand action classifier의 training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/restoretrainingsession(sessionparameters:))

저장된 state를 file system에서 복원해 async hand action classifier의 training session을 다시 만듭니다.

### [Creating a hand action classifier from a checkpoint](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Creating-a-hand-action-classifier-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/init(checkpoint:))

training session checkpoint에서 hand action classifier를 만듭니다.

### [Training a hand action classifier synchronously](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Training-a-hand-action-classifier-synchronously)

[`init(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/init(trainingdata:parameters:))

synchronous training session을 시작해 hand action classifier를 만듭니다.

### [Evaluating a hand action classifier](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Evaluating-a-hand-action-classifier)

[`func evaluation(on: MLHandActionClassifier.DataSource) throws -> MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/evaluation(on:))

label이 지정된 video에서 hand action classifier의 성능을 설명하는 metric을 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/trainingmetrics)

training dataset에서 hand action classifier 성능의 measurement입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/validationmetrics)

validation dataset에서 hand action classifier 성능의 measurement입니다.

### [Testing a hand action classifier](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Testing-a-hand-action-classifier)

[`func prediction(from: URL) throws -> [MLHandActionClassifier.Prediction]`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/prediction(from:))

video 하나에 대한 hand-action prediction array를 생성합니다.

[`func predictions(from: [URL]) throws -> [[MLHandActionClassifier.Prediction]]`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/predictions(from:))

URL array의 각 video에 대한 hand action prediction array를 생성합니다.

[`struct Prediction`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/prediction)

video frame 범위별 prediction과 그 confidence를 함께 담은 collection입니다.

### [Saving a hand action classifier](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Saving-a-hand-action-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/write(to:metadata:))

hand action classifier를 CoreML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/write(tofile:metadata:))

hand action classifier를 Core ML model file로 내보냅니다.

### [Inspecting a hand action classifier model](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Inspecting-a-hand-action-classifier-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/model)

memory에 저장된 hand action classifier의 기반 Core ML model입니다.

[`let modelParameters: MLHandActionClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.property)

hand action model의 configuration parameter입니다.

### [Describing a hand action classifier](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Describing-a-hand-action-classifier)

[`var description: String`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/description)

hand action classifier의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/debugdescription)

debugging에 적합한 hand action classifier의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/playgrounddescription)

playground에서 볼 수 있는 hand action classifier 설명입니다.

### [Supporting types](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource)

annotation이 있는 video 또는 hand joint location data를 포함하는 hand action classifier dataset입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct)

hand action classifier task의 training process에 영향을 주는 parameter 집합입니다.

[`struct VideoAugmentationOptions`](https://developer.apple.com/documentation/createml/mlhandactionclassifier/videoaugmentationoptions)

제공한 video에서 추가 training data를 생성할 때 hand action classification training session이 사용할 수 있는 option입니다.

### [Default Implementations](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlhandactionclassifier/customdebugstringconvertible-implementations)

[API Reference: CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlhandactionclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlhandactionclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlhandactionclassifier#relationships)

---------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlhandactionclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlhandactionclassifier#see-also)

-----------------------------------------------------------------------------------------------

### [Video models](https://developer.apple.com/documentation/createml/mlhandactionclassifier#Video-models)

[Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)

사람의 body movement를 인식하는 machine learning model을 training합니다.

[live video feed에서 human action 감지하기](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed)

일련의 video frame에서 얻은 사람의 pose data를 action-classification model로 보내 body movement를 식별합니다.

[`struct MLActionClassifier`](https://developer.apple.com/documentation/createml/mlactionclassifier)

video로 training해 사람의 body movement를 분류하는 model입니다.

[`struct MLStyleTransfer`](https://developer.apple.com/documentation/createml/mlstyletransfer)

image의 style을 다른 image나 video에 적용하도록 training하는 model입니다.

현재 페이지: MLHandActionClassifier
