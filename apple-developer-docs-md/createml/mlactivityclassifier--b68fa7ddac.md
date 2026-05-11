---
title: "MLActivityClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlactivityclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.129858+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlactivityclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLActivityClassifier

struct

MLActivityClassifier
====================

motion sensor data를 분류하도록 training하는 model입니다.

macOS 10.15+

    struct MLActivityClassifier

[개요](https://developer.apple.com/documentation/createml/mlactivityclassifier#overview)

---------------------------------------------------------------------------------------------

activity classifier는 사용자 device의 motion을 바탕으로 사용자 _activity_ 를 분류할 때 app이 사용할 수 있는 machine-learning model입니다.

activity classifier는 Apple Watch의 accelerometer, gyroscope 같은 device motion sensor의 training dataset을 수집해 만듭니다. 예를 들어 손을 흔들기, 악수하기, 공 던지기를 수행하는 사람들의 motion-sensor data를 모아 이런 activity를 인식하는 activity classifier를 만들 수 있습니다.

Evaluate your trained activity classifier by calling [`evaluation(on:featureColumns:labelColumn:recordingFileColumn:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:)-1ib5p)
 [`evaluation(on:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)-7fmux)
 with a dataset that’s completely distinct from the training and validation datasets. Inspect the metrics the method returns and decide whether the activity classifier performs with enough accuracy. For example, you can assess how often the activity classifier confuses a person waving for shaking hands, or vice versa. If the classifier makes too many mistakes, you can train another classifier with different parameters, or with a training dataset that has more or better motion-sensor examples.

activity classifier 결과가 만족스러우면 Core ML model file로 저장하고 Xcode project에 추가합니다. 그런 다음 app이 사용자 device에서 캡처한 motion-sensor data를 바탕으로 사용자의 activity를 예측하는 데 사용합니다.

[주제](https://developer.apple.com/documentation/createml/mlactivityclassifier#topics)

-----------------------------------------------------------------------------------------

### [activity classifier 비동기 training](https://developer.apple.com/documentation/createml/mlactivityclassifier#Training-an-activity-classifier-asynchronously)

[`static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionparameter:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:))

data source로 표현된 training dataset으로 비동기 activity classifier training session을 시작합니다.

[`static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionparameter:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:))

activity classifier용 비동기 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>`](https://developer.apple.com/documentation/createml/mlactivityclassifier/resume(_:))

비동기 activity classifier training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionparameter: MLTrainingSessionparameter) throws -> MLTrainingSession<MLActivityClassifier>`](https://developer.apple.com/documentation/createml/mlactivityclassifier/restoretrainingsession(sessionparameters:))

기존 training session의 parameter에서 상태를 복원해 activity classifier용 비동기 training session을 생성합니다.

### [checkpoint에서 activity classifier 생성](https://developer.apple.com/documentation/createml/mlactivityclassifier#Creating-an-activity-classifier-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlactivityclassifier/init(checkpoint:))

training session checkpoint에서 activity classifier를 생성합니다.

### [activity classifier 동기 training](https://developer.apple.com/documentation/createml/mlactivityclassifier#Training-an-activity-classifier-synchronously)

[`init(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/init(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:))

data source로 표현된 training dataset으로 activity classifier를 생성합니다.

### [activity classifier 평가](https://developer.apple.com/documentation/createml/mlactivityclassifier#Evaluating-an-activity-classifier)

[`func evaluation(on:featureColumns:labelColumn:recordingFileColumn:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:))

data source의 label된 activity에 대한 activity classifier 성능을 설명하는 metrics를 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactivityclassifier/trainingmetrics)

activity classifier가 training dataset에서 보인 성능 측정값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlactivityclassifier/validationmetrics)

activity classifier가 validation dataset에서 보인 성능 측정값입니다.

[`func evaluation(on:featureColumns:labelColumn:recordingFileColumn:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:))

data source의 label된 activity에 대한 activity classifier 성능을 설명하는 metrics를 생성합니다.

### [activity classifier 테스트](https://developer.apple.com/documentation/createml/mlactivityclassifier#Testing-an-activity-classifier)

[`func predictions(from:perWindowPrediction:)`](https://developer.apple.com/documentation/createml/mlactivityclassifier/predictions(from:perwindowprediction:))

새 observation에서 activity를 예측합니다.

### [activity classifier 저장](https://developer.apple.com/documentation/createml/mlactivityclassifier#Saving-an-activity-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlactivityclassifier/write(to:metadata:))

activity classifier를 Core ML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlactivityclassifier/write(tofile:metadata:))

activity classifier를 Core ML model file로 내보냅니다.

### [activity classifier model 검사](https://developer.apple.com/documentation/createml/mlactivityclassifier#Inspecting-an-activity-classifier-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlactivityclassifier/model)

memory에 저장된 activity classifier의 기반 Core ML model입니다.

[`let modelparameter: MLActivityClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.property)

activity classifier가 training session 동안 사용한 model configuration parameter입니다.

[`var featureColumns: [String]`](https://developer.apple.com/documentation/createml/mlactivityclassifier/featurecolumns)

activity classifier가 training session 동안 사용한 feature column 이름입니다.

[`var labelColumn: String`](https://developer.apple.com/documentation/createml/mlactivityclassifier/labelcolumn)

activity classifier가 training session 동안 사용한 label column 이름입니다.

[`var recordingFileColumn: String`](https://developer.apple.com/documentation/createml/mlactivityclassifier/recordingfilecolumn)

activity classifier가 training session 동안 사용한 data file이 들어 있는 column 이름입니다.

### [activity classifier 설명](https://developer.apple.com/documentation/createml/mlactivityclassifier#Describing-an-activity-classifier)

[`var description: String`](https://developer.apple.com/documentation/createml/mlactivityclassifier/description)

activity classifier의 텍스트 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlactivityclassifier/debugdescription)

debugging 중 출력하기에 적합한 activity classifier의 텍스트 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlactivityclassifier/playgrounddescription)

playground에 표시되는 activity classifier 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlactivityclassifier#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource)

activity classifier용 data source입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct)

activity classifier model의 training 과정을 제어하는 model training parameter입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlactivityclassifier#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlactivityclassifier/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlactivityclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlactivityclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlactivityclassifier#relationships)

-------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlactivityclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

현재 페이지: MLActivityClassifier
