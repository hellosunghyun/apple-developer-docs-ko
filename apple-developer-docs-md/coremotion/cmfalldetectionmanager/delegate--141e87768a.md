---
title: "delegate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/delegate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899904+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/delegate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionManager](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)
    
*   delegate

instance property

delegate
========

fall detection event에 대한 알림을 받을 수 있는 delegate입니다.

watchOS 7.2+

    weak var delegate: (any CMFallDetectionDelegate)? { get set }

[관련 항목](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/delegate#see-also)

----------------------------------------------------------------------------------------------------------

### [event 처리](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/delegate#Handling-Events)

[`protocol CMFallDetectionDelegate`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)

fall detection event와 authorization status 변경에 대한 정보를 받는 delegate입니다.

현재 페이지는 delegate입니다.
