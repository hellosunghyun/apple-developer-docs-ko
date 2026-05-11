---
title: "requestAuthorization(handler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.914019+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionManager](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)
    
*   requestAuthorization(handler:)

instance method

requestAuthorization(handler:)
==============================

낙상 감지 event 알림을 받기 위한 authorization을 요청합니다.

watchOS 7.2+

    func requestAuthorization(handler: @escaping (CMAuthorizationStatus) -> Void)

[Parameters](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------

`handler`

사용자가 authorization 요청을 수락하거나 거절한 뒤 system이 호출하는 block입니다.

system은 다음 parameter를 전달합니다.

`status`

사용자가 선택한 authorization 상태입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:)#Discussion)

------------------------------------------------------------------------------------------------------------------------------------

사용자가 낙상 감지를 승인하면 곧바로 system이 delegate의 [`fallDetectionManager(_:didDetect:completionHandler:)`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:))
 method를 호출하고 최신 낙상 감지 event를 전달합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:)#see-also)

--------------------------------------------------------------------------------------------------------------------------------

### [Authorization 요청하기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:)#Requesting-Authorization)

[`var authorizationStatus: CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus)

낙상 감지 event 알림 수신에 대한 authorization 상태입니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization 상태입니다.

현재 페이지: requestAuthorization(handler:)
