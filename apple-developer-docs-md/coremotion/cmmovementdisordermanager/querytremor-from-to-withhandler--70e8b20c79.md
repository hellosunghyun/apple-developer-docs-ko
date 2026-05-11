---
title: "queryTremor(from:to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909417+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   queryTremor(from:to:withHandler:)

instance method

queryTremor(from:to:withHandler:)
=================================

지정한 시간 구간의 tremor result를 query합니다.

watchOS 5.0+

    func queryTremor(
        from fromDate: Date,
        to toDate: Date,
        withHandler handler: @escaping CMTremorResultHandler
    )

[파라미터](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------------

`fromDate`

query의 시작 날짜와 시간입니다. 시작 시점은 최근 7일 이내여야 합니다.

`toDate`

query의 종료 날짜와 시간입니다. 종료 시점은 최근 7일 이내여야 하며 시작 날짜 이후여야 합니다.

`handler`

query가 반환한 tremor result를 처리하는 block입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)#Discussion)

------------------------------------------------------------------------------------------------------------------------------------------

이 method를 사용해 [`monitorKinesias(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))
 method가 기록한 tremor result를 비동기로 query합니다. movement disorder manager는 tremor result를 기록 시점으로부터 7일 동안만 유지합니다.

manager가 query한 result를 가져오면 이름 없는 background queue에서 handler block을 호출합니다. completion handler를 제공해 이 result에 접근하고 처리합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)#see-also)

--------------------------------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)#Related-Documentation)

[`func monitorKinesias(forDuration: TimeInterval)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))

지정한 시간 간격 동안의 tremor 및 dyskinetic symptom result를 계산하고 저장합니다.

### [Movement Disorder query](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:)#Querying-for-Movement-Disorders)

[`typealias CMTremorResultHandler`](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler)

tremor result에 접근하고 처리하는 completion handler입니다.

[`func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))

지정한 시간 구간의 dyskinetic symptom을 query합니다.

[`typealias CMDyskineticSymptomResultHandler`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler)

dyskinetic symptom result를 처리하는 completion handler입니다.

[`func lastProcessedDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate())

가장 최근에 계산한 result의 날짜를 반환합니다.

현재 페이지는 queryTremor(from:to:withHandler:)입니다
