---
title: "isAbsoluteAltitudeAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.873673+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter)
    
*   isAbsoluteAltitudeAvailable()

type method

isAbsoluteAltitudeAvailable()
=============================

현재 device가 absolute altitude 변화 보고를 지원하는지 나타내는 Boolean 값을 반환합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+watchOS 8.0+

    class func isAbsoluteAltitudeAvailable() -> Bool

[논의](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable()#Discussion)

------------------------------------------------------------------------------------------------------------------------

[`startAbsoluteAltitudeUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmaltimeter/startabsolutealtitudeupdates(to:withhandler:))
 method를 호출하기 전에 altitude update를 사용할 수 있는지 확인하려면 이 method를 사용합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable()#see-also)

--------------------------------------------------------------------------------------------------------------------

### [Determining Altitude Availability](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable()#Determining-Altitude-Availability)

[`class func isRelativeAltitudeAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable())

현재 device가 relative altitude 변화 data를 생성할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmaltimeter/authorizationstatus())

app이 altimeter data를 가져오도록 승인되었는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지는 isAbsoluteAltitudeAvailable()입니다
