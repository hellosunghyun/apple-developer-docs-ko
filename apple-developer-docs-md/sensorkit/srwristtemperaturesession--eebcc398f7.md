---
title: "SRWristTemperatureSession | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.030389+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRWristTemperatureSession

class

SRWristTemperatureSession
=========================

device가 일정 기간 동안 기록한 손목 온도를 나타내는 object입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    class SRWristTemperatureSession

[개요](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#overview)

---------------------------------------------------------------------------------------------------

측정 시간 범위를 가져오려면 [`startDate`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/startdate)
 및 [`duration`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/duration)
 property를 사용합니다. 측정값 sequence를 가져오려면 [`temperatures`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/temperatures-8bqrl)
 property를 사용합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#topics)

-----------------------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#Getting-session-information)

[`var startDate: Date`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/startdate)

device가 손목 온도를 기록한 시각입니다.

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/duration)

device가 온도를 기록한 초 수입니다.

[`var version: String`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/version)

온도를 분석하는 algorithm version입니다.

### [기록된 온도 가져오기](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#Getting-recorded-temperatures)

[`var temperatures: some Sequence<SRWristTemperature>`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession/temperatures-8bqrl)

손목 온도와 각 정확도입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#relationships)

-------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#conforms-to)

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
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#see-also)

---------------------------------------------------------------------------------------------------

### [손목 온도 기록하기](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession#Recording-wrist-temperatures)

[`class SRWristTemperature`](https://developer.apple.com/documentation/sensorkit/srwristtemperature)

사용자가 잠자는 동안의 손목 온도입니다.

현재 페이지: SRWristTemperatureSession
