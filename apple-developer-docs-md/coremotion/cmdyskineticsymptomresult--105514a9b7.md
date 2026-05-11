---
title: "CMDyskineticSymptomResult | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.897397+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMDyskineticSymptomResult

class

CMDyskineticSymptomResult
=========================

1분 구간 동안 dyskinetic symptom이 있었을 가능성에 대한 data를 포함하는 result object입니다.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.1+watchOS 5.0+

    class CMDyskineticSymptomResult

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#mentions)

--------------------------------------------------------------------------------------------------------

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

[개요](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#overview)

----------------------------------------------------------------------------------------------------

Dyskinesia는 파킨슨병 조절을 위해 Levadopa를 복용할 때 부작용으로 나타나는 통제되지 않는 불수의 운동입니다. Dyskinesia는 팔, 다리, 머리처럼 신체 일부에만 나타날 수도 있고, 몸 전체에 영향을 줄 수도 있습니다. 일부 dyskinesia는 안절부절못함, 몸부림, 꿈틀거림, 머리 끄덕임, 몸 흔들림 같은 동작으로 보입니다. 이런 symptom은 약효가 가장 강한 시점에 나타나는 경향이 있습니다. Dyskinesia는 보통 더 높은 Levadopa 용량이 필요할 수 있는 진행성 파킨슨병 환자에게서 나타납니다.

다음 식은 항상 성립합니다: [`percentUnlikely`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/percentunlikely)
 `+` [`percentLikely`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/percentlikely)
 `= 1.0`.

[주제](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#topics)

------------------------------------------------------------------------------------------------

### [시간 구간 읽기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#Reading-the-Time-Interval)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/startdate)

result의 시작 시각과 날짜입니다.

[`var endDate: Date`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate)

result의 종료 시각과 날짜입니다.

### [Dyskinetic symptom data에 접근하기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#Accessing-Dyskinetic-Symptom-Data)

[`var percentUnlikely: Float`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/percentunlikely)

dyskinetic symptom이 없었을 가능성이 높은 시간의 비율입니다.

[`var percentLikely: Float`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/percentlikely)

dyskinetic symptom이 있었을 가능성이 높은 시간의 비율입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#relationships)

--------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#see-also)

----------------------------------------------------------------------------------------------------

### [Movement disorder](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult#Movement-disorder)

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[movement disorder data collection requirement 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

사용자가 app이 수집하는 data를 이해하고 제어할 수 있게 합니다.

[movement disorder algorithm 변경 내역](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

movement disorder algorithm의 주요 변경 사항을 시간순으로 기록한 log입니다.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

movement disorder data를 기록하고 query하는 manager입니다.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

1분 구간 동안 tremor의 존재 여부와 강도에 대한 data를 포함하는 result object입니다.

현재 페이지: CMDyskineticSymptomResult
