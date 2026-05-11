---
title: "CMAttitudeReferenceFrame | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.869433+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAttitudeReferenceFrame

구조

CMAttitudeReferenceFrame
========================

attitude 관련 motion data의 기준 좌표계를 나타내는 constant입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    struct CMAttitudeReferenceFrame

[개요](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#overview)

---------------------------------------------------------------------------------------------------

3차원 공간에서 device의 attitude를 보고하는 service를 시작하면 Core Motion이 pitch, roll, yaw 값을 보고할 기준 좌표계를 설정합니다. 이후의 모든 data 값은 이 기준 좌표계에 대한 device attitude를 나타냅니다. 현재 device에서 사용할 수 있는 기준 좌표계 목록을 가져오려면 [`availableAttitudeReferenceFrames()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/availableattitudereferenceframes())
 class method를 호출합니다.

service를 시작할 때는 현재 device에서 사용할 수 있는 기준 좌표계를 지정해야 합니다. 기준 좌표계를 명시적으로 지정할 수 없는 service는 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 의 [`attitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe)
 property 값을 사용합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#topics)

-----------------------------------------------------------------------------------------------

### [기준 좌표계 가져오기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#Getting-the-reference-frames)

[`static var xArbitraryZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)

Z축이 수직이고 X축이 수평면의 임의 방향을 가리키는 기준 좌표계입니다.

[`static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)

Z축이 수직이며 회전 정확도가 향상되고, X축이 수평면의 임의 방향을 가리키는 기준 좌표계입니다.

[`static var xMagneticNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical)

Z축이 수직이고 X축이 자북을 가리키는 기준 좌표계입니다.

[`static var xTrueNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical)

Z축이 수직이고 X축이 진북을 가리키는 기준 좌표계입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#initializers)

[`init(rawValue: UInt)`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#relationships)

-------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`ExpressibleByArrayLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByArrayLiteral)
    
*   [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    
*   [`SetAlgebra`](https://developer.apple.com/documentation/Swift/SetAlgebra)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#see-also)

---------------------------------------------------------------------------------------------------

### [Device motion](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe#Device-motion)

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

gravity의 영향 같은 환경 bias를 제거하도록 system이 처리한 motion data를 가져옵니다.

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

device의 attitude, rotation rate, acceleration 측정값을 캡슐화한 class입니다.

[`class CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)

특정 시점의 알려진 기준 좌표계에 대한 device 방향입니다.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

headphone motion service를 시작하고 관리하는 object입니다.

현재 페이지: CMAttitudeReferenceFrame
