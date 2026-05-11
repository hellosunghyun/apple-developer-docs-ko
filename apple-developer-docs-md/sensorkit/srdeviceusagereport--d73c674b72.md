---
title: "SRDeviceUsageReport | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.023152+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRDeviceUsageReport

class

SRDeviceUsageReport
===================

사용자가 device, 특정 Apple app, 또는 website를 사용하는 빈도와 상대적인 사용 시간입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRDeviceUsageReport

[개요](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#overview)

---------------------------------------------------------------------------------------------

[`deviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport)
 sensor는 이 class를 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#topics)

-----------------------------------------------------------------------------------------

### [device 사용 요약](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#Summarizing-Device-Use)

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/duration)

report가 포함하는 기간입니다.

[`var totalScreenWakes: Int`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/totalscreenwakes)

device의 전체 screen wake 수입니다.

[`var totalUnlocks: Int`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/totalunlocks)

device의 전체 unlock 수입니다.

[`var totalUnlockDuration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/totalunlockduration)

device가 unlocked 상태로 있는 시간입니다.

### [app 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#Analyzing-App-Use)

[`var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory)

category별 app 사용 시간입니다.

[`class ApplicationUsage`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)

일정 기간 동안 사용자의 app activity를 설명하는 object입니다.

[`struct CategoryKey`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/categorykey)

사용자가 사용하는 app 또는 website의 category입니다.

### [notification 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#Analyzing-Notification-Use)

[`var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusagebycategory)

category별 notification 빈도입니다.

[`class NotificationUsage`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/notificationusage)

notification 빈도와 사용자가 notification과 상호작용하는 방식을 설명하는 object입니다.

### [web 사용 분석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#Analyzing-Web-Use)

[`var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusagebycategory)

category별로 사용자가 domain에 접근한 시간입니다.

[`class WebUsage`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/webusage)

사용자의 website 사용을 설명하는 object입니다.

### [algorithm 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#Getting-algorithm-information)

[`var version: String`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/version)

system이 report 생성에 사용하는 algorithm의 version입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#relationships)

-------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 대상](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#see-also)

---------------------------------------------------------------------------------------------

### [data 해석](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 ambient light 양입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard 구성과 사용 패턴입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object에 대한 사용자 상호작용입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안 사용자의 Messages app activity를 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안 사용자의 phone activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

사용자의 일상적인 이동 루틴에서의 진행 상태입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목에 있는 watch의 구성입니다.

현재 페이지는 SRDeviceUsageReport입니다
