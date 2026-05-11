---
title: "attitudeReferenceFrame | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.889525+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   attitudeReferenceFrame

instance property

attitudeReferenceFrame
======================

현재 사용 중인 reference frame 또는 기본 attitude reference frame을 반환합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var attitudeReferenceFrame: CMAttitudeReferenceFrame { get }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe#mentions)

---------------------------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe#Discussion)

---------------------------------------------------------------------------------------------------------------------

device-motion service가 활성 상태이면 이 property는 현재 사용 중인 reference frame을 반환합니다. service가 비활성 상태더라도 app이 launch 이후 한 번이라도 이 service를 시작했다면 이 property에는 마지막으로 사용한 reference frame이 들어 있습니다. app launch 이후 device-motion service를 시작한 적이 없다면 이 property는 기본 frame of reference인 [`xArbitraryZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)
를 반환합니다.

현재 device에서 device motion을 사용할 수 없다면 이 property의 값은 정의되지 않습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe#see-also)

-----------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe#Related-Documentation)

[`var isDeviceMotionAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable)

device에서 device-motion service를 사용할 수 있는지를 나타내는 Boolean 값입니다.

### [Attitude Reference Frame에 접근하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe#Accessing-Attitude-Reference-Frames)

[`class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/availableattitudereferenceframes())

현재 device의 attitude를 보고하는 데 사용할 수 있는 reference frame의 bitmask를 반환합니다.

현재 페이지: attitudeReferenceFrame
