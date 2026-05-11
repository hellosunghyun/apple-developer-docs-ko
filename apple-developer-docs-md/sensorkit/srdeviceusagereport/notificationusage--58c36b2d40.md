---
title: "SRDeviceUsageReport.NotificationUsage | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.049521+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   SRDeviceUsageReport.NotificationUsage

class

SRDeviceUsageReport.NotificationUsage
=====================================

notification 빈도와 사용자가 notification과 상호작용하는 방식을 설명하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class NotificationUsage

[개요](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#overview)

---------------------------------------------------------------------------------------------------------------

이 class의 각 instance는 특정 app category의 사용자 notification을 나타냅니다. 자세한 내용은 [`notificationUsageByCategory`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory)
.

[주제](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#topics)

-----------------------------------------------------------------------------------------------------------

### [notification 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#Analyzing-Notification-Use)

[`var bundleIdentifier: String?`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier)

notification에 해당하는 app의 bundle identifier입니다.

[`var event: SRDeviceUsageReport.NotificationUsage.Event`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.property)

사용자가 notification과 상호작용하는 방식입니다.

[`enum Event`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum)

사용자가 notification과 상호작용하는 방식입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#relationships)

-------------------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#see-also)

---------------------------------------------------------------------------------------------------------------

### [notification 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage#Analyzing-Notification-Use)

[`var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory)

category별 notification 빈도입니다.

현재 페이지는 SRDeviceUsageReport.NotificationUsage입니다
