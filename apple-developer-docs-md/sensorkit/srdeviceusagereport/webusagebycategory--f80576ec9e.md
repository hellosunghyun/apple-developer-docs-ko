---
title: "webUsageByCategory | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.051430+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   webUsageByCategory

instance property

webUsageByCategory
==================

사용자가 category별로 domain에 접근한 시간입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]] { get }

[설명](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory#Discussion)

--------------------------------------------------------------------------------------------------------------------

framework는 Screen Time에 표시되는 것과 같은 방식으로 category를 해석합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory#see-also)

----------------------------------------------------------------------------------------------------------------

### [web 사용 분석하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory#Analyzing-Web-Use)

[`class WebUsage`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage)

사용자의 website 사용을 설명하는 object입니다.

현재 페이지: webUsageByCategory
