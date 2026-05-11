---
title: "CMAbsoluteAltitudeData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.871487+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAbsoluteAltitudeData

class

CMAbsoluteAltitudeData
======================

absolute altitude의 변화를 기록하는 data입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+visionOS 1.0+watchOS 8.0+

    class CMAbsoluteAltitudeData

[개요](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#overview)

-------------------------------------------------------------------------------------------------

Absolute altitude는 iPhone 12 이후 model과 Apple Watch 6 또는 SE 이후 model에서만 사용할 수 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#topics)

---------------------------------------------------------------------------------------------

### [Altitude data에 접근하기](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#Accessing-Altitude-Data)

[`var altitude: Double`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata/altitude)

해수면을 기준으로 측정한 device의 absolute altitude(미터)입니다.

[`var accuracy: Double`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata/accuracy)

1 standard deviation을 기준으로 한 altimeter의 추정 불확실성(미터)입니다.

[`var precision: Double`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata/precision)

altitude에 권장되는 해상도(미터)입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#relationships)

-----------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#see-also)

-------------------------------------------------------------------------------------------------

### [Altitude data](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata#Altitude-data)

[`class CMAltimeter`](https://developer.apple.com/documentation/coremotion/cmaltimeter)

altitude 관련 변화 전달을 시작하는 object입니다.

[`class CMAltitudeData`](https://developer.apple.com/documentation/coremotion/cmaltitudedata)

기록된 altitude 변화에 대한 data입니다.

현재 페이지: CMAbsoluteAltitudeData
