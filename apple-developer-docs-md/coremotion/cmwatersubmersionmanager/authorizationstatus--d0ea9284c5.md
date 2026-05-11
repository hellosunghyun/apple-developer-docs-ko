---
title: "authorizationStatus | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.877245+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionManager](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
    
*   authorizationStatus

type property

authorizationStatus
===================

app이 submersion data를 받을 사용자 authorization을 가지고 있는지 나타내는 값입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    class var authorizationStatus: CMAuthorizationStatus { get }

[설명](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus#설명)

---------------------------------------------------------------------------------------------------------------------------

app이 처음 `CMWaterSubmersionManager`를 instance화하면 system이 motion data 접근 authorization을 자동으로 요청합니다. 현재 authorization status는 이 property로 확인할 수 있습니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [사용 가능 여부와 authorization 확인](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus#Checking-availability-and-authorization)

[`class var waterSubmersionAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/watersubmersionavailable)

현재 device가 submersion manager를 지원하는지 나타내는 Boolean 값입니다.

현재 페이지는 authorizationStatus입니다
