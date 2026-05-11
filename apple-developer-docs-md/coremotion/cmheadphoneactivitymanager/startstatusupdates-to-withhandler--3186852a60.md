---
title: "startStatusUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.885876+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
    
*   startStatusUpdates(to:withHandler:)

instance method

startStatusUpdates(to:withHandler:)
===================================

지정한 queue를 통해 지정한 handler에 data를 전달하면서 headphone status update를 시작합니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    func startStatusUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMHeadphoneActivityManager.StatusHandler
    )

[설명](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:)#discussion)

---------------------------------------------------------------------------------------------------------------------------------------------

이 method를 호출하기 전에 호환되는 headphone 세트가 이미 연결되어 있으면, 연결된 headphone에 대해 [`CMHeadphoneActivityManager.Status.connected`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/status/connected)
 status update와 함께 handler가 호출됩니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------

### [update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:)#Starting-and-Stopping-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:))

지정한 queue를 통해 지정한 handler에 data를 전달하면서 headphone activity update를 시작합니다.

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates())

headphone activity update를 중지합니다.

[`func stopStatusUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates())

headphone status update를 중지합니다.

현재 페이지는 startStatusUpdates(to:withHandler:)입니다
