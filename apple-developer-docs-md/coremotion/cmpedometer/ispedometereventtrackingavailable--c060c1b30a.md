---
title: "isPedometerEventTrackingAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.908700+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   isPedometerEventTrackingAvailable()

type method

isPedometerEventTrackingAvailable()
===================================

현재 device에서 pedometer event를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.1+watchOS 3.0+

    class func isPedometerEventTrackingAvailable() -> Bool

[반환 값](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable()#return-value)

----------------------------------------------------------------------------------------------------------------------------------

pedometer event를 사용할 수 있으면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 사용할 수 없으면 [`false`](https://developer.apple.com/documentation/Swift/false)
입니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable()#see-also)

--------------------------------------------------------------------------------------------------------------------------

### [Pedometer 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable()#Determining-Pedometer-Availability)

[`class func isStepCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable())

현재 device에서 step counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isDistanceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable())

현재 device에서 distance estimation을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isFloorCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isfloorcountingavailable())

현재 device에서 floor counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPaceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable())

현재 device에서 pace 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isCadenceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable())

현재 device에서 cadence 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())

app이 pedometer data를 수집하도록 승인되었는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지는 isPedometerEventTrackingAvailable()입니다
