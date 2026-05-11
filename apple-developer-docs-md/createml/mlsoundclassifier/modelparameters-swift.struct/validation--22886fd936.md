---
title: "validation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validation"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.159091+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validation#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   validation

instance property

validation
==========

sound classifier의 validation dataset입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    var validation: MLSoundClassifier.ModelParameters.ValidationData

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validation#see-also)

----------------------------------------------------------------------------------------------------------------------------------

### [training parameter 접근](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validation#Accessing-the-training-parameters)

[`var maxIterations: Int`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/maxiterations)

training session이 사용할 수 있는 최대 iteration 수입니다.

[`var overlapFactor: Double`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/overlapfactor)

training session이 audio data의 연속된 두 window를 분석할 때 사용하는 overlap 비율입니다.

[`var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/algorithm)

training session이 sound classifier를 training할 때 사용하는 algorithm입니다.

[`var featureExtractionTimeWindowSize: TimeInterval`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize)

training session이 dataset의 audio file에서 각 audio sample을 읽을 때 사용하는 시간 길이(초 단위)입니다.

현재 페이지: validation
