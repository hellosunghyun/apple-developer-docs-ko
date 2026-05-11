---
title: "CMMovementDisorderManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.894229+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMovementDisorderManager

class

CMMovementDisorderManager
=========================

movement disorder data를 기록하고 query하는 manager입니다.

watchOS 5.0+

    class CMMovementDisorderManager

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#mentions)

--------------------------------------------------------------------------------------------------------

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

[개요](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#overview)

----------------------------------------------------------------------------------------------------

`CMMovementDisorderManager`를 사용하면 3-7Hz 범위의 resting Parkinsonian tremor와 choreiform dyskinetic symptom을 측정할 수 있습니다. data를 수집할 때 사용자는 가장 영향을 많이 받는 팔에 Apple Watch를 착용해야 합니다.

`CMMovementDisorderManager`를 사용하려면 Apple의 entitlement가 필요합니다. entitlement를 신청하려면 [Movement Disorder Entitlement Request](https://developer.apple.com/contact/request/movement-disorder-api-entitlement/)
를 참고합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#topics)

------------------------------------------------------------------------------------------------

### [사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#Checking-Availablility)

[`class func isAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable())

현재 device가 movement disorder manager를 지원하는지 나타내는 Boolean 값입니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus())

사용자가 app이 movement disorder data를 모니터링하고 query하도록 승인했는지 나타내는 값입니다.

[`class func version() -> String?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version())

movement disorder algorithm의 현재 버전을 설명하는 string을 반환합니다.

### [Movement Disorder 기록](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#Recording-Movement-Disorders)

[`func monitorKinesias(forDuration: TimeInterval)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))

지정한 시간 간격 동안의 tremor 및 dyskinetic symptom result를 계산하고 저장합니다.

[`func monitorKinesiasExpirationDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate())

가장 최근 monitoring 기간의 만료 날짜를 반환합니다.

### [Movement Disorder query](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#Querying-for-Movement-Disorders)

[`func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))

제공된 시간 간격의 tremor result를 query합니다.

[`typealias CMTremorResultHandler`](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler)

tremor result에 접근하고 처리하는 completion handler입니다.

[`func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))

제공된 시간 간격의 dyskinetic symptom을 query합니다.

[`typealias CMDyskineticSymptomResultHandler`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresulthandler)

dyskinetic symptom result를 처리하는 completion handler입니다.

[`func lastProcessedDate() -> Date?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate())

가장 최근에 계산된 result의 날짜를 반환합니다.

[관계](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#relationships)

--------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#see-also)

----------------------------------------------------------------------------------------------------

### [Movement disorder](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager#Movement-disorder)

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[movement disorder data collection requirement 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

사용자가 app이 수집하는 data를 이해하고 제어할 수 있도록 보장합니다.

[movement disorder algorithm 변경 내역](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

movement disorder algorithm의 주요 변경 사항을 시간순으로 기록한 로그입니다.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

1분 간격 동안 tremor의 존재 여부와 강도에 관한 data를 담는 result object입니다.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

1분 간격 동안 dyskinetic symptom이 존재할 가능성에 관한 data를 담는 result object입니다.

현재 페이지는 CMMovementDisorderManager입니다
