---
title: "MLSoundClassifier.ModelParameters.ValidationData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.158040+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   MLSoundClassifier.ModelParameters.ValidationData

enum

MLSoundClassifier.ModelParameters.ValidationData
================================================

sound classifier용 validation dataset의 source입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    enum ValidationData

[주제](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata#topics)

----------------------------------------------------------------------------------------------------------------------------------

### [validation data 지정하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata#Designating-validation-data)

[`case split(strategy: MLSplitStrategy)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:))

split strategy를 사용해 sound classifier의 training dataset 일부를 무작위로 선택해 만든 validation dataset입니다.

[`case dataSource(MLSoundClassifier.DataSource)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:))

data source로 표현한 validation dataset입니다.

[`case dictionary([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:))

dictionary로 표현한 validation dataset입니다.

Deprecated

[`case none`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none)

training 후 model validation 단계를 건너뛰는 비어 있는 validation dataset입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata#see-also)

--------------------------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata#Supporting-types)

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype)

sound classifier를 training하는 algorithm option입니다.

[`enum ClassifierType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)

sound classifier training algorithm용 classifier option입니다.

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)

sound-classifier training algorithm용 feature-extractor option입니다.

[`enum FeaturePrintType`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)

Audio Feature Print feature extractor의 type option입니다.

현재 페이지: MLSoundClassifier.ModelParameters.ValidationData
