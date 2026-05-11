---
title: "offWristDate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043327+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   offWristDate

instance property

offWristDate
============

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    var offWristDate: Date? { get }

[설명](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate#Discussion)

-----------------------------------------------------------------------------------------------------------

이 property를 사용해 사용자가 Apple Watch를 착용한 duration을 계산합니다.

[`offWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)
property의 초기값은 현재 날짜이고 [`onWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)
property는 [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0)
입니다. system은 이 property 값을 다음과 같이 변경합니다.

*   사용자가 Apple Watch를 착용하면 [`onWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)
    property가 현재 날짜가 되고 [`offWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)
    property는 그대로 유지됩니다.
    
*   사용자가 Apple Watch를 벗으면 [`offWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)
    property가 현재 날짜가 되고 [`onWristDate`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)
    property는 그대로 유지됩니다.
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate#see-also)

-------------------------------------------------------------------------------------------------------

### [Watch configuration 살펴보기](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

Digital Crown이 사용자 기준 어느 방향을 향하는지 나타내는 값입니다.

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

착용자 기준으로 Digital Crown이 향할 수 있는 방향입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목 위에 있는지 나타내는 값입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 착용하는 손목을 나타내는 값입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

사용자가 watch를 착용하는 위치에 대한 설정입니다.

현재 페이지는 offWristDate입니다
