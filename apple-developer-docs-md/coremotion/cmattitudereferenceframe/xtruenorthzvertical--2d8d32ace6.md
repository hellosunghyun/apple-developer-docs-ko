---
title: "xTrueNorthZVertical | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.886395+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAttitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)
    
*   xTrueNorthZVertical

type property

xTrueNorthZVertical
===================

Z축이 수직이고 X축이 지리적 북극을 가리키는 reference frame입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    static var xTrueNorthZVertical: CMAttitudeReferenceFrame { get }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical#mentions)

---------------------------------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[논의](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical#Discussion)

---------------------------------------------------------------------------------------------------------------------------

이 option은 기기의 attitude를 true north 기준으로 확인할 때 사용합니다. 예를 들어 더 정밀한 navigation을 구현할 때 유용합니다. [`CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)
의 [`yaw`](https://developer.apple.com/documentation/coremotion/cmattitude/yaw)
 (Z-axis) 값은 X축이 true north와 정렬되면 `0`입니다.

기기에는 magnetometer가 있어야 하고 해당 sensor를 사용할 수 있어야 합니다. magnetic north와 true north의 차이를 계산하려면 location service도 사용할 수 있어야 합니다. magnetometer가 현재 calibration되지 않았다면, Core Motion이 사용자가 기기를 움직여 calibration하도록 안내합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [Getting the reference frames](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical#Getting-the-reference-frames)

[`static var xArbitraryZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)

Z축이 수직이고 X축이 수평면에서 임의의 방향을 가리키는 reference frame입니다.

[`static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)

Z축이 수직이며 rotation 정확도가 개선되었고, X축이 수평면에서 임의의 방향을 가리키는 reference frame입니다.

[`static var xMagneticNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical)

Z축이 수직이고 X축이 자북을 가리키는 reference frame입니다.

현재 페이지: xTrueNorthZVertical
