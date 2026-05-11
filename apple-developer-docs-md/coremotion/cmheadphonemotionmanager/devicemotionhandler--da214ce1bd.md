---
title: "CMHeadphoneMotionManager.DeviceMotionHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.902194+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)
    
*   CMHeadphoneMotionManager.DeviceMotionHandler

type 별칭

CMHeadphoneMotionManager.DeviceMotionHandler
============================================

headphone-motion data를 처리하는 block callback의 type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+watchOS 2.0+

    typealias DeviceMotionHandler = (CMDeviceMotion?, (any Error)?) -> Void

[설명](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler#Discussion)

---------------------------------------------------------------------------------------------------------------------------

system은 처리할 device-motion data가 있을 때 `CMDeviceMotionHandler` block을 호출합니다. 이 block은 [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:))
 의 두 번째 argument로 전달합니다. 이 type의 block은 값을 반환하지 않으며, 대신 두 개의 argument를 받습니다.

`motion`

attitude, rotation rate, gravity, user acceleration을 나타내는 structure와 다른 object를 캡슐화하는 [`CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)
 object입니다.

`error`

gyroscope data를 제공하는 동안 발생한 오류를 나타내는 error object입니다. error가 발생하면 gyroscope update를 중지하고 사용자에게 문제를 알려야 합니다. error가 없으면 이 argument는 `nil`입니다. Core Motion error는 [`CMErrorDomain`](https://developer.apple.com/documentation/coremotion/cmerrordomain)
 domain 및 [`CMError`](https://developer.apple.com/documentation/coremotion/cmerror)
 type을 사용합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [headphones 연결 및 연결 해제](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler#Connecting-and-Disconnecting-Headphones)

[`func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:))

headphones를 연결한 뒤 delegate에 callback을 수행합니다.

[`func headphoneMotionManagerDidDisconnect(CMHeadphoneMotionManager)`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:))

headphones 연결을 해제한 뒤 delegate에 callback을 수행합니다.

현재 페이지: CMHeadphoneMotionManager.DeviceMotionHandler
