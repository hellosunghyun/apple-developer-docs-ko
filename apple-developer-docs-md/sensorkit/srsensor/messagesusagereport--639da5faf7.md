---
title: "messagesUsageReport | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.035628+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   messagesUsageReport

type property

messagesUsageReport
===================

Messages app 사용 정보를 제공하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let messagesUsageReport: SRSensor

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport#Discussion)

----------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)
입니다.

Messages app usage 기록 사유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageMessageUsage`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMessageUsage)
 dictionary를 추가해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport#see-also)

------------------------------------------------------------------------------------------------------

### [Reading app activity sensors](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport#Reading-app-activity-sensors)

[`static let phoneUsageReport: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport)

user가 전화 통화 중인 시간을 보고하는 sensor입니다.

현재 페이지: messagesUsageReport
