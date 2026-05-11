---
title: "isPaceAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.908480+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   isPaceAvailable()

type method

isPaceAvailable()
=================

현재 device에서 pace 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    class func isPaceAvailable() -> Bool

[Return Value](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable()#return-value)

----------------------------------------------------------------------------------------------------------------

pace 정보를 사용할 수 있으면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 그렇지 않으면 [`false`](https://developer.apple.com/documentation/Swift/false)
입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable()#Discussion)

------------------------------------------------------------------------------------------------------------

pace 측정은 사용자의 pace를 meter당 초 단위로 판단하는 기능을 의미합니다. 이 capability는 모든 device에서 지원되지 않습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable()#see-also)

--------------------------------------------------------------------------------------------------------

### [Determining Pedometer Availability](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable()#Determining-Pedometer-Availability)

[`class func isStepCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable())

현재 device에서 step counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isDistanceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable())

현재 device에서 거리 추정을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isFloorCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isfloorcountingavailable())

현재 device에서 층수 counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isCadenceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable())

현재 device에서 cadence 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPedometerEventTrackingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable())

현재 device에서 pedometer event를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())

app이 pedometer data를 수집하도록 승인되었는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지는 isPaceAvailable()입니다
