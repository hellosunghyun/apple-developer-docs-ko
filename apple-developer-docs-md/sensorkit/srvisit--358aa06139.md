---
title: "SRVisit | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srvisit"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.024587+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srvisit#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRVisit

class

SRVisit
=======

사용자의 일상적인 이동 루틴 진행 상황입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRVisit

[개요](https://developer.apple.com/documentation/sensorkit/srvisit#overview)

---------------------------------------------------------------------------------

[`visits`](https://developer.apple.com/documentation/sensorkit/srsensor/visits)
 sensor는 이 class를 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srvisit#topics)

-----------------------------------------------------------------------------

### [Visit 식별](https://developer.apple.com/documentation/sensorkit/srvisit#Identifying-a-Visit)

[`var identifier: UUID`](https://developer.apple.com/documentation/sensorkit/srvisit/identifier)

고유한 지리적 위치에 매핑되는 값입니다.

### [Visit 정보 접근](https://developer.apple.com/documentation/sensorkit/srvisit#Accessing-Visit-Information)

[`var arrivalDateInterval: DateInterval`](https://developer.apple.com/documentation/sensorkit/srvisit/arrivaldateinterval)

사용자가 관심 위치에 도착한 시각 범위입니다.

[`var departureDateInterval: DateInterval`](https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval)

사용자가 관심 위치에서 출발한 시각 범위입니다.

[`var distanceFromHome: CLLocationDistance`](https://developer.apple.com/documentation/sensorkit/srvisit/distancefromhome)

home-category location으로부터의 거리입니다.

[`var locationCategory: SRVisit.LocationCategory`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.property)

location type입니다.

[`enum LocationCategory`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum)

location type입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srvisit#relationships)

-------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srvisit#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srvisit#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srvisit#see-also)

---------------------------------------------------------------------------------

### [data 해석](https://developer.apple.com/documentation/sensorkit/srvisit#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 ambient light 양입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app 또는 웹사이트를 사용하는 빈도와 상대적 duration입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard 구성과 사용 패턴입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object와의 사용자 상호 작용입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안의 사용자 Messages app 활동을 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안의 사용자 전화 활동을 설명하는 object입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목 위 watch 구성입니다.

현재 페이지는 SRVisit입니다
