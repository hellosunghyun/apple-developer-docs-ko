---
title: "CMMagnetometerData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmagnetometerdata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.870745+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMagnetometerData

class

CMMagnetometerData
==================

device를 기준으로 한 지구 자기장 측정값입니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    class CMMagnetometerData

[개요](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#overview)

---------------------------------------------------------------------------------------------

앱은 이 class의 instance로 표현되는 magnetometer 측정 sample을 [`startMagnetometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))
 method의 block handler나 `CMMotionManager` class의 [`magnetometerData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)
 property에서 가져올 수 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#topics)

-----------------------------------------------------------------------------------------

### [자기장 세기 가져오기](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#Getting-the-Field-Strength)

[`var magneticField: CMMagneticField`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield)

magnetometer가 측정한 자기장을 반환합니다.

[`struct CMMagneticField`](https://developer.apple.com/documentation/coremotion/cmmagneticfield)

3축 magnetometer data를 포함하는 structure입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#relationships)

-------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

현재 페이지: CMMagnetometerData
