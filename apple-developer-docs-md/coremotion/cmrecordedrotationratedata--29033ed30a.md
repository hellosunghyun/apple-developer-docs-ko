---
title: "CMRecordedRotationRateData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.873350+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMRecordedRotationRateData

class

CMRecordedRotationRateData
==========================

특정 시점의 단일 rotation-rate 측정값을 담는 data object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+macOS 10.15+visionOS 1.0+watchOS 7.0+

    class CMRecordedRotationRateData

[주제](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#topics)

-------------------------------------------------------------------------------------------------

### [rotation data 접근](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#Accessing-Rotation-Data)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata/startdate)

gyroscope가 rotation data를 측정한 시각입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#relationships)

---------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#inherits-from)

*   [`CMRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrotationratedata)
    

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#see-also)

-----------------------------------------------------------------------------------------------------

### [rotation rate 가져오기](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata#Getting-the-Rotation-Rate)

[`var rotationRate: CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate)

device의 gyroscope가 측정한 rotation rate입니다.

[`struct CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationrate)

rotation rate 측정값을 나타내는 struct type입니다.

[`class CMRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrotationratedata)

단일 rotation-rate 측정값을 담는 data object입니다.

현재 페이지는 CMRecordedRotationRateData입니다.
