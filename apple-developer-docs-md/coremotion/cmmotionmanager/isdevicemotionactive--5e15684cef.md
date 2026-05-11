---
title: "isDeviceMotionActive | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.883221+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   isDeviceMotionActive

instance property

isDeviceMotionActive
====================

app이 device-motion service에서 update를 받고 있는지 판단하는 Boolean 값입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var isDeviceMotionActive: Bool { get }

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive#Discussion)

-------------------------------------------------------------------------------------------------------------------

이 property는 마지막으로 [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
를 호출한 이후에 [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))
 또는 [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
가 호출되었는지 나타냅니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive#see-also)

---------------------------------------------------------------------------------------------------------------

### [Related Documentation](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive#Related-Documentation)

[`var isDeviceMotionAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable)

device에서 device-motion service를 사용할 수 있는지 나타내는 Boolean 값입니다.

### [Determining Which Services Are Active](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive#Determining-Which-Services-Are-Active)

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive)

현재 accelerometer update가 진행 중인지 나타내는 Boolean 값입니다.

[`var isGyroActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive)

현재 gyroscope update가 진행 중인지 판단하는 Boolean 값입니다.

[`var isMagnetometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive)

현재 magnetometer update가 진행 중인지 판단하는 Boolean 값입니다.

현재 페이지는 isDeviceMotionActive입니다
