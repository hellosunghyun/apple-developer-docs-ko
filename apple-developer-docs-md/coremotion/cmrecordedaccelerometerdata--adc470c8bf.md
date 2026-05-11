---
title: "CMRecordedAccelerometerData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.870071+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMRecordedAccelerometerData

class

CMRecordedAccelerometerData
===========================

device가 기록한 accelerometer data 한 건입니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    class CMRecordedAccelerometerData

[개요](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#overview)

------------------------------------------------------------------------------------------------------

이 class의 instance를 직접 만들지는 않습니다. 대신 [`CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)
object를 사용해 system에 이미 기록된 data를 가져옵니다.

[주제](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#topics)

--------------------------------------------------------------------------------------------------

### [accelerometer data 가져오기](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#Getting-the-Accelerometer-Data)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/startdate)

sensor sample이 기록된 wall clock 시각입니다.

[`var identifier: UInt64`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier)

accelerometer data의 고유 식별자입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#relationships)

----------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#inherits-from)

*   [`CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)
    

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#see-also)

------------------------------------------------------------------------------------------------------

### [accelerometer](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata#Accelerometers)

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

온보드 accelerometer에서 data를 가져옵니다.

[`class CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

device의 세 accelerometer에서 얻은 data sample입니다.

[`class CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

device에서 accelerometer data를 수집하고 가져오는 object입니다.

[`class CMSensorDataList`](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

system이 기록한 accelerometer data 목록입니다.

현재 페이지: CMRecordedAccelerometerData
