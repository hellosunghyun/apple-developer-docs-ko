---
title: "SRMessagesUsageReport | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srmessagesusagereport"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.024355+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRMessagesUsageReport

class

SRMessagesUsageReport
=====================

일정 기간 동안 사용자의 Messages app activity를 설명하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRMessagesUsageReport

[개요](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#overview)

-----------------------------------------------------------------------------------------------

이 object는 사용자가 message를 보내거나 받는 빈도와 Messages app을 사용하는 상대적인 시간을 설명합니다.

[`messagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport)
 sensor는 이 class를 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#topics)

-------------------------------------------------------------------------------------------

### [message 사용 분석하기](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#Analyzing-Message-Use)

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport/duration)

report가 다루는 기간입니다.

[`var totalIncomingMessages: Int`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport/totalincomingmessages)

사용자가 받은 message 수입니다.

[`var totalOutgoingMessages: Int`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport/totaloutgoingmessages)

사용자가 보낸 message 수입니다.

[`var totalUniqueContacts: Int`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport/totaluniquecontacts)

사용자의 contact 수입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#relationships)

---------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#see-also)

-----------------------------------------------------------------------------------------------

### [data 해석하기](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 주변 광량입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app, 또는 website를 사용하는 빈도와 상대적 사용 시간입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard의 구성과 사용 패턴입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object와의 사용자 상호작용입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안 사용자의 phone activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

일상 이동 루틴에서 사용자의 진행 상태입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목 위에 있는 watch의 구성입니다.

현재 페이지: SRMessagesUsageReport
