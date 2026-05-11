---
title: "isAccelerometerRecordingAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.877720+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)
    
*   isAccelerometerRecordingAvailable()

type method

isAccelerometerRecordingAvailable()
===================================

현재 device에서 accelerometer recording을 지원하는지 나타내는 Boolean 값을 반환합니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+watchOS 2.0+

    class func isAccelerometerRecordingAvailable() -> Bool

[반환 값](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable()#return-value)

---------------------------------------------------------------------------------------------------------------------------------------

accelerometer recording을 사용할 수 있으면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 그렇지 않으면 [`false`](https://developer.apple.com/documentation/Swift/false)
 입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable()#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------

이 class의 method로 accelerometer data를 기록하거나 가져오려 하기 전에 이 method를 호출합니다. accelerometer data recording은 모든 device에서 지원되지 않습니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable()#see-also)

-------------------------------------------------------------------------------------------------------------------------------

### [sensor recording 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable()#Checking-the-Availability-of-Sensor-Recording)

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/authorizationstatus())

app이 sensor data를 기록할 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization 상태입니다.

[`class func isAuthorizedForRecording() -> Bool`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isauthorizedforrecording())

app이 sensor data를 기록할 권한이 있는지 나타내는 Boolean 값을 반환합니다.

사용 중단

현재 페이지: isAccelerometerRecordingAvailable()
