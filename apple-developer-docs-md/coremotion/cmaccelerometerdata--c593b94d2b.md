---
title: "CMAccelerometerData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaccelerometerdata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.869788+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAccelerometerData

class

CMAccelerometerData
===================

device의 세 accelerometer에서 가져온 data sample입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 2.0+

    class CMAccelerometerData

[개요](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#overview)

----------------------------------------------------------------------------------------------

app은 [`startAccelerometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))
 method의 마지막 parameter로 지정한 block handler와, 둘 다 `CMMotionManager` class에 선언된 [`accelerometerData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)
 property를 통해 `CMAccelerometerData` object에 접근합니다. `CMAccelerometerData`의 superclass인 [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
은 [`timestamp`](https://developer.apple.com/documentation/coremotion/cmlogitem/timestamp)
 property로 acceleration 측정이 수행된 시점을 기록합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#topics)

------------------------------------------------------------------------------------------

### [Accelerometer Data에 접근하기](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#Accessing-Accelerometer-Data)

[`var acceleration: CMAcceleration`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata/acceleration)

accelerometer가 측정한 acceleration입니다.

[`struct CMAcceleration`](https://developer.apple.com/documentation/coremotion/cmacceleration)

3축 acceleration 값을 담는 structure type입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#relationships)

--------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [상속하는 type](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#inherited-by)

*   [`CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#see-also)

----------------------------------------------------------------------------------------------

### [Accelerometer](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata#Accelerometers)

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

onboard accelerometer에서 data를 가져옵니다.

[`class CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

device가 기록한 accelerometer data 한 항목입니다.

[`class CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

device에서 accelerometer data를 수집하고 가져오는 object입니다.

[`class CMSensorDataList`](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

system이 기록한 accelerometer data 목록입니다.

현재 페이지: CMAccelerometerData
