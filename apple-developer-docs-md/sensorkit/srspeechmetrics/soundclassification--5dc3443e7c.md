---
title: "soundClassification | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.034346+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   soundClassification

instance property

soundClassification
===================

해당 시간 범위에서 가장 높은 순위의 classification입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var soundClassification: SNClassificationResult? { get }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification#see-also)

-------------------------------------------------------------------------------------------------------------

### [speech metric과 analytics 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification#Getting-speech-metrics-and-analytics)

[`var audioLevel: SRAudioLevel?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/audiolevel)

speech의 audio level입니다.

[`class SRAudioLevel`](https://developer.apple.com/documentation/sensorkit/sraudiolevel)

speech 범위의 audio level을 나타내는 object입니다.

[`var speechRecognition: SFSpeechRecognitionResult?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition)

speech recognition 요청의 partial 또는 final result입니다.

[`var speechExpression: SRSpeechExpression?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechexpression)

해당 speech 범위의 metric과 voice analytics입니다.

현재 페이지는 soundClassification입니다.
