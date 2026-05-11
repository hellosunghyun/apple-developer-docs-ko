---
title: "temperature | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.034995+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRPhotoplethysmogramSample](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample)
    
*   temperature

instance property

temperature
===========

photoplethysmogram(PPG) thermometer가 기록한 sample입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    var temperature: Measurement<UnitTemperature>? { get }

[관련 항목](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature#see-also)

----------------------------------------------------------------------------------------------------------------

### [PPG data 접근](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature#Accessing-PPG-data)

[`var startDate: Date`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/startdate)

photoplethysmogram(PPG) sensor data recording의 시작 날짜입니다.

[`var nanosecondsSinceStart: Int64`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/nanosecondssincestart)

data recording 시작 이후 경과한 시간(ns)입니다.

[`var usage: [SRPhotoplethysmogramSample.Usage]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.property)

사람 또는 system이 reading을 수행하는 방식입니다.

[`struct Usage`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct)

사람 또는 system이 photoplethysmogram(PPG) reading을 수행할 수 있는 방식입니다.

[`var opticalSamples: [SRPhotoplethysmogramOpticalSample]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/opticalsamples)

photoplethysmogram(PPG) optical sensor가 기록한 sample입니다.

[`class SRPhotoplethysmogramOpticalSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample)

photoplethysmogram(PPG) optical sensor의 data sample입니다.

[`var accelerometerSamples: [SRPhotoplethysmogramAccelerometerSample]`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/accelerometersamples)

photoplethysmogram(PPG) accelerometer가 기록한 sample입니다.

[`class SRPhotoplethysmogramAccelerometerSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample)

photoplethysmogram(PPG) accelerometer의 data sample입니다.

현재 페이지는 temperature입니다
