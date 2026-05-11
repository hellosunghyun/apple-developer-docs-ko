---
title: "mediaEvents | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.041775+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   mediaEvents

type property

mediaEvents
===========

messaging app에서 image와 video 같은 media와의 상호작용 정보를 제공하는 sensor입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    static let mediaEvents: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents#설명)

--------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
type은 [`SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)
.

사용자의 media 상호작용을 관찰하려면 [`SRSensorUsageMediaEvents`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMediaEvents)
 dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
를 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key에 추가해 이유를 제공해야 합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents#see-also)

----------------------------------------------------------------------------------------------

### [사용자 activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

가속도 motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 heart rate data를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

속도와 경사 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자 걸음 수 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

회전 motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

사용자의 Siri 발화를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 위치 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 자는 동안의 손목 온도를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

현재 페이지는 mediaEvents입니다
