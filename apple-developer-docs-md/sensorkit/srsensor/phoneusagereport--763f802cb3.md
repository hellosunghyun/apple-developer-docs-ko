---
title: "phoneUsageReport | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.037567+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   phoneUsageReport

type property

phoneUsageReport
================

사용자가 통화 중인 시간을 보고하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let phoneUsageReport: SRSensor

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport#Discussion)

-------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)
입니다.

phone usage를 기록하는 이유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsagePhoneUsage`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsagePhoneUsage)
 dictionary를 추가해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport#see-also)

---------------------------------------------------------------------------------------------------

### [app activity sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport#Reading-app-activity-sensors)

[`static let messagesUsageReport: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport)

Messages app 사용 정보를 제공하는 sensor입니다.

현재 페이지: phoneUsageReport
