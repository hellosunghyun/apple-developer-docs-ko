---
title: "isActivityAvailable | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.892223+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   isActivityAvailable

instance property

isActivityAvailable
===================

현재 device가 headphone activity를 지원하는지 나타내는 Boolean 값입니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    var isActivityAvailable: Bool { get }

[논의](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable#discussion)

-----------------------------------------------------------------------------------------------------------------------------

device가 headphone activity를 지원하면 status update를 시작한 다음, 지원되는 headphone이 연결되었음을 나타내는 update를 기다립니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable#see-also)

-------------------------------------------------------------------------------------------------------------------------

### [Availability 확인하기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable#Checking-Availability)

[`var isActivityActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityactive)

headphone motion activity가 활성 상태인지 나타내는 Boolean 값입니다.

[`var isStatusAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable)

현재 device가 headphone status를 지원하는지 나타내는 Boolean 값입니다.

[`var isStatusActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusactive)

headphone status가 활성 상태인지 나타내는 Boolean 값입니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus())

headphone activity monitoring의 authorization status를 반환합니다.

현재 페이지: isActivityAvailable
