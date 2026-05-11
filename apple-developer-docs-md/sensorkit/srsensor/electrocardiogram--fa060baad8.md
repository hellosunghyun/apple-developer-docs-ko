---
title: "electrocardiogram | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.042452+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   electrocardiogram

type property

electrocardiogram
=================

sample ECG sensor data를 stream하는 sensor입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    static let electrocardiogram: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram#Discussion)

--------------------------------------------------------------------------------------------------------

이 sensor의 sample은 [`SRElectrocardiogramSample`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample)
 object 배열입니다.

information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 `SRSensorUsageECG` dictionary를 추가해 electrocardiogram(ECG) data를 기록하는 이유를 제공해야 합니다.

또한 다음과 같이 `com.apple.developer.sensorkit.reader.allow` entitlement에 `ecg` key를 추가해야 합니다.

    <plist version="1.0">
    <dict>
            <key>com.apple.developer.sensorkit.reader.allow</key>
            <array>
                    <string>ecg</string>
            </array>
    </dict>
    </plist>
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram#see-also)

----------------------------------------------------------------------------------------------------

### [사용자 활동 Sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram#Reading-user-activity-sensors)

[`static let accelerometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

acceleration motion data를 제공하는 sensor입니다.

[`static let faceMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

사용자 얼굴을 설명하는 data를 제공하는 sensor입니다.

[`static let heartRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

사용자의 heart rate data를 제공하는 sensor입니다.

[`static let mediaEvents: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

메시징 app에서 image와 video 같은 media와의 상호 작용 정보를 제공하는 sensor입니다.

[`static let odometer: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

속도와 경사 정보가 포함된 sensor입니다.

[`static let pedometerData: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

사용자의 걸음 수 정보를 제공하는 sensor입니다.

[`static let rotationRate: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

rotation motion data를 제공하는 sensor입니다.

[`static let siriSpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

사용자의 Siri speech를 설명하는 data를 제공하는 sensor입니다.

[`static let telephonySpeechMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

전화 통화 중 speech를 설명하는 data를 제공하는 sensor입니다.

[`static let visits: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

자주 방문한 위치 정보를 제공하는 sensor입니다.

[`static let wristTemperature: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

사용자가 잠자는 동안의 손목 온도를 제공하는 sensor입니다.

[`static let photoplethysmogram: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/photoplethysmogram)

sample PPG sensor data를 stream하는 sensor입니다.

현재 페이지: electrocardiogram
