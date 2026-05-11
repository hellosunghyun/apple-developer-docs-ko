---
title: "isGyroActive | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.886301+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   isGyroActive

instance property

isGyroActive
============

현재 gyroscope update가 진행 중인지 나타내는 Boolean 값입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var isGyroActive: Bool { get }

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive#Discussion)

-----------------------------------------------------------------------------------------------------------

이 property는 마지막으로 [`stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())
가 호출된 이후 [`startGyroUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))
 또는 [`startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())
가 호출되었는지를 나타냅니다. (start method를 호출하지 않았더라도 app은 예를 들어 [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
를 호출한 뒤 gyroscope에서 update를 받고 있을 수 있지만, 이 property는 [`false`](https://developer.apple.com/documentation/Swift/false)
를 반환합니다.)

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive#see-also)

-------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive#Related-Documentation)

[`var isGyroAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroavailable)

device에서 gyroscope를 사용할 수 있는지를 나타내는 Boolean 값입니다.

### [어떤 service가 활성 상태인지 확인하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive#Determining-Which-Services-Are-Active)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)

app이 device-motion service에서 update를 받고 있는지를 나타내는 Boolean 값입니다.

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive)

현재 accelerometer update가 진행 중인지를 나타내는 Boolean 값입니다.

[`var isMagnetometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive)

현재 magnetometer update가 진행 중인지 판단하는 Boolean 값입니다.

현재 페이지: isGyroActive
