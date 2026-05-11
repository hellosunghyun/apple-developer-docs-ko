---
title: "xMagneticNorthZVertical | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.886198+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAttitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)
    
*   xMagneticNorthZVertical

type property

xMagneticNorthZVertical
=======================

Z축은 수직이고 X축은 자북을 가리키는 reference frame입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    static var xMagneticNorthZVertical: CMAttitudeReferenceFrame { get }

[언급된 항목](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical#mentions)

-------------------------------------------------------------------------------------------------------------------------------

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[설명](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical#Discussion)

-------------------------------------------------------------------------------------------------------------------------------

이 option을 사용하면 자북을 기준으로 device의 attitude를 판단할 수 있습니다. 예를 들어 app에 나침반 기능을 구현할 때 사용할 수 있습니다. [`CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)
의 [`yaw`](https://developer.apple.com/documentation/coremotion/cmattitude/yaw)
(Z-axis) 값은 X축이 자북과 정렬될 때 `0`입니다.

device에는 magnetometer가 있어야 하며 해당 sensor를 사용할 수 있어야 합니다. magnetometer가 현재 calibration되지 않았다면 Core Motion이 사용자가 device를 움직여 calibration하도록 안내합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical#see-also)

---------------------------------------------------------------------------------------------------------------------------

### [reference frame 가져오기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical#Getting-the-reference-frames)

[`static var xArbitraryZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)

Z축은 수직이고 X축은 수평면에서 임의 방향을 가리키는 reference frame입니다.

[`static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)

Z축은 수직이며 회전 정확도가 향상되어 있고, X축은 수평면에서 임의 방향을 가리키는 reference frame입니다.

[`static var xTrueNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical)

Z축은 수직이고 X축은 진북을 가리키는 reference frame입니다.

현재 페이지: xMagneticNorthZVertical
