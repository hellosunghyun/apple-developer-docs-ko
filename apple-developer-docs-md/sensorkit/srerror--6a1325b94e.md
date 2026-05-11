---
title: "SRError | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.059698+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRError

struct

SRError
=======

SensorKit이 보고하는 error입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    struct SRError

[주제](https://developer.apple.com/documentation/sensorkit/srerror#topics)

-----------------------------------------------------------------------------

### [Error 정보 확인하기](https://developer.apple.com/documentation/sensorkit/srerror#Inspecting-Error-Information)

[`static var errorDomain: String`](https://developer.apple.com/documentation/sensorkit/srerror/errordomain)

### [Error 원인 식별하기](https://developer.apple.com/documentation/sensorkit/srerror#Identifying-an-Error-Cause)

[`static var promptDeclined: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/promptdeclined)

사용자가 sensor 승인 workflow를 취소할 때 발생합니다.

[`static var dataInaccessible: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`static var fetchRequestInvalid: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/fetchrequestinvalid)

app이 fetch request를 잘못 구성했을 때 발생합니다.

[`static var invalidEntitlement: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/invalidentitlement)

app에 필요한 entitlement가 없을 때 발생합니다.

[`static var noAuthorization: SRError.Code`](https://developer.apple.com/documentation/sensorkit/srerror/noauthorization)

사용자가 Settings app에서 sensor access를 거부할 때 발생합니다.

[관계](https://developer.apple.com/documentation/sensorkit/srerror#relationships)

-------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srerror#conforms-to)

*   [`CustomNSError`](https://developer.apple.com/documentation/Foundation/CustomNSError)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Error`](https://developer.apple.com/documentation/Swift/Error)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srerror#see-also)

---------------------------------------------------------------------------------

### [Error 해석하기](https://developer.apple.com/documentation/sensorkit/srerror#Interpreting-Errors)

[`let SRErrorDomain: String`](https://developer.apple.com/documentation/sensorkit/srerrordomain)

framework에 고유한 error domain입니다.

[`enum Code`](https://developer.apple.com/documentation/sensorkit/srerror/code)

recording이나 fetch를 중지시키는 문제 유형입니다.

현재 페이지: SRError
