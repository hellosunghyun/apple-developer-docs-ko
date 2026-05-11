---
title: "CMMotionActivityHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903655+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMotionActivityHandler

type alias

CMMotionActivityHandler
=======================

device와 연관된 현재 motion을 보고하는 block입니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    typealias CMMotionActivityHandler = (CMMotionActivity?) -> Void

[논의](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler#Discussion)

------------------------------------------------------------------------------------------------------

이 block은 다음 parameter를 받습니다.

`activity`

device의 현재 motion type을 정의하는 motion activity object입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler#see-also)

--------------------------------------------------------------------------------------------------

### [activity update 시작 및 중지하기](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler#Starting-and-Stopping-Activity-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:))

현재 motion data update 전달을 app에 시작합니다.

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates())

motion update 전달을 app에 중지합니다

현재 페이지: CMMotionActivityHandler
