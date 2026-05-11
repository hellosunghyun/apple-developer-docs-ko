---
title: "bundleIdentifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050080+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.ApplicationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)
    
*   bundleIdentifier

instance property

bundleIdentifier
================

사용 중인 app의 bundle identifier입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var bundleIdentifier: String? { get }

[논의](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------

framework는 bundle identifier가 Apple app에 해당할 때만 이 property에 값을 설정합니다. 그렇지 않으면 [`reportApplicationIdentifier`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)
 property를 사용해 해당 app을 연관 지을 수 있습니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier#see-also)

-------------------------------------------------------------------------------------------------------------------------------

### [App 식별하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier#Identifying-the-App)

[`var reportApplicationIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)

실제 application identifier를 대신하는 pseudonym입니다.

[`var supplementalCategories: [SRSupplementalCategory]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories)

app에 대한 추가 정보를 제공하는 category입니다.

[`class SRSupplementalCategory`](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory)

app category에 추가 context를 제공하는 더 세부적인 category입니다.

현재 페이지: bundleIdentifier
