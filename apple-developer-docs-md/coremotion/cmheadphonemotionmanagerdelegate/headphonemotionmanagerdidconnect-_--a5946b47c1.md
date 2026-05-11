---
title: "headphoneMotionManagerDidConnect(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.902493+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneMotionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate)
    
*   headphoneMotionManagerDidConnect(\_:)

instance method

headphoneMotionManagerDidConnect(\_:)
=====================================

headphone을 연결한 뒤 delegate에 callback을 보냅니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+macOS 14.0+watchOS 7.0+

    optional func headphoneMotionManagerDidConnect(_ manager: CMHeadphoneMotionManager)

[Parameters](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------------------

`manager`

연결된 headphone의 manager입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------------

### [Headphone 연결 및 연결 해제](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:)#Connecting-and-Disconnecting-Headphones)

[`func headphoneMotionManagerDidDisconnect(CMHeadphoneMotionManager)`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:))

headphone 연결을 해제한 뒤 delegate에 callback을 보냅니다.

[`typealias DeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler)

headphone-motion data를 처리하는 block callback type입니다.

현재 페이지: headphoneMotionManagerDidConnect(\_:)
