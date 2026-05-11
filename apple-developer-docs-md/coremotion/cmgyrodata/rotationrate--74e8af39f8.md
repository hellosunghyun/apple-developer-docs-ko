---
title: "rotationRate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.881175+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMGyroData](https://developer.apple.com/documentation/coremotion/cmgyrodata)
    
*   rotationRate

instance property

rotationRate
============

device의 gyroscope가 측정한 rotation rate입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 2.0+

    var rotationRate: CMRotationRate { get }

[논의](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate#Discussion)

------------------------------------------------------------------------------------------------------

이 property는 device가 세 축을 기준으로 회전하는 속도를 측정한 값을 제공합니다. 이 property는 gyroscope의 raw data를 제공하지만, [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
의 같은 이름 property는 Core Motion algorithm이 bias를 제거한 gyroscope data를 측정한 [`CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationrate)
 structure를 제공합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate#see-also)

--------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate#Related-Documentation)

[UIKit app용 event handling guide](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)

### [Rotation Rate 가져오기](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate#Getting-the-Rotation-Rate)

[`struct CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationrate)

rotation rate 측정값을 나타내는 structure type입니다.

[`class CMRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrotationratedata)

단일 rotation-rate 측정값을 담는 data object입니다.

[`class CMRecordedRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)

특정 시점의 단일 rotation-rate 측정값을 담는 data object입니다.

현재 페이지는 rotationRate입니다
