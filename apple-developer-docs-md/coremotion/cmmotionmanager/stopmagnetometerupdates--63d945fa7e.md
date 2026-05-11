---
title: "stopMagnetometerUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899197+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   stopMagnetometerUpdates()

instance method

stopMagnetometerUpdates()
=========================

magnetometer update를 중지합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+watchOS 2.0+

    func stopMagnetometerUpdates()

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates()#see-also)

--------------------------------------------------------------------------------------------------------------------

### [Magnetometer update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates()#Managing-Magnetometer-Updates)

[`var magnetometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)

system이 block handler에 magnetometer data를 전달하는 간격(초)입니다.

[`func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))

operation queue에서 지정한 handler와 함께 magnetometer update를 시작합니다.

[`func startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())

block handler 없이 magnetometer update를 시작합니다.

[`var magnetometerData: CMMagnetometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)

최신 magnetometer data sample입니다.

[`typealias CMMagnetometerHandler`](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

magnetometer data를 처리하는 block callback의 type입니다.

현재 페이지는 stopMagnetometerUpdates()
