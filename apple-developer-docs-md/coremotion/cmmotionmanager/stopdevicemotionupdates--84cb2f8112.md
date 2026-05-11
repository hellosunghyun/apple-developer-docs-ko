---
title: "stopDeviceMotionUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.896164+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   stopDeviceMotionUpdates()

instance method

stopDeviceMotionUpdates()
=========================

device-motion update를 중지합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func stopDeviceMotionUpdates()

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates()#mentions)

------------------------------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates()#see-also)

--------------------------------------------------------------------------------------------------------------------

### [Managing Device Motion Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates()#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 초 단위 interval입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

지정한 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용해 block handler 없이 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

최신 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback type입니다.

현재 페이지: stopDeviceMotionUpdates()
