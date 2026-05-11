---
title: "telephonySpeechMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.042158+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   telephonySpeechMetrics

type property

telephonySpeechMetrics
======================

phone call 중의 speech를 설명하는 data를 제공하는 sensor입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+

    static let telephonySpeechMetrics: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics#Discussion)

-------------------------------------------------------------------------------------------------------------

The [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type for this sensor is [`SRSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)
.

The metrics provide details about the user’s voice, such as tenor, pitch, cadence, and speech timing, which includes words per minute and the average duration between words.

이 sensor는 raw audio data를 제공하지 않습니다.

You need to provide a reason to analyze speech by adding the [`SRSensorUsageSpeechMetrics`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageSpeechMetrics)
 dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key in the information property list.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics#see-also)

---------------------------------------------------------------------------------------------------------

### [Reading user activity sensors](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

acceleration motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 heart rate data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

messaging app에서 image, video 같은 media와 상호작용한 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

speed와 slope 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자의 step 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

사용자가 Siri에 한 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 location 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 수면 중일 때 wrist temperature를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지: telephonySpeechMetrics
