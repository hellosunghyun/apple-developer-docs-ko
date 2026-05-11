---
title: "MLSoundClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130252+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLSoundClassifier

struct

MLSoundClassifier
=================

audio file로 training해 device에서 sound를 인식하고 식별하는 machine learning model입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    struct MLSoundClassifier

[개요](https://developer.apple.com/documentation/createml/mlsoundclassifier#overview)

------------------------------------------------------------------------------------------

sound classifier는 app에서 sound를 식별하고 분류하는 machine learning model입니다. audio file dataset을 모아 [`MLSoundClassifier`](https://developer.apple.com/documentation/createml/mlsoundclassifier)
로 model을 training해 sound classifier를 만듭니다.

app이 식별하려는 sound를 가장 잘 대표하는 audio file을 녹음하거나 수집해 audio dataset을 구성합니다. 또한 sound classifier가 들을 수 있지만 관련은 없는 noise 묶음인 _negative class_ 도 예시 sound를 녹음하거나 수집해 만듭니다.

예를 들어 웃음과 박수를 식별하는 sound classifier를 만든다고 가정해 보겠습니다. 사람들이 웃는 소리와 박수 소리 예시 audio를 모으는 것에 더해 background noise용 추가 category를 넣을 수 있습니다. 극장이나 원형극장처럼 다양한 환경에서 녹음한 음원을 추가하면 sound classifier가 관심 sound와 환경 noise를 구분할 수 있습니다. 즉, 실제로 박수가 없을 때는 sound classifier가 “Applause”를 prediction하지 않습니다. 다른 classifier와 마찬가지로 prediction을 요청하면 sound classifier는 training dataset에서 학습한 category 중 하나를 항상 반환합니다.

sound classifier가 학습할 각 sound category마다 최소 10개의 audio example을 모으고, background noise용 negative class도 최소 하나 포함합니다. audio example은 Core Audio가 지원하는 어떤 file format이라도 사용할 수 있으며 다음을 포함합니다.

*   M4A
    
*   MP3
    
*   AIFF
    
*   WAV
    

bit depth와 sample rate가 일관된 audio file을 수집해 sound classifier의 bias를 줄입니다. 이런 bias는 성능에 악영향을 줄 수 있습니다.

다른 Create ML model type을 만들 때와 비슷한 단계로 sound classifier를 training, evaluation, export합니다. Create ML training workflow에 대한 자세한 내용은 다음 문서를 참고합니다.

*   [Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)
    
*   [Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)
    

sound classifier의 Core ML model을 Xcode project에 추가하고 runtime에 이를 사용해 [`SNClassifySoundRequest`](https://developer.apple.com/documentation/SoundAnalysis/SNClassifySoundRequest)
를 만듭니다. app은 다음 문서의 단계에 따라 각각 audio file 또는 audio stream의 sound를 식별하는 데 이 sound request를 사용합니다.

*   [Audio File의 Sound 분류하기](https://developer.apple.com/documentation/SoundAnalysis/classifying-sounds-in-an-audio-file)
    
*   [Audio Stream의 Sound 분류하기](https://developer.apple.com/documentation/SoundAnalysis/classifying-sounds-in-an-audio-stream)
    

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier#topics)

--------------------------------------------------------------------------------------

### [sound classifier를 비동기로 training하기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Training-a-sound-classifier-asynchronously)

[`static train(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:))

data source로 표현한 training dataset으로 비동기 sound classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

sound classifier용 비동기 training session을 만듭니다.

[`static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/resume(_:))

sound classifier용 비동기 training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:))

기존 training session의 state를 parameter에서 복원해 sound classifier용 비동기 training session을 만듭니다.

[`static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))

sound file data source에서 sound feature를 추출하는 비동기 session을 시작합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

### [checkpoint에서 sound classifier 만들기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Creating-a-sound-classifier-from-a-checkpoint)

[`init(checkpoint: MLCheckpoint) throws`](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(checkpoint:))

training session checkpoint에서 sound classifier를 만듭니다.

### [sound classifier를 동기로 training하기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Training-a-sound-classifier-synchronously)

[`init(trainingData:parameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:))

data source로 표현한 training dataset으로 sound classifier를 만듭니다.

### [sound classifier 평가하기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Evaluating-a-sound-classifier)

[`func evaluation(on:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:))

data source로 표현한 dataset에서 sound classifier의 성능을 평가해 metric을 생성합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlsoundclassifier/trainingmetrics)

training dataset에서 classifier 성능을 측정한 값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlsoundclassifier/validationmetrics)

validation dataset에서 image classifier 성능을 측정한 값입니다.

### [sound classifier 테스트하기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Testing-a-sound-classifier)

[`func predictions(from: [URL]) throws -> [String]`](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:))

audio file array에 대한 prediction을 생성합니다.

[`func predictions(from: [URL], overlapFactor: Double, predictionTimeWindowSize: TimeInterval) throws -> [String]`](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:))

audio file array에 대해 overlap factor와 time window size를 사용한 prediction을 생성합니다.

### [sound classifier 저장하기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Saving-a-sound-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:))

sound classifier를 file system의 위치에 model file로 export합니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:))

sound classifier를 file system 경로에 model file로 export합니다.

### [sound classifier model 살펴보기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Inspecting-a-sound-classifier-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlsoundclassifier/model)

memory에 저장된 sound classifier의 기반 model instance입니다.

[`let modelParameters: MLSoundClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.property)

training session 동안 sound classifier가 사용한 model configuration parameter입니다.

### [sound classifier 설명하기](https://developer.apple.com/documentation/createml/mlsoundclassifier#Describing-a-sound-classifier)

[`var description: String`](https://developer.apple.com/documentation/createml/mlsoundclassifier/description)

sound classifier의 텍스트 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlsoundclassifier/debugdescription)

debugging 출력에 적합한 sound classifier의 텍스트 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlsoundclassifier/playgrounddescription)

playground에서의 sound classifier 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlsoundclassifier#Supporting-types)

[`enum DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)

file system 또는 data table에 있는 sound-classifier dataset 표현입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)

sound-classifier model을 training하는 과정에 영향을 주는 parameter입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlsoundclassifier#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlsoundclassifier/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlsoundclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlsoundclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlsoundclassifier#relationships)

----------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/createml/mlsoundclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

현재 페이지는 MLSoundClassifier입니다.
