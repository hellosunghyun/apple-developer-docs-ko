---
title: "isAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.894433+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   isAvailable()

type method

isAvailable()
=============

현재 device가 movement disorder manager를 지원하는지 나타내는 Boolean value입니다.

watchOS 5.0+

    class func isAvailable() -> Bool

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable()#see-also)

------------------------------------------------------------------------------------------------------------------

### [Checking Availablility](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable()#Checking-Availablility)

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus())

user가 app에 movement disorder data를 모니터링하고 query할 권한을 부여했는지 나타내는 value입니다.

[`class func version() -> String?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version())

movement disorder algorithm의 현재 version을 설명하는 string을 반환합니다.

현재 페이지: isAvailable()
