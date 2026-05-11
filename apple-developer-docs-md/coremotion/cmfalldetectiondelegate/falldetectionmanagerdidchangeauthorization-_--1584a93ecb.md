---
title: "fallDetectionManagerDidChangeAuthorization(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization(_:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.914331+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization(_:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionDelegate](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)
    
*   fallDetectionManagerDidChangeAuthorization(_:)

instance method

fallDetectionManagerDidChangeAuthorization(_:)
===============================================

fall detection authorization status가 변경되었음을 나타냅니다.

watchOS 7.2+

    optional func fallDetectionManagerDidChangeAuthorization(_ fallDetectionManager: CMFallDetectionManager)

[파라미터](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization(_:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------

`fallDetectionManager`

이 event의 fall detection manager입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization(_:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------------

system은 fall detection authorization status가 바뀐 뒤 이 method를 호출합니다. 현재 status는 fall detection manager의 [`authorizationStatus`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus) property로 확인합니다.

현재 페이지는 fallDetectionManagerDidChangeAuthorization(_)입니다.
