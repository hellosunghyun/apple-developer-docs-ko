---
title: "headphoneMotionManagerDidDisconnect(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.902292+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneMotionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate)
    
*   headphoneMotionManagerDidDisconnect(\_:)

instance method

headphoneMotionManagerDidDisconnect(\_:)
========================================

headphone 연결이 해제된 후 delegate에 callback을 수행합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+macOS 14.0+watchOS 7.0+

    optional func headphoneMotionManagerDidDisconnect(_ manager: CMHeadphoneMotionManager)

[parameter](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------------

`manager`

연결이 해제된 headphone의 manager입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:)#see-also)

---------------------------------------------------------------------------------------------------------------------------------------------------

### [Headphone 연결 및 연결 해제](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:)#Connecting-and-Disconnecting-Headphones)

[`func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:))

headphone이 연결된 후 delegate에 callback을 수행합니다.

[`typealias DeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler)

headphone-motion data를 처리하는 block callback의 type입니다.

현재 페이지: headphoneMotionManagerDidDisconnect(\_:)
