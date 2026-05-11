---
title: "featureExtractionTimeWindowSize | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.159192+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   featureExtractionTimeWindowSize

instance property

featureExtractionTimeWindowSize
===============================

dataset의 audio file에서 읽은 각 audio sample에 training session이 사용하는 시간 길이(초)입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    var featureExtractionTimeWindowSize: TimeInterval { get set }

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize#discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

time-window 크기의 기본값은 `0.975`초이며 범위는 `[0.5, 15.0]`이어야 합니다.

[`MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:))
를 사용하는 training session은 이 값을 무시하고 항상 `0.975`초의 time-window 크기를 사용합니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------------------

### [Accessing the training parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize#Accessing-the-training-parameters)

[`var validation: MLSoundClassifier.ModelParameters.ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validation)

sound classifier의 validation dataset입니다.

[`var maxIterations: Int`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/maxiterations)

training session이 사용할 수 있는 최대 iteration 수입니다.

[`var overlapFactor: Double`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/overlapfactor)

training session이 audio data에서 연속한 두 window를 분석할 때 사용하는 overlap 비율입니다.

[`var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/algorithm)

training session이 sound classifier를 training할 때 사용하는 algorithm입니다.

현재 페이지: featureExtractionTimeWindowSize
