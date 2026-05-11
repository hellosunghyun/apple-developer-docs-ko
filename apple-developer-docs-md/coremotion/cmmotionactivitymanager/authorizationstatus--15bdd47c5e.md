---
title: "authorizationStatus() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.904027+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
    
*   authorizationStatus()

type method

authorizationStatus()
=====================

app이 저장된 motion data를 가져올 권한이 있는지 나타내는 값을 반환합니다.

iOS 11.0+iPadOS 11.0+Mac Catalyst 13.1+watchOS 4.0+

    class func authorizationStatus() -> CMAuthorizationStatus

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus()#see-also)

------------------------------------------------------------------------------------------------------------------------

### [Determining Activity Availability](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus()#Determining-Activity-Availability)

[`class func isActivityAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable())

현재 device에서 motion data를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization 상태입니다.

현재 페이지: authorizationStatus()
