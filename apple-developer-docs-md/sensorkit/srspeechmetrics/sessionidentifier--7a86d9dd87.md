---
title: "sessionIdentifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.041541+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   sessionIdentifier

instance property

sessionIdentifier
=================

audio session 식별자입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var sessionIdentifier: String { get }

[논의](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier#Discussion)

---------------------------------------------------------------------------------------------------------------

예를 들어 이 property는 phone call 또는 Siri utterance의 식별자입니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier#see-also)

-----------------------------------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier#Getting-session-information)

[`var sessionFlags: SRSpeechMetrics.SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property)

audio processing에 대한 세부 정보입니다.

[`struct SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)

audio stream 처리에 대한 가능한 세부 정보입니다.

[`var timeSinceAudioStart: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart)

audio stream이 시작된 이후 경과한 초 수입니다.

[`var timestamp: Date`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp)

speech가 발생한 날짜와 시각입니다.

현재 페이지: sessionIdentifier
