---
title: "SRSensor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.029421+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRSensor

struct

SRSensor
========

app이 읽을 수 있는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    struct SRSensor

[언급된 문서](https://developer.apple.com/documentation/sensorkit/srsensor#mentions)

--------------------------------------------------------------------------------------

[sensor reading을 위해 project 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)

[논의](https://developer.apple.com/documentation/sensorkit/srsensor#Discussion)

--------------------------------------------------------------------------------------

이 structure의 property를 사용해 다양한 sensor에 접근합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srsensor#topics)

------------------------------------------------------------------------------

### [device sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor#Reading-device-sensors)

[`static let deviceUsageReport: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport)

device 사용 정보가 포함된 sensor입니다.

[`static let keyboardMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)

keyboard 사용 정보가 포함된 sensor입니다.

[`static let onWristState: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate)

손목 위 watch의 위치를 설명하는 sensor입니다.

### [app activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor#Reading-app-activity-sensors)

[`static let messagesUsageReport: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport)

Messages app 사용 정보가 포함된 sensor입니다.

[`static let phoneUsageReport: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport)

사용자가 통화 중인 시간을 보고하는 sensor입니다.

### [사용자 activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

가속도 motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 heart rate data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

메시징 app 안에서 image와 video 같은 media와의 상호작용 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

속도와 경사 정보를 제공하는 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자의 걸음 수 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

회전 motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

사용자의 Siri speech를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 위치 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 잠자는 동안 손목 온도를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

[`static let electrocardiogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)

sample ECG sensor data를 stream하는 sensor입니다.

### [환경 sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor#Reading-environment-sensors)

[`static let ambientLightSensor: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor)

주변 광량 정보를 제공하는 sensor입니다.

[`static let ambientPressure: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure)

압력과 온도 metric을 제공하는 sensor입니다.

### [sensor 만들기](https://developer.apple.com/documentation/sensorkit/srsensor#Creating-a-sensor)

[`init(rawValue: String)`](https://developer.apple.com/documentation/sensorkit/srsensor/init(rawvalue:))

raw value로 sensor를 만듭니다.

### [type property](https://developer.apple.com/documentation/sensorkit/srsensor#Type-Properties)

[`static let acousticSettings: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/acousticsettings)

[`static let sleepSessions: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sleepsessions)

[관계](https://developer.apple.com/documentation/sensorkit/srsensor#relationships)

--------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srsensor#conforms-to)

*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor#see-also)

----------------------------------------------------------------------------------

### [sensor reader 만들기](https://developer.apple.com/documentation/sensorkit/srsensor#Creating-a-sensor-reader)

[`init(sensor: SRSensor)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/init(sensor:))

새 sensor reader object를 초기화합니다.

[`var sensor: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor)

이 object가 읽는 특정 sensor입니다.

현재 페이지: SRSensor
