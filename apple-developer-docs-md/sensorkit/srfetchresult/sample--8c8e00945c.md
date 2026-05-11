---
title: "sample | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srfetchresult/sample"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045711+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRFetchResult](https://developer.apple.com/documentation/sensorkit/srfetchresult)
    
*   sample

instance property

sample
======

sensor reader가 가져온 recording입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    @NSCopying
    var sample: SampleType { get }

[논의](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#Discussion)

--------------------------------------------------------------------------------------------------

framework는 app이 reader의 sensor를 기준으로 result type을 알고 있다고 가정합니다.

### [Sample types](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#Sample-types)

이 property의 type은 framework가 개별 sample type을 파생시키는 superclass입니다. app의 sensor reader에 연결된 sensor에 따라 fetch result의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
을 sensor에 대응하는 sample type으로 type cast합니다. 다음 목록은 sensor별 sample type을 제공합니다.

[`accelerometer`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)

\[[`CMRecordedAccelerometerData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedAccelerometerData)\
\]

[`ambientLightSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor)

[`SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

[`ambientPressure`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure)

`[`[`CMRecordedPressureData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedPressureData)\
`]`

[`deviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport)

[`SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

[`faceMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)

[`SRFaceMetrics`](https://developer.apple.com/documentation/sensorkit/srfacemetrics)

[`heartRate`](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)

[`CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/CoreMotion/CMHighFrequencyHeartRateData)

[`keyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)

[`SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

[`mediaEvents`](https://developer.apple.com/documentation/sensorkit/srsensor/mediaevents)

[`SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

[`messagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport)

[`SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

[`odometer`](https://developer.apple.com/documentation/sensorkit/srsensor/odometer)

[`CMOdometerData`](https://developer.apple.com/documentation/CoreMotion/CMOdometerData)

[`onWristState`](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate)

[`SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

[`pedometerData`](https://developer.apple.com/documentation/sensorkit/srsensor/pedometerdata)

[`CMPedometerData`](https://developer.apple.com/documentation/CoreMotion/CMPedometerData)

[`phoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport)

[`SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

[`rotationRate`](https://developer.apple.com/documentation/sensorkit/srsensor/rotationrate)

\[[`CMRecordedRotationRateData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedRotationRateData)\
\]

[`siriSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/sirispeechmetrics)

[`SRSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)

[`telephonySpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)

[`SRSpeechMetrics`](https://developer.apple.com/documentation/sensorkit/srspeechmetrics)

[`visits`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)

[`SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

[`wristTemperature`](https://developer.apple.com/documentation/sensorkit/srsensor/wristtemperature)

[`SRWristTemperature`](https://developer.apple.com/documentation/sensorkit/srwristtemperature)

[같이 보기](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#see-also)

----------------------------------------------------------------------------------------------

### [Sampling Data](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#Sampling-Data)

[`var timestamp: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchresult/timestamp)

framework가 sample을 기록한 시간입니다.

현재 페이지: sample
