---
title: "unknown | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.887046+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity)
    
*   unknown

instance property

unknown
=======

motion 유형을 알 수 없는지 나타내는 Boolean 값입니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+macOS 15.0+watchOS 2.0+

    var unknown: Bool { get }

[설명](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown#Discussion)

-------------------------------------------------------------------------------------------------------

현재 motion 유형을 추정할 수 없으면 이 property는 [`true`](https://developer.apple.com/documentation/Swift/true)입니다. 예를 들어 device가 최근 켜졌고 motion 유형을 판단할 만큼 충분한 motion data가 아직 수집되지 않았다면 이 값이 [`true`](https://developer.apple.com/documentation/Swift/true)일 수 있습니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown#see-also)

---------------------------------------------------------------------------------------------------

### [motion 유형 가져오기](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown#Getting-the-Type-of-Motion)

[`var stationary: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/stationary)

device가 정지 상태인지 나타내는 Boolean 값입니다.

[`var walking: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/walking)

device가 걷고 있는 사람에게 있는지 나타내는 Boolean 값입니다.

[`var running: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/running)

device가 뛰고 있는 사람에게 있는지 나타내는 Boolean 값입니다.

[`var automotive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/automotive)

device가 자동차 안에 있는지 나타내는 Boolean 값입니다.

[`var cycling: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/cycling)

device가 자전거에 있는지 나타내는 Boolean 값입니다.

현재 페이지는 unknown입니다.
