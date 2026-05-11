---
title: "rotationRate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.042065+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   rotationRate

type property

rotationRate
============

rotation motion data를 제공하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let rotationRate: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate#Discussion)

---------------------------------------------------------------------------------------------------

The [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type for this sensor is \[[`CMRecordedRotationRateData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedRotationRateData)\
\].

rotation rate data를 기록하는 사유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageMotion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMotion)
 dictionary를 추가해야 합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate#see-also)

-----------------------------------------------------------------------------------------------

### [user activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

acceleration motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

user의 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

user의 heart rate data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

messaging app에서 image와 video 같은 media와의 상호작용 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

speed와 slope 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

user의 step 정보를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

user가 Siri에 말한 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 위치 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

user가 잠자는 동안 손목 온도를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지는 rotationRate입니다
