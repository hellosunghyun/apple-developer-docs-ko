---
title: "startMagnetometerUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900652+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startMagnetometerUpdates(to:withHandler:)

instance method

startMagnetometerUpdates(to:withHandler:)
=========================================

operation queue에서 지정한 handler와 함께 magnetometer update를 시작합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+watchOS 2.0+

    func startMagnetometerUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMMagnetometerHandler
    )

[parameter](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------

`queue`

caller가 제공하는 operation queue입니다. 처리된 event가 높은 빈도로 도착할 수 있으므로 main operation queue 사용은 권장하지 않습니다.

`handler`

새 magnetometer data를 처리하기 위해 각 update마다 호출되는 block입니다. 이 block은 [`CMMagnetometerHandler`](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)
 type을 따라야 합니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:)#Discussion)

----------------------------------------------------------------------------------------------------------------------------------------

app이 더 이상 magnetometer update를 처리하지 않아야 하면 [`stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())
 를 호출해야 합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------

### [Magnetometer update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:)#Managing-Magnetometer-Updates)

[`var magnetometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)

system이 block handler에 magnetometer data를 전달하는 간격(초)입니다.

[`func startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())

block handler 없이 magnetometer update를 시작합니다.

[`func stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())

magnetometer update를 중지합니다.

[`var magnetometerData: CMMagnetometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)

최신 magnetometer data sample입니다.

[`typealias CMMagnetometerHandler`](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

magnetometer data를 처리하는 block callback의 type입니다.

현재 페이지는 startMagnetometerUpdates(to:withHandler:)
