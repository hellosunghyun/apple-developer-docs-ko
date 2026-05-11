---
title: "MLActionClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlactionclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131073+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlactionclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLActionClassifier

struct

MLActionClassifier
==================

video로 사람의 몸동작을 분류하도록 training하는 model입니다.

macOS 11.0+

    struct MLActionClassifier

[주제](https://developer.apple.com/documentation/createml/mlactionclassifier#topics)

---------------------------------------------------------------------------------------

### [Training an action classifier asynchronously](https://developer.apple.com/documentation/createml/mlactionclassifier#Training-an-action-classifier-asynchronously)

[`static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>`](https://developer.apple.com/documentation/createml/mlactionclassifier/train(trainingdata:parameters:sessionparameters:))

비동기 action classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>`](https://developer.apple.com/documentation/createml/mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

action classifier용 비동기 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>`](https://developer.apple.com/documentation/createml/mlactionclassifier/resume(_:))

비동기 action classifier training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>`](https://developer.apple.com/documentation/createml/mlactionclassifier/restoretrainingsession(sessionparameters:))

기존 training session의 state를 parameters에서 복원해 action classifier용 비동기 training session을 생성합니다.

### [Creating an action classifier from a checkpoint](https://developer.apple.com/documentation/createml/mlactionclassifier#Creating-an-action-classifier-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlactionclassifier/init(checkpoint:))

training session checkpoint에서 action classifier를 생성합니다.

### [Training an action classifier synchronously](https://developer.apple.com/documentation/createml/mlactionclassifier#Training-an-action-classifier-synchronously)

[`init(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlactionclassifier/init(trainingdata:parameters:))

data source로 표현한 training dataset으로 action classifier를 생성합니다.

### [Evaluating an action classifier](https://developer.apple.com/documentation/createml/mlactionclassifier#Evaluating-an-action-classifier)

[`func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/evaluation(on:))

data source로 표현한 labeled video에서 action classifier 성능을 설명하는 metric을 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics)

training dataset에서의 action classifier 성능 측정값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics)

validation dataset에서의 action classifier 성능 측정값입니다.

### [Testing an action classifier](https://developer.apple.com/documentation/createml/mlactionclassifier#Testing-an-action-classifier)

[`func prediction(from: URL) throws -> [MLActionClassifier.Prediction]`](https://developer.apple.com/documentation/createml/mlactionclassifier/prediction(from:))

video에서 classifier가 인식하는 각 action에 대한 prediction을 생성합니다.

[`func predictions(from: [URL]) throws -> [[MLActionClassifier.Prediction]]`](https://developer.apple.com/documentation/createml/mlactionclassifier/predictions(from:))

각 video 입력에 대한 prediction sequence를 생성합니다.

[`struct Prediction`](https://developer.apple.com/documentation/createml/mlactionclassifier/prediction)

신뢰도와 함께 짝지어진 prediction 모음으로, video frame 범위에 대응합니다.

### [Saving an action classifier](https://developer.apple.com/documentation/createml/mlactionclassifier#Saving-an-action-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlactionclassifier/write(to:metadata:))

action classifier를 file system의 위치에 Core ML model file로 export합니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlactionclassifier/write(tofile:metadata:))

action classifier를 file path에 Core ML model file로 export합니다.

### [Inspecting an action classifier model](https://developer.apple.com/documentation/createml/mlactionclassifier#Inspecting-an-action-classifier-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlactionclassifier/model)

memory에 저장된 action classifier의 기반 Core ML model입니다.

[`let modelParameters: MLActionClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.property)

action classifier가 training session 동안 사용한 model configuration parameter입니다.

### [Describing an action classifier](https://developer.apple.com/documentation/createml/mlactionclassifier#Describing-an-action-classifier)

[`var description: String`](https://developer.apple.com/documentation/createml/mlactionclassifier/description)

action classifier의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlactionclassifier/debugdescription)

debugging 중 출력에 적합한 action classifier의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlactionclassifier/playgrounddescription)

playground에 표시되는 action classifier 설명입니다.

### [Supporting types](https://developer.apple.com/documentation/createml/mlactionclassifier#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource)

action classifier용 data source입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct)

action classifier의 training process에 영향을 주는 parameter입니다.

[`struct VideoAugmentationOptions`](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions)

action classifier training session에 사용하는 video augmentation입니다.

### [Default Implementations](https://developer.apple.com/documentation/createml/mlactionclassifier#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlactionclassifier/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlactionclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlactionclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlactionclassifier#relationships)

-----------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlactionclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlactionclassifier#see-also)

-------------------------------------------------------------------------------------------

### [Video models](https://developer.apple.com/documentation/createml/mlactionclassifier#Video-models)

[Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)

사람의 몸동작을 인식하는 machine learning model을 training합니다.

[live video feed에서 human action 감지하기](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed)

일련의 video frame에서 사람의 pose data를 action-classification model로 보내 몸동작을 식별합니다.

[`struct MLHandActionClassifier`](https://developer.apple.com/documentation/createml/mlhandactionclassifier)

제공한 사람 손동작 video로 training해 손동작 분류 model을 생성하는 task입니다.

[`struct MLStyleTransfer`](https://developer.apple.com/documentation/createml/mlstyletransfer)

한 image의 style을 다른 image나 video에 적용하도록 training하는 model입니다.

현재 페이지: MLActionClassifier
