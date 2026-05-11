---
title: "CMStepQueryHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepqueryhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.903188+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMStepQueryHandler

type alias

CMStepQueryHandler
==================

query operation의 step 수를 보고하는 block입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+

    typealias CMStepQueryHandler = (Int, (any Error)?) -> Void

[설명](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler#Discussion)

-------------------------------------------------------------------------------------------------

이 block은 두 개의 parameter를 받습니다.

`numberOfSteps`

query가 지정한 시작 시각과 종료 시각 사이에 발생한 step 수입니다.

`error`

data를 수집하는 중 문제가 있었음을 나타내는 error object입니다. step 수를 올바르게 판단한 경우에는 `nil`입니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler#see-also)

---------------------------------------------------------------------------------------------

### [과거 step counting data 가져오기](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler#Getting-Historical-Step-Counting-Data)

[`func queryStepCountStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMStepQueryHandler)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:))

지정한 기간의 과거 step count data를 수집해 반환합니다.

Deprecated

현재 페이지: CMStepQueryHandler
