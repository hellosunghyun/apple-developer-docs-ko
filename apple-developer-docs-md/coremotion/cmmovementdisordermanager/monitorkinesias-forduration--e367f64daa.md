---
title: "monitorKinesias(forDuration:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.913304+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   monitorKinesias(forDuration:)

instance method

monitorKinesias(forDuration:)
=============================

지정한 시간 간격 동안 tremor와 dyskinetic symptom result를 계산하고 저장합니다.

watchOS 5.0+

    func monitorKinesias(forDuration duration: TimeInterval)

[Parameters](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------

`duration`

초 단위 monitoring 기간입니다. 최대 기간은 7일입니다.

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#mentions)

--------------------------------------------------------------------------------------------------------------------------------------

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

[논의](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#Discussion)

--------------------------------------------------------------------------------------------------------------------------------------

이 method를 호출해 tremor와 dyskinetic symptom result의 monitoring, 계산, 저장을 시작합니다. manager는 기록 시점 이후 7일 동안 result를 저장합니다. 이 7일 구간 안에서는 언제든 result에 접근할 수 있으며, 그 이후에는 만료됩니다. result를 가져오려면 [`queryTremor(from:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))
 및 [`queryDyskineticSymptom(from:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))
 method를 호출합니다.

result가 현재 monitoring 및 계산 중인지 확인하려면 [`monitorKinesiasExpirationDate()`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate())
 method를 호출합니다. monitoring 기간의 최대 길이는 7일입니다. 만료일 이후에도 monitoring을 계속하려면 monitoring 기간이 끝나기 전에 [`monitorKinesias(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))
를 다시 호출해 subscription을 갱신해야 합니다. 반복 호출하면 monitoring 기간은 연장할 수 있지만 단축할 수는 없습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#Related-Documentation)

[`func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))

지정한 시간 간격의 tremor result를 query합니다.

[`func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))

지정한 시간 간격의 dyskinetic symptom을 query합니다.

### [Movement Disorder 기록하기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:)#Recording-Movement-Disorders)

[`func monitorKinesiasExpirationDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate())

가장 최근 monitoring 기간의 만료일을 반환합니다.

현재 페이지: monitorKinesias(forDuration:)
