---
title: "monitorKinesiasExpirationDate() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.909561+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   monitorKinesiasExpirationDate()

instance method

monitorKinesiasExpirationDate()
===============================

가장 최근 monitoring period의 expiration date를 반환합니다.

watchOS 5.0+

    func monitorKinesiasExpirationDate() -> Date?

[Return Value](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate()#return-value)

--------------------------------------------------------------------------------------------------------------------------------------------

현재 expiration date입니다. 아직 monitoring을 시작하지 않았다면 `nil`을 반환합니다.

[논의](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate()#Discussion)

----------------------------------------------------------------------------------------------------------------------------------------

이 date는 [`monitorKinesias(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))
 method를 호출할 때 설정됩니다. [`monitorKinesias(forDuration:)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))
를 다시 호출하면 이 date를 연장할 수 있지만, monitoring duration을 줄일 수는 없습니다.

expiration date를 사용하면 현재 user를 monitoring 중인지 판단할 수 있습니다.

    guard let experiationDate = movementDisorderManager.monitorKinesiasExpirationDate() else {
        // 아직 user monitoring을 시작하지 않았습니다.
        return
    }
    
    
    if experiationDate > Date() {
        // 현재 user를 monitoring 중입니다.
    } else {
        // monitoring period가 종료되었습니다.
    }
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate()#see-also)

------------------------------------------------------------------------------------------------------------------------------------

### [Movement Disorder 기록하기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate()#Recording-Movement-Disorders)

[`func monitorKinesias(forDuration: TimeInterval)`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))

지정한 time interval 동안 tremor 및 dyskinetic symptom result를 계산하고 저장합니다.

현재 페이지: monitorKinesiasExpirationDate()
