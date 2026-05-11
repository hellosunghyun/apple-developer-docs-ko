---
title: "CMHeadphoneActivityManager.ActivityHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.882503+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   CMHeadphoneActivityManager.ActivityHandler

typealias

CMHeadphoneActivityManager.ActivityHandler
==========================================

headphone motion activity data를 사용할 수 있을 때 호출하는 handler type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+watchOS 2.0+

    typealias ActivityHandler = (CMMotionActivity?, (any Error)?) -> Void

[참고 항목](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler#see-also)

---------------------------------------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler#Supporting-Types)

[`enum Status`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/status)

headphone 연결 status update입니다.

[`typealias StatusHandler`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/statushandler)

status update와 함께 호출하는 handler type입니다.

현재 페이지는 CMHeadphoneActivityManager.ActivityHandler입니다
