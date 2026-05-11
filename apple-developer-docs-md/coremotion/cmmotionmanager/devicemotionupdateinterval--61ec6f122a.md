---
title: "deviceMotionUpdateInterval | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.889837+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   deviceMotionUpdateInterval

instance property

deviceMotionUpdateInterval
==========================

device-motion update를 block handler에 제공하는 간격(초)입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var deviceMotionUpdateInterval: TimeInterval { get set }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval#mentions)

-------------------------------------------------------------------------------------------------------------------------

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval#Discussion)

-------------------------------------------------------------------------------------------------------------------------

system은 이 property 값으로 정해지는 일정한 간격에 따라 [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))에 지정한 block handler로 device-motion update를 전달합니다.
 at regular intervals determined by the value of this property. The interval units are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of device-motion data, it should always check the timestamps of the delivered [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
 instances to determine the true update interval.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Device Motion update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

지정한 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용해 device-motion update를 시작하지만 block handler는 사용하지 않습니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

가장 최근의 device-motion data sample입니다.

[`Type Alias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback의 type입니다.

현재 페이지: deviceMotionUpdateInterval
