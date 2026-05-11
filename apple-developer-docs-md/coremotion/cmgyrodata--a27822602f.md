---
title: "CMGyroData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmgyrodata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.870644+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmgyrodata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMGyroData

class

CMGyroData
==========

device의 rotation rate를 한 번 측정한 값입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 2.0+

    class CMGyroData

[개요](https://developer.apple.com/documentation/coremotion/cmgyrodata#overview)

-------------------------------------------------------------------------------------

application은 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 class의 [`startGyroUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))
 method 또는 [`startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())
 method를 호출한 뒤 정해진 간격으로 `CMGyroData` object를 받거나 sample합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmgyrodata#topics)

---------------------------------------------------------------------------------

### [Getting the Rotation Rate](https://developer.apple.com/documentation/coremotion/cmgyrodata#Getting-the-Rotation-Rate)

[`var rotationRate: CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate)

device의 gyroscope가 측정한 rotation rate입니다.

[`struct CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationrate)

rotation rate 측정값을 나타내는 structure type입니다.

[`class CMRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrotationratedata)

rotation-rate 측정값 하나를 담는 data object입니다.

[`class CMRecordedRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)

특정 시점의 rotation-rate 측정값 하나를 담는 data object입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmgyrodata#relationships)

-----------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmgyrodata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmgyrodata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmgyrodata#see-also)

-------------------------------------------------------------------------------------

### [Gyroscopes](https://developer.apple.com/documentation/coremotion/cmgyrodata#Gyroscopes)

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

내장 gyroscope에서 data를 가져옵니다.

현재 페이지: CMGyroData
