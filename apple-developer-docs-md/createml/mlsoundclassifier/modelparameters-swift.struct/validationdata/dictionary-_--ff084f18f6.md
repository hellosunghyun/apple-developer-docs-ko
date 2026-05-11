---
title: "MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.159813+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   [MLSoundClassifier.ModelParameters.ValidationData](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
    *   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
        
    *   [MLSoundClassifier.ModelParameters.ValidationData](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)
        
*   MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:) Deprecated

Case

MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:)
================================================================

dictionary로 표현된 validation dataset입니다.

iOS 15.0–16.0DeprecatediPadOS 15.0–16.0DeprecatedMac Catalyst 15.0–16.0DeprecatedmacOS 10.15–11.0DeprecatedvisionOS 1.0+

    case dictionary([String : [URL]])

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:)#discussion)

---------------------------------------------------------------------------------------------------------------------------------------------------------

*   dictionary: dictionary로 표현된 label audio file collection을 사용하는 validation dataset입니다. dictionary의 각 key는 label이며, 값은 audio-file URL array입니다.
    

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------------------

### [validation data 지정하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:)#Designating-validation-data)

[`case split(strategy: MLSplitStrategy)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:))

split strategy를 사용해 sound classifier의 training dataset 일부를 무작위로 선택해 파생한 validation dataset입니다.

[`case dataSource(MLSoundClassifier.DataSource)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:))

data source로 표현된 validation dataset입니다.

[`case none`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none)

training 후 model validation phase를 건너뛰는 빈 validation dataset입니다.

현재 페이지: MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:)
