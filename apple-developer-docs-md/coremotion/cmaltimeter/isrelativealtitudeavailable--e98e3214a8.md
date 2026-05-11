---
title: "isRelativeAltitudeAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.881443+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter)
    
*   isRelativeAltitudeAvailable()

type method

isRelativeAltitudeAvailable()
=============================

현재 device가 relative altitude 변화 data를 생성하는 기능을 지원하는지 나타내는 Boolean 값을 반환합니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+watchOS 2.0+

    class func isRelativeAltitudeAvailable() -> Bool

[Return Value](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable()#return-value)

----------------------------------------------------------------------------------------------------------------------------

device가 relative altitude 변화를 지원하면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 지원하지 않으면 [`false`](https://developer.apple.com/documentation/Swift/false)
입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable()#Discussion)

------------------------------------------------------------------------------------------------------------------------

[`startRelativeAltitudeUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmaltimeter/startrelativealtitudeupdates(to:withhandler:))
 method를 호출하기 전에 altitude update를 사용할 수 있는지 확인할 때 이 method를 사용합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable()#see-also)

--------------------------------------------------------------------------------------------------------------------

### [Determining Altitude Availability](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable()#Determining-Altitude-Availability)

[`class func isAbsoluteAltitudeAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable())

현재 device가 absolute altitude 변화를 보고하는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmaltimeter/authorizationstatus())

app이 altimeter data를 가져올 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization 상태입니다.

현재 페이지: isRelativeAltitudeAvailable()
