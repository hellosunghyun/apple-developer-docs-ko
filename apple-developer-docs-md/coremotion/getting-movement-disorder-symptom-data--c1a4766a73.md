---
title: "Getting movement disorder symptom data | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891728+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   movement disorder symptom data 가져오기

Article

movement disorder symptom data 가져오기
======================================

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[개요](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#overview)

-----------------------------------------------------------------------------------------------------------------

[`CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
 class는 app에서 Parkinson병의 tremor 및 dyskinetic symptom을 지속적으로 측정하고 기록할 수 있도록 전력 효율적인 방법을 제공합니다.

movement disorder manager에서 data를 가져오기 시작하면 Apple Watch가 motion data를 수집하기 시작합니다. 배터리 수명을 보존하기 위해 manager는 real time으로 계산하지 않습니다. 대신 raw data를 주기적으로, 그리고 기회가 있을 때 분석하여 결과를 사용자의 device에 저장합니다. 디스크 공간을 보존하기 위해 manager는 결과를 7일 동안만 유지합니다. 이 기간 동안 manager를 사용해 결과를 query할 수 있습니다.

질환 감지와 기록의 과학적 검증 및 algorithm에 대한 자세한 내용은 [Smartwatch inertial sensors continuously monitor real-world motor fluctuations in Parkinson’s disease](http://stm.sciencemag.org/cgi/content/full/13/579/eabd7865?ijkey=Md/cIhqXrFvws&keytype=ref&siteid=scitransmed)
를 참고하거나 [Science Translational Medicine Magazine](https://stm.sciencemag.org/content/scitransmed/13/579/eabd7865.full.pdf?ijkey=Md/cIhqXrFvws&keytype=ref&siteid=scitransmed)
에서 PDF를 다운로드하세요.

`CMMovementDisorderManager`를 사용하는 app은 다음 요구 사항을 충족해야 합니다.

*   사용자의 Parkinson병 진단을 확인합니다.
    
*   clinician이 진단했거나 사용자가 직접 보고한 symptom만 보고합니다.
    
*   가장 큰 영향을 받는 팔에 Apple Watch를 착용하도록 사용자에게 안내해 가장 유용한 data를 수집하도록 합니다.
    

watchOS app에서 Parkinson tremor 또는 dyskinetic symptom data를 가져오려면 다음 단계를 따릅니다.

1.  WatchKit extension의 `Info.plist` file에 motion usage description을 제공합니다.
    
2.  [`CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
     object를 생성합니다.
    
3.  현재 device에서 movement disorder monitoring을 사용할 수 있는지 확인합니다.
    
4.  사용자 monitoring을 시작합니다.
    
5.  tremor 또는 dyskinetic symptom을 query합니다.
    

### [motion usage description 제공](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#Provide-the-motion-usage-description)

watchOS app은 WatchKit extension의 `Info.plist` file에 `String` value를 갖는 [NSMotionUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSMotionUsageDescription)
 key를 제공해야 합니다. system은 사용자의 data 기록 권한을 요청할 때마다 motion usage description을 표시합니다. 이 description string은 Motion and Fitness 권한 요청 prompt에 나타납니다.

최소한 description에는 다음 텍스트가 포함되어야 합니다. “또한 이 app은 사용자의 tremor 및 dyskinetic symptom data에 접근하려고 합니다. 이 기능은 이미 Parkinson’s disease 진단을 받은 사람만을 위한 용도입니다.”

이 텍스트 뒤에 사용자가 app에 권한을 부여해야 하는 이유와, app이 data를 어떻게 사용할 것인지 설명하는 추가 정보를 포함할 수 있습니다.

### [결과 모니터링 및 query](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#Monitor-and-query-for-results)

다음 예제는 movement disorder manager를 설정하고 사용자의 symptom 모니터링을 시작하는 방법을 보여줍니다.

    // movement disorder manager를 사용할 수 있는지 확인합니다.
    guard CMMovementDisorderManager.isAvailable() else {
        // 이 device에서는 movement disorder manager를 사용할 수 없습니다.
        return
    }
    
    
    // Movement Disorder Manager instance를 만듭니다.
    movementDisorderManager = CMMovementDisorderManager()
    
    
    // 사용자 monitoring을 시작합니다. 최대 기간은 7일입니다.
    movementDisorderManager.monitorKinesias(forDuration: 60.0 * 60.0 * 24.0 * 7.0)
    

monitoring을 시작하면 manager가 [`CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)
를 활용해 높은 sampling rate의 accelerometer data를 수동적으로 기록합니다. 활성화되면 [`CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)
는 100 Hz sample을 기록합니다. movement disorder algorithm은 이후 이 data를 주기적으로, 그리고 기회가 있을 때 사용해 tremor와 dyskinetic symptom을 계산합니다.

movement disorder manager는 이 계산 결과를 7일 동안 device에 저장합니다. 결과에 접근하려면 다음 예제처럼 manager를 사용해 원하는 결과를 query합니다.

    // 마지막 result batch의 종료 날짜를 가져옵니다.
    guard let endDate = movementDisorderManager.lastProcessedDate() else {
        // manager가 아직 result를 처리하지 않았습니다.
        return
    }
    
    
    // 마지막 tremor result batch를 가져옵니다.
    movementDisorderManager.queryTremor(from: previousDate, to: endDate) { (tremorResults, error) in
        
        // Check for errors.
        if let error = error {
            // Handle the error here.
            print("*** An error occurred: \(error.localizedDescription) ***")
            return
        }
        
        // Do something with the tremor results here.
    }
    
    
    // Get the last batch of dyskinetic symptom results.
    movementDisorderManager.queryDyskineticSymptom(from: previousDate, to: endDate) { (dyskineticSymptomResults, error) in
        
        // Check for errors.
        if let error = error {
            // Handle the error here.
            print("*** An error occurred: \(error.localizedDescription) ***")
            return
        }
        
        // Do something with the dyskinetic symptom results here.
    }
    
    
    previousDate = endDate
    

초기 만료 시점을 넘겨 monitoring을 연장하려면 [`monitorKinesias(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))
 method를 다시 호출합니다.

### [manager의 제한 사항 이해하기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#Understand-the-managers-limitations)

[`CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
는 3-7 Hz 범위의 Parkinson병 resting tremor를 측정합니다. resting tremor의 존재와 상대적 심각도에 대한 metric을 [`CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)
 object로 반환합니다. [`CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
는 choreiform dyskinetic symptom에 대한 metric도 계산하며, 사용자가 Apple Watch를 착용한 손목에서 관찰되는 dyskinetic symptom의 가능성 있는 존재 여부를 측정합니다. 결과는 [`CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)
 object로 반환합니다.

[`CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
는 다음 제약 조건에서 동작합니다.

*   사용자는 가장 큰 영향을 받는 팔에 Apple Watch를 착용해야 합니다.
    
*   dyskinetic symptom 추적은 영향을 받는 팔에 chorea가 있는 사용자에게만 사용해야 하며, 이는 사용자의 자가 보고이거나 clinician의 진단이어야 합니다.
    
*   tremor에는 여러 종류가 있습니다. movement disorder manager는 resting tremor를 명시적으로 추적하며 action tremor나 postural tremor는 추적하지 않고, finger tremor도 추적하지 못할 수 있습니다.
    
*   manager는 dystonia를 명시적으로 추적하지 않습니다.
    
*   결과에는 false positive와 false negative가 포함될 수 있습니다. 사용자의 활동, watch band 착용 상태, 동반 질환(예: restless legs syndrome 및 non-Parkinsonian tremor)이 결과 품질에 영향을 줄 수 있습니다.
    

manager는 Apple Watch를 착용한 손목의 symptom만 명시적으로 측정합니다. 하지만 Apple Watch는 영향을 받은 다른 신체 부위에서 몸을 통해 전달된 symptom도 감지할 수 있어, 오해를 부르거나 잘못된 metric이 생성될 수 있습니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#see-also)

-----------------------------------------------------------------------------------------------------------------

### [Movement disorder](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#Movement-disorder)

[movement disorder data collection requirements 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

사용자가 app이 수집하는 data를 이해하고 제어할 수 있도록 합니다.

[movement disorder algorithm 변경 기록](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

movement disorder algorithm의 주요 변경 사항을 시간순으로 기록한 로그입니다.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

movement disorder data를 기록하고 query하는 manager입니다.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

1분 간격 동안 tremor의 존재와 강도에 대한 data를 담는 result object입니다.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

1분 간격 동안 dyskinetic symptom의 가능성 있는 존재에 대한 data를 담는 result object입니다.

현재 페이지: Getting movement disorder symptom data
