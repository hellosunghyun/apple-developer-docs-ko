---
title: "SRMediaEvent | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srmediaevent"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.024081+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srmediaevent#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRMediaEvent

class

SRMediaEvent
============

image나 video 같은 media object에 대한 사용자 상호작용입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    class SRMediaEvent

[주제](https://developer.apple.com/documentation/sensorkit/srmediaevent#topics)

----------------------------------------------------------------------------------

### [media object 식별하기](https://developer.apple.com/documentation/sensorkit/srmediaevent#Identifying-Media-Objects)

[`var mediaIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srmediaevent/mediaidentifier)

media object의 고유 식별자입니다.

### [media event 추적하기](https://developer.apple.com/documentation/sensorkit/srmediaevent#Tracking-Media-Events)

[`var eventType: SRMediaEventType`](https://developer.apple.com/documentation/sensorkit/srmediaevent/eventtype)

media에 대한 사용자 상호작용 type입니다.

[`enum SRMediaEventType`](https://developer.apple.com/documentation/sensorkit/srmediaeventtype)

sensor가 추적하는 media에 대한 사용자 상호작용 type입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srmediaevent#relationships)

------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srmediaevent#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srmediaevent#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srmediaevent#see-also)

--------------------------------------------------------------------------------------

### [data 해석하기](https://developer.apple.com/documentation/sensorkit/srmediaevent#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 ambient light 양입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 자신의 device, 특정 Apple app 또는 website를 사용하는 빈도와 상대적 지속 시간입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard의 구성과 사용 패턴입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안 사용자의 Messages app activity를 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안 사용자의 phone activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

일상적인 이동 루틴에서 사용자의 진행 상태입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목에 찬 watch의 구성입니다.

현재 페이지: SRMediaEvent
