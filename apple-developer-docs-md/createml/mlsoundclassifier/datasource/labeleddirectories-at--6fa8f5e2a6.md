---
title: "MLSoundClassifier.DataSource.labeledDirectories(at:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144026+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   MLSoundClassifier.DataSource.labeledDirectories(at:)

Case

MLSoundClassifier.DataSource.labeledDirectories(at:)
====================================================

각 하위 폴더에 audio file이 들어 있는 folder에서 data source를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    Case labeledDirectories(at: URL)

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------

`at`

URL : audio file 폴더들이 들어 있는 file system의 folder를 가리키는 URL입니다. data source는 각 folder 이름을 그 안에 있는 audio content의 classification label로 사용합니다.

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:)#discussion)

---------------------------------------------------------------------------------------------------------------------------------

이 data source는 각 subdirectory 이름을 그 안에 포함된 audio file의 label로 사용합니다. 예를 들어 `Laughter` subdirectory가 들어 있는 directory라면, data source는 해당 subdirectory의 각 audio file에 `"Laughter"` label을 적용합니다.

    // Build a URL to the directory that contains the labeled directories.
    let home = FileManager.default.homeDirectoryForCurrentUser
    let documents = home.appendingPathComponent("Documents")
    let labeledDirectories = documents.appendingPathComponent("Labeled Audio Directories")
    
    
    // Labeled Audio Directories/
    // ├── Laughter/
    // │ ├── Laughter1.m4a
    // │ ├── 20190229164259.m4a
    // │ ├── .
    // │ ├── .
    // │ ├── .
    // │ └── AudienceLaughing.mp3
    // └── Applause
    //   ├── misc-clapping.mp3
    //   ├── 20190229164211.m4a
    //   ├── .
    //   ├── .
    //   ├── .
    //   └── AudienceClapping.m4a
    
    
// labeled directory에서 data source를 만듭니다.
    let soundDataSource = MLSoundClassifier.DataSource.labeledDirectories(at: labeledDirectories)
    
    
// 이 data source로 sound classifier를 training합니다.
    let soundClassifier = try MLSoundClassifier(trainingData: soundDataSource)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------

### [data source 생성](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:)#Creating-a-data-source)

[`Case labeledFiles(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:))

각 file 이름이 해당 sound를 나타내는 audio file이 들어 있는 folder에서 data source를 생성합니다.

[`Case filesByLabel([String : [URL]])`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:))

dictionary에서 data source를 생성합니다.

[`Case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionparameter)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:))

audio feature data table에서 data source를 생성합니다.

[`Case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionparameter)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))

audio feature data frame에서 data source를 생성합니다.

[`struct FeatureExtractionparameter`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

현재 페이지: MLSoundClassifier.DataSource.labeledDirectories(at:)
