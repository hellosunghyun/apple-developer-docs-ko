---
title: "crownOrientation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045123+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   crownOrientation

instance property

crownOrientation
================

Digital Crown이 사용자를 기준으로 어느 방향을 향하는지 나타내는 값입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var crownOrientation: SRWristDetection.CrownOrientation { get }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property#see-also)

--------------------------------------------------------------------------------------------------------------------------

### [Inspecting Watch Configuration](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property#Inspecting-Watch-Configuration)

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

Digital Crown이 착용자를 기준으로 향할 수 있는 방향입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목에 착용되어 있는지 나타내는 값입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 어느 손목에 착용하는지 나타내는 값입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

사용자가 watch를 착용하는 위치에 대한 preference입니다.

현재 페이지: crownOrientation
