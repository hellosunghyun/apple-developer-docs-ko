---
title: "startEventUpdates(handler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909188+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   startEventUpdates(handler:)

instance method

startEventUpdates(handler:)
===========================

app으로 pedometer event 전달을 시작합니다.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.1+watchOS 3.0+

    func startEventUpdates(handler: @escaping CMPedometerEventHandler)

[parameter](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:)#parameters)

----------------------------------------------------------------------------------------------------------------------

`handler`

The block to execute when a pedometer event is available. This parameter must not be `nil`.

[설명](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:)#Discussion)

----------------------------------------------------------------------------------------------------------------------

Pedometer events report changes in the user’s pedestrian activity.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:)#see-also)

------------------------------------------------------------------------------------------------------------------

### [Gathering Live Pedometer Data](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:)#Gathering-Live-Pedometer-Data)

[`func startUpdates(from: Date, withHandler: CMPedometerHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))

최근 보행 관련 data를 app에 전달하기 시작합니다.

[`func stopUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())

최근 보행 data update를 app에 전달하는 작업을 중지합니다.

[`func stopEventUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopeventupdates())

app으로 pedometer event 전달을 중지합니다.

[`typealias CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

pedometer 관련 data를 처리하는 block입니다.

[`typealias CMPedometerEventHandler`](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)

pedometer event를 처리하는 block입니다.

현재 페이지: startEventUpdates(handler:)
