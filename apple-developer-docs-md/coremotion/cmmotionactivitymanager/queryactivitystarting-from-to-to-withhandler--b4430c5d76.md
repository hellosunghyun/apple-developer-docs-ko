---
title: "queryActivityStarting(from:to:to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903560+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
    
*   queryActivityStarting(from:to:to:withHandler:)

instance method

queryActivityStarting(from:to:to:withHandler:)
==============================================

지정한 기간의 과거 motion data를 수집해 반환합니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    func queryActivityStarting(
        from start: Date,
        to end: Date,
        to queue: OperationQueue,
        withHandler handler: @escaping CMMotionActivityQueryHandler
    )

[parameter](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------

`start`

motion data를 수집할 시작 시각입니다. 이 parameter는 `nil`이면 안 됩니다.

`end`

motion data를 수집할 종료 시각입니다. 이 parameter는 `nil`이면 안 됩니다.

`queue`

지정한 `handler` block을 실행할 operation queue입니다. custom queue를 지정하거나 app의 main thread와 연결된 operation queue를 사용할 수 있습니다. 이 parameter는 `nil`이면 안 됩니다.

`handler`

result와 함께 실행할 block입니다. 이 block의 parameter에 대한 정보는 [`CMMotionActivityQueryHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)
를 참고하십시오. 이 parameter는 `nil`이면 안 됩니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------------

이 method는 async로 실행되며 즉시 반환하고, result는 지정한 `handler` block에 전달합니다. 보고되는 activity에는 최대 몇 분까지 지연이 있을 수 있습니다.

system은 최대 최근 7일치 activity data만 저장합니다. 지정한 시간 범위에 sample이 없으면 code가 [`CMErrorUnknown`](https://developer.apple.com/documentation/coremotion/cmerrorunknown)
인 error object를 `handler` block에 전달합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------------

### [과거 activity data 가져오기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:)#Getting-Historical-Activity-Data)

[`typealias CMMotionActivityQueryHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)

지정한 query interval 사이에 발생한 motion update를 보고하는 block입니다.

현재 페이지는 queryActivityStarting(from:to:to:withHandler:)입니다.
