---
title: "featureExtractionTimeWindowSize | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.157351+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.FeatureExtractionParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)
    
*   featureExtractionTimeWindowSize

instance property

featureExtractionTimeWindowSize
===============================

feature-extraction session이 audio file을 sample할 때마다 얼마나 많은 audio data를 읽을지 결정하는 시간 길이(초)입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    var featureExtractionTimeWindowSize: TimeInterval { get set }

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize#discussion)

----------------------------------------------------------------------------------------------------------------------------------------------------------

time-window 크기의 기본값은 `0.975`초이며 범위는 `[0.5, 15.0]`이어야 합니다.

[`MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:))
 를 사용하는 feature-extraction session은 이 값을 무시하고 항상 `0.975`초의 time-window 크기를 사용합니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize#see-also)

------------------------------------------------------------------------------------------------------------------------------------------------------

### [Feature Extraction Parameter 접근하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize#Accessing-feature-extraction-parameters)

[`var overlapFactor: Double`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor)

feature-extraction session이 audio data에서 연속한 두 window를 분석할 때 사용하는 overlap 비율입니다.

[`var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor)

session이 audio file에서 feature를 추출하는 데 사용하는 algorithm type입니다.

현재 페이지: featureExtractionTimeWindowSize
