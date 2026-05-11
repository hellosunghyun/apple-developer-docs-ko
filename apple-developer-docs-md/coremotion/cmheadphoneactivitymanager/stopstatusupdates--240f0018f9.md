---
title: "stopStatusUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.885766+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   stopStatusUpdates()

instance method

stopStatusUpdates()
===================

headphone status update를 중지합니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    func stopStatusUpdates()

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates()#see-also)

-------------------------------------------------------------------------------------------------------------------------

### [Starting and Stopping Updates](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates()#Starting-and-Stopping-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:))

지정한 queue를 통해 지정한 handler에 data를 전달하면서 headphone activity update를 시작합니다.

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates())

headphone activity update를 중지합니다.

[`func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:))

지정한 queue를 통해 지정한 handler에 data를 전달하면서 headphone status update를 시작합니다.

현재 페이지는 stopStatusUpdates()입니다
