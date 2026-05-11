---
title: "SRAuthorizationStatus | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srauthorizationstatus"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.037467+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRAuthorizationStatus

enum

SRAuthorizationStatus
=====================

사용자가 app이 특정 sensor를 읽는 것을 승인했는지 나타내는 상태입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum SRAuthorizationStatus

[주제](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#topics)

-------------------------------------------------------------------------------------------

### [Enumeration case](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#Enumeration-Cases)

[`case authorized`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/authorized)

사용자가 이 application에 authorization을 부여했습니다.

[`case denied`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/denied)

사용자가 이 application에 authorization을 거부했거나 Settings에서 data collection이 비활성화되어 있습니다.

[`case notDetermined`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/notdetermined)

사용자가 아직 이 application에 대해 선택하지 않았습니다.

### [Initializer](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#relationships)

---------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#see-also)

-----------------------------------------------------------------------------------------------

### [사용자 authorization 확인](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus#Checking-user-authorization)

[`var authorizationStatus: SRAuthorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)

사용자가 app이 이 reader의 sensor에 access하도록 동의했는지에 대한 status입니다.

[`class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))

하나 이상의 sensor를 읽기 위한 사용자 permission을 요청합니다.

현재 페이지는 SRAuthorizationStatus입니다.
