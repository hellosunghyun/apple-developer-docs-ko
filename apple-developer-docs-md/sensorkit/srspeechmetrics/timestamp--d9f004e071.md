---
title: "timestamp | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.036344+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   timestamp

instance property

timestamp
=========

speech가 발생한 날짜와 시간입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var timestamp: Date { get }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp#see-also)

---------------------------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp#Getting-session-information)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)

audio session의 identifier입니다.

[`var sessionFlags: SRSpeechMetrics.SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property)

audio processing에 대한 세부 정보입니다.

[`struct SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)

audio stream 처리에 관한 가능한 세부 정보입니다.

[`var timeSinceAudioStart: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart)

audio stream이 시작된 이후 경과한 초 수입니다.

현재 페이지: timestamp
