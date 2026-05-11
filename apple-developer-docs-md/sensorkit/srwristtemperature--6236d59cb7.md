---
title: "SRWristTemperature | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristtemperature"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.030500+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristtemperature#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRWristTemperature

class

SRWristTemperature
==================

사용자가 수면 중일 때 손목의 온도입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    class SRWristTemperature

[개요](https://developer.apple.com/documentation/sensorkit/srwristtemperature#overview)

--------------------------------------------------------------------------------------------

[`wristTemperature`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)
 sensor는 이 class를 자신의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srwristtemperature#topics)

----------------------------------------------------------------------------------------

### [온도 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srwristtemperature#Getting-temperature-information)

[`var timestamp: Date`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/timestamp)

device가 온도를 기록한 날짜와 시각입니다.

[`var value: Measurement<UnitTemperature>`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/value)

섭씨 단위의 온도 sensor 값입니다.

[`var errorEstimate: Measurement<UnitTemperature>`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/errorestimate)

온도 측정의 error 양에 대한 추정치입니다.

### [정확도 판단](https://developer.apple.com/documentation/sensorkit/srwristtemperature#Determining-the-accuracy)

[`var condition: SRWristTemperature.Condition`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/condition-swift.property)

정확도에 영향을 주는 측정 상태입니다.

[`struct Condition`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/condition-swift.struct)

온도 측정에 영향을 줄 수 있는 watch 사용자의 활동입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srwristtemperature#relationships)

------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srwristtemperature#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srwristtemperature#conforms-to)

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
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srwristtemperature#see-also)

--------------------------------------------------------------------------------------------

### [손목 온도 기록](https://developer.apple.com/documentation/sensorkit/srwristtemperature#Recording-wrist-temperatures)

[`class SRWristTemperatureSession`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession)

device가 일정 기간 동안 기록한 손목 온도를 나타내는 object입니다.

현재 페이지는 SRWristTemperature입니다.
