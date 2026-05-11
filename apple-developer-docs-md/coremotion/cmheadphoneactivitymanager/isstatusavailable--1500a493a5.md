---
title: "isStatusAvailable | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.892031+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   isStatusAvailable

instance property

isStatusAvailable
=================

현재 device가 headphone status를 지원하는지 나타내는 Boolean 값입니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    var isStatusAvailable: Bool { get }

[관련 항목](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [사용 가능 여부 확인하기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable#Checking-Availability)

[`var isActivityAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable)

현재 device가 headphone activity를 지원하는지 나타내는 Boolean 값입니다.

[`var isActivityActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityactive)

headphone motion activity가 활성 상태인지 나타내는 Boolean 값입니다.

[`var isStatusActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusactive)

headphone status가 활성 상태인지 나타내는 Boolean 값입니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus())

headphone activity monitoring의 authorization status를 반환합니다.

현재 페이지: isStatusAvailable
