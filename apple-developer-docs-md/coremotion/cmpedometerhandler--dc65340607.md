---
title: "CMPedometerHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.910058+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMPedometerHandler

type alias

CMPedometerHandler
==================

pedometer 관련 data를 처리하는 block입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+watchOS 2.0+

    typealias CMPedometerHandler = (CMPedometerData?, (any Error)?) -> Void

[설명](https://developer.apple.com/documentation/coremotion/cmpedometerhandler#Discussion)

-------------------------------------------------------------------------------------------------

`CMPedometer` object에서 data를 요청할 때 이 type의 block을 제공합니다. data를 사용할 수 있게 되면 pedometer object가 이 data를 block에 전달해 처리합니다. data를 가져오는 중 error가 발생하면 pedometer object가 대신 error object를 제공합니다.

이 block은 return value가 없으며 다음 parameter를 받습니다.

`pedometerData`

사용 가능한 data를 담은 [`CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
 object입니다. data를 가져오는 중 error가 발생한 경우 이 parameter는 `nil`입니다.

`error`

문제가 있으면 [`NSError`](https://developer.apple.com/documentation/Foundation/NSError)
 object이고, pedometer data를 성공적으로 가져왔으면 `nil`입니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmpedometerhandler#see-also)

---------------------------------------------------------------------------------------------

### [실시간 Pedometer Data 수집](https://developer.apple.com/documentation/coremotion/cmpedometerhandler#Gathering-Live-Pedometer-Data)

[`func startUpdates(from: Date, withHandler: CMPedometerHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))

최근 보행 관련 data 전달을 app으로 시작합니다.

[`func stopUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())

최근 보행 data update 전달을 app으로 중지합니다.

[`func startEventUpdates(handler: CMPedometerEventHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:))

pedometer event 전달을 app으로 시작합니다.

[`func stopEventUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopeventupdates())

pedometer event 전달을 app으로 중지합니다.

[`typealias CMPedometerEventHandler`](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)

pedometer event를 처리하는 block입니다.

현재 페이지: CMPedometerHandler
