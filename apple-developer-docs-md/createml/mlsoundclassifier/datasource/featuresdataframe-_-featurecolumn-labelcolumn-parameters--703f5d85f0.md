---
title: "MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148888+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)

Case

MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)
========================================================================================

audio feature의 data frame에서 data source를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    case featuresDataFrame(
        DataFrame,
        featureColumn: String = __Defaults.featureColumnName,
        labelColumn: String = __Defaults.labelColumnName,
        parameters: MLSoundClassifier.FeatureExtractionParameters = FeatureExtractionParameters()
    )

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

`dataFrame`

label된 audio data가 들어 있는 data frame입니다.

`featureColumn`

audio feature가 들어 있는 column 이름입니다.

`labelColumn`

audio label이 들어 있는 column 이름입니다.

`parameters`

feature-extraction phase를 구성하는 데 사용하는 [`MLSoundClassifier.FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)
instance입니다.

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:)#discussion)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`extractFeatures(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))
를 사용해 audio feature의 [`DataFrame`](https://developer.apple.com/documentation/TabularData/DataFrame)
을 만듭니다.

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

### [data source 생성하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:)#Creating-a-data-source)

[`case labeledDirectories(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:))

각각 audio file을 담은 subfolder가 있는 folder에서 data source를 생성합니다.

[`case labeledFiles(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:))

folder에 들어 있는 audio file에서 data source를 생성하며, 각 file 이름은 해당 sound를 나타냅니다.

[`case filesByLabel([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:))

dictionary에서 data source를 생성합니다.

[`case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:))

audio feature의 data table에서 data source를 생성합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

현재 페이지: MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)
