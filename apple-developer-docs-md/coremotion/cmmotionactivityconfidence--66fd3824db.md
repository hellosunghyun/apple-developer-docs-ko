---
title: "CMMotionActivityConfidence | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.907269+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMotionActivityConfidence

enum

CMMotionActivityConfidence
==========================

motion data가 정확하다는 confidence입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    enum CMMotionActivityConfidence

[주제](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#topics)

-------------------------------------------------------------------------------------------------

### [constant](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#Constants)

[`case low`](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/low)

confidence가 낮습니다.

[`case medium`](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/medium)

confidence가 양호합니다.

[`case high`](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/high)

confidence가 높습니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#relationships)

---------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#see-also)

-----------------------------------------------------------------------------------------------------

### [motion metadata 가져오기](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence#Getting-Metadata-for-the-Motion)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/startdate)

motion 변화가 발생한 시각입니다.

[`var confidence: CMMotionActivityConfidence`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/confidence)

motion type 평가에 대한 confidence입니다.

현재 페이지: CMMotionActivityConfidence
