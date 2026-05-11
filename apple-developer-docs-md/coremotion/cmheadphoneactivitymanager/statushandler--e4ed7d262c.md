---
title: "CMHeadphoneActivityManager.StatusHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/statushandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.882395+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/statushandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   CMHeadphoneActivityManager.StatusHandler

type alias

CMHeadphoneActivityManager.StatusHandler
========================================

status update와 함께 호출되는 handler의 type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+watchOS 2.0+

    typealias StatusHandler = (CMHeadphoneActivityManager.Status, (any Error)?) -> Void

[관련 항목](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/statushandler#see-also)

-------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/statushandler#Supporting-Types)

[`enum Status`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/status)

headphone 연결 status update입니다.

[`typealias ActivityHandler`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler)

headphone motion activity data를 사용할 수 있을 때 호출되는 handler의 type입니다.

현재 페이지는 CMHeadphoneActivityManager.StatusHandler
