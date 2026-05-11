---
title: "authorizationStatus | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.030866+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   authorizationStatus

instance property

authorizationStatus
===================

사용자가 app이 이 reader의 sensor에 접근하도록 동의했는지 나타내는 status입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var authorizationStatus: SRAuthorizationStatus { get }

[논의](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus#Discussion)

----------------------------------------------------------------------------------------------------------------

app이 특정 sensor의 data를 읽으려면 먼저 이 property 값에 접근해 사용자의 승인을 확인합니다. 값이 [`SRAuthorizationStatus.authorized`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/authorized)
이면 app은 recording을 시작하고([`startRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())
 참고) data fetch를 실행할 수 있습니다([`fetch(_:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:))
 참고).

값이 [`SRAuthorizationStatus.denied`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/denied)
이면 사용자가 Settings에서 reader sensor에 대한 authorization을 켜기 전까지 app은 recording을 시작하거나 fetch를 실행할 수 없습니다.

값이 [`SRAuthorizationStatus.notDetermined`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/notdetermined)
이면 사용자가 app 내 prompt에 아직 응답하지 않은 상태입니다. prompt를 표시하려면 [`requestAuthorization(sensors:completion:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))
를 호출합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus#see-also)

------------------------------------------------------------------------------------------------------------

### [사용자 authorization 확인](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus#Checking-user-authorization)

[`class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))

하나 이상의 sensor를 읽기 위한 사용자 permission을 요청합니다.

[`enum SRAuthorizationStatus`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus)

사용자가 app의 특정 sensor 읽기를 승인했는지 나타내는 상태입니다.

현재 페이지는 authorizationStatus입니다
