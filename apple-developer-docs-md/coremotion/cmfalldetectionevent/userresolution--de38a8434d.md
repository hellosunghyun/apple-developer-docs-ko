---
title: "CMFallDetectionEvent.UserResolution | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.915484+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionEvent](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)
    
*   CMFallDetectionEvent.UserResolution

enum

CMFallDetectionEvent.UserResolution
===================================

fall detection event에 대한 user resolution입니다.

watchOS 7.2+

    enum UserResolution

[개요](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#overview)

--------------------------------------------------------------------------------------------------------------

event의 resolution은 fall detection notification에 대한 user의 동작을 반영합니다. 예를 들어 user는 notification 안에서 버튼을 탭해 응답할 수 있고, Digital Crown을 눌러 notification을 닫을 수도 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#topics)

----------------------------------------------------------------------------------------------------------

### [Resolutions](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#Resolutions)

[`case confirmed`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/confirmed)

user가 event를 확인했습니다.

[`case dismissed`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/dismissed)

user가 fall event alert를 닫았지만, event를 명시적으로 확인하거나 거부하지는 않았습니다.

[`case rejected`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/rejected)

user가 fall event를 거부했습니다.

[`case unresponsive`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/unresponsive)

user가 fall event에 응답하지 않았고, system도 회복 동작을 감지하지 못했습니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#relationships)

------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#see-also)

--------------------------------------------------------------------------------------------------------------

### [Accessing Fall Data](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution#Accessing-Fall-Data)

[`var resolution: CMFallDetectionEvent.UserResolution`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution)

event의 resolution입니다.

현재 페이지: CMFallDetectionEvent.UserResolution
