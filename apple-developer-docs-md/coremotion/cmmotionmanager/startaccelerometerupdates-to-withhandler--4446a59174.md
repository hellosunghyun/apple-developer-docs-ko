---
title: "startAccelerometerUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899416+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startAccelerometerUpdates(to:withHandler:)

instance method

startAccelerometerUpdates(to:withHandler:)
==========================================

operation queue에서 지정한 handler와 함께 accelerometer update를 시작합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startAccelerometerUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMAccelerometerHandler
    )

[parameter](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------

`queue`

caller가 제공하는 operation queue입니다. 처리된 event가 높은 빈도로 도착할 수 있으므로 main operation queue 사용은 권장하지 않습니다.

`handler`

새 accelerometer data를 처리하도록 각 update마다 호출되는 block입니다. 이 block은 [`CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)
 type을 준수해야 합니다.

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)#mentions)

-----------------------------------------------------------------------------------------------------------------------------------------

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------

app이 더 이상 accelerometer update를 처리하지 않으려면 반드시 [`stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())
 를 호출해야 합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------

### [Accelerometer Update 관리하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:)#Managing-Accelerometer-Updates)

[`var accelerometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)

block handler에 accelerometer update를 제공하는 간격(초)입니다.

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())

handler 없이 accelerometer update를 시작합니다.

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())

accelerometer update를 중지합니다.

[`var accelerometerData: CMAccelerometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)

가장 최근의 accelerometer data sample입니다.

[`typealias CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

accelerometer data를 처리하는 block callback의 type입니다.

현재 페이지: startAccelerometerUpdates(to:withHandler:)
