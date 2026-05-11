---
title: "startAccelerometerUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900838+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startAccelerometerUpdates()

instance method

startAccelerometerUpdates()
===========================

handler 없이 accelerometer update를 시작합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startAccelerometerUpdates()

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates()#mentions)

--------------------------------------------------------------------------------------------------------------------------

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates()#Discussion)

--------------------------------------------------------------------------------------------------------------------------

[`accelerometerData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)
 property를 통해 최신 accelerometer data를 가져올 수 있습니다. app이 accelerometer update를 더 이상 처리하지 않아야 하면 [`stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())
를 호출해야 합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates()#see-also)

----------------------------------------------------------------------------------------------------------------------

### [accelerometer update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates()#Managing-Accelerometer-Updates)

[`var accelerometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)

block handler에 accelerometer update를 전달하는 간격(초)입니다.

[`func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))

operation queue에서 지정한 handler와 함께 accelerometer update를 시작합니다.

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())

accelerometer update를 중지합니다.

[`var accelerometerData: CMAccelerometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)

최신 accelerometer data sample입니다.

[`typealias CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

accelerometer data를 처리하는 block callback type입니다.

현재 페이지는 startAccelerometerUpdates()입니다
