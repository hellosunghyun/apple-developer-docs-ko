---
title: "CMWaterSubmersionEvent.State | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.879202+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionEvent](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)
    
*   CMWaterSubmersionEvent.State

enum

CMWaterSubmersionEvent.State
============================

device의 submersion state입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 4.0+visionOS 1.0+watchOS 2.0+

    enum State

[주제](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#topics)

--------------------------------------------------------------------------------------------------------------

### [Submersion states](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#Submersion-states)

[`case notSubmerged`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum/notsubmerged)

device가 물에 잠기지 않은 상태입니다.

[`case submerged`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum/submerged)

device가 물에 잠긴 상태입니다.

[`case unknown`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum/unknown)

submersion state를 알 수 없습니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#relationships)

----------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#see-also)

------------------------------------------------------------------------------------------------------------------

### [Accessing event data](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum#Accessing-event-data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/date)

event의 시간과 날짜입니다.

[`var state: CMWaterSubmersionEvent.State`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.property)

새로운 submersion state입니다.

현재 페이지: CMWaterSubmersionEvent.State
