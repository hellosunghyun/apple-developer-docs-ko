---
title: "CMDeviceMotion.SensorLocation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.872707+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMDeviceMotion](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
    
*   CMDeviceMotion.SensorLocation

enum

CMDeviceMotion.SensorLocation
=============================

device의 sensor 위치를 정의합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    enum SensorLocation

[주제](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#topics)

---------------------------------------------------------------------------------------------------------------

### [Sensor 위치](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#Sensor-Locations)

[`` case `default` ``](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum/default)

기본 sensor 위치입니다.

[`case headphoneLeft`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum/headphoneleft)

sensor가 왼쪽 headphone에 있습니다.

[`case headphoneRight`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum/headphoneright)

sensor가 오른쪽 headphone에 있습니다.

### [Initializer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#relationships)

-----------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#see-also)

-------------------------------------------------------------------------------------------------------------------

### [Sensor 위치 가져오기](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum#Getting-the-Sensor-Location)

[`var sensorLocation: CMDeviceMotion.SensorLocation`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.property)

device-motion data를 계산하는 sensor의 위치입니다.

현재 페이지: CMDeviceMotion.SensorLocation
