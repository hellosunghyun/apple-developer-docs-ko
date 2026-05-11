---
title: "authorizationStatus | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.913921+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionManager](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)
    
*   authorizationStatus

instance property

authorizationStatus
===================

fall detection event 알림을 받기 위한 authorization status입니다.

watchOS 7.2+

    var authorizationStatus: CMAuthorizationStatus { get }

[같이 보기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Authorization 요청하기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus#Requesting-Authorization)

[`func requestAuthorization(handler: (CMAuthorizationStatus) -> Void)`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:))

fall detection event 알림을 받을 authorization을 요청합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지: authorizationStatus
