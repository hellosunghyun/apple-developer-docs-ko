---
title: "siriSpeechMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.041657+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   siriSpeechMetrics

type property

siriSpeechMetrics
=================

사용자가 Siri에 말한 speech를 설명하는 data를 제공하는 sensor입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+

    static let siriSpeechMetrics: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics#Discussion)

--------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
 입니다.

이 metric은 tenor, pitch, cadence, speech timing 등 사용자의 음성에 대한 세부 정보를 제공합니다. 여기에는 분당 단어 수와 단어 사이의 평균 시간도 포함됩니다.

이 sensor는 raw audio data를 제공하지 않습니다. 사용자 privacy를 위해 SensorKit은 result에서 transcript string을 제거합니다.

speech를 분석하는 이유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageSpeechMetrics`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageSpeechMetrics)
 dictionary를 추가해야 합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics#see-also)

----------------------------------------------------------------------------------------------------

### [사용자 activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

가속도 motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자의 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 심박수 data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

메시징 app의 image, video 같은 media와의 상호작용 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

속도와 경사 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자의 걸음 수 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문하는 location 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 잠자는 동안의 손목 온도를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지: siriSpeechMetrics
