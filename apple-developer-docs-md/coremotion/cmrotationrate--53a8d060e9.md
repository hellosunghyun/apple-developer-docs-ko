---
title: "CMRotationRate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmrotationrate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.881056+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmrotationrate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMRotationRate

struct

CMRotationRate
==============

rotation rate 측정값을 나타내는 struct type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    struct CMRotationRate

[주제](https://developer.apple.com/documentation/coremotion/cmrotationrate#topics)

-------------------------------------------------------------------------------------

### [Rotation Rate 가져오기](https://developer.apple.com/documentation/coremotion/cmrotationrate#Getting-the-Rotation-Rates)

[`var x: Double`](https://developer.apple.com/documentation/coremotion/cmrotationrate/x)

X축 값입니다.

[`var y: Double`](https://developer.apple.com/documentation/coremotion/cmrotationrate/y)

Y축 값입니다.

[`var z: Double`](https://developer.apple.com/documentation/coremotion/cmrotationrate/z)

Z축 값입니다.

### [이니셜라이저](https://developer.apple.com/documentation/coremotion/cmrotationrate#Initializers)

[`init()`](https://developer.apple.com/documentation/coremotion/cmrotationrate/init())

[`init(x: Double, y: Double, z: Double)`](https://developer.apple.com/documentation/coremotion/cmrotationrate/init(x:y:z:))

[관계](https://developer.apple.com/documentation/coremotion/cmrotationrate#relationships)

---------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmrotationrate#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmrotationrate#see-also)

-----------------------------------------------------------------------------------------

### [Rotation Rate 가져오기](https://developer.apple.com/documentation/coremotion/cmrotationrate#Getting-the-Rotation-Rate)

[`var rotationRate: CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate)

device의 gyroscope가 측정한 rotation rate입니다.

[`class CMRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrotationratedata)

단일 rotation-rate 측정값을 담는 data object입니다.

[`class CMRecordedRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)

특정 시점의 단일 rotation-rate 측정값을 담는 data object입니다.

현재 페이지는 CMRotationRate입니다
