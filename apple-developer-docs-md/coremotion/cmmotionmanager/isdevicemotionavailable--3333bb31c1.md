---
title: "isDeviceMotionAvailable | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.879640+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   isDeviceMotionAvailable

instance property

isDeviceMotionAvailable
=======================

device-motion service를 device에서 사용할 수 있는지 나타내는 Boolean value입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var isDeviceMotionAvailable: Bool { get }

[언급 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable#mentions)

----------------------------------------------------------------------------------------------------------------------

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable#Discussion)

----------------------------------------------------------------------------------------------------------------------

device-motion service는 device에 accelerometer와 gyroscope가 모두 있을 때 사용할 수 있습니다. 모든 device에는 accelerometer가 있으므로, 이 property는 기능적으로 [`isGyroAvailable`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroavailable)
.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable#see-also)

------------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable#Related-Documentation)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)

app이 device-motion service에서 update를 받고 있는지 결정하는 Boolean value입니다.

### [service 사용 가능 여부 확인하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable#Determining-the-Availability-of-Services)

[`var isAccelerometerAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeravailable)

accelerometer를 device에서 사용할 수 있는지 나타내는 Boolean value입니다.

[`var isGyroAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroavailable)

gyroscope를 device에서 사용할 수 있는지 나타내는 Boolean value입니다.

[`var isMagnetometerAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeravailable)

magnetometer를 device에서 사용할 수 있는지 나타내는 Boolean value입니다.

현재 페이지: isDeviceMotionAvailable
