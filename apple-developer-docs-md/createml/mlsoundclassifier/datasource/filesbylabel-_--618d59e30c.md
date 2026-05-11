---
title: "MLSoundClassifier.DataSource.filesByLabel(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.146346+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   MLSoundClassifier.DataSource.filesByLabel(\_:)

case

MLSoundClassifier.DataSource.filesByLabel(\_:)
==============================================

dictionary에서 data source를 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    case filesByLabel([String : [URL]])

[파라미터](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:)#parameters)

--------------------------------------------------------------------------------------------------------------------------

`dictionary`

labeled audio file collection을 담는 dictionary입니다. dictionary의 각 key는 label이고, 각 key의 값은 audio-file URL 배열입니다.

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:)#discussion)

--------------------------------------------------------------------------------------------------------------------------

이 data source는 dictionary의 각 key를 사용해 연결된 URL 배열의 audio file에 label을 지정합니다. 다음 코드는 `"Laughter"`와 `"Applause"` 두 label이 있는 dictionary를 만드는 방법을 보여줍니다.

    // Documents directory URL을 가져옵니다.
    guard let documentsURL = FileManager.default.urls(for: .documentDirectory,
                                                      in: .userDomainMask).first else {
        fatalError("Can't find Documents directory.")
    }
    
    
    // training data가 들어 있는 ~/Documents/Sounds directory의 URL을 만듭니다.
    let url = documentsURL.appendingPathComponent("Sounds")
    
    
    // label을 key로 하고 audio file URL 배열을 값으로 하는 dictionary를 만듭니다.
    let trainingData = [\
        "Laughter": [\
            url.appendingPathComponent("Laughter.1.aif"),\
            url.appendingPathComponent("Laughter.2.wav")\
        ],\
        "Applause": [\
            url.appendingPathComponent("Applause.1.mp3"),\
            url.appendingPathComponent("Applause.2.caf")\
        ]\
    ]
    
    
    let soundClassifier = try MLSoundClassifier(trainingData: trainingData)
    

각 label key의 값은 각각 laughter와 applause audio file을 가리키는 URL 배열입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:)#see-also)

----------------------------------------------------------------------------------------------------------------------

### [data source 생성](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/filesbylabel(_:)#Creating-a-data-source)

[`case labeledDirectories(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:))

각 subfolder에 audio file이 들어 있는 folder에서 data source를 만듭니다.

[`case labeledFiles(at: URL)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:))

각 audio file 이름이 해당 sound를 나타내는 folder에서 data source를 만듭니다.

[`case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:))

audio feature data table에서 data source를 만듭니다.

[`case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))

audio feature data frame에서 data source를 만듭니다.

[`struct FeatureExtractionParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)

audio file에서 sound feature를 추출하는 과정에 영향을 주는 parameter입니다.

현재 페이지는 MLSoundClassifier.DataSource.filesByLabel(\_:)입니다
