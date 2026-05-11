---
title: "onWrist | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043502+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   onWrist

instance property

onWrist
=======

watch가 사용자의 손목에 있는지를 나타내는 값입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var onWrist: Bool { get }

[참고 항목](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist#see-also)

--------------------------------------------------------------------------------------------------

### [watch 구성 확인](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

Digital Crown이 사용자를 기준으로 어느 방향을 향하는지를 나타내는 값입니다.

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

Digital Crown이 착용자를 기준으로 향할 수 있는 방향입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시각입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시각입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 어느 손목에 착용하는지를 나타내는 값입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

watch를 착용하는 위치에 대한 사용자 설정입니다.

현재 페이지는 onWrist입니다
