---
title: "featureExtractor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.157241+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.FeatureExtractionParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)
    
*   featureExtractor

instance property

featureExtractor
================

session이 audio file에서 feature를 추출할 때 사용하는 algorithm type입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor#see-also)

---------------------------------------------------------------------------------------------------------------------------------------

### [feature extraction parameter 접근](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor#Accessing-feature-extraction-parameters)

[`var overlapFactor: Double`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor)

feature-extraction session이 audio data의 연속된 두 window를 분석할 때 사용하는 overlap 비율입니다.

[`var featureExtractionTimeWindowSize: TimeInterval`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize)

feature-extraction session이 audio file을 sample할 때마다 얼마나 많은 audio data를 읽을지 결정하는 시간 길이(초)입니다.

현재 페이지는 featureExtractor입니다
