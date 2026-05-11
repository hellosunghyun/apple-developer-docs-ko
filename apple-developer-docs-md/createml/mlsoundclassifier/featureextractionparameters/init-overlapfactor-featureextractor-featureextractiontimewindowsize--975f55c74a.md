---
title: "init(overlapFactor:featureExtractor:featureExtractionTimeWindowSize:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144800+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.FeatureExtractionParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)
    
*   init(overlapFactor:featureExtractor:featureExtractionTimeWindowSize:)

initializer

init(overlapFactor:featureExtractor:featureExtractionTimeWindowSize:)
=====================================================================

feature-extraction session용 parameter를 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    init(
        overlapFactor: Double = __Defaults.overlapFactor,
        featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType = __Defaults.featureExtractor,
        featureExtractionTimeWindowSize: TimeInterval?
    )

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`overlapFactor`

연속된 audio analysis window 사이의 overlap 비율입니다. 값은 `[0.0, 1.0)` 범위여야 합니다.`featureExtractor`audio file에서 feature를 추출할 때 session이 사용하는 algorithm type입니다.`featureExtractionTimeWindowSize`dataset의 audio file에서 읽은 각 audio sample에 대해 feature-extraction session이 사용하는 시간 길이(초)입니다. 값은 `[0.5, 15.0]` 범위여야 합니다.[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:)#see-also)--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------### [feature extraction parameter 생성](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:)#Creating-feature-extraction-parameters)[`init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:))기본 time window size를 사용하는 feature-extraction session용 parameter를 만듭니다.현재 페이지는 init(overlapFactor:featureExtractor:featureExtractionTimeWindowSize:)입니다.
