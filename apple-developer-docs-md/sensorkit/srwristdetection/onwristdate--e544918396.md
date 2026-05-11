---
title: "onWristDate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043412+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   onWristDate

instance property

onWristDate
===========

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    var onWristDate: Date? { get }

[설명](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate#Discussion)

----------------------------------------------------------------------------------------------------------

이 property를 사용해 사용자가 Apple Watch를 착용한 duration을 계산합니다.

[`onWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)
 property의 초기값은 [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0)
이고, [`offWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)
 property의 초기값은 현재 날짜입니다. system은 이 property들의 값을 다음과 같이 변경합니다:

*   사용자가 Apple Watch를 착용하면 [`onWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)
     property는 현재 날짜가 되고 [`offWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)
     property는 그대로 유지됩니다.
    
*   사용자가 Apple Watch를 벗으면 [`offWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)
     property는 현재 날짜가 되고, [`onWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)
     property는 그대로 유지됩니다.
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate#see-also)

------------------------------------------------------------------------------------------------------

### [Watch configuration 확인](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

사용자를 기준으로 Digital Crown이 향하는 방향을 나타내는 value입니다.

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

착용자를 기준으로 Digital Crown이 향할 수 있는 방향입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목에 있는지 나타내는 value입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 착용하는 손목을 나타내는 value입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

사용자가 watch를 착용하는 위치에 대한 설정입니다.

현재 페이지는 onWristDate
