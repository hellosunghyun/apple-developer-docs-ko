---
title: "isCadenceAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.908594+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   isCadenceAvailable()

type method

isCadenceAvailable()
====================

현재 device에서 cadence 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+watchOS 2.0+

    class func isCadenceAvailable() -> Bool

[반환 값](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable()#return-value)

-------------------------------------------------------------------------------------------------------------------

[`true`](https://developer.apple.com/documentation/Swift/true)
는 cadence 정보를 사용할 수 있을 때이고, [`false`](https://developer.apple.com/documentation/Swift/false)
는 사용할 수 없을 때입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable()#Discussion)

---------------------------------------------------------------------------------------------------------------

cadence 측정은 사용자가 초당 몇 걸음을 걷는지 판단하는 기능을 뜻합니다. 이 기능은 모든 device에서 지원되지는 않습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable()#see-also)

-----------------------------------------------------------------------------------------------------------

### [Pedometer 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable()#Determining-Pedometer-Availability)

[`class func isStepCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable())

현재 device에서 step counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isDistanceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable())

현재 device에서 거리 추정을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isFloorCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isfloorcountingavailable())

현재 device에서 층수 계산을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPaceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable())

현재 device에서 pace 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPedometerEventTrackingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable())

현재 device에서 pedometer event를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())

app이 pedometer data를 수집할 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

현재 페이지는 isCadenceAvailable()입니다
