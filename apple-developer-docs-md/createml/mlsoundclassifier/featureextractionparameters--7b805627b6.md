---
title: "MLSoundClassifier.FeatureExtractionParameters | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144153+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   MLSoundClassifier.FeatureExtractionParameters

struct

MLSoundClassifier.FeatureExtractionParameters
=============================================

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    struct FeatureExtractionParameters

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#topics)

------------------------------------------------------------------------------------------------------------------

### [Creating feature extraction parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#Creating-feature-extraction-parameters)

[`init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, featureExtractionTimeWindowSize: TimeInterval?)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:))

feature-extraction session용 parameter를 생성합니다.

[`init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:))

기본 time window size를 사용하는 feature-extraction session용 parameter를 생성합니다.

### [Accessing feature extraction parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#Accessing-feature-extraction-parameters)

[`var overlapFactor: Double`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor)

feature-extraction session이 audio data의 연속된 두 window를 분석할 때 사용하는 overlap 비율입니다.

[`var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor)

session이 audio file에서 feature를 추출할 때 사용하는 algorithm type입니다.

[`var featureExtractionTimeWindowSize: TimeInterval`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize)

feature-extraction session이 audio file을 sampling할 때 한 번에 읽는 audio data 양을 결정하는 시간 길이(초)입니다.

[관계](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#relationships)

--------------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#conforms-to)

*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#see-also)

----------------------------------------------------------------------------------------------------------------------

### [Training a sound classifier asynchronously](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters#Training-a-sound-classifier-asynchronously)

[`static train(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:))

data source로 표현한 training dataset으로 비동기 sound classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

sound classifier용 비동기 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/resume(_:))

sound classifier용 비동기 training session을 시작하거나 계속 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:))

기존 training session state를 parameter에서 복원해 sound classifier용 비동기 training session을 생성합니다.

[`static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))

sound file data source에서 sound feature를 추출하는 비동기 session을 시작합니다.

현재 페이지: MLSoundClassifier.FeatureExtractionParameters
