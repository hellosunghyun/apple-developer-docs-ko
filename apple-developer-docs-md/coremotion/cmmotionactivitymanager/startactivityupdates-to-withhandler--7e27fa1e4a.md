---
title: "startActivityUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903861+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
    
*   startActivityUpdates(to:withHandler:)

instance method

startActivityUpdates(to:withHandler:)
=====================================

현재 motion data update를 app으로 전달하기 시작합니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    func startActivityUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMMotionActivityHandler
    )

[Parameters](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------

`queue`

지정한 `handler` block을 실행할 operation queue입니다. custom queue를 지정하거나 app의 main thread와 연결된 operation queue를 사용할 수 있습니다. 이 parameter는 `nil`이면 안 됩니다.

`handler`

현재 motion type의 변화를 감지했을 때 실행할 block입니다. 이 block의 parameter 정보는 [`CMMotionActivityHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)
를 참고하세요. 이 property는 `nil`이면 안 됩니다.

[논의](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:)#Discussion)

--------------------------------------------------------------------------------------------------------------------------------------------

이 method는 motion data tracking을 async로 시작합니다. 이 method를 호출하면 motion activity manager가 지정한 `queue`에서 `handler` block을 실행해 device에 현재 적용 중인 motion을 보고합니다. 그 이후에는 motion data가 바뀔 때만 motion activity manager가 `handler` block을 실행합니다.

`handler` block은 best effort 기준으로 실행되며 app이 suspended 상태일 때는 update가 전달되지 않습니다. app이 suspended 상태인 동안 update가 도착했다면, 실행을 재개할 때 마지막 update 하나를 app에 전달합니다. app이 suspended 상태였던 동안 발생한 모든 update를 가져오려면 [`queryActivityStarting(from:to:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:))
method를 사용합니다.

activity update를 시작하면 motion activity manager는 [`stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates())
method를 호출할 때까지 자신의 block에 변화를 보고합니다. 이 method를 새 block과 함께 다시 호출하면 activity manager는 이전 block으로의 update 전달을 중단하고 새 block으로 전달합니다. motion activity manager object 자체가 deallocated되면 update는 완전히 중단됩니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------

### [Starting and Stopping Activity Updates](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:)#Starting-and-Stopping-Activity-Updates)

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates())

motion update의 app 전달을 중단합니다

[`typealias CMMotionActivityHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)

device와 연관된 현재 motion을 보고하는 block입니다.

현재 페이지: startActivityUpdates(to:withHandler:)
