---
title: "CMAltimeter | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaltimeter"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.871017+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaltimeter#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAltimeter

class

CMAltimeter
===========

altitude 관련 변화를 전달하기 시작하는 object입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+watchOS 2.0+

    class CMAltimeter

[개요](https://developer.apple.com/documentation/coremotion/cmaltimeter#overview)

--------------------------------------------------------------------------------------

altitude event는 relative altitude와 absolute altitude의 변화를 모두 보고합니다. 예를 들어 hiking app은 이 object를 사용해 등산 중 사용자의 고도 변화량을 추적하거나, 등산 중 현재 absolute altitude를 보고할 수 있습니다.

altitude event는 모든 device에서 사용할 수 있는 것이 아니므로, relative altitude update를 시작하기 전에 항상 [`isRelativeAltitudeAvailable()`](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable())
 method를 호출하고, absolute altitude update를 시작하기 전에는 [`isAbsoluteAltitudeAvailable()`](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable())
를 호출해야 합니다.

altitude data 사용 가능 여부를 확인한 뒤에는 [`startRelativeAltitudeUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmaltimeter/startrelativealtitudeupdates(to:withhandler:))
 method를 호출해 relative altitude data 수신을 시작하거나, absolute altitude data를 위해 [`startAbsoluteAltitudeUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmaltimeter/startabsolutealtitudeupdates(to:withhandler:))
 method를 호출합니다.

Core Motion은 data 변경 여부와 관계없이 일정 간격으로 event를 생성하고, 지정한 block에 이를 전달합니다. event data가 더 이상 필요 없으면 각각 [`stopRelativeAltitudeUpdates()`](https://developer.apple.com/documentation/coremotion/cmaltimeter/stoprelativealtitudeupdates())
 또는 [`stopAbsoluteAltitudeUpdates()`](https://developer.apple.com/documentation/coremotion/cmaltimeter/stopabsolutealtitudeupdates())
 method를 호출합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmaltimeter#topics)

----------------------------------------------------------------------------------

### [Altitude 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmaltimeter#Determining-Altitude-Availability)

[`class func isAbsoluteAltitudeAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmaltimeter/isabsolutealtitudeavailable())

현재 device가 absolute altitude 변화를 보고하는지 나타내는 Boolean 값을 반환합니다.

[`class func isRelativeAltitudeAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable())

현재 device가 relative altitude 변화에 대한 data 생성을 지원하는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmaltimeter/authorizationstatus())

app이 altimeter data를 가져올 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

### [Altitude update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmaltimeter#Starting-and-Stopping-Altitude-Updates)

[`func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)`](https://developer.apple.com/documentation/coremotion/cmaltimeter/startabsolutealtitudeupdates(to:withhandler:))

지정한 handler에 absolute altitude data 전달을 시작합니다.

[`func stopAbsoluteAltitudeUpdates()`](https://developer.apple.com/documentation/coremotion/cmaltimeter/stopabsolutealtitudeupdates())

이 altimeter object의 absolute altitude data 전달을 중지합니다.

[`typealias CMAbsoluteAltitudeHandler`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudehandler)

absolute altitude data를 받는 block입니다.

[`func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)`](https://developer.apple.com/documentation/coremotion/cmaltimeter/startrelativealtitudeupdates(to:withhandler:))

지정한 handler에 relative altitude data 전달을 시작합니다.

[`func stopRelativeAltitudeUpdates()`](https://developer.apple.com/documentation/coremotion/cmaltimeter/stoprelativealtitudeupdates())

이 altimeter object의 relative altitude data 전달을 중지합니다.

[`typealias CMAltitudeHandler`](https://developer.apple.com/documentation/coremotion/cmaltitudehandler)

relative altitude data를 받는 block입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmaltimeter#relationships)

------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmaltimeter#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmaltimeter#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmaltimeter#see-also)

--------------------------------------------------------------------------------------

### [Altitude data](https://developer.apple.com/documentation/coremotion/cmaltimeter#Altitude-data)

[`class CMAbsoluteAltitudeData`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata)

absolute altitude의 변화를 기록하는 data입니다.

[`class CMAltitudeData`](https://developer.apple.com/documentation/coremotion/cmaltitudedata)

기록된 altitude 변화에 대한 data입니다.

현재 페이지는 CMAltimeter입니다
