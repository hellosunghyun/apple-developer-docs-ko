---
title: "heartRate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/heartrate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.032254+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   heartRate

type property

heartRate
=========

user의 heart rate data를 제공하는 sensor입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    static let heartRate: SRSensor

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate#Discussion)

------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/CoreMotion/CMHighFrequencyHeartRateData)
 입니다.

heart rate를 기록하는 이유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageHeartRate`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageHeartRate)
 dictionary를 추가해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate#see-also)

--------------------------------------------------------------------------------------------

### [Reading user activity sensors](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

acceleration motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

user의 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

messaging app에서 image, video 같은 media와의 interaction 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

speed와 slope 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

user의 걸음 수 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

Siri에 대한 user speech를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 위치에 대한 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

user가 수면 중일 때의 wrist temperature를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지: heartRate
