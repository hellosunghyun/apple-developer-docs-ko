---
title: "speechRecognition | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.034438+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   speechRecognition

instance property

speechRecognition
=================

speech recognition request의 부분 결과 또는 최종 결과입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var speechRecognition: SFSpeechRecognitionResult? { get }

[참고 항목](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition#see-also)

-----------------------------------------------------------------------------------------------------------

### [speech metric 및 analytics 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition#Getting-speech-metrics-and-analytics)

[`var audioLevel: SRAudioLevel?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/audiolevel)

speech의 audio level입니다.

[`class SRAudioLevel`](https://developer.apple.com/documentation/sensorkit/sraudiolevel)

speech 범위의 audio level을 나타내는 object입니다.

[`var soundClassification: SNClassificationResult?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification)

해당 시간 범위에서 가장 높은 순위의 classification입니다.

[`var speechExpression: SRSpeechExpression?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechexpression)

speech 범위에 대한 metric과 voice analytics입니다.

현재 페이지: speechRecognition
