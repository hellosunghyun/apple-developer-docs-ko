---
title: "timeSinceAudioStart | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.036431+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   timeSinceAudioStart

instance property

timeSinceAudioStart
===================

audio stream이 시작된 이후의 초 단위 시간입니다.

iOS 17.2+iPadOS 17.2+Mac Catalyst 17.2+

    var timeSinceAudioStart: TimeInterval { get }

[논의](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart#Discussion)

-----------------------------------------------------------------------------------------------------------------

전화 통화처럼 audio stream이 시작되면 SensorKit이 주기적으로 sample을 수집합니다. 이 field를 사용해 audio stream 안에서 sample의 순서를 판단합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart#see-also)

-------------------------------------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart#Getting-session-information)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)

audio session의 identifier입니다.

[`var sessionFlags: SRSpeechMetrics.SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property)

audio processing에 대한 세부 정보입니다.

[`struct SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct)

audio stream 처리에 대한 가능한 세부 정보입니다.

[`var timestamp: Date`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp)

speech가 발생한 날짜와 시각입니다.

현재 페이지: timeSinceAudioStart
