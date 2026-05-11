---
title: "xArbitraryZVertical | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.880052+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAttitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)
    
*   xArbitraryZVertical

type property

xArbitraryZVertical
===================

Z축은 수직이고 X축은 수평면의 임의 방향을 가리키는 reference frame입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    static var xArbitraryZVertical: CMAttitudeReferenceFrame { get }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical#mentions)

---------------------------------------------------------------------------------------------------------------------------

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[설명](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical#Discussion)

---------------------------------------------------------------------------------------------------------------------------

device-motion service를 시작하면 Core Motion이 reference frame을 device의 초기 orientation으로 설정합니다. device의 attitude를 true north나 magnetic north 기준으로 알 필요 없이, 시간에 따른 rotation 변화만 추적하면 되는 경우 이 옵션을 사용할 수 있습니다.

이 옵션은 device attitude를 결정할 때 더 적은 sensor를 사용하므로 [`xArbitraryCorrectedZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)
 옵션보다 전력 효율이 더 높습니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [reference frame 가져오기](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical#Getting-the-reference-frames)

[`static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)

Z축은 수직이고 rotation 정확도가 향상되며, X축은 수평면의 임의 방향을 가리키는 reference frame입니다.

[`static var xMagneticNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical)

Z축은 수직이고 X축은 지구의 magnetic north pole을 가리키는 reference frame입니다.

[`static var xTrueNorthZVertical: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical)

Z축은 수직이고 X축은 지리적 북극을 가리키는 reference frame입니다.

현재 페이지: xArbitraryZVertical
