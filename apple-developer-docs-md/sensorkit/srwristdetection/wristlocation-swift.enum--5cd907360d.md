---
title: "SRWristDetection.WristLocation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.032058+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection)
    
*   SRWristDetection.WristLocation

enum

SRWristDetection.WristLocation
==============================

사용자가 watch를 어느 손목에 착용하는지에 대한 선호입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum WristLocation

[주제](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#topics)

---------------------------------------------------------------------------------------------------------------

### [손목 선호 설정](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#Wrist-Preferences)

[`case left`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum/left)

사용자가 watch를 왼쪽 손목에 착용함을 나타냅니다.

[`case right`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum/right)

사용자가 watch를 오른쪽 손목에 착용함을 나타냅니다.

### [이니셜라이저](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#relationships)

-----------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#see-also)

-------------------------------------------------------------------------------------------------------------------

### [Watch 구성 확인하기](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

Digital Crown이 사용자 기준으로 어느 방향을 향하는지 나타내는 값입니다.

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

Digital Crown이 착용자 기준으로 향할 수 있는 방향입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목에 있는지 나타내는 값입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 착용하는 손목을 나타내는 값입니다.

현재 페이지: SRWristDetection.WristLocation
