---
title: "samplingFrequency | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.063315+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRPhotoplethysmogramAccelerometerSample](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample)
    
*   samplingFrequency

instance property

samplingFrequency
=================

hertz 단위의 accelerometer data recording frequency입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    var samplingFrequency: Measurement<UnitFrequency> { get }

[참고 항목](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency#see-also)

-----------------------------------------------------------------------------------------------------------------------------------

### [accelerometer data 접근하기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency#Accessing-accelerometer-data)

[`var nanosecondsSinceStart: Int64`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/nanosecondssincestart)

accelerometer data recording이 시작된 이후 경과한 시간(nanosecond)입니다.

[`var x: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/x)

G 중력 단위의 x축 가속도입니다.

[`var y: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/y)

G 중력 단위의 y축 가속도입니다.

[`var z: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/z)

G 중력 단위의 z축 가속도입니다.

현재 페이지는 samplingFrequency입니다
