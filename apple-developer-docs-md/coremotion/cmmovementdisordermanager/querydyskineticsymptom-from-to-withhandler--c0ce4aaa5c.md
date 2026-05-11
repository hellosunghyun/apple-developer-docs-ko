---
title: "queryDyskineticSymptom(from:to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909682+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   queryDyskineticSymptom(from:to:withHandler:)

instance method

queryDyskineticSymptom(from:to:withHandler:)
============================================

제공한 시간 간격의 dyskinetic symptom을 query합니다.

watchOS 5.0+

    func queryDyskineticSymptom(
        from fromDate: Date,
        to toDate: Date,
        withHandler handler: @escaping CMDyskineticSymptomResultHandler
    )

[parameter](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------

`fromDate`

query의 시작 날짜와 시간입니다. 시작 시점은 지난 7일 이내여야 합니다.

`toDate`

query의 종료 날짜와 시간입니다. 종료 시점은 지난 7일 이내여야 하며 시작 날짜 이후여야 합니다.

`handler`

query가 반환한 dyskinetic symptom result를 처리하는 block입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------------

이 method를 사용해 [`monitorKinesias(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))
 method가 기록한 dyskinetic symptom을 비동기적으로 query합니다. movement disorder manager는 기록 시점 이후 7일 동안만 dyskinetic symptom result를 보관합니다.

manager가 query한 result를 가져오면 익명의 background queue에서 handler block을 호출합니다. completion handler를 제공해 이 result에 접근하고 처리합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)#Related-Documentation)

[`func monitorKinesias(forDuration: TimeInterval)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))

지정한 시간 간격 동안 tremor 및 dyskinetic symptom result를 계산해 저장합니다.

### [Movement Disorder Query하기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:)#Querying-for-Movement-Disorders)

[`func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))

제공한 시간 간격의 tremor result를 query합니다.

[`typealias CMTremorResultHandler`](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler)

tremor result에 접근하고 처리하는 completion handler입니다.

[`typealias CMDyskineticSymptomResultHandler`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler)

dyskinetic symptom result를 처리하는 completion handler입니다.

[`func lastProcessedDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate())

가장 최근에 계산한 result의 날짜를 반환합니다.

현재 페이지: queryDyskineticSymptom(from:to:withHandler:)
