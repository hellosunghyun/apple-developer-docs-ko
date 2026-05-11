---
title: "stopActivityUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.885974+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   stopActivityUpdates()

instance method

stopActivityUpdates()
=====================

headphone activity update를 중지합니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    func stopActivityUpdates()

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates()#see-also)

---------------------------------------------------------------------------------------------------------------------------

### [Starting and Stopping Updates](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates()#Starting-and-Stopping-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:))

headphone activity update를 시작하고 지정한 queue를 통해 handler에 data를 전달합니다.

[`func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:))

headphone status update를 시작하고 지정한 queue를 통해 handler에 data를 전달합니다.

[`func stopStatusUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates())

headphone status update를 중지합니다.

현재 페이지: stopActivityUpdates()
