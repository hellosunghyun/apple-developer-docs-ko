---
title: "Adhering to the movement disorder data collection requirements | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891828+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   movement disorder data collection requirements 준수하기

문서

movement disorder data collection requirements 준수하기
======================================================

app이 수집하는 data를 사용자가 이해하고 제어할 수 있도록 합니다.

[개요](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements#overview)

-----------------------------------------------------------------------------------------------------------------------------------------

movement disorder API를 사용할 때는 app이 data collection을 투명하게 처리하는 것이 매우 중요합니다. app에는 data 사용 정책을 설명하는 소개 화면이 있어야 합니다. 또한 일부 data type에는 특정 고지가 필요합니다.

### [app의 data 사용 정책 설명하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements#Explain-your-apps-data-use-policy)

movement disorder monitoring을 수행하는 app은 사용자가 app을 처음 실행할 때 소개 화면을 표시해야 합니다. 이 화면에는 다음 내용을 설명해야 합니다.

*   app의 목적과 대상 사용자
    
*   movement disorder monitoring 중 app이 수집하는 data
    
*   data를 사용할 계획
    
*   app이 background에서 실행되는 동안에도 data를 수집하는지 여부
    
*   나중에 data collection을 거부하는 방법
    

### [필수 고지 포함하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements#Include-required-disclosures)

일부 data type의 경우 app은 소개 화면에 추가 텍스트를 포함해야 합니다. 다음 각 상황에 대해 지정된 텍스트를 추가합니다.

휴식기 tremor data

“This app is monitoring and collecting your Parkinsonian resting tremor data, only if you self-report or have been clinically diagnosed with resting tremor, and indicate within the app that this is true.”

무도병성 dyskinesia data

“This app is monitoring and collecting your choreiform dyskinesia data, only if you self-report or have been clinically diagnosed with choreiform dyskinesias, and indicate within the app that this is true.”

background의 movement disorder data

“This app is able to collect your movement disorder data even when the app is not active, on screen, or responding to your user input.”

[관련 항목](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------

### [Movement disorder](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements#Movement-disorder)

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[movement disorder algorithm 변경 내역](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

movement disorder algorithm의 주요 변경 사항을 시간순으로 기록한 로그입니다.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

movement disorder data를 기록하고 query하는 manager입니다.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

1분 간격 동안 tremor의 존재 여부와 강도에 관한 data를 담는 result object입니다.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

1분 간격 동안 운동이상 증상의 존재 가능성에 관한 data를 담는 result object입니다.

현재 페이지는 movement disorder data collection requirements 준수하기입니다.
