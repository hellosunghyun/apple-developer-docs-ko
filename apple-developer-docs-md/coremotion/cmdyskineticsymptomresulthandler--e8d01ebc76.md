---
title: "CMDyskineticSymptomResultHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909930+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMDyskineticSymptomResultHandler

type alias

CMDyskineticSymptomResultHandler
================================

dyskinetic symptom result를 처리하는 completion handler입니다.

watchOS 5.0+

    typealias CMDyskineticSymptomResultHandler = ([CMDyskineticSymptomResult], (any Error)?) -> Void

[Parameters](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler#parameters)

---------------------------------------------------------------------------------------------------------------

`dyskineticSymptomResult`

query가 찾은 dyskinetic symptom result의 array입니다.

`error`

error가 발생하면 이 parameter에 error 정보가 들어가고, 그렇지 않으면 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler#see-also)

-----------------------------------------------------------------------------------------------------------

### [movement disorder query하기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler#Querying-for-Movement-Disorders)

[`func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))

지정한 시간 간격의 tremor result를 query합니다.

[`typealias CMTremorResultHandler`](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler)

tremor result에 접근하고 처리하는 completion handler입니다.

[`func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))

지정한 시간 간격의 dyskinetic symptom을 query합니다.

[`func lastProcessedDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate())

가장 최근에 계산한 result의 날짜를 반환합니다.

현재 페이지: CMDyskineticSymptomResultHandler
