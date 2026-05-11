---
title: "CMFallDetectionDelegate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.897664+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMFallDetectionDelegate

protocol

CMFallDetectionDelegate
=======================

낙상 감지 event와 authorization status 변경 정보를 받는 delegate입니다.

watchOS 7.2+

    protocol CMFallDetectionDelegate : NSObjectProtocol

[주제](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#topics)

----------------------------------------------------------------------------------------------

### [낙상 감지하기](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#Detecting-Falls)

[`func fallDetectionManager(CMFallDetectionManager, didDetect: CMFallDetectionEvent, completionHandler: () -> Void)`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:))

낙상 감지 event가 발생했음을 나타냅니다.

### [authorization 변경 감지하기](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#Detecting-Authorization-Changes)

[`func fallDetectionManagerDidChangeAuthorization(CMFallDetectionManager)`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization(_:))

낙상 감지 authorization status가 변경되었음을 나타냅니다.

[관계](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#relationships)

------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#inherits-from)

*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#see-also)

--------------------------------------------------------------------------------------------------

### [낙상 감지](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate#Fall-detection)

[`class CMFallDetectionManager`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)

낙상 감지 event를 관리하는 object입니다.

[`class CMFallDetectionEvent`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)

낙상 감지 event에 관한 data를 담은 object입니다.

[`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription)

낙상 감지 event data 접근 permission을 app이 요청하는 이유를 사용자에게 설명하는 메시지입니다.

현재 페이지: CMFallDetectionDelegate
