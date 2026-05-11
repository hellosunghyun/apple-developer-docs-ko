---
title: "MLSoundClassifier.ModelParameters.ModelAlgorithmType.transferLearning(featureExtractor:classifier:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.164587+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
    *   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
        
*   [MLSoundClassifier.ModelParameters.ModelAlgorithmType](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype)
    
*   MLSoundClassifier.ModelParameters.ModelAlgorithmType.transferLearning(featureExtractor:classifier:)

case

MLSoundClassifier.ModelParameters.ModelAlgorithmType.transferLearning(featureExtractor:classifier:)
===================================================================================================

운영체제에 내장된 범용 model의 지식을 활용하는 algorithm입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    case transferLearning(
        featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType,
        classifier: MLSoundClassifier.ModelParameters.ClassifierType
    )

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`featureExtractor`

algorithm이 audio data에서 feature를 감지하는 데 사용하는 extractor type입니다.

`classifier`

algorithm이 audio data를 분류하는 데 사용하는 model type입니다.

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:)#discussion)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

다음과 같은 상황에서는 일반적으로 이 transfer-learning algorithm을 사용해 object detector를 training합니다.

*   training dataset의 example 수가 제한적입니다.
    
*   object detector의 Core ML model file 크기를 최대한 작게 유지하고 싶습니다.
    

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [algorithm 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:)#Designating-an-algorithm)

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)

sound-classifier training algorithm의 feature-extractor 옵션입니다.

[`enum ClassifierType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)

sound classifier training algorithm의 classifier 옵션입니다.

현재 페이지는 MLSoundClassifier.ModelParameters.ModelAlgorithmType.transferLearning(featureExtractor:classifier:)입니다
