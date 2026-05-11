---
title: "SRSpeechMetrics.SessionFlags | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.036522+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
    
*   SRSpeechMetrics.SessionFlags

struct

SRSpeechMetrics.SessionFlags
============================

audio stream 처리에 관한 가능한 세부 정보입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    struct SessionFlags

[개요](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#overview)

-------------------------------------------------------------------------------------------------------------------

이 flag를 사용해 audio processing이 system voice processor를 거쳤는지 판단합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#topics)

---------------------------------------------------------------------------------------------------------------

### [Session flags](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#Session-flags)

[`static var bypassVoiceProcessing: SRSpeechMetrics.SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct/bypassvoiceprocessing)

audio processing이 system voice processor를 우회합니다.

### [Creating session flags](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#Creating-session-flags)

[`init(rawValue: UInt)`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct/init(rawvalue:))

지정한 값으로 새 structure를 생성해 반환합니다.

[관계](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#relationships)

-----------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`ExpressibleByArrayLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByArrayLiteral)
    
*   [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    
*   [`SetAlgebra`](https://developer.apple.com/documentation/Swift/SetAlgebra)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#see-also)

-------------------------------------------------------------------------------------------------------------------

### [Getting session information](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.struct#Getting-session-information)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionidentifier)

audio session의 identifier입니다.

[`var sessionFlags: SRSpeechMetrics.SessionFlags`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/sessionflags-swift.property)

audio processing에 대한 세부 정보입니다.

[`var timeSinceAudioStart: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timesinceaudiostart)

audio stream이 시작된 후 경과한 초 수입니다.

[`var timestamp: Date`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/timestamp)

speech가 발생한 날짜와 시간입니다.

현재 페이지: SRSpeechMetrics.SessionFlags
