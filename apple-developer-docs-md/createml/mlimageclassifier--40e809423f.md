---
title: "MLImageClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlimageclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131767+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlimageclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLImageClassifier

struct

MLImageClassifier
=================

image를 분류하도록 training하는 model입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+visionOS 1.0+

    struct MLImageClassifier

[언급 항목](https://developer.apple.com/documentation/createml/mlimageclassifier#mentions)

----------------------------------------------------------------------------------------------

[Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)

[Model 정확도 높이기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[개요](https://developer.apple.com/documentation/createml/mlimageclassifier#overview)

------------------------------------------------------------------------------------------

app에 포함해 image를 분류할 수 있는 machine learning model을 training하려면 image classifier를 사용합니다.

model을 만들 때는 label이 지정된 image로 구성된 training dataset과, training 과정을 제어하는 parameter를 함께 제공합니다. 예를 들어 `Elephant`와 `Giraffe`라는 label이 붙은 두 folder에 코끼리와 기린 image를 넣어, model이 이 동물을 인식하도록 training할 수 있습니다.

training이 끝나면, model이 이전에 본 적 없는 label image가 들어 있는 testing dataset을 보여 주어 training된 model을 평가합니다. 이 평가에서 얻는 metric으로 model 성능이 충분한지 판단할 수 있습니다. 예를 들어 코끼리와 기린 classifier가 기린을 코끼리로 얼마나 자주 잘못 분류하는지 확인할 수 있습니다. model의 실수가 너무 많다면 training data를 더 추가하거나 더 좋은 data로 바꾸고, parameter를 조정해 다시 시도합니다.

model 성능이 충분하면 `mlmodel` 확장자를 가진 Core ML model file로 저장합니다. 그런 다음 이 model file을 [Vision과 Core ML로 image 분류하기](https://developer.apple.com/documentation/CoreML/classifying-images-with-vision-and-core-ml)
 sample code project처럼 Core ML model file을 사용해 image를 분류하는 app에 import할 수 있습니다.

[주제](https://developer.apple.com/documentation/createml/mlimageclassifier#topics)

--------------------------------------------------------------------------------------

### [image classifier를 async로 training하기](https://developer.apple.com/documentation/createml/mlimageclassifier#Training-an-image-classifier-asynchronously)

[`static func makeTrainingSession(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>`](https://developer.apple.com/documentation/createml/mlimageclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

training session을 생성하거나 복원합니다.

[`static func train(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLImageClassifier>`](https://developer.apple.com/documentation/createml/mlimageclassifier/train(trainingdata:parameters:sessionparameters:))

data source로 표현한 training dataset으로 async image classifier training session을 시작합니다.

[`static func resume(MLTrainingSession<MLImageClassifier>) throws -> MLJob<MLImageClassifier>`](https://developer.apple.com/documentation/createml/mlimageclassifier/resume(_:))

async image classifier training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>`](https://developer.apple.com/documentation/createml/mlimageclassifier/restoretrainingsession(sessionparameters:))

기존 training session의 state를 parameter에서 복원해 image classifier용 async training session을 만듭니다.

### [checkpoint에서 image classifier 만들기](https://developer.apple.com/documentation/createml/mlimageclassifier#Creating-an-image-classifier-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlimageclassifier/init(checkpoint:))

training session checkpoint에서 image classifier를 만듭니다.

### [image classifier를 동기식으로 training하기](https://developer.apple.com/documentation/createml/mlimageclassifier#Training-an-image-classifier-synchronously)

[`init(trainingData:parameters:)`](https://developer.apple.com/documentation/createml/mlimageclassifier/init(trainingdata:parameters:))

data source로 표현한 training dataset으로 image classifier를 만듭니다.

### [image classifier 평가](https://developer.apple.com/documentation/createml/mlimageclassifier#Evaluating-an-image-classifier)

[`func evaluation(on:)`](https://developer.apple.com/documentation/createml/mlimageclassifier/evaluation(on:))

data source로 표현한 label image에 대한 image classifier 성능을 설명하는 metric을 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlimageclassifier/trainingmetrics)

training dataset에 대한 classifier 성능 측정값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlimageclassifier/validationmetrics)

validation dataset에 대한 image classifier 성능 측정값입니다.

### [image classifier 테스트](https://developer.apple.com/documentation/createml/mlimageclassifier#Testing-an-image-classifier)

[`func prediction(from:)`](https://developer.apple.com/documentation/createml/mlimageclassifier/prediction(from:))

image에 대한 prediction을 생성합니다.

[`func predictions(from: [URL]) throws -> [String]`](https://developer.apple.com/documentation/createml/mlimageclassifier/predictions(from:))

image 배열에 대한 prediction을 생성합니다.

### [image classifier 저장](https://developer.apple.com/documentation/createml/mlimageclassifier#Saving-an-image-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:))

image classifier를 file system의 위치로 Core ML model file 형태로 export합니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:))

image classifier를 지정한 file path로 Core ML model file 형태로 export합니다.

### [image classifier model 검사](https://developer.apple.com/documentation/createml/mlimageclassifier#Inspecting-an-image-classifier-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlimageclassifier/model)

memory에 저장된 image classifier의 기반 Core ML model입니다.

[`let modelParameters: MLImageClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.property)

image classifier가 training session 동안 사용한 model configuration parameter입니다.

### [image classifier 설명](https://developer.apple.com/documentation/createml/mlimageclassifier#Describing-an-image-classifier)

[`var description: String`](https://developer.apple.com/documentation/createml/mlimageclassifier/description)

image classifier의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlimageclassifier/debugdescription)

debugging 중 출력에 적합한 image classifier의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlimageclassifier/playgrounddescription)

playground에 표시되는 image classifier 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlimageclassifier#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource)

image classifier용 data source입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct)

image classifier model training 과정에 영향을 주는 parameter입니다.

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlimageclassifier/featureextractortype)

image classifier training session에서 image feature를 추출하는 기반 base model입니다.

[`struct CustomFeatureExtractor`](https://developer.apple.com/documentation/createml/mlimageclassifier/customfeatureextractor)

training session이 image classifier를 training할 때 사용하는 custom feature extractor입니다.

[`struct ImageAugmentationOptions`](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions)

training 과정이 제공한 training data로부터 더 많은 training data를 생성할 때 사용할 수 있는 variation입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlimageclassifier#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlimageclassifier/customdebugstringconvertible-implementations)

[API Reference: CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlimageclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlimageclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlimageclassifier#relationships)

----------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlimageclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlimageclassifier#see-also)

------------------------------------------------------------------------------------------

### [image model](https://developer.apple.com/documentation/createml/mlimageclassifier#Image-models)

[Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)

image를 분류하는 machine learning model을 training하고 Core ML app에 추가합니다.

[`struct MLObjectDetector`](https://developer.apple.com/documentation/createml/mlobjectdetector)

image 안의 하나 이상의 object를 분류하도록 training하는 model입니다.

[`struct MLHandPoseClassifier`](https://developer.apple.com/documentation/createml/mlhandposeclassifier)

제공한 사람 손 image로 training해 hand pose classification model을 만드는 task입니다.

현재 페이지는 MLImageClassifier입니다.
