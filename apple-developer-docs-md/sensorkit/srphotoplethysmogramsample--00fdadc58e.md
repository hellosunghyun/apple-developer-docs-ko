---
title: "SRPhotoplethysmogramSample | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.033192+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRPhotoplethysmogramSample

class

SRPhotoplethysmogramSample
==========================

sample photoplethysmogram(PPG) sensor data입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    class SRPhotoplethysmogramSample

[개요](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#overview)

----------------------------------------------------------------------------------------------------

PPG sensor는 이 object 배열을 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

Apple Watch는 LED 조명과 빛에 민감한 photodiode(PD)를 함께 사용해 심장 박동으로 인한 맥동을 추적합니다. Apple Watch model마다 LED와 PD 개수가 다를 수 있습니다. 자세한 내용은 [`SRPhotoplethysmogramOpticalSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample)
 을 참고하세요.

자세한 내용은 다음 문서를 참고하세요.

*   [Monitor your heart rate with Apple Watch](https://support.apple.com/en-us/HT204666)
    
*   [Using Apple Watch for Arrhythmia Detection](https://www.apple.com/healthcare/docs/site/Apple_Watch_Arrhythmia_Detection.pdf)
    
*   [How to use the Blood Oxygen app on Apple Watch](https://support.apple.com/en-us/HT211027)
    
*   [Blood Oxygen app on Apple Watch](https://www.apple.com/healthcare/docs/site/Blood_Oxygen_app_on_Apple_Watch_October_2022.pdf)
    

[주제](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#topics)

------------------------------------------------------------------------------------------------

### [Accessing PPG data](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#Accessing-PPG-data)

[`var startDate: Date`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/startdate)

photoplethysmogram(PPG) sensor data 기록의 시작 날짜입니다.

[`var nanosecondsSinceStart: Int64`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/nanosecondssincestart)

data 기록 시작 이후 경과한 nanosecond 시간입니다.

[`var usage: [SRPhotoplethysmogramSample.Usage]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.property)

사람 또는 system이 측정을 수행할 때 사용한 방식입니다.

[`struct Usage`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct)

사람 또는 system이 photoplethysmogram(PPG) 측정을 수행할 수 있는 방식입니다.

[`var opticalSamples: [SRPhotoplethysmogramOpticalSample]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/opticalsamples)

photoplethysmogram(PPG) optical sensor가 기록한 sample입니다.

[`class SRPhotoplethysmogramOpticalSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample)

photoplethysmogram(PPG) optical sensor의 data sample입니다.

[`var accelerometerSamples: [SRPhotoplethysmogramAccelerometerSample]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/accelerometersamples)

photoplethysmogram(PPG) accelerometer가 기록한 sample입니다.

[`class SRPhotoplethysmogramAccelerometerSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample)

photoplethysmogram(PPG) accelerometer의 data sample입니다.

[`var temperature: Measurement<UnitTemperature>?`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature)

photoplethysmogram(PPG) thermometer가 기록한 sample입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#relationships)

--------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample#conforms-to)

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
    

현재 페이지: SRPhotoplethysmogramSample
