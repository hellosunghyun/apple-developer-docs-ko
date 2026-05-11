---
title: "stopUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909074+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   stopUpdates()

instance method

stopUpdates()
=============

app으로 전달되는 최신 pedestrian data update를 중지합니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    func stopUpdates()

[설명](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates()#Discussion)

--------------------------------------------------------------------------------------------------------

[`startUpdates(from:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)) method 호출로 시작한 연속 update 전달을 중지할 때 이 method를 사용합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates()#see-also)

----------------------------------------------------------------------------------------------------

### [실시간 pedometer data 수집](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates()#Gathering-Live-Pedometer-Data)

[`func startUpdates(from: Date, withHandler: CMPedometerHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))

app으로 최신 pedestrian 관련 data 전달을 시작합니다.

[`func startEventUpdates(handler: CMPedometerEventHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:))

app으로 pedometer event 전달을 시작합니다.

[`func stopEventUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopeventupdates())

app으로 pedometer event 전달을 중지합니다.

[`typealias CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

pedometer 관련 data를 처리하는 block입니다.

[`typealias CMPedometerEventHandler`](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)

pedometer event를 처리하는 block입니다.

현재 페이지는 stopUpdates()입니다.
