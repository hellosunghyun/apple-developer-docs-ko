---
title: "isAccelerometerActive | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.886079+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   isAccelerometerActive

instance property

isAccelerometerActive
=====================

accelerometer update가 현재 진행 중인지 나타내는 Boolean 값입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var isAccelerometerActive: Bool { get }

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive#Discussion)

--------------------------------------------------------------------------------------------------------------------

이 property는 마지막으로 [`stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())
를 호출한 이후에 [`startAccelerometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))
또는 [`startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())
를 호출했는지 나타냅니다. start method를 호출하지 않았더라도, 예를 들어 [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
를 호출한 뒤 app이 accelerometer에서 update를 받고 있을 수는 있지만, 이 property는 [`false`](https://developer.apple.com/documentation/Swift/false)
를 반환합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive#see-also)

----------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive#Related-Documentation)

[`var isAccelerometerAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeravailable)

device에서 accelerometer를 사용할 수 있는지 나타내는 Boolean 값입니다.

### [활성 상태인 service 확인하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive#Determining-Which-Services-Are-Active)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)

app이 device-motion service에서 update를 받고 있는지 확인하는 Boolean 값입니다.

[`var isGyroActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive)

gyroscope update가 현재 진행 중인지 확인하는 Boolean 값입니다.

[`var isMagnetometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive)

magnetometer update가 현재 진행 중인지 확인하는 Boolean 값입니다.

현재 페이지: isAccelerometerActive
