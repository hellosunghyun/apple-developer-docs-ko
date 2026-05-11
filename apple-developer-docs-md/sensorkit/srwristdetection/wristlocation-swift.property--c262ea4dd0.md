---
title: "wristLocation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043237+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   wristLocation

instance property

wristLocation
=============

사용자가 시계를 착용한 손목을 나타내는 값입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var wristLocation: SRWristDetection.WristLocation { get }

[참고 항목](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [Watch 구성 확인](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

사용자를 기준으로 Digital Crown이 향하는 방향을 나타내는 값입니다.

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

착용자를 기준으로 Digital Crown이 향할 수 있는 방향입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목 위에 있는지를 나타내는 값입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

사용자가 watch를 어느 손목에 착용하는지에 대한 설정입니다.

현재 페이지는 wristLocation입니다
