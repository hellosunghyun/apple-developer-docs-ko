---
title: "isStepCountingAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.907167+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   isStepCountingAvailable()

type method

isStepCountingAvailable()
=========================

현재 device에서 step counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    class func isStepCountingAvailable() -> Bool

[Return Value](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable()#return-value)

------------------------------------------------------------------------------------------------------------------------

step counting을 사용할 수 있으면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 그렇지 않으면 [`false`](https://developer.apple.com/documentation/Swift/false)
입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable()#see-also)

----------------------------------------------------------------------------------------------------------------

### [Determining Pedometer Availability](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable()#Determining-Pedometer-Availability)

[`class func isDistanceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable())

현재 device에서 거리 추정을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isFloorCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isfloorcountingavailable())

현재 device에서 층수 counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPaceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable())

현재 device에서 pace 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isCadenceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable())

현재 device에서 cadence 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPedometerEventTrackingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable())

현재 device에서 pedometer event를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())

app이 pedometer data를 수집하도록 승인되었는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지는 isStepCountingAvailable()입니다
