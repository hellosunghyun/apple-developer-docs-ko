---
title: "invalidEntitlement | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.059164+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
    
*   invalidEntitlement

type property

invalidEntitlement
==================

app에 필요한 entitlement가 없을 때 발생합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static var invalidEntitlement: SRError.Code { get }

[설명](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement#Discussion)

--------------------------------------------------------------------------------------------------------

app이 sensor data를 읽을 수 있으려면 system은 app의 code signature에 특수 entitlement가 포함되어 있기를 요구합니다. 자세한 내용은 [sensor reading을 위해 project 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)
을 참조하십시오.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement#see-also)

----------------------------------------------------------------------------------------------------

### [error 원인 식별하기](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement#Identifying-an-Error-Cause)

[`static var promptDeclined: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined)

사용자가 sensor 승인 workflow를 취소할 때 발생합니다.

[`static var dataInaccessible: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`static var fetchRequestInvalid: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid)

app이 fetch request를 잘못 구성했을 때 발생합니다.

[`static var noAuthorization: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization)

사용자가 Settings app에서 sensor access를 거부할 때 발생합니다.

현재 페이지는 invalidEntitlement입니다
