---
title: "CMRotationRateData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmrotationratedata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.873447+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmrotationratedata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMRotationRateData

class

CMRotationRateData
==================

단일 rotation-rate 측정값을 담는 data object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+macOS 10.15+visionOS 1.0+watchOS 7.0+

    class CMRotationRateData

[주제](https://developer.apple.com/documentation/coremotion/cmrotationratedata#topics)

-----------------------------------------------------------------------------------------

### [Rotation Data에 접근하기](https://developer.apple.com/documentation/coremotion/cmrotationratedata#Accessing-Rotation-Data)

[`var rotationRate: CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationratedata/rotationrate)

gyroscope가 측정한 rotation rate입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmrotationratedata#relationships)

-------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmrotationratedata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [상속하는 type](https://developer.apple.com/documentation/coremotion/cmrotationratedata#inherited-by)

*   [`CMRecordedRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmrotationratedata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmrotationratedata#see-also)

---------------------------------------------------------------------------------------------

### [Rotation Rate 가져오기](https://developer.apple.com/documentation/coremotion/cmrotationratedata#Getting-the-Rotation-Rate)

[`var rotationRate: CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate)

device의 gyroscope가 측정한 rotation rate입니다.

[`struct CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationrate)

rotation rate 측정값을 나타내는 structure type입니다.

[`class CMRecordedRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)

특정 시점의 단일 rotation-rate 측정값을 담는 data object입니다.

현재 페이지: CMRotationRateData
