---
title: "queryStepCountStarting(from:to:to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903283+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
    
*   *   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
        
*   queryStepCountStarting(from:to:to:withHandler:) Deprecated

instance method

queryStepCountStarting(from:to:to:withHandler:)
===============================================

지정한 기간의 과거 step count data를 수집해 반환합니다.

iOS 7.0–8.0DeprecatediPadOS 7.0–8.0DeprecatedMac Catalyst 13.1–13.1DeprecatedvisionOS 1.0–1.0Deprecated

    func queryStepCountStarting(
        from start: Date,
        to end: Date,
        to queue: OperationQueue,
        withHandler handler: @escaping CMStepQueryHandler
    )

[Parameters](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------

`start`

step count data를 수집할 때 사용할 시작 시각입니다. 이 parameter는 `nil`이면 안 됩니다.

`end`

step count data를 수집할 때 사용할 종료 시각입니다. 이 parameter는 `nil`이면 안 됩니다.

`queue`

The operation queue on which to execute the specified `handler` block. You can specify a custom queue or use the operation queue associated with your app’s main thread. This parameter must not be `nil`.

`handler`

The block to execute with the results. For information about the parameters of this block, see [`CMStepQueryHandler`](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)
. This parameter must not be `nil`.

[논의](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:)#Discussion)

--------------------------------------------------------------------------------------------------------------------------------------------

This method runs asynchronously, returning immediately and delivering the results to the specified `handler` block. The system stores only the last seven days worth of step data at most. If there are no samples for the specified range of time, a value of 0 is passed to the `handler` block.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------

### [과거 Step Counting Data 가져오기](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:)#Getting-Historical-Step-Counting-Data)

[`typealias CMStepQueryHandler`](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)

query operation의 step 수를 보고하는 block입니다.

현재 페이지: queryStepCountStarting(from:to:to:withHandler:)
