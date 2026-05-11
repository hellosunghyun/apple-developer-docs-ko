---
title: "sensor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043672+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   sensor

instance property

sensor
======

이 object가 읽는 특정 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var sensor: SRSensor { get }

[논의](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor#Discussion)

---------------------------------------------------------------------------------------------------

framework는 [`init(sensor:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/init(sensor:))
에 전달한 sensor로 이 property를 설정합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor#see-also)

-----------------------------------------------------------------------------------------------

### [Creating a sensor reader](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor#Creating-a-sensor-reader)

[`init(sensor: SRSensor)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/init(sensor:))

새 sensor reader object를 초기화합니다.

[`struct SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor)

app이 읽을 수 있는 sensor입니다.

현재 페이지: sensor
