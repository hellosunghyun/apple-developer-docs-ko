---
title: "MLSoundClassifier.ModelParameters.ValidationData.split(strategy:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.159611+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
    *   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
        
*   [MLSoundClassifier.ModelParameters.ValidationData](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)
    
*   MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)

case

MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)
=================================================================

split strategy를 사용해 sound classifier의 training dataset 일부를 무작위로 선택해 만든 validation dataset입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    case split(strategy: MLSplitStrategy)

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:)#discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

*   strategy: 이 case가 training dataset에서 validation dataset을 만들 때 사용하는 partition method입니다.
    

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------------------

### [validation data 지정](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:)#Designating-validation-data)

[`case dataSource(MLSoundClassifier.DataSource)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:))

data source로 표현한 validation dataset입니다.

[`case dictionary([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:))

dictionary로 표현한 validation dataset입니다.

Deprecated

[`case none`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none)

training 후 model validation 단계를 건너뛰는 빈 validation dataset입니다.

현재 페이지는 MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)입니다
