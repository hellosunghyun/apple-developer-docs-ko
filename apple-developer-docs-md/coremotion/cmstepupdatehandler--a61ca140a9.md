---
title: "CMStepUpdateHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepupdatehandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903384+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMStepUpdateHandler

typealias

CMStepUpdateHandler
===================

update가 시작된 이후 기록한 step 수를 보고하는 block입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+

    typealias CMStepUpdateHandler = (Int, Date, (any Error)?) -> Void

[설명](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler#Discussion)

--------------------------------------------------------------------------------------------------

이 block은 다음 parameter를 받습니다.

`numberOfSteps`

[`startStepCountingUpdates(to:updateOn:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:))
 method를 호출한 이후의 총 step 수입니다.

`timestamp`

현재 step count를 보고한 시각입니다.

`error`

data를 수집하는 중 문제가 있었음을 나타내는 error object이며, step 수를 올바르게 확인했으면 `nil`입니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler#see-also)

----------------------------------------------------------------------------------------------

### [step counting update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler#Starting-and-Stopping-Step-Counting-Updates)

[`func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:))

현재 step-counting data 전달을 app에 시작합니다.

Deprecated

[`func stopStepCountingUpdates()`](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates())

step-counting update 전달을 app에 중지합니다.

Deprecated

현재 페이지는 CMStepUpdateHandler입니다
