---
title: "MLSoundClassifier.ModelParameters.ValidationData.none | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none"
section: "Create ML"
scraped_at: "2026-05-11T03:53:53.714957+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
    *   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
        
*   [MLSoundClassifier.ModelParameters.ValidationData](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)
    
*   MLSoundClassifier.ModelParameters.ValidationData.none

Case

MLSoundClassifier.ModelParameters.ValidationData.none
=====================================================

training 후 model validation phase를 건너뛰는 빈 validation dataset입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    case none

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------

### [Designating validation data](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/none#Designating-validation-data)

[`case split(strategy: MLSplitStrategy)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:))

split strategy를 사용해 sound classifier training dataset의 일부를 무작위로 선택해 만든 validation dataset입니다.

[`case dataSource(MLSoundClassifier.DataSource)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:))

data source로 표현한 validation dataset입니다.

[`case dictionary([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:))

dictionary로 표현한 validation dataset입니다.

Deprecated

현재 페이지: MLSoundClassifier.ModelParameters.ValidationData.none
