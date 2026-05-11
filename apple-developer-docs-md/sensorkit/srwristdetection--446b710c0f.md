---
title: "SRWristDetection | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristdetection"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.024691+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristdetection#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRWristDetection

class

SRWristDetection
================

착용자의 손목에서 watch가 어떻게 설정되었는지 나타내는 구성 정보입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRWristDetection

[개요](https://developer.apple.com/documentation/sensorkit/srwristdetection#overview)

------------------------------------------------------------------------------------------

[`onWristState`](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate)
 sensor는 이 class를 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srwristdetection#topics)

--------------------------------------------------------------------------------------

### [Watch 구성 확인하기](https://developer.apple.com/documentation/sensorkit/srwristdetection#Inspecting-Watch-Configuration)

[`var crownOrientation: SRWristDetection.CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.property)

Digital Crown이 사용자 기준으로 어느 방향을 향하는지 나타내는 값입니다.

[`enum CrownOrientation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/crownorientation-swift.enum)

Digital Crown이 착용자 기준으로 향할 수 있는 방향입니다.

[`var onWrist: Bool`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwrist)

watch가 사용자의 손목에 있는지 나타내는 값입니다.

[`var onWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/onwristdate)

사용자가 Apple Watch를 손목에 착용한 날짜와 시간입니다.

[`var offWristDate: Date?`](https://developer.apple.com/documentation/sensorkit/srwristdetection/offwristdate)

사용자가 Apple Watch를 손목에서 벗은 날짜와 시간입니다.

[`var wristLocation: SRWristDetection.WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.property)

사용자가 watch를 착용하는 손목을 나타내는 값입니다.

[`enum WristLocation`](https://developer.apple.com/documentation/sensorkit/srwristdetection/wristlocation-swift.enum)

사용자가 watch를 어느 손목에 착용하는지에 대한 선호입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srwristdetection#relationships)

----------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srwristdetection#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srwristdetection#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srwristdetection#see-also)

------------------------------------------------------------------------------------------

### [Data 해석하기](https://developer.apple.com/documentation/sensorkit/srwristdetection#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 주변 환경의 ambient light 양입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app, website를 사용하는 빈도와 상대적 사용 시간을 나타냅니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard의 구성과 사용 패턴입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object에 대한 사용자 상호 작용입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안 사용자의 Messages app 활동을 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안 사용자의 전화 활동을 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

사용자의 일상적인 이동 루틴에서의 진행 정보입니다.

현재 페이지: SRWristDetection
