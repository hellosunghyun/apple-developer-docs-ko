---
title: "isActivityAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.906623+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
    
*   isActivityAvailable()

type method

isActivityAvailable()
=====================

현재 device에서 motion data를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    class func isActivityAvailable() -> Bool

[반환 값](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable()#return-value)

--------------------------------------------------------------------------------------------------------------------------------

motion data를 사용할 수 있으면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 그렇지 않으면 [`false`](https://developer.apple.com/documentation/Swift/false)
 입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable()#Discussion)

----------------------------------------------------------------------------------------------------------------------------

motion data는 모든 iOS device에서 사용할 수 있는 것은 아닙니다. 현재 device에서 지원하는지 확인하려면 이 method를 사용합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable()#see-also)

------------------------------------------------------------------------------------------------------------------------

### [Activity 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable()#Determining-Activity-Availability)

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus())

app이 저장된 motion data를 가져올 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization 상태입니다.

현재 페이지: isActivityAvailable()
