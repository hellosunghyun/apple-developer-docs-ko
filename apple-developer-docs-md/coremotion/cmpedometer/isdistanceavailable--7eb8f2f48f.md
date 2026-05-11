---
title: "isDistanceAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.908233+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   isDistanceAvailable()

type method

isDistanceAvailable()
=====================

현재 device에서 distance estimation을 사용할 수 있는지 나타내는 Boolean 값입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    class func isDistanceAvailable() -> Bool

[반환 값](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable()#return-value)

--------------------------------------------------------------------------------------------------------------------

[`true`](https://developer.apple.com/documentation/Swift/true)
 distance estimation을 사용할 수 있으면 [`false`](https://developer.apple.com/documentation/Swift/false)
 사용할 수 없으면 

[설명](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable()#Discussion)

----------------------------------------------------------------------------------------------------------------

distance estimation은 step 정보를 사용해 사용자가 이동한 대략적인 거리를 제공할 수 있음을 의미합니다. 이 기능은 모든 device에서 지원되지는 않습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable()#see-also)

------------------------------------------------------------------------------------------------------------

### [pedometer 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable()#Determining-Pedometer-Availability)

[`class func isStepCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable())

현재 device에서 step counting을 사용할 수 있는지 나타내는 Boolean 값입니다.

[`class func isFloorCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isfloorcountingavailable())

현재 device에서 floor counting을 사용할 수 있는지 나타내는 Boolean 값입니다.

[`class func isPaceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable())

현재 device에서 pace 정보를 사용할 수 있는지 나타내는 Boolean 값입니다.

[`class func isCadenceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable())

현재 device에서 cadence 정보를 사용할 수 있는지 나타내는 Boolean 값입니다.

[`class func isPedometerEventTrackingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable())

현재 device에서 pedometer event를 사용할 수 있는지 나타내는 Boolean 값입니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())

app이 pedometer data를 수집하도록 승인되었는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지: isDistanceAvailable()
