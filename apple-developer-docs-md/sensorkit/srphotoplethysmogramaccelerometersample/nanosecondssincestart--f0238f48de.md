---
title: "nanosecondsSinceStart | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/nanosecondssincestart"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.062933+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/nanosecondssincestart#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRPhotoplethysmogramAccelerometerSample](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample)
    
*   nanosecondsSinceStart

instance property

nanosecondsSinceStart
=====================

accelerometer data 기록이 시작된 이후 경과한 시간(나노초)입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    var nanosecondsSinceStart: Int64 { get }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/nanosecondssincestart#see-also)

---------------------------------------------------------------------------------------------------------------------------------------

### [accelerometer data 접근](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/nanosecondssincestart#Accessing-accelerometer-data)

[`var samplingFrequency: Measurement<UnitFrequency>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency)

헤르츠 단위의 accelerometer data 기록 주파수입니다.

[`var x: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/x)

G(중력가속도) 단위의 x축 acceleration입니다.

[`var y: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/y)

G(중력가속도) 단위의 y축 acceleration입니다.

[`var z: Measurement<UnitAcceleration>`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/z)

G(중력가속도) 단위의 z축 acceleration입니다.

현재 페이지는 nanosecondsSinceStart입니다
