---
title: "SRDeviceUsageReport.ApplicationUsage | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.049222+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   SRDeviceUsageReport.ApplicationUsage

class

SRDeviceUsageReport.ApplicationUsage
====================================

일정 기간 동안 사용자의 app activity를 설명하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class ApplicationUsage

[개요](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#overview)

--------------------------------------------------------------------------------------------------------------

이 class의 각 instance는 특정 app category에 속한 app 하나를 나타냅니다. 자세한 내용은 [`applicationUsageByCategory`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory)
를 참고합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#topics)

----------------------------------------------------------------------------------------------------------

### [app 식별하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#Identifying-the-App)

[`var bundleIdentifier: String?`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)

사용 중인 app의 bundle identifier입니다.

[`var reportApplicationIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)

실제 application identifier를 대신하는 pseudonymn입니다.

[`var supplementalCategories: [SRSupplementalCategory]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories)

app에 대한 추가 정보를 제공하는 category입니다.

[`class SRSupplementalCategory`](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory)

app category에 추가 context를 제공하는 더 상세한 category입니다.

### [app 사용 시간 측정하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#Timing-App-Use)

[`var usageTime: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/usagetime)

사용자가 app을 사용하는 시간입니다.

[`var relativeStartTime: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime)

report interval에서 첫 번째 app의 시작 시각을 기준으로 사용자가 app을 시작한 시각입니다.

### [text input 살펴보기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#Inspecting-Text-Input)

[`var textInputSessions: [SRTextInputSession]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions)

application usage 동안 발생한 text input session type입니다.

[`class SRTextInputSession`](https://developer.apple.com/documentation/sensorkit/srtextinputsession)

특정 keyboard에서 사용자가 입력한 character입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#relationships)

------------------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#see-also)

--------------------------------------------------------------------------------------------------------------

### [app 사용 분석하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage#Analyzing-App-Use)

[`var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusagebycategory)

category별 app usage 시간입니다.

[`struct CategoryKey`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/categorykey)

사용자가 사용하는 app 또는 website의 category입니다.

현재 페이지: SRDeviceUsageReport.ApplicationUsage
