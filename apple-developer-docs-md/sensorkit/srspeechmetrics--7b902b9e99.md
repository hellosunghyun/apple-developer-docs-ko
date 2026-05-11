---
title: "SRSpeechMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.029242+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRSpeechMetrics

class

SRSpeechMetrics
===============

speech 범위에 대한 metric을 나타내는 object입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    class SRSpeechMetrics

[개요](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#overview)

-----------------------------------------------------------------------------------------

audio level을 가져오려면 [`audioLevel`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/audiolevel)
 property를 사용합니다. 그 외에는 [`speechRecognition`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition)
, [`soundClassification`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification)
, [`speechExpression`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechexpression)
 property를 사용해 speech 특성을 가져옵니다.

[`siriSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)
 sensor는 이 class를 자신의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#topics)

-------------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#Getting-session-information)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)

audio session의 identifier입니다.

[`var sessionFlags: SRSpeechMetrics.SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property)

audio processing의 세부 정보입니다.

[`struct SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)

audio stream 처리에 대한 가능한 세부 정보입니다.

[`var timeSinceAudioStart: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart)

audio stream이 시작된 이후 경과한 초 수입니다.

[`var timestamp: Date`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp)

speech가 발생한 날짜와 시각입니다.

### [speech metric 및 analytics 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#Getting-speech-metrics-and-analytics)

[`var audioLevel: SRAudioLevel?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/audiolevel)

speech의 audio level입니다.

[`class SRAudioLevel`](https://developer.apple.com/documentation/sensorkit/sraudiolevel)

speech 범위의 audio level을 나타내는 object입니다.

[`var speechRecognition: SFSpeechRecognitionResult?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition)

speech recognition request의 부분 결과 또는 최종 결과입니다.

[`var soundClassification: SNClassificationResult?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification)

해당 시간 범위에서 가장 높은 순위의 classification입니다.

[`var speechExpression: SRSpeechExpression?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechexpression)

speech 범위의 metric과 voice analytics입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#relationships)

---------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#see-also)

-----------------------------------------------------------------------------------------

### [speech 분석](https://developer.apple.com/documentation/sensorkit/srspeechmetrics#Analyzing-speech)

[`class SRSpeechExpression`](https://developer.apple.com/documentation/sensorkit/srspeechexpression)

speech 범위의 metric과 voice analytics를 나타내는 object입니다.

현재 페이지: SRSpeechMetrics
