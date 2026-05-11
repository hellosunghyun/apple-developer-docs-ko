---
title: "reportApplicationIdentifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050179+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.ApplicationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)
    
*   reportApplicationIdentifier

instance property

reportApplicationIdentifier
===========================

실제 application identifier를 위한 pseudonym입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+

    var reportApplicationIdentifier: String { get }

[설명](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier#Discussion)

----------------------------------------------------------------------------------------------------------------------------------------------

이 property의 value는 app의 실제 identity를 드러내지 않으면서 report 전체에서 하나의 app을 고유하게 가리킵니다. 사용자 privacy를 위해 [`bundleIdentifier`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)
가 `nil`인 경우 system은 이 property에 pseudonymous string을 할당합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier#see-also)

------------------------------------------------------------------------------------------------------------------------------------------

### [app 식별](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier#Identifying-the-App)

[`var bundleIdentifier: String?`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)

사용 중인 app의 bundle identifier입니다.

[`var supplementalCategories: [SRSupplementalCategory]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories)

app에 대한 추가 정보를 제공하는 category입니다.

[`class SRSupplementalCategory`](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory)

app category에 추가 context를 제공하는 더 자세한 category입니다.

현재 페이지: reportApplicationIdentifier
