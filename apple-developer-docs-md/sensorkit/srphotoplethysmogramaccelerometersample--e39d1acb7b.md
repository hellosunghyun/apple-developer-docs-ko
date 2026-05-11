---
title: "SRPhotoplethysmogramAccelerometerSample | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.057759+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRPhotoplethysmogramAccelerometerSample

class

SRPhotoplethysmogramAccelerometerSample
=======================================

photoplethysmogram (PPG) accelerometer의 data sample입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    class SRPhotoplethysmogramAccelerometerSample

[주제](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#topics)

-------------------------------------------------------------------------------------------------------------

### [accelerometer data에 접근하기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#Accessing-accelerometer-data)

[`var nanosecondsSinceStart: Int64`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/nanosecondssincestart)

accelerometer data recording 시작 이후 경과한 시간을 나노초 단위로 나타냅니다.

[`var samplingFrequency: Measurement<UnitFrequency>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency)

accelerometer data recording의 주파수이며, 단위는 hertz입니다.

[`var x: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/x)

G(중력 가속도) 단위의 x축 가속도입니다.

[`var y: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/y)

G(중력 가속도) 단위의 y축 가속도입니다.

[`var z: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/z)

G(중력 가속도) 단위의 z축 가속도입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#relationships)

---------------------------------------------------------------------------------------------------------------------------

### [상속 관계](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#see-also)

-----------------------------------------------------------------------------------------------------------------

### [PPG data에 접근하기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample#Accessing-PPG-data)

[`var startDate: Date`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/startdate)

photoplethysmogram (PPG) sensor data recording의 시작 날짜입니다.

[`var nanosecondsSinceStart: Int64`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/nanosecondssincestart)

data recording 시작 이후 경과한 시간이며, 단위는 나노초입니다.

[`var usage: [SRPhotoplethysmogramSample.Usage]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.property)

사람 또는 system이 측정을 수행한 방식입니다.

[`struct Usage`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct)

사람 또는 system이 photoplethysmogram (PPG) 측정을 수행할 수 있는 방식입니다.

[`var opticalSamples: [SRPhotoplethysmogramOpticalSample]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/opticalsamples)

photoplethysmogram (PPG) optical sensor가 기록한 sample입니다.

[`class SRPhotoplethysmogramOpticalSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample)

photoplethysmogram (PPG) optical sensor의 data sample입니다.

[`var accelerometerSamples: [SRPhotoplethysmogramAccelerometerSample]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/accelerometersamples)

photoplethysmogram (PPG) accelerometer가 기록한 sample입니다.

[`var temperature: Measurement<UnitTemperature>?`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature)

photoplethysmogram (PPG) thermometer가 기록한 sample입니다.

현재 페이지: SRPhotoplethysmogramAccelerometerSample
