---
title: "Movement disorder algorithm changelog | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891931+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   Movement disorder algorithm changelog

문서

Movement disorder algorithm changelog
=====================================

movement disorder algorithm의 주요 변경 사항을 시간순으로 정리한 기록입니다.

[개요](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#overview)

----------------------------------------------------------------------------------------------------------------

movement disorder algorithm은 Parkinson’s disease의 tremor와 dyskinetic symptom을 측정하고 기록합니다. 이 data를 받아 사용하는 방법은 [movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)
를 참고하세요.

### [미출시](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#Unreleased)

*   algorithm의 현재 version을 확인하는 [`version()`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version())
     method를 watchOS 9에서 사용할 수 있습니다.
    

### [1.0.0 — 2018-07-17](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#100-2018-07-17)

#### [추가됨](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#Added)

*   watchOS 5 이상에서 사용하는 algorithm을 공개했습니다.
    

[참고 항목](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#see-also)

----------------------------------------------------------------------------------------------------------------

### [Movement disorder](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog#Movement-disorder)

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[movement disorder data collection requirement 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

사용자가 app이 수집하는 data를 이해하고 제어할 수 있게 합니다.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

movement disorder data를 기록하고 query하는 manager입니다.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

1분 간격 동안 tremor의 존재 여부와 강도에 관한 data를 담은 result object입니다.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

1분 간격 동안 dyskinetic symptom이 존재할 가능성에 관한 data를 담은 result object입니다.

현재 페이지는 Movement disorder algorithm changelog입니다
