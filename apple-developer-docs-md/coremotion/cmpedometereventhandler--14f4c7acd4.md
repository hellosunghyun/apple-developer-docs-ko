---
title: "CMPedometerEventHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometereventhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.910315+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMPedometerEventHandler

type alias

CMPedometerEventHandler
=======================

pedometer event를 처리하는 block입니다.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.1+macOS 10.15+watchOS 3.0+

    typealias CMPedometerEventHandler = (CMPedometerEvent?, (any Error)?) -> Void

[논의](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler#Discussion)

------------------------------------------------------------------------------------------------------

[`CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)
object에서 pedometer event를 요청할 때 이 type의 block을 제공합니다. 새 event를 사용할 수 있게 되면 pedometer object가 이 data를 block에 전달해 처리하게 합니다. data를 가져오는 중 error가 발생하면 pedometer object는 대신 error object를 제공합니다.

이 block은 return value가 없고 다음 parameter를 받습니다.

`pedometerEvent`

event 정보를 담은 [`CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)
object입니다. data를 가져오는 중 error가 발생하면 이 parameter는 nil입니다.

`error`

문제가 있으면 [`NSError`](https://developer.apple.com/documentation/Foundation/NSError)
object가 들어가고, pedometer event를 성공적으로 가져왔으면 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler#see-also)

--------------------------------------------------------------------------------------------------

### [live pedometer data 수집하기](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler#Gathering-Live-Pedometer-Data)

[`func startUpdates(from: Date, withHandler: CMPedometerHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))

최근 보행 관련 data update 전달을 app에 시작합니다.

[`func stopUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())

최근 보행 data update 전달을 app에 중지합니다.

[`func startEventUpdates(handler: CMPedometerEventHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:))

pedometer event 전달을 app에 시작합니다.

[`func stopEventUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopeventupdates())

pedometer event 전달을 app에 중지합니다.

[`typealias CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

pedometer 관련 data를 처리하는 block입니다.

현재 페이지: CMPedometerEventHandler
