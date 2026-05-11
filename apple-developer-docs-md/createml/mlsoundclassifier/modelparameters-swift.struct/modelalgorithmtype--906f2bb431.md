---
title: "MLSoundClassifier.ModelParameters.ModelAlgorithmType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.158137+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   MLSoundClassifier.ModelParameters.ModelAlgorithmType

enum

MLSoundClassifier.ModelParameters.ModelAlgorithmType
====================================================

sound classifier를 training하는 algorithm option입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    enum ModelAlgorithmType

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#topics)

--------------------------------------------------------------------------------------------------------------------------------------

### [algorithm 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#Designating-an-algorithm)

[`case transferLearning(featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, classifier: MLSoundClassifier.ModelParameters.ClassifierType)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:))

operating system에 내장된 범용 model의 지식을 활용하는 algorithm입니다.

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)

sound-classifier training algorithm의 feature-extractor option입니다.

[`enum ClassifierType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)

sound classifier training algorithm의 classifier option입니다.

### [algorithm 설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#Describing-an-algorithm)

[`var description: String`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/description)

training algorithm의 text 표현입니다.

[관계](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#relationships)

----------------------------------------------------------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#conforms-to)

*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#see-also)

------------------------------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype#Supporting-types)

[`enum ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)

sound classifier용 validation dataset의 source입니다.

[`enum ClassifierType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)

sound classifier training algorithm의 classifier option입니다.

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)

sound-classifier training algorithm의 feature-extractor option입니다.

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type option입니다.

현재 페이지는 MLSoundClassifier.ModelParameters.ModelAlgorithmType입니다
