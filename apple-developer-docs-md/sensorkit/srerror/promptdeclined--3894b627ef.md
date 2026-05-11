---
title: "promptDeclined | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.059520+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
    
*   promptDeclined

type property

promptDeclined
==============

사용자가 sensor 승인 workflow를 취소할 때 발생합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static var promptDeclined: SRError.Code { get }

[설명](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined#Discussion)

----------------------------------------------------------------------------------------------------

[`requestAuthorization(sensors:completion:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))
은 사용자가 Cancel을 눌러 prompt를 거부하면 이 error를 completion closure에 전달합니다. 사용자가 argument sensor에 대한 접근을 이미 허용했거나 거부한 뒤에 이 function을 호출하면 framework도 prompt를 취소합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined#see-also)

------------------------------------------------------------------------------------------------

### [error 원인 식별하기](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined#Identifying-an-Error-Cause)

[`static var dataInaccessible: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`static var fetchRequestInvalid: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid)

app이 fetch request를 잘못 구성했을 때 발생합니다.

[`static var invalidEntitlement: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement)

app에 필요한 entitlement가 없을 때 발생합니다.

[`static var noAuthorization: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization)

사용자가 Settings app에서 sensor access를 거부할 때 발생합니다.

현재 페이지는 promptDeclined입니다
