---
title: "onWristState | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045254+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   onWristState

type property

onWristState
============

손목 위 watch의 위치를 설명하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let onWristState: SRSensor

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate#Discussion)

---------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)
입니다.

information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageWristDetection`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageWristDetection)
 dictionary를 추가해 watch 위치를 감지하는 이유를 제공해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate#see-also)

-----------------------------------------------------------------------------------------------

### [device sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate#Reading-device-sensors)

[`static let deviceUsageReport: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport)

device 사용 정보가 포함된 sensor입니다.

[`static let keyboardMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)

keyboard 사용 정보가 포함된 sensor입니다.

현재 페이지: onWristState
