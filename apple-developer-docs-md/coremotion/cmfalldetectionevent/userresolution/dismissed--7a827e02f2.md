---
title: "CMFallDetectionEvent.UserResolution.dismissed | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.916078+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionEvent](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)
    
*   *   [CMFallDetectionEvent](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)
        
*   [CMFallDetectionEvent.UserResolution](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution)
    
*   CMFallDetectionEvent.UserResolution.dismissed

케이스

CMFallDetectionEvent.UserResolution.dismissed
=============================================

사용자가 fall event alert를 닫았지만, event를 명시적으로 확인하거나 거부하지는 않았음을 나타냅니다.

watchOS 7.2+

    case dismissed

[설명](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed#Discussion)

----------------------------------------------------------------------------------------------------------------------------

사용자는 Digital Crown을 누르거나 닫기 버튼을 탭해 alert를 닫을 수 있습니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed#see-also)

------------------------------------------------------------------------------------------------------------------------

### [Resolution](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed#Resolutions)

[`case confirmed`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/confirmed)

사용자가 event를 확인했습니다.

[`case rejected`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/rejected)

사용자가 fall event를 거부했습니다.

[`case unresponsive`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/unresponsive)

사용자가 fall event에 응답하지 않았고 system도 회복 동작을 감지하지 못했습니다.

현재 페이지는 CMFallDetectionEvent.UserResolution.dismissed입니다.
