---
title: "xArbitraryCorrectedZVertical | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.883321+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAttitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)
    
*   xArbitraryCorrectedZVertical

type property

xArbitraryCorrectedZVertical
============================

Z축이 수직이고 회전 정확도가 향상되며, X축이 수평면의 임의 방향을 가리키는 reference frame입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical#mentions)

------------------------------------------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[논의](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical#Discussion)

------------------------------------------------------------------------------------------------------------------------------------

device-motion service를 시작하면 Core Motion은 현재 device orientation을 사용해 초기 reference frame을 설정합니다. device의 attitude를 true north 또는 magnetic north를 기준으로 알 필요는 없고, 시간에 따른 회전 변화만 추적하면 될 때 이 option을 사용할 수 있습니다.

이 option은 magnetometer를 사용해 z축(yaw) 측정의 장기 정확도를 높입니다. device에는 magnetometer가 있어야 하고, 해당 sensor를 사용할 수 있으며 calibration도 완료되어야 합니다.

이 option은 [`xArbitraryZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)
 option보다 CPU를 더 사용합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical#see-also)

--------------------------------------------------------------------------------------------------------------------------------

### [Getting the reference frames](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical#Getting-the-reference-frames)

[`static var xArbitraryZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)

Z축이 수직이고 X축이 수평면의 임의 방향을 가리키는 reference frame입니다.

[`static var xMagneticNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical)

Z축이 수직이고 X축이 자기 북극을 가리키는 reference frame입니다.

[`static var xTrueNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical)

Z축이 수직이고 X축이 지리적 북극을 가리키는 reference frame입니다.

현재 페이지: xArbitraryCorrectedZVertical
