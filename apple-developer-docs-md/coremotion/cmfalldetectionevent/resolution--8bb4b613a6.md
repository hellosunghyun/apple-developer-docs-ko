---
title: "resolution | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.915376+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionEvent](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)
    
*   resolution

instance property

resolution
==========

event의 resolution입니다.

watchOS 7.2+

    var resolution: CMFallDetectionEvent.UserResolution { get }

[설명](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution#Discussion)

--------------------------------------------------------------------------------------------------------------

event의 resolution은 fall detection 알림에 대한 사용자의 응답 동작을 반영합니다. 예를 들어 사용자는 알림 안의 버튼을 탭해 응답하거나, digital crown을 눌러 알림을 닫을 수 있습니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution#see-also)

----------------------------------------------------------------------------------------------------------

### [Fall data에 접근하기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution#Accessing-Fall-Data)

[`enum UserResolution`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution)

fall detection event에 대한 user resolution입니다.

현재 페이지: resolution
