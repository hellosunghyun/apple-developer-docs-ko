---
title: "predictions(from:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.135964+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   predictions(from:)

instance method

predictions(from:)
==================

audio file 배열에 대한 prediction을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func predictions(from audioFiles: [URL]) throws -> [String]

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:)#parameters)

-----------------------------------------------------------------------------------------------------------------

`audioFiles`

sound classifier가 category를 분류할 audio-file URL 배열입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:)#return-value)

---------------------------------------------------------------------------------------------------------------------

audio file에 대한 prediction label 배열입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:)#see-also)

-------------------------------------------------------------------------------------------------------------

### [sound classifier 테스트하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:)#Testing-a-sound-classifier)

[`func predictions(from: [URL], overlapFactor: Double, predictionTimeWindowSize: TimeInterval) throws -> [String]`](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:))

겹침 factor와 time window 크기를 사용해 audio file 배열의 prediction을 생성합니다.

현재 페이지: predictions(from:)
