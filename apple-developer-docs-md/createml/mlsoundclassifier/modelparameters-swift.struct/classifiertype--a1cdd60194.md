---
title: "MLSoundclassifier.Model파라미터.classifierType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype"
section: "Create ML"
scraped_at: "2026-05-11T03:54:14.156036+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundclassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundclassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundclassifier.Model파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   MLSoundclassifier.Model파라미터.classifierType

enumeration

MLSoundclassifier.Model파라미터.classifierType
================================================

sound classifier training algorithm의 classifier 옵션입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    enum classifierType

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#topics)

----------------------------------------------------------------------------------------------------------------------------------

### [algorithm의 classifier 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#Designating-an-algorithms-classifier)

[`case logisticRegressor`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype/logisticregressor)

logistic regression을 사용해 input vector를 category로 분류하는 통계 model입니다.

[`case multilayerPerceptron(layerSizes: [Int])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype/multilayerperceptron(layersizes:))

3개 이상의 layer를 사용해 input을 category로 분류하는 neural network model입니다.

### [classifier type 설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#Describing-a-classifier-type)

[`var description: String`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype/description)

classifier type의 text 표현입니다.

[관계](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#relationships)

------------------------------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#conforms-to)

*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#see-also)

--------------------------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype#Supporting-types)

[`enum ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)

sound classifier용 validation dataset의 source입니다.

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype)

sound classifier를 training하는 algorithm 옵션입니다.

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)

sound-classifier training algorithm의 feature extractor 옵션입니다.

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type 옵션입니다.

현재 페이지는 MLSoundclassifier.Model파라미터.classifierType입니다
