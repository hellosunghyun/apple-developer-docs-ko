---
title: "SRSpeechExpression | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechexpression"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.029580+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechexpression#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRSpeechExpression

class

SRSpeechExpression
==================

일정 구간의 speech에 대한 metric과 voice analytics를 나타내는 object입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    class SRSpeechExpression

[개요](https://developer.apple.com/documentation/sensorkit/srspeechexpression#overview)

--------------------------------------------------------------------------------------------

이 class의 property를 사용해 사용자의 confidence level이나 mood 같은 speech 특성을 가져옵니다.

[주제](https://developer.apple.com/documentation/sensorkit/srspeechexpression#topics)

----------------------------------------------------------------------------------------

### [speech metric 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechexpression#Getting-speech-metrics)

[`var timeRange: CMTimeRange`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/timerange)

metric과 analytics가 적용되는 audio stream의 시간 범위입니다.

[`var version: String`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/version)

system이 metric과 analytics를 생성할 때 사용하는 algorithm version입니다.

### [speech analytics 가져오기](https://developer.apple.com/documentation/sensorkit/srspeechexpression#Getting-speech-analytics)

[`var confidence: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/confidence)

speaker의 confidence level입니다.

[`var mood: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/mood)

normal speech와 비교해 speaker의 발화가 얼마나 불분명하거나, 피곤하거나, 지친 것처럼 들리는지를 나타냅니다.

[`var valence: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/valence)

speaker의 감정이나 정서가 얼마나 긍정적 또는 부정적인지를 나타내는 정도입니다.

[`var activation: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation)

speaker의 energy 또는 activation 수준입니다.

[`var dominance: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance)

speaker가 얼마나 강하게 또는 약하게 들리는지를 나타내는 정도입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srspeechexpression#relationships)

------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srspeechexpression#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srspeechexpression#conforms-to)

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
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srspeechexpression#see-also)

--------------------------------------------------------------------------------------------

### [speech 분석](https://developer.apple.com/documentation/sensorkit/srspeechexpression#Analyzing-speech)

[`class SRSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)

일정 구간의 speech에 대한 metric을 나타내는 object입니다.

현재 페이지는 SRSpeechExpression입니다
