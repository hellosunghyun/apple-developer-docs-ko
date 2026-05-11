---
title: "makeTrainingSession(trainingData:parameters:sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148156+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   makeTrainingSession(trainingData:parameters:sessionParameters:)

type method

makeTrainingSession(trainingData:parameters:sessionParameters:)
===============================================================

sound classifier용 asynchronous training session을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func makeTrainingSession(
        trainingData: MLSoundClassifier.DataSource,
        parameters: MLSoundClassifier.ModelParameters = .init(),
        sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters
    ) throws -> MLTrainingSession<MLSoundClassifier>

[파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

`trainingData`

[`MLSoundClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
로 표현한 labeled audio file collection입니다.

`parameters`

training session용 model을 구성할 때 사용하는 [`MLSoundClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
 instance입니다.

`sessionParameters`

training session을 구성할 때 사용하는 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#return-value)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

sound classifier training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------------------------

### [sound classifier 비동기 training](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:)#Training-a-sound-classifier-asynchronously)

[`static train(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:))

data source로 표현한 training dataset으로 asynchronous sound classifier training session을 시작합니다.

[`static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/resume(_:))

sound classifier용 asynchronous training session을 시작하거나 이어서 진행합니다.

[`static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:))

기존 training session의 state를 파라미터에서 복원해 sound classifier용 asynchronous training session을 생성합니다.

[`static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))

sound file data source에서 sound feature를 추출하는 asynchronous session을 시작합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 파라미터입니다.

현재 페이지는 makeTrainingSession(trainingData:parameters:sessionParameters:)입니다
