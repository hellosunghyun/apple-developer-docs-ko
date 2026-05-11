---
title: "CMAcceleration | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmacceleration"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.872912+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmacceleration#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAcceleration

struct

CMAcceleration
==============

3축 acceleration 값을 포함하는 structure type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    struct CMAcceleration

[개요](https://developer.apple.com/documentation/coremotion/cmacceleration#overview)

-----------------------------------------------------------------------------------------

G는 지구 중력장(9.81 m s−2)이 가하는 힘과 같은 중력 단위입니다.

[주제](https://developer.apple.com/documentation/coremotion/cmacceleration#topics)

-------------------------------------------------------------------------------------

### [initializer](https://developer.apple.com/documentation/coremotion/cmacceleration#Initializers)

[`init()`](https://developer.apple.com/documentation/coremotion/cmacceleration/init())

[`init(x: Double, y: Double, z: Double)`](https://developer.apple.com/documentation/coremotion/cmacceleration/init(x:y:z:))

### [Acceleration 값 가져오기](https://developer.apple.com/documentation/coremotion/cmacceleration#Getting-the-Acceleration-Values)

[`var x: Double`](https://developer.apple.com/documentation/coremotion/cmacceleration/x)

G(중력) 단위의 X축 acceleration입니다.

[`var y: Double`](https://developer.apple.com/documentation/coremotion/cmacceleration/y)

G(중력) 단위의 Y축 acceleration입니다.

[`var z: Double`](https://developer.apple.com/documentation/coremotion/cmacceleration/z)

G(중력) 단위의 Z축 acceleration입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmacceleration#relationships)

---------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmacceleration#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmacceleration#see-also)

-----------------------------------------------------------------------------------------

### [Accelerometer data에 접근하기](https://developer.apple.com/documentation/coremotion/cmacceleration#Accessing-Accelerometer-Data)

[`var acceleration: CMAcceleration`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata/acceleration)

accelerometer가 측정한 acceleration입니다.

현재 페이지: CMAcceleration
