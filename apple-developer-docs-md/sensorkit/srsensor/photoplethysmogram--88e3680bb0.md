---
title: "photoplethysmogram | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.042358+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   photoplethysmogram

type property

photoplethysmogram
==================

sample PPG sensor data를 stream하는 sensor입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    static let photoplethysmogram: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram#Discussion)

---------------------------------------------------------------------------------------------------------

이 sensor의 sample은 [`SRPhotoplethysmogramSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample)
object array입니다.

information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
key에 `SRSensorUsagePPG` dictionary를 추가해 photoplethysmogram (PPG) data를 기록하는 이유를 제공해야 합니다.

또한 다음과 같이 `com.apple.developer.sensorkit.reader.allow` entitlement에 `ppg` key도 추가해야 합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram#see-also)

-----------------------------------------------------------------------------------------------------

### [user activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

acceleration motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자의 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 heart rate data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

messaging app에서 image와 video 같은 media와의 상호작용 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

speed와 slope 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자의 걸음 수 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

사용자의 Siri 음성을 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문하는 위치 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 잠든 동안의 손목 온도를 제공하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지는 photoplethysmogram입니다.
