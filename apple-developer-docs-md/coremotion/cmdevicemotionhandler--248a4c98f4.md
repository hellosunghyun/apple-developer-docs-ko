---
title: "CMDeviceMotionHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.896018+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMDeviceMotionHandler

type alias

CMDeviceMotionHandler
=====================

device-motion data를 처리하는 block callback type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    typealias CMDeviceMotionHandler = (CMDeviceMotion?, (any Error)?) -> Void

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler#mentions)

----------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[논의](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler#Discussion)

----------------------------------------------------------------------------------------------------

Blocks of type `CMDeviceMotionHandler` are called when there is device-motion data to process. You pass the block into [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))
 as the second argument. Blocks of this type return no value but take two arguments:

`motion`

A [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
 object, which encapsulates other objects and a structure representing attitude, rotation rate, gravity, and user acceleration.

`error`

An error object representing an error encountered in providing device-motion data. If an error occurs, you should stop device-motion data updates and inform the user of the problem. If there is no error, this argument is `nil`. Core Motion errors are of the [`CMErrorDomain`](https://developer.apple.com/documentation/coremotion/cmerrordomain)
 domain and the [`CMError`](https://developer.apple.com/documentation/coremotion/cmerror)
 type.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler#see-also)

------------------------------------------------------------------------------------------------

### [Device Motion Update 관리하기](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 간격(초)입니다.

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

가장 최근 device-motion data sample입니다.

현재 페이지: CMDeviceMotionHandler
