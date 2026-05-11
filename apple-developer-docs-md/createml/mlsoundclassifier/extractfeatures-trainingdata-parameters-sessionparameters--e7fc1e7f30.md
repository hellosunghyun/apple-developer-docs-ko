---
title: "extractFeatures(trainingData:parameters:sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144429+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   extractFeatures(trainingData:parameters:sessionParameters:)

type method

extractFeatures(trainingData:parameters:sessionParameters:)
===========================================================

sound file data source에서 sound feature를 추출하는 asynchronous session을 시작합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func extractFeatures(
        trainingData: MLSoundClassifier.DataSource,
        parameters: MLSoundClassifier.FeatureExtractionParameters = FeatureExtractionParameters(),
        sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters
    ) throws -> MLJob<MLSoundClassifier.DataSource>

[파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------------------------

`trainingData`

label이 지정된 audio file collection을 포함하는 [`MLSoundClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource) instance입니다.

`parameters`

feature extraction session을 구성할 때 사용하는 [`MLSoundClassifier.FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters) instance입니다.

`sessionParameters`

feature extraction session을 구성할 때 사용하는 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters) instance입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)#return-value)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

sound feature extraction session을 나타내는 [`MLJob`](https://developer.apple.com/documentation/createml/mljob)입니다.

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)#discussion)

----------------------------------------------------------------------------------------------------------------------------------------------------------

같은 training data를 사용하는 여러 sound classifier의 training 시간을 줄이려면 이 method를 사용합니다. 이 method가 반환하는 [`MLJob`](https://developer.apple.com/documentation/createml/mljob) instance를 사용해 audio feature를 [`MLSoundClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)로 저장합니다. 그런 다음 audio feature data source를 사용해 하나 이상의 sound classifier를 training합니다.

audio feature를 포함하는 [`DataFrame`](https://developer.apple.com/documentation/TabularData/DataFrame) 또는 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)에 대해서도 각각 [`MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))와 [`MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:))를 사용해 data source를 만들 수 있습니다.

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------------------

### [sound classifier 비동기 training](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:)#Training-a-sound-classifier-asynchronously)

[`static train(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:))

data source로 표현한 training dataset으로 asynchronous sound classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

sound classifier용 asynchronous training session을 생성합니다.

[`static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/resume(_:))

sound classifier용 asynchronous training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:))

기존 training session의 상태를 parameter에서 복원해 sound classifier용 asynchronous training session을 생성합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

현재 페이지는 extractFeatures(trainingData:parameters:sessionParameters:)입니다
