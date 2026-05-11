---
title: "CMSensorRecorder | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmsensorrecorder"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.870297+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMSensorRecorder

class

CMSensorRecorder
================

device에서 accelerometer data를 수집하고 가져오는 object입니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+watchOS 2.0+

    class CMSensorRecorder

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#mentions)

-----------------------------------------------------------------------------------------------

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

[개요](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#overview)

-------------------------------------------------------------------------------------------

sensor recorder를 사용해 accelerometer data 수집을 시작합니다. 이후 sensor recorder를 사용해 기록된 data를 가져와 분석할 수 있습니다. 기록된 data를 사용해 특정 motion 유형을 평가하고 그 결과를 app에 반영할 수 있습니다.

sensor recorder를 사용하려면 이 class의 instance를 만들고 [`recordAccelerometer(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:))
 method를 호출해 data 기록을 시작합니다. 기록을 명시적으로 중지할 필요는 없습니다. 지정한 시간이 지나고 recording 시간을 연장하는 다른 app이 없으면 system이 자동으로 기록을 중지합니다. 다음 예제는 20분 분량의 accelerometer data를 기록하는 방법을 보여줍니다.

[주제](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#topics)

---------------------------------------------------------------------------------------

### [Checking the Availability of Sensor Recording](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#Checking-the-Availability-of-Sensor-Recording)

[`class func isAccelerometerRecordingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable())

현재 device가 accelerometer recording을 지원하는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/authorizationstatus())

app이 sensor data를 기록할 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization 상태입니다.

[`class func isAuthorizedForRecording() -> Bool`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isauthorizedforrecording())

app이 sensor data를 기록할 권한이 있는지 나타내는 Boolean 값을 반환합니다.

Deprecated

### [Recording Accelerometer Data](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#Recording-Accelerometer-Data)

[`func recordAccelerometer(forDuration: TimeInterval)`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:))

지정한 기간 동안 accelerometer data 기록을 시작합니다.

### [Retrieving Past Accelerometer Data](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#Retrieving-Past-Accelerometer-Data)

[`func accelerometerData(from: Date, to: Date) -> CMSensorDataList?`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/accelerometerdata(from:to:))

지정한 날짜 사이에 수집한 accelerometer data를 가져옵니다.

[관계](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#relationships)

-----------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#see-also)

-------------------------------------------------------------------------------------------

### [Accelerometers](https://developer.apple.com/documentation/coremotion/cmsensorrecorder#Accelerometers)

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

onboard accelerometer에서 data를 가져옵니다.

[`class CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

device의 3축 accelerometer에서 가져온 data sample입니다.

[`class CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

device가 기록한 accelerometer data 한 건입니다.

[`class CMSensorDataList`](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

system이 기록한 accelerometer data 목록입니다.

현재 페이지: CMSensorRecorder
