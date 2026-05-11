---
title: "SRError.Code | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror/code"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.058918+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror/code#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
    
*   SRError.Code

enum

SRError.Code
============

recording이나 fetch를 중단시키는 문제의 종류입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum Code

[주제](https://developer.apple.com/documentation/sensorkit/srerror/code#topics)

----------------------------------------------------------------------------------

### [Errors](https://developer.apple.com/documentation/sensorkit/srerror/code#Errors)

[`case promptDeclined`](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined)

user가 sensor 승인 workflow를 취소할 때 발생합니다.

[`case dataInaccessible`](https://developer.apple.com/documentation/sensorkit/srerror/code/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`case fetchRequestInvalid`](https://developer.apple.com/documentation/sensorkit/srerror/code/fetchrequestinvalid)

app이 fetch request를 잘못 구성했을 때 발생합니다.

[`case invalidEntitlement`](https://developer.apple.com/documentation/sensorkit/srerror/code/invalidentitlement)

app에 필요한 entitlement가 없을 때 발생합니다.

[`case noAuthorization`](https://developer.apple.com/documentation/sensorkit/srerror/code/noauthorization)

user가 Settings app에서 sensor 접근을 거부할 때 발생합니다.

### [error 생성하기](https://developer.apple.com/documentation/sensorkit/srerror/code#Creating-an-error)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srerror/code/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srerror/code#relationships)

------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srerror/code#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srerror/code#see-also)

--------------------------------------------------------------------------------------

### [Error 해석하기](https://developer.apple.com/documentation/sensorkit/srerror/code#Interpreting-Errors)

[`let SRErrorDomain: String`](https://developer.apple.com/documentation/sensorkit/srerrordomain)

framework 전용 error domain입니다.

[`struct SRError`](https://developer.apple.com/documentation/sensorkit/srerror)

SensorKit이 보고하는 error입니다.

현재 페이지: SRError.Code
