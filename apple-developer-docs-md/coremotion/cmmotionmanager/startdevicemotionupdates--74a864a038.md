---
title: "startDeviceMotionUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.895878+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startDeviceMotionUpdates()

instance method

startDeviceMotionUpdates()
==========================

block handler 없이 device-motion update를 시작합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startDeviceMotionUpdates()

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates()#Discussion)

-------------------------------------------------------------------------------------------------------------------------

최신 device-motion data는 [`deviceMotion`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)
 property로 가져올 수 있습니다. app에서 더 이상 device-motion update를 처리하지 않을 때는 [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
 를 호출해야 합니다. 이 method는 device-motion update에 [`attitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe)
 이 반환하는 reference frame을 사용합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates()#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Device Motion Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates()#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 전달하는 간격(초)입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

지정한 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용해 device-motion update를 시작하지만 block handler는 사용하지 않습니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

최신 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback type입니다.

현재 페이지: startDeviceMotionUpdates()
