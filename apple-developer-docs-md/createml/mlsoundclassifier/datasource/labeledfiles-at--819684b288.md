---
title: "MLSoundClassifier.DataSource.labeledFiles(at:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.145794+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   MLSoundClassifier.DataSource.labeledFiles(at:)

Case

MLSoundClassifier.DataSource.labeledFiles(at:)
==============================================

각 file 이름이 나타내는 sound를 기준으로 지정된 audio file이 들어 있는 folder에서 data source를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    case labeledFiles(at: URL)

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:)#parameters)

---------------------------------------------------------------------------------------------------------------------------

`at`

URL: file system에서 audio file이 들어 있는 folder의 URL입니다. data source는 각 audio file 이름의 첫 번째 component를 classification label로 사용합니다.

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:)#discussion)

---------------------------------------------------------------------------------------------------------------------------

`labeledFiles` case를 사용해 audio file directory에서 sound classifier data source를 생성합니다. 각 file 이름은 sound classification label로 시작하고, 그 뒤에 마침표와 임의의 string이 오며, 마지막은 file extension으로 끝나야 합니다. 예를 들어 sound classifier의 training file 이름을 `Laughter.3.png`, `Applause.1.jpg`, `Applause.2.jpg`처럼 지정할 수 있습니다.

이 예제에서 이 audio file 이름들은 sound classifier에 최소 두 개의 class label을 제공합니다.

*   `Laughter`
    
*   `Applause`
    

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:)#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [Creating a data source](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:)#Creating-a-data-source)

[`case labeledDirectories(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:))

각 subfolder에 audio file이 들어 있는 folder에서 data source를 생성합니다.

[`case filesByLabel([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:))

dictionary에서 data source를 생성합니다.

[`case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:))

audio feature의 data table에서 data source를 생성합니다.

[`case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))

audio feature의 data frame에서 data source를 생성합니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 process에 영향을 주는 parameter입니다.

현재 페이지: MLSoundClassifier.DataSource.labeledFiles(at:)
