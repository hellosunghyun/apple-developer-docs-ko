---
title: "MLSoundClassifier.ModelParameters.FeatureExtractorType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.146967+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   MLSoundClassifier.ModelParameters.FeatureExtractorType

enum

MLSoundClassifier.ModelParameters.FeatureExtractorType
======================================================

sound-classifier training algorithm의 feature-extractor 옵션입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    enum FeatureExtractorType

[개요](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#overview)

--------------------------------------------------------------------------------------------------------------------------------------------

`vggish`보다 다음과 같은 장점이 있는 model을 만들려면 [`MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:))
 feature extractor를 사용합니다.

*   더 높은 prediction 정확도
    
*   더 낮은 latency
    
*   더 작은 model file 크기
    
*   더 짧은 training 시간
    

이전 OS version을 지원하려면 [`MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:))
를 사용합니다.

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#topics)

----------------------------------------------------------------------------------------------------------------------------------------

### [feature extractor 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#Designating-a-feature-extractor)

[`case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType, revision: Int)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:))

Audio Feature Print extractor를 나타냅니다.

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type 옵션입니다.

[`case vggish(revision: Int)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:))

이전 OS version과 호환되는 VGGish feature extractor를 나타냅니다.

### [feature extractor 설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#Describing-a-feature-extractor)

[`var description: String`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/description)

feature-extractor type의 text 표현입니다.

[관계](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#relationships)

------------------------------------------------------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#conforms-to)

*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#see-also)

--------------------------------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype#Supporting-types)

[`enum ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)

sound classifier용 validation dataset의 source입니다.

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype)

sound classifier를 training하는 algorithm 옵션입니다.

[`enum ClassifierType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)

sound classifier training algorithm의 classifier 옵션입니다.

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type 옵션입니다.

현재 페이지는 MLSoundClassifier.ModelParameters.FeatureExtractorType입니다.
