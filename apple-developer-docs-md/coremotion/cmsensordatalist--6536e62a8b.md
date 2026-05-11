---
title: "CMSensorDataList | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmsensordatalist"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.870424+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmsensordatalist#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMSensorDataList

class

CMSensorDataList
================

system이 기록한 accelerometer data 목록입니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+watchOS 2.0+

    class CMSensorDataList

[개요](https://developer.apple.com/documentation/coremotion/cmsensordatalist#overview)

-------------------------------------------------------------------------------------------

이 class의 instance를 직접 만들지 않습니다. 대신 [`CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder) object에서 accelerometer data를 query한 결과로 받습니다.

다음 예제처럼 sensor data list object를 사용해 accelerometer data를 열거합니다:

    -(void)processSamplesFromDate:(NSDate*)start toDate:(NSDate)end {
       CMSensorRecorder* recorder = [[CMSensorRecorder alloc] init];
       CMSensorDataList* list = [recorder accelerometerDataFrom:start to:end];
     
       for (CMRecordedAccelerometerData* data in list) {
          // data를 처리합니다.
          NSLog(@"Sample: (%f, %f, %f)", data.acceleration.x,
                  data.acceleration.y, data.acceleration.z);
       }
    }
    

[관계](https://developer.apple.com/documentation/coremotion/cmsensordatalist#relationships)

-----------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmsensordatalist#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmsensordatalist#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSFastEnumeration`](https://developer.apple.com/documentation/Foundation/NSFastEnumeration)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmsensordatalist#see-also)

-------------------------------------------------------------------------------------------

### [accelerometer](https://developer.apple.com/documentation/coremotion/cmsensordatalist#Accelerometers)

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

내장 accelerometer에서 data를 가져옵니다.

[`class CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

device의 3축 accelerometer에서 가져온 data sample입니다.

[`class CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

device가 기록한 accelerometer data 한 건입니다.

[`class CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

device에서 accelerometer data를 수집하고 가져오는 object입니다.

현재 페이지는 CMSensorDataList입니다.
