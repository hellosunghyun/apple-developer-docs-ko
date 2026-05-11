---
title: "startDeviceMotionUpdates(using:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.895741+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startDeviceMotionUpdates(using:)

instance method

startDeviceMotionUpdates(using:)
================================

reference frame을 사용하지만 block handler 없이 device-motion update를 시작합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startDeviceMotionUpdates(using referenceFrame: CMAttitudeReferenceFrame)

[파라미터](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------

`referenceFrame`

device-motion update에 사용할 reference frame을 식별하는 constant입니다. 현재 device에서 사용할 수 있는 reference frame을 지정하는 것은 개발자의 책임입니다. 현재 사용할 수 있는 reference frame을 확인하려면 [`availableAttitudeReferenceFrames()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/availableattitudereferenceframes())
를 호출합니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)#Discussion)

-------------------------------------------------------------------------------------------------------------------------------

[`deviceMotion`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)
 property로 최신 device-motion data를 가져올 수 있습니다. app에서 더 이상 device-motion update를 처리하지 않으려면 [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
를 호출해야 합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)#see-also)

---------------------------------------------------------------------------------------------------------------------------

### [Device Motion Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:)#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 간격(초)입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

operation queue에서 지정한 reference frame과 block handler를 사용해 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

operation queue에서 지정한 block handler를 사용해 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

최신 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback type입니다.

현재 페이지는 startDeviceMotionUpdates(using:)입니다
