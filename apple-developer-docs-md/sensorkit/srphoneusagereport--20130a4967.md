---
title: "SRPhoneUsageReport | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srphoneusagereport"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.024469+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRPhoneUsageReport

class

SRPhoneUsageReport
==================

일정 기간 동안의 사용자 phone activity를 설명하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRPhoneUsageReport

[개요](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#overview)

--------------------------------------------------------------------------------------------

이 object는 device가 전화를 걸거나 받는 빈도와, 사용자가 통화 중인 상대적 시간을 설명합니다.

[`phoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport)
 sensor는 이 class를 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#topics)

----------------------------------------------------------------------------------------

### [Phone 사용 분석하기](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#Analyzing-Phone-Use)

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport/duration)

report가 다루는 기간입니다.

[`var totalIncomingCalls: Int`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport/totalincomingcalls)

user가 받은 통화 수입니다.

[`var totalOutgoingCalls: Int`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport/totaloutgoingcalls)

user가 건 통화 수입니다.

[`var totalPhoneCallDuration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport/totalphonecallduration)

모든 통화의 총 duration입니다.

[`var totalUniqueContacts: Int`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport/totaluniquecontacts)

user의 고유 연락처 수입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#relationships)

------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#see-also)

--------------------------------------------------------------------------------------------

### [data 해석하기](https://developer.apple.com/documentation/sensorkit/srphoneusagereport#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 ambient light 양입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app, 또는 website를 사용하는 빈도와 상대적 duration입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard의 configuration과 사용 pattern입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object와의 user interaction입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안의 사용자 Messages app activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

사용자의 일상 이동 루틴에서의 진행 상태입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목에 있는 watch의 configuration입니다.

현재 페이지: SRPhoneUsageReport
