---
title: "SensorKit | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.021293+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit#app-main)

framework

SensorKit
=========

iPhone 또는 paired Apple Watch의 sensor에서 data와 파생 metric을 가져옵니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

[개요](https://developer.apple.com/documentation/sensorkit#overview)

-------------------------------------------------------------------------

system이 device의 다양한 sensor를 사용해 정보를 수집할 때, SensorKit은 app이 선택된 raw data 또는 system이 sensor에서 처리한 metric에 접근할 수 있게 해줍니다. 예를 들면 다음과 같습니다.

*   step 정보
    
*   accelerometer 또는 rotation-rate data
    
*   사용자의 손목 위 watch configuration
    
*   실제 환경의 ambient light
    
*   사용자의 일상적인 통근 또는 이동에 대한 세부 정보
    

전체 목록은 [`SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor)
를 참고하십시오.

[주제](https://developer.apple.com/documentation/sensorkit#topics)

---------------------------------------------------------------------

### [Essentials](https://developer.apple.com/documentation/sensorkit#Essentials)

[SensorKit 업데이트](https://developer.apple.com/documentation/Updates/SensorKit)

SensorKit의 중요한 변경 사항을 알아봅니다.

### [Setup](https://developer.apple.com/documentation/sensorkit#Setup)

[sensor reading을 위해 project 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)

sensor data에 접근하기 위한 system 및 user permission을 얻도록 app에 metadata를 추가합니다.

[`class SRSensorReader`](https://developer.apple.com/documentation/sensorkit/srsensorreader)

특정 sensor에 대해 user authorization을 수립하고 data를 기록하는 object입니다.

### [Authorization](https://developer.apple.com/documentation/sensorkit#Authorization)

[`com.apple.developer.sensorkit.reader.allow`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensorkit.reader.allow)

app의 사전 승인된 연구에 필요한 sensor data에 접근하기 위한 entitlement입니다.

### [Querying data](https://developer.apple.com/documentation/sensorkit#Querying-data)

[`class SRFetchRequest`](https://developer.apple.com/documentation/sensorkit/srfetchrequest)

sample query의 조건을 정의하는 object입니다.

[`class SRFetchResult`](https://developer.apple.com/documentation/sensorkit/srfetchresult)

sensor reader가 fetch한 기록된 data입니다.

### [Interpreting data](https://developer.apple.com/documentation/sensorkit#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 ambient light 양입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app 또는 website를 사용하는 빈도와 상대적인 사용 시간입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard의 configuration과 usage pattern입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object와의 사용자 상호작용입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안의 사용자 Messages app activity를 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안의 사용자 phone activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

사용자의 일상적인 이동 루틴에서의 진행 정보입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목 위에 있는 watch configuration입니다.

### [Deleting samples](https://developer.apple.com/documentation/sensorkit#Deleting-samples)

[`class SRDeletionRecord`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord)

framework가 sample을 삭제하는 이유를 설명하는 object입니다.

### [Analyzing speech](https://developer.apple.com/documentation/sensorkit#Analyzing-speech)

[`class SRSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)

speech 구간에 대한 metric을 나타내는 object입니다.

[`class SRSpeechExpression`](https://developer.apple.com/documentation/sensorkit/srspeechexpression)

speech 구간에 대한 metric과 voice analytics를 나타내는 object입니다.

### [Analyzing faces](https://developer.apple.com/documentation/sensorkit#Analyzing-faces)

[`class SRFaceMetrics`](https://developer.apple.com/documentation/sensorkit/srfacemetrics)

사용자 얼굴에 대한 metric을 나타내는 object입니다.

[`var SR_ARKIT_SUPPORTED: Int32`](https://developer.apple.com/documentation/sensorkit/sr_arkit_supported)

SensorKit framework용 SDK에서 ARKit framework를 사용할 수 있는지 나타내는 flag입니다.

### [Recording wrist temperatures](https://developer.apple.com/documentation/sensorkit#Recording-wrist-temperatures)

[`class SRWristTemperatureSession`](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession)

일정 기간 동안 device가 기록한 wrist temperature를 나타내는 object입니다.

[`class SRWristTemperature`](https://developer.apple.com/documentation/sensorkit/srwristtemperature)

사용자가 잠자는 동안의 손목 온도입니다.

### [Recording ectrocardiogram data](https://developer.apple.com/documentation/sensorkit#Recording-ectrocardiogram-data)

[`class SRElectrocardiogramSample`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample)

sample electrocardiogram sensor data입니다.

### [Recording photoplethysmogram data](https://developer.apple.com/documentation/sensorkit#Recording-photoplethysmogram-data)

[`class SRPhotoplethysmogramSample`](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample)

sample photoplethysmogram (PPG) sensor data입니다.

### [Classes](https://developer.apple.com/documentation/sensorkit#Classes)

[`class SRAcousticSettings`](https://developer.apple.com/documentation/sensorkit/sracousticsettings)

[`class SRSleepSession`](https://developer.apple.com/documentation/sensorkit/srsleepsession)

현재 페이지는 SensorKit입니다
