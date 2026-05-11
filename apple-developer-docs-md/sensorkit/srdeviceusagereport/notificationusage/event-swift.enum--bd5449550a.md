---
title: "SRDeviceUsageReport.NotificationUsage.Event | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.051150+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.NotificationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage)
    
*   SRDeviceUsageReport.NotificationUsage.Event

enum

SRDeviceUsageReport.NotificationUsage.Event
===========================================

사용자가 notification과 상호작용하는 방식입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum Event

[주제](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#topics)

----------------------------------------------------------------------------------------------------------------------------

### [event](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#Events)

[`case appLaunch`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/applaunch)

app launch에 대한 notification입니다.

[`case bannerPulldown`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/bannerpulldown)

banner pull down에 대한 notification입니다.

[`case clear`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/clear)

clear event에 대한 notification입니다.

[`case deduped`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/deduped)

deduped event에 대한 notification입니다.

[`case defaultAction`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/defaultaction)

default action에 대한 notification입니다.

[`case deviceActivated`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/deviceactivated)

device activation에 대한 notification입니다.

[`case deviceUnlocked`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/deviceunlocked)

device unlock에 대한 notification입니다.

[`case expired`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/expired)

expiration event에 대한 notification입니다.

[`case hide`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/hide)

hide event에 대한 notification입니다.

[`case longLook`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/longlook)

long look에 대한 notification입니다.

[`case notificationCenterClearAll`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/notificationcenterclearall)

clear-all event에 대한 notification입니다.

[`case received`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/received)

received event에 대한 notification입니다.

[`case removed`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/removed)

removed event에 대한 notification입니다.

[`case silence`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/silence)

silence event에 대한 notification입니다.

[`case supplementaryAction`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/supplementaryaction)

supplementary action에 대한 notification입니다.

[`case tapCoalesce`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/tapcoalesce)

tap-coalesce event에 대한 notification입니다.

[`case unknown`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/unknown)

알 수 없는 event에 대한 notification입니다.

### [initializer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#relationships)

------------------------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#see-also)

--------------------------------------------------------------------------------------------------------------------------------

### [notification 사용 분석하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.enum#Analyzing-Notification-Use)

[`var bundleIdentifier: String?`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/bundleidentifier)

notification에 해당하는 app의 bundle identifier입니다.

[`var event: SRDeviceUsageReport.NotificationUsage.Event`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage/event-swift.property)

사용자가 notification과 상호작용하는 방식입니다.

현재 페이지: SRDeviceUsageReport.NotificationUsage.Event
