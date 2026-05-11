---
title: "startStepCountingUpdates(to:updateOn:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.907466+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
    
*   *   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
        
*   startStepCountingUpdates(to:updateOn:withHandler:) Deprecated

instance method

startStepCountingUpdates(to:updateOn:withHandler:)
==================================================

현재 step-counting data를 app에 전달하기 시작합니다.

iOS 7.0–8.0DeprecatediPadOS 7.0–8.0DeprecatedMac Catalyst 13.1–13.1DeprecatedvisionOS 1.0–1.0Deprecated

    func startStepCountingUpdates(
        to queue: OperationQueue,
        updateOn stepCounts: Int,
        withHandler handler: @escaping CMStepUpdateHandler
    )

[파라미터](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------

`queue`

지정한 `handler` block을 실행할 operation queue입니다. custom queue를 지정하거나 app의 main thread에 연결된 operation queue를 사용할 수 있습니다. 이 파라미터는 `nil`이면 안 됩니다.

`stepCounts`

`handler` block을 실행하기 전에 기록할 step 수입니다. step 수는 0보다 커야 합니다.

`handler`

step 수가 기준에 도달하거나 이를 초과했을 때 실행할 block입니다. 이 block의 파라미터 정보는 [`CMStepUpdateHandler`](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)
를 참고하세요. 이 property는 `nil`이면 안 됩니다.

[설명](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------

이 method는 사용자의 step 추적을 시작하고, 결과를 전달하기 위해 제공한 block을 주기적으로 호출합니다. 이 method를 호출하면 step counter는 현재 step count 값을 0으로 재설정한 뒤 counting을 시작합니다. step counter가 `stepCounts` 파라미터에 지정된 step 수를 기록할 때마다 지정한 `handler` block을 실행합니다. 예를 들어 `stepCounts`가 100이면 100 step, 200 step, 300 step 등에서 update를 보냅니다. handler에 보고되는 step 수는 항상 이 method를 호출한 이후의 총 step 수입니다.

`handler` block은 step count 임계값을 넘을 때마다 best effort 기준으로 실행됩니다. 임계값을 넘겼을 때 app이 suspend 상태라면 block은 실행되지 않습니다. app이 다시 resume된 뒤에도 임계값을 다시 넘기기 전까지는 block이 실행되지 않습니다.

step-counting update 전달을 중지하려면 [`stopStepCountingUpdates()`](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates())
 method를 호출합니다. step counter object 자체가 deallocate될 때도 update는 중지됩니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------

### [Step Counting update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:)#Starting-and-Stopping-Step-Counting-Updates)

[`func stopStepCountingUpdates()`](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates())

step-counting update 전달을 app에 중지합니다.

Deprecated

[`typealias CMStepUpdateHandler`](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)

update가 시작된 이후 기록된 step 수를 보고하는 block입니다.

현재 페이지는 startStepCountingUpdates(to:updateOn:withHandler:)입니다
