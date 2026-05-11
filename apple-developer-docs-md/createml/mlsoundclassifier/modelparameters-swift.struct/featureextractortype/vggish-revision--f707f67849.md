---
title: "MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:47.553232+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
    *   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
        
*   [MLSoundClassifier.ModelParameters.FeatureExtractorType](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)
    
*   MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)

case

MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)
========================================================================

이전 OS version과 호환되는 VGGish feature extractor를 나타냅니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    case vggish(revision: Int = 1)

[파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

`revision`

VGGish feature extractor의 version입니다.

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:)#discussion)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

`revision`의 associated value를 제공하지 않으면 이 case는 가장 최신 version을 사용합니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:)#see-also)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

### [feature extractor 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:)#Designating-a-feature-extractor)

[`case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType, revision: Int)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:))

Audio Feature Print extractor를 나타냅니다.

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type option입니다.

현재 페이지는 MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)입니다
