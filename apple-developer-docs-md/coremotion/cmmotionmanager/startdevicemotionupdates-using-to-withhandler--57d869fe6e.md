---
title: "startDeviceMotionUpdates(using:to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.892620+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startDeviceMotionUpdates(using:to:withHandler:)

instance method

startDeviceMotionUpdates(using:to:withHandler:)
===============================================

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startDeviceMotionUpdates(
        using referenceFrame: CMAttitudeReferenceFrame,
        to queue: OperationQueue,
        withHandler handler: @escaping CMDeviceMotionHandler
    )

[파라미터](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------------

`referenceFrame`

device-motion update에 사용할 reference frame을 식별하는 constant입니다. 현재 device에서 사용할 수 있는 reference frame을 지정하는 책임은 개발자에게 있습니다. 현재 사용할 수 있는 reference frame을 확인하려면 [`availableAttitudeReferenceFrames()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/availableattitudereferenceframes())
를 호출합니다.

`queue`

caller가 제공하는 operation queue입니다. 처리된 event가 높은 빈도로 도착할 수 있으므로 main operation queue를 사용하는 것은 권장하지 않습니다.

`handler`

새 device-motion data를 처리하기 위해 각 update마다 호출되는 block입니다. 이 block은 [`CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)
type을 따라야 합니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)#Discussion)

----------------------------------------------------------------------------------------------------------------------------------------------

app이 device-motion update를 더 이상 처리하지 않게 하려면 [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
를 호출해야 합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------

### [device motion update 관리하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:)#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 간격(초)입니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

operation queue에서 지정한 block handler를 사용해 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용해 device-motion update를 시작하지만 block handler는 사용하지 않습니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

가장 최근의 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback의 type입니다.

현재 페이지는 startDeviceMotionUpdates(using:to:withHandler:)입니다
