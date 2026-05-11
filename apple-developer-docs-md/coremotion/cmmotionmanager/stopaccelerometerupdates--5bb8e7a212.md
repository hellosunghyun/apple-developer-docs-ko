---
title: "stopAccelerometerUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.898941+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   stopAccelerometerUpdates()

instance method

stopAccelerometerUpdates()
==========================

accelerometer update를 중지합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func stopAccelerometerUpdates()

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates()#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Accelerometer Update 관리하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates()#Managing-Accelerometer-Updates)

[`var accelerometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)

block handler에 accelerometer update를 제공하는 간격(초)입니다.

[`func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))

operation queue에서 지정한 handler와 함께 accelerometer update를 시작합니다.

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())

handler 없이 accelerometer update를 시작합니다.

[`var accelerometerData: CMAccelerometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)

가장 최근의 accelerometer data sample입니다.

[`typealias CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

accelerometer data를 처리하는 block callback의 type입니다.

현재 페이지: stopAccelerometerUpdates()
