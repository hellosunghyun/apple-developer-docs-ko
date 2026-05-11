---
title: "supplementalCategories | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050269+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.ApplicationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)
    
*   supplementalCategories

instance property

supplementalCategories
======================

app에 대한 추가 정보를 제공하는 category입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    var supplementalCategories: [SRSupplementalCategory] { get }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories#see-also)

-------------------------------------------------------------------------------------------------------------------------------------

### [app 식별하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories#Identifying-the-App)

[`var bundleIdentifier: String?`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)

사용 중인 app의 bundle identifier입니다.

[`var reportApplicationIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)

실제 application identifier를 대신하는 pseudonym입니다.

[`class SRSupplementalCategory`](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory)

app category에 추가 context를 제공하는 더 자세한 category입니다.

현재 페이지: supplementalCategories
