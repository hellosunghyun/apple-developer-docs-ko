---
title: "MLSoundClassifier.ModelParameters.FeaturePrintType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype"
section: "Create ML"
scraped_at: "2026-05-11T03:54:07.357326+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   MLSoundClassifier.ModelParameters.FeaturePrintType

enum

MLSoundClassifier.ModelParameters.FeaturePrintType
==================================================

Audio Feature Print feature extractor의 type option입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    enum FeaturePrintType

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#topics)

------------------------------------------------------------------------------------------------------------------------------------

### [feature-print type 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#Designating-a-feature-print-type)

[`case sound`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype/sound)

sound classifier용 feature print type을 생성합니다.

### [feature-print type 설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#Describing-a-feature-print-type)

[`var description: String`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype/description)

feature-print type의 text 표현입니다.

[관계](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#relationships)

--------------------------------------------------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#see-also)

----------------------------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype#Supporting-types)

[`enum ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)

sound classifier용 validation dataset의 source입니다.

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype)

sound classifier를 training하는 algorithm option입니다.

[`enum ClassifierType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)

sound classifier training algorithm의 classifier option입니다.

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)

sound-classifier training algorithm의 feature-extractor option입니다.

현재 페이지는 MLSoundClassifier.ModelParameters.FeaturePrintType
