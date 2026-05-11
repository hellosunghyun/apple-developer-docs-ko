---
title: "CMAltitudeData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaltitudedata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.871648+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaltitudedata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAltitudeData

class

CMAltitudeData
==============

기록된 고도 변화에 대한 data입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+watchOS 2.0+

    class CMAltitudeData

[개요](https://developer.apple.com/documentation/coremotion/cmaltitudedata#overview)

-----------------------------------------------------------------------------------------

이 class의 instance는 직접 생성하지 않습니다. altimeter 변화를 받으려면 [`CMAltimeter`](https://developer.apple.com/documentation/coremotion/cmaltimeter)
 class의 instance를 만들고, 그 object로 event를 query하거나 event 전달을 시작합니다. altimeter object는 적절한 시점에 이 class의 새 instance를 만들고, 지정한 handler에 전달합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmaltitudedata#topics)

-------------------------------------------------------------------------------------

### [고도 data 가져오기](https://developer.apple.com/documentation/coremotion/cmaltitudedata#Getting-the-Altitude-Data)

[`var relativeAltitude: NSNumber`](https://developer.apple.com/documentation/coremotion/cmaltitudedata/relativealtitude)

처음 보고된 event 이후의 고도 변화량(미터)입니다.

[`var pressure: NSNumber`](https://developer.apple.com/documentation/coremotion/cmaltitudedata/pressure)

기록된 압력(kPa)입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmaltitudedata#relationships)

---------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmaltitudedata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmaltitudedata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmaltitudedata#see-also)

-----------------------------------------------------------------------------------------

### [고도 data](https://developer.apple.com/documentation/coremotion/cmaltitudedata#Altitude-data)

[`class CMAltimeter`](https://developer.apple.com/documentation/coremotion/cmaltimeter)

고도 관련 변화 전달을 시작하는 object입니다.

[`class CMAbsoluteAltitudeData`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata)

절대 고도 변화를 기록하는 data입니다.

현재 페이지는 CMAltitudeData입니다.
