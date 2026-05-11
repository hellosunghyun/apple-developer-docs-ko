---
title: "startUpdates(from:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.908937+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   startUpdates(from:withHandler:)

instance method

startUpdates(from:withHandler:)
===============================

최근 pedestrian 관련 data를 app에 전달하기 시작합니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    func startUpdates(
        from start: Date,
        withHandler handler: @escaping CMPedometerHandler
    )

[파라미터](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)#parameters)

--------------------------------------------------------------------------------------------------------------------------

`start`

data 보고를 시작할 날짜입니다. 과거의 날짜를 지정해 해당 시점부터 현재까지의 data를 가져올 수 있습니다. 이 파라미터는 `nil`이면 안 됩니다.

`handler`

data를 사용할 수 있을 때 실행할 block입니다. 새 data가 도착하면 이 block이 background thread에서 반복적으로 호출됩니다. 이 파라미터는 `nil`이면 안 됩니다. 이 block에 대한 정보는 [`CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)
를 참고합니다.

[설명](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)#Discussion)

--------------------------------------------------------------------------------------------------------------------------

이 method를 호출하면 pedometer object가 data와 함께 handler block을 정기적으로 호출하기 시작합니다. `handler` block에 전달되는 data는 지정한 `start` 날짜부터 현재 시각까지 누적된 data를 나타냅니다. (시작 및 종료 날짜는 handler에 전달되는 [`CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
 object에서 가져올 수 있습니다.) 이 method는 event 전달 과정을 비동기로 시작하고 serial dispatch queue에서 block을 실행하므로, 특정 시점에는 block의 한 복사본만 실행됩니다.

app이 suspend되면 update 전달이 일시적으로 중단됩니다. foreground 또는 background 실행으로 돌아오면 pedometer object가 다시 update를 시작합니다.

event 전달을 중지하려면 [`stopUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())
 method를 호출합니다.

이 method로 event 전달을 시작한 뒤 [`queryPedometerData(from:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:))
 method로 추가 query를 수행해도 안전합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)#see-also)

----------------------------------------------------------------------------------------------------------------------

### [실시간 Pedometer Data 수집](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:)#Gathering-Live-Pedometer-Data)

[`func stopUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())

최근 pedestrian data update의 app 전달을 중지합니다.

[`func startEventUpdates(handler: CMPedometerEventHandler)`](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:))

pedometer event의 app 전달을 시작합니다.

[`func stopEventUpdates()`](https://developer.apple.com/documentation/coremotion/cmpedometer/stopeventupdates())

pedometer event의 app 전달을 중지합니다.

[`typealias CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

pedometer 관련 data를 처리하는 block입니다.

[`typealias CMPedometerEventHandler`](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)

pedometer event를 처리하는 block입니다.

현재 페이지는 startUpdates(from:withHandler:)입니다
