---
title: "MLObjectDetector | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlobjectdetector"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131674+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlobjectdetector#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLObjectDetector

struct

MLObjectDetector
================

image 안의 하나 이상의 object를 분류하도록 training하는 model입니다.

macOS 10.15+

    struct MLObjectDetector

[언급된 문서](https://developer.apple.com/documentation/createml/mlobjectdetector#mentions)

---------------------------------------------------------------------------------------------

[object detector data source 만들기](https://developer.apple.com/documentation/createml/building-an-object-detector-data-source)

[개요](https://developer.apple.com/documentation/createml/mlobjectdetector#overview)

-----------------------------------------------------------------------------------------

[`MLObjectDetector`](https://developer.apple.com/documentation/createml/mlobjectdetector)
 task를 사용해 image 안의 항목, 즉 _object_ 를 식별할 수 있는 machine learning model을 training합니다. 예를 들어 바나나, 크루아상, 음료처럼 테이블 위의 아침 식사 항목을 인식하도록 object detector를 training할 수 있습니다.

object detector는 image와 image 안 각 object에 대한 annotation 조합으로 training해 생성합니다. 그런 다음 이를 Core ML model로 저장하고 app에서 비슷한 항목을 인식하는 데 사용합니다.

[주제](https://developer.apple.com/documentation/createml/mlobjectdetector#topics)

-------------------------------------------------------------------------------------

### [data source 만들기](https://developer.apple.com/documentation/createml/mlobjectdetector#Creating-a-data-source)

[object detector data source 만들기](https://developer.apple.com/documentation/createml/building-an-object-detector-data-source)

object detector용 training data를 여러 가지 구조화 방식 중 하나로 구성합니다.

### [object detector를 비동기로 training하기](https://developer.apple.com/documentation/createml/mlobjectdetector#Training-an-object-detector-asynchronously)

[`static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLObjectDetector>`](https://developer.apple.com/documentation/createml/mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:))

비동기 object-detector training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>`](https://developer.apple.com/documentation/createml/mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:))

비동기 object-detector training session을 생성합니다.

[`static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>`](https://developer.apple.com/documentation/createml/mlobjectdetector/resume(_:))

비동기 object-detector training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>`](https://developer.apple.com/documentation/createml/mlobjectdetector/restoretrainingsession(sessionparameters:))

기존 training session의 state를 parameter에서 복원해 object detector용 비동기 training session을 생성합니다.

### [checkpoint에서 object detector 만들기](https://developer.apple.com/documentation/createml/mlobjectdetector#Creating-an-object-detector-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlobjectdetector/init(checkpoint:))

training session checkpoint로 object detector를 생성합니다.

### [object detector를 동기식으로 training하기](https://developer.apple.com/documentation/createml/mlobjectdetector#Training-an-object-detector-synchronously)

[`init(trainingData: MLObjectDetector.DataSource, parameters: MLObjectDetector.ModelParameters, annotationType: MLObjectDetector.AnnotationType) throws`](https://developer.apple.com/documentation/createml/mlobjectdetector/init(trainingdata:parameters:annotationtype:))

data source로 object detector를 생성합니다.

[`init(trainingData: MLDataTable, imageColumn: String, annotationColumn: String, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlobjectdetector/init(trainingdata:imagecolumn:annotationcolumn:annotationtype:parameters:))

data table로 object detector를 생성합니다.

Deprecated

### [object detector 평가하기](https://developer.apple.com/documentation/createml/mlobjectdetector#Evaluating-an-object-detector)

[`func evaluation(on: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetector/evaluation(on:))

data source의 annotated image를 사용해 object detector 성능을 평가한 metrics를 생성합니다.

[`func evaluation(on: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetector/evaluation(on:imagecolumn:annotationcolumn:))

data table의 annotated image를 사용해 object detector 성능을 평가한 metrics를 생성합니다.

Deprecated

[`var trainingMetrics: MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetector/trainingmetrics)

training dataset에서 object detector 성능을 나타내는 측정값입니다.

[`var validationMetrics: MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetector/validationmetrics)

validation dataset에서 object detector 성능을 나타내는 측정값입니다.

### [object detector 테스트하기](https://developer.apple.com/documentation/createml/mlobjectdetector#Testing-an-object-detector)

[`func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects`](https://developer.apple.com/documentation/createml/mlobjectdetector/prediction(from:))

image에서 object를 찾아 감지한 각 object의 annotation을 생성합니다.

[`func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]`](https://developer.apple.com/documentation/createml/mlobjectdetector/predictions(from:))

image 배열에서 object를 찾아 각 입력 image마다 annotation collection 배열을 생성합니다.

[`typealias DetectedObjects`](https://developer.apple.com/documentation/createml/mlobjectdetector/detectedobjects)

object detector가 image에서 찾은 항목을 나타내는 annotation 배열입니다.

[`struct ObjectAnnotation`](https://developer.apple.com/documentation/createml/mlobjectdetector/objectannotation)

object detector가 image에서 찾은 항목의 label, 위치, confidence score입니다.

### [object detector 저장하기](https://developer.apple.com/documentation/createml/mlobjectdetector#Saving-an-object-detector)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlobjectdetector/write(to:metadata:))

object detector를 Core ML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlobjectdetector/write(tofile:metadata:))

Exports the object detector as a Core ML model file.

### [object detector model 살펴보기](https://developer.apple.com/documentation/createml/mlobjectdetector#Inspecting-an-object-detector-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlobjectdetector/model)

object detector의 기반 Core ML model instance입니다.

[`let modelParameters: MLObjectDetector.ModelParameters`](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.property)

object detector가 training session 동안 사용한 model configuration parameter입니다.

### [object detector 설명하기](https://developer.apple.com/documentation/createml/mlobjectdetector#Describing-an-object-detector)

[`var description: String`](https://developer.apple.com/documentation/createml/mlobjectdetector/description)

object detector의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlobjectdetector/debugdescription)

debugging 중 출력에 적합한 object detector의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlobjectdetector/playgrounddescription)

playground 안에서 사용하는 object detector 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlobjectdetector#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource)

object detector용 data source입니다.

[`enum AnnotationType`](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype)

사용할 수 있는 image annotation type입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct)

object detection model training 과정에 영향을 주는 parameter입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlobjectdetector#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlobjectdetector/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlobjectdetector/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlobjectdetector/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlobjectdetector#relationships)

---------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlobjectdetector#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlobjectdetector#see-also)

-----------------------------------------------------------------------------------------

### [Image model](https://developer.apple.com/documentation/createml/mlobjectdetector#Image-models)

[Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)

image를 분류하는 machine learning model을 training한 뒤 Core ML app에 추가합니다.

[`struct MLImageClassifier`](https://developer.apple.com/documentation/createml/mlimageclassifier)

image를 분류하도록 training하는 model입니다.

[`struct MLHandPoseClassifier`](https://developer.apple.com/documentation/createml/mlhandposeclassifier)

A task that creates a hand pose classification model by training with images of people’s hands that you provide.

현재 페이지: MLObjectDetector
