---
title: "startActivityUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.889137+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   startActivityUpdates(to:withHandler:)

instance method

startActivityUpdates(to:withHandler:)
=====================================

headphone activity update를 시작하고 지정한 queue를 통해 handler에 data를 전달합니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    func startActivityUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMHeadphoneActivityManager.ActivityHandler
    )

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------

### [Starting and Stopping Updates](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:)#Starting-and-Stopping-Updates)

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates())

headphone activity update를 중지합니다.

[`func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:))

headphone status update를 시작하고 지정한 queue를 통해 handler에 data를 전달합니다.

[`func stopStatusUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates())

headphone status update를 중지합니다.

현재 페이지: startActivityUpdates(to:withHandler:)
