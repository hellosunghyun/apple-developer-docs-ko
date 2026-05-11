---
title: "CMMotionActivityQueryHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.882170+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMotionActivityQueryHandler

type alias

CMMotionActivityQueryHandler
============================

지정한 query interval 사이에 발생한 motion update를 보고하는 block입니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    typealias CMMotionActivityQueryHandler = ([CMMotionActivity]?, (any Error)?) -> Void

[논의](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler#Discussion)

-----------------------------------------------------------------------------------------------------------

이 block은 다음 parameter를 받습니다.

`activities`

발생한 update를 나타내는 [`CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)
 object array입니다. array의 object는 지정한 시간 interval 내에서 발생한 시각 순으로 정렬됩니다. 각 motion object의 [`startDate`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/startdate)
 property를 사용해 update가 발생한 시점을 확인합니다.

`error`

data 수집 중 문제가 발생했음을 나타내는 error object이며, motion data를 정상적으로 판별한 경우에는 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler#see-also)

-------------------------------------------------------------------------------------------------------

### [Getting Historical Activity Data](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler#Getting-Historical-Activity-Data)

[`func queryActivityStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMMotionActivityQueryHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:))

지정한 기간의 과거 motion data를 수집해 반환합니다

현재 페이지는 CMMotionActivityQueryHandler입니다
