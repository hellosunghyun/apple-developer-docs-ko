---
title: "requestAuthorization(sensors:completion:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.035438+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   requestAuthorization(sensors:completion:)

type method

requestAuthorization(sensors:completion:)
=========================================

하나 이상의 sensor를 읽기 위한 사용자 permission을 요청합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class func requestAuthorization(
        sensors: Set<SRSensor>,
        completion: @escaping @Sendable ((any Error)?) -> Void
    )

    class func requestAuthorization(sensors: Set<SRSensor>) async throws

[parameter](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------

`sensors`

app이 요청하는 하나 이상의 sensor입니다.

`completion`

framework가 사용자 authorization을 판단한 뒤 실행할 closure입니다.

[설명](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:)#Discussion)

--------------------------------------------------------------------------------------------------------------------------------------

[`authorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)
가 [`SRAuthorizationStatus.notDetermined`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/notdetermined)
인 sensor에 대해서는, 이 function을 호출해 사용자 authorization을 요청하는 prompt를 표시합니다. prompt가 사라지면 framework가 `completion` closure를 호출합니다. 사용자가 sensor access를 승인했는지는 delegate가 [`sensorReader(_:didChange:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:))
호출을 기다린 뒤 판단해야 합니다.

사용자가 이미 in-app prompt에 응답한 sensor를 이 function에 전달하면 framework는 [`SRError.Code.promptDeclined`](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined)
와 함께 prompt를 취소합니다. 특정 sensor에 대한 prompt에 이미 응답했다면, 그 sensor의 [`authorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)
는 [`SRAuthorizationStatus.authorized`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/authorized)
또는 [`SRAuthorizationStatus.denied`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/denied)
입니다. 사용자는 Settings > Privacy > Research Sensor & Usage Data에서 sensor의 authorization status를 바꿀 수 있습니다.

authorization workflow에 대한 자세한 내용은 [sensor reading용 project 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)
를 참고하십시오.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------

### [사용자 authorization 확인](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:)#Checking-user-authorization)

[`var authorizationStatus: SRAuthorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)

사용자가 app이 이 reader의 sensor에 access하도록 동의했는지에 대한 status입니다.

[`enum SRAuthorizationStatus`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus)

사용자가 app이 특정 sensor를 읽는 것을 승인했는지 나타내는 상태입니다.

현재 페이지는 requestAuthorization(sensors:completion:)입니다.
