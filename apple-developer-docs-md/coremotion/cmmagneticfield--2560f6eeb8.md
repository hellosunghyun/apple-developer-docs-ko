---
title: "CMMagneticField | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmagneticfield"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.873552+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmagneticfield#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMagneticField

struct

CMMagneticField
===============

3축 magnetometer data를 담는 structure입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    struct CMMagneticField

[주제](https://developer.apple.com/documentation/coremotion/cmmagneticfield#topics)

--------------------------------------------------------------------------------------

### [field 값 가져오기](https://developer.apple.com/documentation/coremotion/cmmagneticfield#Getting-the-Field-Values)

[`var x: Double`](https://developer.apple.com/documentation/coremotion/cmmagneticfield/x)

microtesla 단위의 X축 magnetic field입니다.

[`var y: Double`](https://developer.apple.com/documentation/coremotion/cmmagneticfield/y)

microtesla 단위의 Y축 magnetic field입니다.

[`var z: Double`](https://developer.apple.com/documentation/coremotion/cmmagneticfield/z)

microtesla 단위의 Z축 magnetic field입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmmagneticfield#Initializers)

[`init()`](https://developer.apple.com/documentation/coremotion/cmmagneticfield/init())

[`init(x: Double, y: Double, z: Double)`](https://developer.apple.com/documentation/coremotion/cmmagneticfield/init(x:y:z:))

[관계](https://developer.apple.com/documentation/coremotion/cmmagneticfield#relationships)

----------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmmagneticfield#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmagneticfield#see-also)

------------------------------------------------------------------------------------------

### [field 세기 가져오기](https://developer.apple.com/documentation/coremotion/cmmagneticfield#Getting-the-Field-Strength)

[`var magneticField: CMMagneticField`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield)

magnetometer가 측정한 magnetic field를 반환합니다.

현재 페이지: CMMagneticField
