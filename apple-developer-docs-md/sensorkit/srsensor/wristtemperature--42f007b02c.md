---
title: "wristTemperature | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.042264+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   wristTemperature

type property

wristTemperature
================

사용자가 잠자는 동안 손목 온도를 제공하는 sensor입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    static let wristTemperature: SRSensor

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature#Discussion)

-------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRWristTemperature`](https://developer.apple.com/documentation/sensorkit/srwristtemperature)
 입니다.

information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageWristTemperature`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageWristTemperature)
 dictionary를 추가해 손목 온도를 기록하는 이유를 제공해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature#see-also)

---------------------------------------------------------------------------------------------------

### [Reading user activity sensors](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

가속 motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 심박수 data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

messaging app에서 image와 video 같은 media와 상호작용한 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

속도와 경사 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자 step 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

사용자가 Siri에 말한 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 위치 정보를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지: wristTemperature
