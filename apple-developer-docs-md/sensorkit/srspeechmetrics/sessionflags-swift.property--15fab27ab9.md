---
title: "sessionFlags | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.036621+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   sessionFlags

instance property

sessionFlags
============

audio 처리에 대한 세부 정보입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var sessionFlags: SRSpeechMetrics.SessionFlags { get }

[관련 항목](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property#see-also)

---------------------------------------------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property#Getting-session-information)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)

audio session identifier입니다.

[`struct SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)

audio stream 처리와 관련된 가능한 세부 정보입니다.

[`var timeSinceAudioStart: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart)

audio stream 시작 이후 경과한 시간(초)입니다.

[`var timestamp: Date`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp)

speech가 발생한 날짜와 시간입니다.

현재 페이지는 sessionFlags입니다
