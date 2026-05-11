---
title: "MLHandPoseClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131578+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLHandPoseClassifier

struct

MLHandPoseClassifier
====================

제공한 사람 손 image를 training해 hand pose classification model을 생성하는 task입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    struct MLHandPoseClassifier

[주제](https://developer.apple.com/documentation/createml/mlhandposeclassifier#topics)

-----------------------------------------------------------------------------------------

### [hand pose classifier 비동기 training](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Training-a-hand-pose-classifier-asynchronously)

[`static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:))

비동기 hand pose classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

비동기 hand pose classifier training session을 생성합니다.

[`static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:))

비동기 hand pose classifier training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:))

file system에 저장된 state를 복원해 비동기 hand pose classifier training session을 다시 생성합니다.

### [checkpoint에서 hand pose classifier 생성](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Creating-a-hand-pose-classifier-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/init(checkpoint:))

training session checkpoint에서 hand pose classifier를 생성합니다.

### [hand pose classifier 동기 training](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Training-a-hand-pose-classifier-synchronously)

[`init(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/init(trainingdata:parameters:))

동기 training session을 시작해 hand pose classifier를 생성합니다.

### [hand pose classifier 평가](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Evaluating-a-hand-pose-classifier)

[`func evaluation(on: MLHandPoseClassifier.DataSource) throws -> MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:))

label이 지정된 image dataset으로 hand pose classifier 성능을 설명하는 metrics를 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics)

training dataset에서의 hand pose classifier 성능 측정값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/validationmetrics)

validation dataset에서의 hand pose classifier 성능 측정값입니다.

### [hand pose classifier 테스트](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Testing-a-hand-pose-classifier)

[`func prediction(from: URL) throws -> [(label: String, confidence: Double)]`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:))

image에 대한 hand pose prediction을 생성합니다.

[`func predictions(from: [URL]) throws -> [[(label: String, confidence: Double)]]`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:))

URL array의 각 image에 대한 hand pose prediction array를 생성합니다.

### [hand pose classifier 저장](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Saving-a-hand-pose-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:))

hand pose classifier를 CoreML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:))

hand pose classifier를 Core ML model file로 내보냅니다.

### [hand pose classifier model 검사](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Inspecting-a-hand-pose-classifier-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/model)

memory에 저장된 hand pose classifier의 underlying Core ML model입니다.

[`let modelParameters: MLHandPoseClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.property)

hand pose model의 configuration parameter입니다.

### [hand pose classifier 설명](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Describing-a-hand-pose-classifier)

[`var description: String`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/description)

hand pose classifier의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/debugdescription)

debugging에 적합한 hand pose classifier의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/playgrounddescription)

playground에서 볼 수 있는 hand pose classifier 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource)

annotated image 또는 hand joint location data를 포함하는 hand pose classifier dataset입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct)

hand pose classifier task의 training process에 영향을 주는 parameter 집합입니다.

[`struct ImageAugmentationOptions`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/imageaugmentationoptions)

제공한 image에서 추가 training data를 생성할 때 hand pose classification training session이 사용할 수 있는 option입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlhandposeclassifier/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlhandposeclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlhandposeclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlhandposeclassifier#relationships)

-------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlhandposeclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlhandposeclassifier#see-also)

---------------------------------------------------------------------------------------------

### [Image model](https://developer.apple.com/documentation/createml/mlhandposeclassifier#Image-models)

[Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)

image를 분류하는 machine learning model을 training하고 Core ML app에 추가합니다.

[`struct MLImageClassifier`](https://developer.apple.com/documentation/createml/mlimageclassifier)

image를 분류하도록 training하는 model입니다.

[`struct MLObjectDetector`](https://developer.apple.com/documentation/createml/mlobjectdetector)

image 안의 하나 이상의 object를 분류하도록 training하는 model입니다.

현재 페이지는 MLHandPoseClassifier
