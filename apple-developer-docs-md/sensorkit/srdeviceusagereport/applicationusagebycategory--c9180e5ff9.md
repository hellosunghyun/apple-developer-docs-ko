---
title: "applicationUsageByCategory | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.049132+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   applicationUsageByCategory

instance property

applicationUsageByCategory
==========================

category별 app 사용 시간입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]] { get }

[설명](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory#Discussion)

----------------------------------------------------------------------------------------------------------------------------

framework는 app이 `iTunesMetadata.plist`에서 제공하는 primary genre를 사용해 category를 해석합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory#see-also)

------------------------------------------------------------------------------------------------------------------------

### [App 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory#Analyzing-App-Use)

[`class ApplicationUsage`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)

일정 기간 동안 사용자의 app activity를 설명하는 object입니다.

[`struct CategoryKey`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/categorykey)

사용자가 사용하는 app 또는 웹사이트의 category입니다.

현재 페이지는 applicationUsageByCategory입니다
