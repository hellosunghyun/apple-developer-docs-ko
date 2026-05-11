---
title: "isMagnetometerActive | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.889424+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   isMagnetometerActive

instance property

isMagnetometerActive
====================

magnetometer update가 현재 진행 중인지 판단하는 Boolean 값입니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+watchOS 2.0+

    var isMagnetometerActive: Bool { get }

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive#Discussion)

-------------------------------------------------------------------------------------------------------------------

이 property는 마지막으로 [`stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())
method를 호출한 이후 [`startMagnetometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))
또는 [`startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())
method를 호출했는지 나타냅니다. (start method를 호출하지 않았더라도, 예를 들어 [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
를 호출한 뒤 app이 magnetometer update를 받을 수는 있지만 이 property는 [`false`](https://developer.apple.com/documentation/Swift/false)
를 반환합니다.)

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive#see-also)

---------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive#Related-Documentation)

[`var isMagnetometerAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeravailable)

device에서 magnetometer를 사용할 수 있는지 나타내는 Boolean 값입니다.

### [활성 service 확인하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive#Determining-Which-Services-Are-Active)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)

app이 device-motion service로부터 update를 받고 있는지 판단하는 Boolean 값입니다.

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive)

accelerometer update가 현재 진행 중인지 나타내는 Boolean 값입니다.

[`var isGyroActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive)

gyroscope update가 현재 진행 중인지 판단하는 Boolean 값입니다.

현재 페이지: isMagnetometerActive
