---
title: "showsDeviceMovementDisplay | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.889721+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   showsDeviceMovementDisplay

instance property

showsDeviceMovementDisplay
==========================

device-movement display를 표시할지 제어합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var showsDeviceMovementDisplay: Bool { get set }

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay#Discussion)

-------------------------------------------------------------------------------------------------------------------------

device를 움직여야 하는 경우(예: compass calibration) 이 property 값은 system의 device-movement display를 표시할지 나타냅니다. device를 움직여야 하면 [`CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler) type의 block handler가 [`CMErrorDeviceRequiresMovement`](https://developer.apple.com/documentation/coremotion/cmerrordevicerequiresmovement) error를 한 번 보고합니다. 기본값은 [`false`](https://developer.apple.com/documentation/Swift/false)입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Device Motion update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay#Managing-Device-Motion-Updates)

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 간격(초)입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

지정한 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용하지만 block handler 없이 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

가장 최근의 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback의 type입니다.

현재 페이지: showsDeviceMovementDisplay
