---
title: "CMTremorResult | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmtremorresult"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.897256+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmtremorresult#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMTremorResult

class

CMTremorResult
==============

1분 간격 동안 tremor의 존재 여부와 강도에 대한 data를 담는 result object입니다.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 5.0+

    class CMTremorResult

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmtremorresult#mentions)

---------------------------------------------------------------------------------------------

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

[개요](https://developer.apple.com/documentation/coremotion/cmtremorresult#overview)

-----------------------------------------------------------------------------------------

다음 식은 항상 참입니다: [`percentUnknown`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown)
 `+` [`percentNone`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentnone)
 `+` [`percentSlight`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentslight)
 `+` [`percentMild`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentmild)
 `+` [`percentModerate`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentmoderate)
 `+` [`percentStrong`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentstrong)
 `= 1.0`.

[주제](https://developer.apple.com/documentation/coremotion/cmtremorresult#topics)

-------------------------------------------------------------------------------------

### [시간 구간 읽기](https://developer.apple.com/documentation/coremotion/cmtremorresult#Reading-the-Time-Interval)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmtremorresult/startdate)

result의 시작 시각과 날짜입니다.

[`var endDate: Date`](https://developer.apple.com/documentation/coremotion/cmtremorresult/enddate)

result의 종료 시각과 날짜입니다.

### [Tremor data 접근하기](https://developer.apple.com/documentation/coremotion/cmtremorresult#Accessing-Tremor-Data)

[`var percentUnknown: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown)

algorithm이 판단을 내리지 못한 시간의 비율입니다.

[`var percentNone: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentnone)

tremor가 감지되지 않은 시간의 비율입니다.

[`var percentSlight: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentslight)

tremor가 있었을 가능성이 높고 변위 amplitude가 slight였던 시간의 비율입니다.

[`var percentMild: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentmild)

tremor가 있었을 가능성이 높고 변위 amplitude가 mild였던 시간의 비율입니다.

[`var percentModerate: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentmoderate)

tremor가 있었을 가능성이 높고 변위 amplitude가 moderate였던 시간의 비율입니다.

[`var percentStrong: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentstrong)

tremor가 있었을 가능성이 높고 변위 amplitude가 strong였던 시간의 비율입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmtremorresult#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmtremorresult/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmtremorresult#relationships)

---------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmtremorresult#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmtremorresult#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmtremorresult#see-also)

-----------------------------------------------------------------------------------------

### [Movement disorder](https://developer.apple.com/documentation/coremotion/cmtremorresult#Movement-disorder)

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[movement disorder data collection requirement 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

사용자가 앱이 수집하는 data를 이해하고 제어할 수 있게 합니다.

[movement disorder algorithm 변경 내역](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

movement disorder algorithm의 주요 변경 사항을 시간순으로 기록한 log입니다.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

movement disorder data를 기록하고 query하는 manager입니다.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

1분 간격 동안 dyskinetic symptom이 있었을 가능성에 대한 data를 담는 result object입니다.

현재 페이지: CMTremorResult
