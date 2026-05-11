---
title: "MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148752+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)

case

MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)
==================================================================================

audio feature data table에서 data source를 생성합니다.

iOS 15.0–17.0DeprecatediPadOS 15.0–17.0DeprecatedMac Catalyst 15.0–17.0DeprecatedmacOS 11.0–14.0DeprecatedvisionOS 1.0+

    case features(
        table: MLDataTable,
        featureColumn: String = __Defaults.featureColumnName,
        labelColumn: String = __Defaults.labelColumnName,
        parameters: MLSoundClassifier.FeatureExtractionParameters = FeatureExtractionParameters()
    )

[파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

`table`

labeled audio data를 포함하는 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
 instance입니다.

`featureColumn`

audio feature를 포함하는 column의 이름입니다.

`labelColumn`

audio label을 포함하는 column의 이름입니다.

`parameters`

feature-extraction 단계를 구성할 때 사용하는 [`MLSoundClassifier.FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)
 instance입니다.

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:)#discussion)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

[`extractFeatures(trainingData:parameters:sessionParameters:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))
 를 사용해 audio feature의 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
 을 생성합니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

### [data source 생성](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:)#Creating-a-data-source)

[`case labeledDirectories(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:))

각 subfolder가 audio file을 포함하는 folder에서 data source를 생성합니다.

[`case labeledFiles(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:))

각 audio file이 나타내는 sound 이름으로 파일명이 지정된 folder에서 data source를 생성합니다.

[`case filesByLabel([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:))

dictionary에서 data source를 생성합니다.

[`case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))

audio feature data frame에서 data source를 생성합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

현재 페이지: MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)
