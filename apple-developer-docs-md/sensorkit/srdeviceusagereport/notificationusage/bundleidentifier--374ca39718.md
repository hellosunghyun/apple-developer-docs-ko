---
title: "bundleIdentifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.051344+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.NotificationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage)
    
*   bundleIdentifier

instance property

bundleIdentifier
================

notification에 해당하는 app의 bundle identifier입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var bundleIdentifier: String? { get }

[논의](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier#Discussion)

------------------------------------------------------------------------------------------------------------------------------------

framework는 bundle identifier가 Apple app에 해당하는 경우에만 이 property에 값을 설정합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier#see-also)

--------------------------------------------------------------------------------------------------------------------------------

### [notification 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier#Analyzing-Notification-Use)

[`var event: SRDeviceUsageReport.NotificationUsage.Event`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.property)

사용자가 notification과 상호작용하는 방식입니다.

[`enum Event`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum)

사용자가 notification과 상호작용하는 방식들입니다.

현재 페이지는 bundleIdentifier입니다
