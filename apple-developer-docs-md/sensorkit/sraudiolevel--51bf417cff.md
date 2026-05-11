---
title: "SRAudioLevel | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/sraudiolevel"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.034541+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/sraudiolevel#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRAudioLevel

class

SRAudioLevel
============

speech 범위의 audio level을 나타내는 object입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    class SRAudioLevel

[개요](https://developer.apple.com/documentation/sensorkit/sraudiolevel#overview)

--------------------------------------------------------------------------------------

[`loudness`](https://developer.apple.com/documentation/sensorkit/sraudiolevel/loudness)
property를 사용해 audio level value를 가져옵니다.

[주제](https://developer.apple.com/documentation/sensorkit/sraudiolevel#topics)

----------------------------------------------------------------------------------

### [Getting metrics](https://developer.apple.com/documentation/sensorkit/sraudiolevel#Getting-metrics)

[`var timeRange: CMTimeRange`](https://developer.apple.com/documentation/sensorkit/sraudiolevel/timerange)

level이 적용되는 audio stream의 시간 범위입니다.

[`var loudness: Double`](https://developer.apple.com/documentation/sensorkit/sraudiolevel/loudness)

decibel 단위의 audio level measurement입니다.

[관계](https://developer.apple.com/documentation/sensorkit/sraudiolevel#relationships)

------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/sraudiolevel#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/sraudiolevel#conforms-to)

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
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/sraudiolevel#see-also)

--------------------------------------------------------------------------------------

### [Getting speech metrics and analytics](https://developer.apple.com/documentation/sensorkit/sraudiolevel#Getting-speech-metrics-and-analytics)

[`var audioLevel: SRAudioLevel?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/audiolevel)

speech의 audio level입니다.

[`var speechRecognition: SFSpeechRecognitionResult?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechrecognition)

speech recognition request의 partial 또는 final result입니다.

[`var soundClassification: SNClassificationResult?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification)

해당 시간 범위에서 가장 높은 순위의 classification입니다.

[`var speechExpression: SRSpeechExpression?`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/speechexpression)

speech 범위에 대한 metric과 voice analytics입니다.

현재 페이지: SRAudioLevel
