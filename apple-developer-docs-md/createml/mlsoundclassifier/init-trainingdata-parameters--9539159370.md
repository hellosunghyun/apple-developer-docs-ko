---
title: "init(trainingData:parameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142848+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   init(trainingData:parameters:)

initializer

init(trainingData:parameters:)
==============================

data source로 표현된 training dataset으로 sound classifier를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    init(
        trainingData: MLSoundClassifier.DataSource,
        parameters: MLSoundClassifier.ModelParameters = ModelParameters()
    ) throws

모든 선언 보기

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------

`trainingData`

label된 audio file collection을 포함하는 [`MLSoundClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
 instance입니다.

`parameters`

training session용 model을 구성할 때 사용하는 [`MLSoundClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
 instance입니다.

[설명](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)#discussion)

-----------------------------------------------------------------------------------------------------------------------------

이 initializer를 사용해 [`MLSoundClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
 로 sound classifier를 training합니다. 예를 들어 audio file을 label별 directory로 정리할 수 있습니다. [`MLSoundClassifier.DataSource.labeledDirectories(at:)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:))
 를 참고하세요.

    // Documents directory URL을 가져옵니다.
    guard let documentsURL = FileManager.default.urls(for: .documentDirectory,
                                                      in: .userDomainMask).first else {
        fatalError("Can't find Documents directory.")
    }
    
    
    // training data가 들어 있는 ~/Documents/Sounds directory의 URL을 만듭니다.
    let soundsURL = documentsURL.appendingPathComponent("Sounds")
    
    
    // Sounds directory에는 sound class별 subdirectory가 들어 있습니다.
    // 각 subdirectory 이름이 그 안에 있는 audio file의 label입니다.
    //
    // Sounds
    // -- Laughter
    // -- Recording1.wav
    // -- Recording4.wav
    // -- ...
    // -- Applause
    // -- Recording2.wav
    // -- Recording5.wav
    // -- ...
    
    
    // Sounds directory에서 data source를 생성합니다.
    let trainingData = MLSoundClassifier.DataSource.labeledDirectories(at: soundsURL)
    
    
    // data source로 sound classifier를 training합니다.
    let soundClassifier = try MLSoundClassifier(trainingData: trainingData)
    

현재 페이지: init(trainingData:parameters:)
