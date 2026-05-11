---
title: "relativeStartTime | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050559+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.ApplicationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)
    
*   relativeStartTime

instance property

relativeStartTime
=================

report interval에서 첫 번째 app의 시작 시각을 기준으로 사용자가 app을 시작한 시각입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    var relativeStartTime: TimeInterval { get }

[설명](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime#Discussion)

------------------------------------------------------------------------------------------------------------------------------------

같은 report 안의 app instance 순서를 정하고 instance 사이 시간 간격을 판단할 때 이 property를 사용합니다. report interval에서 이 property의 첫 번째 instance 값은 `0`입니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime#see-also)

--------------------------------------------------------------------------------------------------------------------------------

### [app 사용 시점](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime#Timing-App-Use)

[`var usageTime: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/usagetime)

사용자가 app을 사용한 시간입니다.

현재 페이지는 relativeStartTime입니다.
