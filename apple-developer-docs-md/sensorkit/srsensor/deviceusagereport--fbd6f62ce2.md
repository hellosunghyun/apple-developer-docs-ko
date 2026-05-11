---
title: "deviceUsageReport | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.031386+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   deviceUsageReport

type property

deviceUsageReport
=================

device usage 정보를 제공하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let deviceUsageReport: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport#Discussion)

--------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
입니다.

device usage를 기록하는 사유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageDeviceUsage`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageDeviceUsage)
 dictionary를 추가해야 합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport#see-also)

----------------------------------------------------------------------------------------------------

### [device sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport#Reading-device-sensors)

[`static let keyboardMetrics: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)

keyboard usage 정보를 제공하는 sensor입니다.

[`static let onWristState: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate)

watch가 손목에서 어떤 위치에 있는지 설명하는 sensor입니다.

현재 페이지는 deviceUsageReport입니다
