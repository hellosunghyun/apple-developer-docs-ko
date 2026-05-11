---
title: "lastProcessedDate() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.911499+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   lastProcessedDate()

instance method

lastProcessedDate()
===================

가장 최근에 계산한 result의 날짜를 반환합니다.

watchOS 5.0+

    func lastProcessedDate() -> Date?

[Return Value](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate()#return-value)

--------------------------------------------------------------------------------------------------------------------------------

가장 최근에 계산한 result의 날짜이며, 사용할 수 있는 result가 없으면 `nil`입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate()#Discussion)

----------------------------------------------------------------------------------------------------------------------------

manager는 result를 batch 단위로 처리하므로 data를 바로 사용할 수 없을 수 있습니다. 이 method를 사용해 현재 처리한 data의 종료 날짜를 확인합니다. manager가 monitor 만료 날짜까지의 모든 항목을 처리할 때까지 추가 data를 계속 사용할 수 있게 됩니다.

아직 사용자 monitoring을 시작하지 않았거나 manager가 아직 어떤 data도 처리하지 않았다면 이 method는 `nil`을 반환합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate()#see-also)

------------------------------------------------------------------------------------------------------------------------

### [movement disorder query](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate()#Querying-for-Movement-Disorders)

[`func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))

지정한 시간 interval의 tremor result를 query합니다.

[`typealias CMTremorResultHandler`](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler)

tremor result에 접근하고 처리하는 completion handler입니다.

[`func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))

지정한 시간 interval의 dyskinetic symptom을 query합니다.

[`typealias CMDyskineticSymptomResultHandler`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler)

dyskinetic symptom result를 처리하는 completion handler입니다.

현재 페이지는 lastProcessedDate()입니다
