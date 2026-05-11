---
title: "CMPedometer | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.887261+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMPedometer

class

CMPedometer
===========

system이 생성한 실시간 보행 data를 가져오는 object입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    class CMPedometer

[개요](https://developer.apple.com/documentation/coremotion/cmpedometer#overview)

--------------------------------------------------------------------------------------

pedometer object를 사용해 step count와 이동 거리, 올라가거나 내려간 층수 같은 정보를 가져옵니다. pedometer object는 query할 수 있는 과거 data cache를 관리하며, data가 처리될 때 실시간 update를 요청할 수도 있습니다.

pedometer object를 사용하려면 이 class의 instance를 만들고 적절한 method를 호출합니다. 이미 수집된 data를 가져오려면 [`queryPedometerData(from:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:))
 method를 사용합니다. 실시간 update를 받으려면 [`startUpdates(from:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))
 method를 사용해 제공한 handler로 event 전달을 시작합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmpedometer#topics)

----------------------------------------------------------------------------------

### [Pedometer 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmpedometer#Determining-Pedometer-Availability)

[`class func isStepCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isstepcountingavailable())

현재 device에서 step counting을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isDistanceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isdistanceavailable())

현재 device에서 거리 추정을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isFloorCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/isfloorcountingavailable())

현재 device에서 층수 계산을 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPaceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispaceavailable())

현재 device에서 pace 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isCadenceAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/iscadenceavailable())

현재 device에서 cadence 정보를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func isPedometerEventTrackingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmpedometer/ispedometereventtrackingavailable())

현재 device에서 pedometer event를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmpedometer/authorizationstatus())

app이 pedometer data를 수집할 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

### [실시간 Pedometer Data 수집](https://developer.apple.com/documentation/coremotion/cmpedometer#Gathering-Live-Pedometer-Data)

[`func startUpdates(from: Date, withHandler: CMPedometerHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))

최근 보행 관련 data를 app에 전달하기 시작합니다.

[`func stopUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())

최근 보행 data update의 app 전달을 중지합니다.

[`func startEventUpdates(handler: CMPedometerEventHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:))

app에 pedometer event를 전달하기 시작합니다.

[`func stopEventUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopeventupdates())

app에 대한 pedometer event 전달을 중지합니다.

[`typealias CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

pedometer 관련 data를 처리하는 block입니다.

[`typealias CMPedometerEventHandler`](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)

pedometer event를 처리하는 block입니다.

### [과거 Pedometer Data 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometer#Fetching-Historical-Pedometer-Data)

[`func queryPedometerData(from: Date, to: Date, withHandler: CMPedometerHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:))

지정한 시작 날짜와 종료 날짜 사이의 data를 가져옵니다.

[관계](https://developer.apple.com/documentation/coremotion/cmpedometer#relationships)

------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmpedometer#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmpedometer#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometer#see-also)

--------------------------------------------------------------------------------------

### [Pedometer와 피트니스](https://developer.apple.com/documentation/coremotion/cmpedometer#Pedometer-and-fitness)

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

사용자가 걸어서 이동한 거리에 대한 정보입니다.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

사용자의 보행 activity 변화입니다.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

사용자가 device와 함께 걸은 step 수입니다.

Deprecated

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

운동용 odometer data를 나타내는 class입니다.

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

1Hz로 수집한 heart rate data를 나타내는 class입니다.

현재 페이지는 CMPedometer입니다
