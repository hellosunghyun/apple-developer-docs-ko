---
title: "noAuthorization | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror/noauthorization"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.059050+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
    
*   noAuthorization

type property

noAuthorization
===============

사용자가 Settings app에서 sensor access를 거부했을 때 발생합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static var noAuthorization: SRError.Code { get }

[관련 항목](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization#see-also)

-------------------------------------------------------------------------------------------------

### [error 원인 식별](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization#Identifying-an-Error-Cause)

[`static var promptDeclined: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined)

사용자가 sensor approval workflow를 취소했을 때 발생합니다.

[`static var dataInaccessible: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`static var fetchRequestInvalid: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid)

app이 fetch request를 잘못 구성했을 때 발생합니다.

[`static var invalidEntitlement: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement)

app에 필요한 entitlement가 없을 때 발생합니다.

현재 페이지는 noAuthorization입니다.
