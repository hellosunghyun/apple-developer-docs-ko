---
title: "overlapFactor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.147132+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.FeatureExtractionParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)
    
*   overlapFactor

instance property

overlapFactor
=============

feature-extraction session이 audio data에서 연속된 두 window를 분석할 때 사용하는 overlap 비율입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    var overlapFactor: Double

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor#discussion)

----------------------------------------------------------------------------------------------------------------------------------------

overlap factor는 `[0.0, 1.0)` 범위에 있어야 하며, feature-extraction session이 각 파일에서 얼마나 많은 audio data를 분석할지에 영향을 줍니다. overlap factor가 작을수록 읽는 audio data sample 수가 적어 더 빨리 끝나지만 model의 prediction accuracy가 떨어질 수 있습니다. overlap factor가 클수록 각 파일에서 더 많은 audio sample을 읽으므로 session의 training data와 processing 시간이 늘어납니다. 추가된 training data는 sound classifier의 accuracy를 높일 수 있지만, 추가 processing 시간만큼의 가치가 없을 정도로 개선 폭이 작을 수도 있습니다.\
\
feature-extraction session은 `(featureExtractionTimeWindowSize * (1.0 - overlapFactor))` 식을 사용해 sample 사이에서 시간축으로 얼마나 _step_ (advance)할지 결정합니다.\
\
| Window size | Overlap factor | Step time |\
| --- | --- | --- |\
| `1.0` | `0.0` | `1.0` |\
| `2.0` | `0.0` | `2.0` |\
| `5.0` | `0.0` | `5.0` |\
| `1.0` | `0.5` | `0.5` |\
| `2.0` | `0.5` | `1.0` |\
| `5.0` | `0.5` | `2.5` |\
| `1.0` | `0.75` | `0.25` |\
| `2.0` | `0.75` | `0.5` |\
| `5.0` | `0.75` | `1.25` |\
\
예를 들어 window size가 `1.0`이고 overlap factor가 `0.0`인 session이 5초 길이 audio file을 분석하면 audio를 다섯 번 sample합니다. 각 sample의 time offset은 `0.0`, `1.0`, `2.0`, `3.0`, `4.0`입니다.\
\
window size가 `1.0`이고 overlap factor가 `0.5`인 다른 session은 같은 audio file을 0.5초 간격으로 10번 sample합니다. 첫 번째 session과 달리 이 session은 처음과 마지막 0.5초를 제외한 각 audio data 구간을 두 번씩 sample합니다.\
\
window size가 `1.0`이고 overlap factor가 `0.75`인 세 번째 session은 같은 5초 audio file을 0.25초 간격으로 20번 sample합니다. 이 세 번째 session은 대부분의 audio 구간을 네 번씩 sample하며, 양 끝에 가까운 구간은 한 번, 두 번 또는 세 번 sample합니다.\
\
[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor#see-also)\
\
------------------------------------------------------------------------------------------------------------------------------------\
\
### [feature extraction parameter에 접근하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/overlapfactor#Accessing-feature-extraction-parameters)\
\
[`var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor)\
\
session이 audio file에서 feature를 추출할 때 사용하는 algorithm type입니다.\
\
[`var featureExtractionTimeWindowSize: TimeInterval`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize)\
\
feature-extraction session이 audio file을 sample할 때마다 얼마나 많은 audio data를 읽을지 결정하는 시간 길이(초)입니다.\
\
현재 페이지: overlapFactor
