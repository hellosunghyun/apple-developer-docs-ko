---
title: "SRWristDetection.CrownOrientation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044957+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   SRWristDetection.CrownOrientation

enum

SRWristDetection.CrownOrientation
=================================

착용자를 기준으로 Digital Crown이 향할 수 있는 방향입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum CrownOrientation

[주제](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#topics)

------------------------------------------------------------------------------------------------------------------

### [방향](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#Orientations)

[`Case left`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum/left)

착용자를 기준으로 Digital Crown이 왼쪽을 향함을 나타냅니다.

[`Case right`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum/right)

착용자를 기준으로 Digital Crown이 오른쪽을 향함을 나타냅니다.

### [initializer](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#relationships)

--------------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#see-also)

----------------------------------------------------------------------------------------------------------------------

### [Watch 구성 검사](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

사용자를 기준으로 Digital Crown이 향하는 방향을 나타내는 값입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목에 착용되어 있는지 나타내는 값입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 착용하는 손목을 나타내는 값입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

사용자가 watch를 착용하는 손목에 대한 설정입니다.

현재 페이지: SRWristDetection.CrownOrientation
