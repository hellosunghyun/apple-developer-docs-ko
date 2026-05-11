---
title: "fetchRequestInvalid | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.059284+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
    
*   fetchRequestInvalid

type property

fetchRequestInvalid
===================

app이 fetch request를 잘못 구성했을 때 발생합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static var fetchRequestInvalid: SRError.Code { get }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid#see-also)

-----------------------------------------------------------------------------------------------------

### [Error 원인 식별하기](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid#Identifying-an-Error-Cause)

[`static var promptDeclined: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined)

사용자가 sensor 승인 workflow를 취소했을 때 발생합니다.

[`static var dataInaccessible: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`static var invalidEntitlement: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement)

app에 필요한 entitlement가 없을 때 발생합니다.

[`static var noAuthorization: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization)

사용자가 Settings app에서 sensor access를 거부했을 때 발생합니다.

현재 페이지: fetchRequestInvalid
