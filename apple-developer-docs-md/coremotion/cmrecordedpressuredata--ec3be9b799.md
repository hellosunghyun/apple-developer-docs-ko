---
title: "CMRecordedPressureData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.871773+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMRecordedPressureData

class

CMRecordedPressureData
======================

기록된 pressure data 측정값입니다.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.1+watchOS 5.0+

    class CMRecordedPressureData

[개요](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#overview)

-------------------------------------------------------------------------------------------------

SensorKit의 [`ambientPressure`](https://developer.apple.com/documentation/SensorKit/SRSensor/ambientPressure)
 sensor를 사용해 ambient pressure data를 읽습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#topics)

---------------------------------------------------------------------------------------------

### [instance property](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#Instance-Properties)

[`var identifier: UInt64`](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata/identifier)

이 측정값을 고유하게 식별하는 값입니다.

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata/startdate)

system이 이 측정값을 기록한 날짜와 시간입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#relationships)

-----------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#inherits-from)

*   [`CMAmbientPressureData`](https://developer.apple.com/documentation/coremotion/cmambientpressuredata)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#see-also)

-------------------------------------------------------------------------------------------------

### [Ambient pressure](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata#Ambient-pressure)

[`class CMAmbientPressureData`](https://developer.apple.com/documentation/coremotion/cmambientpressuredata)

ambient pressure와 temperature의 측정값입니다.

현재 페이지: CMRecordedPressureData
