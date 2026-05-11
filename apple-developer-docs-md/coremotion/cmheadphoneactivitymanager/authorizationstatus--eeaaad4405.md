---
title: "authorizationStatus() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.889231+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   authorizationStatus()

type method

authorizationStatus()
=====================

headphone activity monitoring에 대한 authorization status를 반환합니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    class func authorizationStatus() -> CMAuthorizationStatus

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus()#see-also)

---------------------------------------------------------------------------------------------------------------------------

### [Checking Availability](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus()#Checking-Availability)

[`var isActivityAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable)

현재 device가 headphone activity를 지원하는지 나타내는 Boolean value입니다.

[`var isActivityActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityactive)

headphone motion activity가 활성 상태인지 나타내는 Boolean value입니다.

[`var isStatusAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable)

현재 device가 headphone status를 지원하는지 나타내는 Boolean value입니다.

[`var isStatusActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusactive)

headphone status가 활성 상태인지 나타내는 Boolean value입니다.

현재 페이지: authorizationStatus()
