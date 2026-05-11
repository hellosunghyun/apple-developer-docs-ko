---
title: "notificationUsageByCategory | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.049428+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   notificationUsageByCategory

instance property

notificationUsageByCategory
===========================

category별 notification 빈도입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]] { get }

[논의](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory#Discussion)

-----------------------------------------------------------------------------------------------------------------------------

framework는 app이 `iTunesMetadata.plist`에 제공한 primary genre를 사용해 category를 해석합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory#see-also)

-------------------------------------------------------------------------------------------------------------------------

### [Analyzing Notification Use](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory#Analyzing-Notification-Use)

[`class NotificationUsage`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage)

notification 빈도와 사용자가 notification과 상호작용하는 방식을 설명하는 object입니다.

현재 페이지는 notificationUsageByCategory입니다
