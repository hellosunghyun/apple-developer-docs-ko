---
title: "stopActivityUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903743+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
    
*   stopActivityUpdates()

instance method

stopActivityUpdates()
=====================

app으로의 motion update 전달을 중지합니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    func stopActivityUpdates()

[논의](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates()#Discussion)

----------------------------------------------------------------------------------------------------------------------------

Call this method to stop the delivery of updates that you started by calling the [`startActivityUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:))
 method. This method does not stop queries started using the [`queryActivityStarting(from:to:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:))
 method.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates()#see-also)

------------------------------------------------------------------------------------------------------------------------

### [Activity Update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates()#Starting-and-Stopping-Activity-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:))

현재 motion data update를 app에 전달하기 시작합니다.

[`typealias CMMotionActivityHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)

device와 관련된 현재 motion을 보고하는 block입니다.

현재 페이지: stopActivityUpdates()
