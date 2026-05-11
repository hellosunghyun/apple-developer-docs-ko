---
title: "stopStepCountingUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.907370+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
    
*   *   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
        
*   stopStepCountingUpdates() Deprecated

instance method

stopStepCountingUpdates()
=========================

step-counting update의 app 전달을 중단합니다.

iOS 7.0–8.0DeprecatediPadOS 7.0–8.0DeprecatedMac Catalyst 13.1–13.1DeprecatedvisionOS 1.0–1.0Deprecated

    func stopStepCountingUpdates()

[논의](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates()#Discussion)

----------------------------------------------------------------------------------------------------------------------

이 method를 호출하면 [`startStepCountingUpdates(to:updateOn:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:))
method로 시작한 update 전달을 중단합니다. 이 method는 [`queryStepCountStarting(from:to:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:))
method로 시작한 query는 중단하지 않습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates()#see-also)

------------------------------------------------------------------------------------------------------------------

### [Starting and Stopping Step Counting Updates](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates()#Starting-and-Stopping-Step-Counting-Updates)

[`func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:))

현재 step-counting data의 app 전달을 시작합니다.

Deprecated

[`typealias CMStepUpdateHandler`](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)

update가 시작된 이후 기록된 step 수를 보고하는 block입니다.

현재 페이지: stopStepCountingUpdates()
