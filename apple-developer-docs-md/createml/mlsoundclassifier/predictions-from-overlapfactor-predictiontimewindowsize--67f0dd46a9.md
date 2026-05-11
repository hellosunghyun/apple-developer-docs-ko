---
title: "predictions(from:overlapFactor:predictionTimeWindowSize:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.139705+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   predictions(from:overlapFactor:predictionTimeWindowSize:)

instance method

predictions(from:overlapFactor:predictionTimeWindowSize:)
=========================================================

overlap factor와 time window size를 사용해 audio file array에 대한 prediction을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    func predictions(
        from audioFiles: [URL],
        overlapFactor: Double,
        predictionTimeWindowSize: TimeInterval
    ) throws -> [String]

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------------

`audioFiles`

sound classifier가 분류할 audio-file URL array입니다.

`overlapFactor`

model이 audio data block을 분석할 때 연속된 analysis window 사이에 겹치는 양입니다.

`predictionTimeWindowSize`

method가 각 prediction마다 model로 보내는 audio buffer의 길이입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:)#return-value)

------------------------------------------------------------------------------------------------------------------------------------------------------------

audio file에 대한 prediction label array입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------------------

### [Testing a sound classifier](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:)#Testing-a-sound-classifier)

[`func predictions(from: [URL]) throws -> [String]`](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:))

audio file array에 대한 prediction을 생성합니다.

현재 페이지: predictions(from:overlapFactor:predictionTimeWindowSize:)
