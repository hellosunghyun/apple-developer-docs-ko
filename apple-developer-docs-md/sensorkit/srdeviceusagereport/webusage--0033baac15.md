---
title: "SRDeviceUsageReport.WebUsage | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.053139+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   SRDeviceUsageReport.WebUsage

class

SRDeviceUsageReport.WebUsage
============================

사용자의 website 사용을 설명하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class WebUsage

[개요](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#overview)

------------------------------------------------------------------------------------------------------

이 class의 각 instance는 특정 app category에 속한 website 하나를 나타냅니다. 자세한 내용은 [`webUsageByCategory`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory)
 를 참고합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#topics)

--------------------------------------------------------------------------------------------------

### [웹 사용 시간 측정하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#Timing-Web-Use)

[`var totalUsageTime: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage/totalusagetime)

report가 포함하는 web usage time의 양입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#relationships)

----------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#see-also)

------------------------------------------------------------------------------------------------------

### [웹 사용 분석하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage#Analyzing-Web-Use)

[`var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory)

사용자가 category별로 domain에 접근한 시간의 양입니다.

현재 페이지: SRDeviceUsageReport.WebUsage
