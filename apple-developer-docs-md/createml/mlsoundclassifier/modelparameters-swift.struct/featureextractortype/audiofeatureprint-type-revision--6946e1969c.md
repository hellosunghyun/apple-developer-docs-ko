---
title: "MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:)"
section: "Create ML"
scraped_at: "2026-05-11T03:54:01.004252+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
    *   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
        
*   [MLSoundClassifier.ModelParameters.FeatureExtractorType](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)
    
*   MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)

Case

MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)
========================================================================================

Audio Feature Print extractor를 나타냅니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    case audioFeaturePrint(
        type: MLSoundClassifier.ModelParameters.FeaturePrintType = .sound,
        revision: Int = 1
    )

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`type`

Audio Feature Print extractor type입니다.

`revision`

`type`에 전달하는 extractor의 version입니다.

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:)#discussion)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`type`과 `revision`에 associated value를 제공하지 않으면 이 case는 [`MLSoundClassifier.ModelParameters.FeaturePrintType.sound`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype/sound)
의 최신 version을 사용합니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Designating a feature extractor](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:)#Designating-a-feature-extractor)

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type option입니다.

[`case vggish(revision: Int)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:))

이전 OS version과 호환되는 VGGish feature extractor를 나타냅니다.

현재 페이지: MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)
