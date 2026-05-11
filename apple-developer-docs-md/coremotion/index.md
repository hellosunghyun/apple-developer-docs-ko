---
title: "Core Motion | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.866592+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion#app-main)

framework

Core Motion
===========

accelerometer, gyroscope, pedometer 및 environment 관련 event를 처리합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

[개요](https://developer.apple.com/documentation/coremotion#overview)

--------------------------------------------------------------------------

Core Motion은 iOS, iPadOS, watchOS, visionOS device에서 사용 가능한 onboard hardware의 motion 및 environment 관련 data를 보고합니다. 이 hardware에는 device의 accelerometer와 gyroscope가 포함되며, 지원되는 경우 pedometer, magnetometer, barometer도 포함됩니다. 이 data는 app에서 user interaction, fitness tracking, health 관련 기능 등의 입력으로 사용할 수 있습니다. 예를 들어 game은 accelerometer와 gyroscope 입력을 사용해 화면 속 동작을 제어할 수 있습니다.

이 framework의 service는 motion data를 raw value 또는 processed value 형태로 제공하며, 많은 service가 두 종류를 모두 제공합니다. raw value는 hardware의 수정되지 않은 data를 반영하고, processed value는 data 활용에 악영향을 줄 수 있는 bias를 제거합니다. 예를 들어 processed accelerometer value는 중력으로 인한 가속도가 아니라 사용자로 인해 발생한 가속도만 반영합니다.

모든 service를 모든 device에서 사용할 수 있는 것은 아니며, 필요한 hardware가 있는 device에서도 일부 service를 사용할 수 없을 수 있습니다. 예를 들어 많은 Core Motion service는 visionOS app에서 사용할 수 있지만, visionOS에서 실행되는 호환 iPad 및 iPhone app에서는 사용할 수 없습니다. motion 관련 service를 사용하기 전에 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 object를 사용해 해당 service의 사용 가능 여부를 확인하세요.

[주제](https://developer.apple.com/documentation/coremotion#topics)

----------------------------------------------------------------------

### [핵심 항목](https://developer.apple.com/documentation/coremotion#Essentials)

[Core Motion 업데이트](https://developer.apple.com/documentation/Updates/CoreMotion)

Core Motion의 중요한 변경 사항을 알아봅니다.

[`class CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)

motion service를 시작하고 관리하는 object입니다.

### [Device motion](https://developer.apple.com/documentation/coremotion#Device-motion)

중력과 기타 bias를 반영해 조정된 acceleration, attitude, rotation, magnetic field data에 접근합니다.

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

중력의 영향 같은 environment bias를 제거하도록 system이 처리한 motion data를 가져옵니다.

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

device의 attitude, rotation rate, acceleration 측정값을 캡슐화한 object입니다.

[`class CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)

특정 시점에서 알려진 reference frame을 기준으로 한 device의 방향입니다.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

attitude 관련 motion data의 reference frame을 나타내는 constant입니다.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

headphone motion service를 시작하고 관리하는 object입니다.

### [Accelerometer](https://developer.apple.com/documentation/coremotion#Accelerometers)

device의 세 축에 대한 accelerometer data에 접근합니다.

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

onboard accelerometer에서 data를 가져옵니다.

[`class CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

device의 세 accelerometer에서 얻은 data sample입니다.

[`class CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

device가 기록한 accelerometer data 한 건입니다.

[`class CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

device에서 accelerometer data를 수집하고 가져오는 object입니다.

[`class CMSensorDataList`](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

system이 기록한 accelerometer data 목록입니다.

### [Gyroscope](https://developer.apple.com/documentation/coremotion#Gyroscopes)

raw gyroscope data에 접근합니다.

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

onboard gyroscope에서 data를 가져옵니다.

[`class CMGyroData`](https://developer.apple.com/documentation/coremotion/cmgyrodata)

device의 rotation rate 측정값 한 건입니다.

### [Magnetometer](https://developer.apple.com/documentation/coremotion#Magnetometer)

raw magnetometer data에 접근합니다.

[`class CMMagnetometerData`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)

device를 기준으로 한 지구 자기장 측정값입니다.

### [Altitude data](https://developer.apple.com/documentation/coremotion#Altitude-data)

barometric sensor 정보를 기반으로 altitude data에 접근합니다.

[`class CMAltimeter`](https://developer.apple.com/documentation/coremotion/cmaltimeter)

altitude 관련 변화의 전달을 시작하는 object입니다.

[`class CMAbsoluteAltitudeData`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata)

absolute altitude 변화를 기록하는 data입니다.

[`class CMAltitudeData`](https://developer.apple.com/documentation/coremotion/cmaltitudedata)

기록된 altitude 변화에 대한 data입니다.

### [Ambient pressure](https://developer.apple.com/documentation/coremotion#Ambient-pressure)

[`class CMRecordedPressureData`](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata)

기록된 pressure data 측정값입니다.

[`class CMAmbientPressureData`](https://developer.apple.com/documentation/coremotion/cmambientpressuredata)

ambient pressure와 temperature의 측정값입니다.

### [Water submersion](https://developer.apple.com/documentation/coremotion#Water-submersion)

[submersion data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

water-submersion manager를 사용해 Apple Watch Ultra에서 water pressure, temperature, depth data를 받습니다.

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

submersion 중 pressure와 temperature data 수집을 관리하는 object입니다.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

ambient pressure, water pressure, water temperature, submersion event에 대한 update를 받는 delegate입니다.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

device의 submersion 상태가 바뀌었음을 나타내는 event입니다.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

pressure와 depth에 관한 data를 담은 update입니다.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

water temperature에 관한 data를 담은 update입니다.

### [Activity](https://developer.apple.com/documentation/coremotion#Activity)

[`class CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

device에 저장된 motion data에 대한 접근을 관리하는 object입니다.

[`class CMHeadphoneActivityManager`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)

headphone activity service를 시작하고 관리하는 object입니다.

[`class CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

단일 motion update event에 대한 data입니다.

[headphone에서 motion-activity data 가져오기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones)

headphone의 motion-activity 변화를 app이 수신하도록 구성합니다.

### [Pedometer 및 fitness](https://developer.apple.com/documentation/coremotion#Pedometer-and-fitness)

built-in motion processor의 step-counting data에 접근합니다.

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

system이 생성한 live walking data를 가져오는 object입니다.

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

사용자가 도보로 이동한 거리에 대한 정보입니다.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

사용자의 보행 activity 변화입니다.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

사용자가 device와 함께 걸은 step 수입니다.

Deprecated

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

workout용 odometer data를 나타내는 class입니다.

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

1Hz로 수집한 heart rate data를 나타내는 class입니다.

### [Movement disorder](https://developer.apple.com/documentation/coremotion#Movement-disorder)

[movement disorder symptom data 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Apple Watch의 movement disorder manager에서 data를 가져옵니다.

[movement disorder data collection requirement 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

사용자가 app이 수집하는 data를 이해하고 제어할 수 있게 합니다.

[movement disorder algorithm 변경 내역](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

movement disorder algorithm의 주요 변경 사항을 시간순으로 정리한 기록입니다.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

movement disorder data를 기록하고 query하는 manager입니다.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

1분 간격 동안 tremor의 존재 여부와 강도에 관한 data를 담은 result object입니다.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

1분 간격 동안 dyskinetic symptom이 존재할 가능성에 관한 data를 담은 result object입니다.

### [Fall detection](https://developer.apple.com/documentation/coremotion#Fall-detection)

[`class CMFallDetectionManager`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)

fall detection event를 관리하는 object입니다.

[`protocol CMFallDetectionDelegate`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)

fall detection event 정보와 authorization status 변경 사항을 받는 delegate입니다.

[`class CMFallDetectionEvent`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)

fall detection event에 관한 data를 담은 object입니다.

[`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription)

fall detection event data 접근 권한을 app이 요청하는 이유를 사용자에게 설명하는 메시지입니다.

### [과거 data](https://developer.apple.com/documentation/coremotion#Historical-data)

기록된 motion event에 접근해 movement pattern 분석에 활용합니다.

[`class CMBatchedSensorManager`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)

### [공통 data](https://developer.apple.com/documentation/coremotion#Common-data)

[`class CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)

모든 motion 관련 data object의 base class입니다.

현재 페이지는 Core Motion입니다
