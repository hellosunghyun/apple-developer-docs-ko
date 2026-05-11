---
title: "SRDeletionRecord | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeletionrecord"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.028781+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRDeletionRecord

class

SRDeletionRecord
================

framework가 sample을 삭제한 이유를 설명하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRDeletionRecord

[개요](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#overview)

------------------------------------------------------------------------------------------

기록된 sensor data에 간격이 생길 때 deletion record는 framework가 의도적으로 record를 제거한 경우를 설명합니다. deletion record는 record를 사용할 수 없는 시간 범위([`startTime`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/starttime)
 및 [`endTime`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/endtime)
 참고)와 제거 이유인 [`reason`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/reason)
 을 지정합니다.

특정 sensor의 deletion record에 접근하려면 source sensor에 [`NSString`](https://developer.apple.com/documentation/Foundation/NSString)
 의 `sr_sensorForDeletionRecordsFromSensor()` extension을 적용해 새 reader를 만듭니다.

    let deletionRecordsReader = SRSensorReader(sensor: ambientLightSensor.rawValue.sr_sensorForDeletionRecordsFromSensor())
    deletionRecordsReader.delegate = myAmbientLightDeletionRecordsDelegate
    

[주제](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#topics)

--------------------------------------------------------------------------------------

### [삭제 이유 접근하기](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#Accessing-the-Deletion-Reason)

[`var reason: SRDeletionReason`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/reason)

framework가 sample을 삭제한 이유입니다.

[`enum SRDeletionReason`](https://developer.apple.com/documentation/sensorkit/srdeletionreason)

framework가 sample을 삭제하는 이유입니다.

### [삭제 시각 접근하기](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#Accessing-the-Deletion-Time)

[`var startTime: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/starttime)

framework가 sample 삭제를 시작하는 시각입니다.

[`var endTime: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/endtime)

framework가 sample 삭제를 마치는 시각입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#relationships)

----------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 대상](https://developer.apple.com/documentation/sensorkit/srdeletionrecord#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

현재 페이지: SRDeletionRecord
