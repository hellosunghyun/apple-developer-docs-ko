---
title: "deviceMotion | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.895593+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   deviceMotion

instance property

deviceMotion
============

가장 최근의 device-motion data sample입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var deviceMotion: CMDeviceMotion? { get }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion#mentions)

-----------------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion#Discussion)

-----------------------------------------------------------------------------------------------------------

device-motion data를 사용할 수 없으면 이 property의 값은 `nil`입니다. [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
를 호출한 뒤 device-motion data를 받는 app은 이 property의 값을 주기적으로 확인하고 device-motion data를 처리합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion#see-also)

-------------------------------------------------------------------------------------------------------

### [Managing Device Motion Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 간격(초)입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

지정한 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

block handler 없이 reference frame을 사용해 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback의 type입니다.

현재 페이지: deviceMotion
