---
title: "queryPedometerData(from:to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.910191+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)
    
*   queryPedometerData(from:to:withHandler:)

instance method

queryPedometerData(from:to:withHandler:)
========================================

지정한 시작 날짜와 종료 날짜 사이의 data를 가져옵니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    func queryPedometerData(
        from start: Date,
        to end: Date,
        withHandler handler: @escaping CMPedometerHandler
    )

[Parameters](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------

`start`

원하는 data의 시작 날짜입니다. 이 parameter는 `nil`이면 안 됩니다.

`end`

원하는 data의 종료 날짜입니다. 이 parameter는 `nil`이면 안 됩니다.

`handler`

The block to execute with the resulting data. This block is called once on the same serial dispatch queue used to process continuous updates. This parameter must not be `nil`. For information about this block, see [`CMPedometerHandler`](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)
.

[논의](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------

지정한 날짜 사이의 과거 pedometer data를 가져오려면 이 method를 사용합니다. 이 method는 비동기로 실행되며, 제공한 block으로 data를 전달합니다. 저장되어 가져올 수 있는 data는 최근 7일치뿐입니다. 시작 날짜를 7일보다 더 이전으로 지정하면 사용 가능한 data만 반환합니다.

It is safe to call this method at the same time that you are generating continuous updates using the [`startUpdates(from:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))
 method.

현재 페이지: queryPedometerData(from:to:withHandler:)
