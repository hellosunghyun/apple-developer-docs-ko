---
title: "CMTremorResultHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmtremorresulthandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909811+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMTremorResultHandler

type alias

CMTremorResultHandler
=====================

tremor result에 접근하고 처리하기 위한 completion handler입니다.

watchOS 5.0+

    typealias CMTremorResultHandler = ([CMTremorResult], (any Error)?) -> Void

[parameter](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler#parameters)

----------------------------------------------------------------------------------------------------

`tremorResult`

query가 찾은 tremor result 배열입니다.

`error`

error가 발생한 경우 이 parameter에 error 정보가 들어가고, 그렇지 않으면 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler#see-also)

------------------------------------------------------------------------------------------------

### [운동 장애 query](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler#Querying-for-Movement-Disorders)

[`func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))

지정한 시간 interval의 tremor result를 query합니다.

[`func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))

지정한 시간 interval의 dyskinetic symptom을 query합니다.

[`typealias CMDyskineticSymptomResultHandler`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler)

dyskinetic symptom result를 처리하는 completion handler입니다.

[`func lastProcessedDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate())

가장 최근에 계산된 result의 날짜를 반환합니다.

현재 페이지는 CMTremorResultHandler입니다.
