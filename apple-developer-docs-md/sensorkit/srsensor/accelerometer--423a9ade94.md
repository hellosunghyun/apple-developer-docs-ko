---
title: "accelerometer | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.030728+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   accelerometer

type property

accelerometer
=============

가속도 motion data를 제공하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let accelerometer: SRSensor

[언급된 문서](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer#mentions)

----------------------------------------------------------------------------------------------------

[sensor reading을 위해 project 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer#Discussion)

----------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 \[[`CMRecordedAccelerometerData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedAccelerometerData)\
\]입니다.

accelerometer data를 기록하는 이유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageMotion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMotion)
 dictionary를 추가해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer#see-also)

------------------------------------------------------------------------------------------------

### [Reading user activity sensors](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer#Reading-user-activity-sensors)

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 heart rate data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

messaging app에서 image와 video 같은 media와의 상호작용 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

속도와 경사 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자의 step 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

Siri에 대한 사용자의 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문하는 위치 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 잠자는 동안 손목 온도를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지는 accelerometer입니다
