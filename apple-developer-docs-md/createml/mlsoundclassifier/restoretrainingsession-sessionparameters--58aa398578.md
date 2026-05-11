---
title: "restoreTrainingSession(sessionParameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144673+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   restoreTrainingSession(sessionParameters:)

type method

restoreTrainingSession(sessionParameters:)
==========================================

기존 training session의 상태를 parameter에서 복원해 sound classifier용 비동기 training session을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>

[파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------

`sessionParameters`

[`makeTrainingSession(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))
 을 사용해 training session을 만들 때 사용한 [`MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
 instance입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:)#return-value)

---------------------------------------------------------------------------------------------------------------------------------------------

sound classifier training session을 나타내는 [`MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)
 입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------

### [sound classifier 비동기 training](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:)#Training-a-sound-classifier-asynchronously)

[`static train(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:))

data source로 표현된 training dataset으로 비동기 sound classifier training session을 시작합니다.

[`static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))

sound classifier용 비동기 training session을 생성합니다.

[`static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/resume(_:))

sound classifier용 비동기 training session을 시작하거나 이어서 진행합니다.

[`static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>`](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))

sound file data source에서 sound feature를 추출하는 비동기 session을 시작합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

현재 페이지: restoreTrainingSession(sessionParameters:)
