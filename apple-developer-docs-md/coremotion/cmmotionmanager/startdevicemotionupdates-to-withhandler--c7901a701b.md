---
title: "startDeviceMotionUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.895445+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startDeviceMotionUpdates(to:withHandler:)

instance method

startDeviceMotionUpdates(to:withHandler:)
=========================================

operation queue에서 지정한 block handler를 사용해 device-motion update를 시작합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startDeviceMotionUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMDeviceMotionHandler
    )

[Parameters](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------

`queue`

caller가 제공하는 operation queue입니다. 처리된 event가 높은 빈도로 도착할 수 있으므로 main operation queue 사용은 권장하지 않습니다.

`handler`

새 device-motion data를 처리하도록 update마다 호출되는 block입니다. 이 block은 [`CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)
 type을 따라야 합니다.

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)#Discussion)

----------------------------------------------------------------------------------------------------------------------------------------

이 method는 [`attitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe)
 property의 reference frame을 기준으로 motion을 보고합니다. app이 더 이상 device-motion update를 처리하지 않아야 할 때는 [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
를 호출해야 합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------

### [Device Motion Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:)#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 전달하는 간격(초)입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

operation queue에서 지정한 reference frame과 block handler를 사용해 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용해 device-motion update를 시작하지만 block handler는 사용하지 않습니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

최신 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback type입니다.

현재 페이지는 startDeviceMotionUpdates(to:withHandler:)입니다
