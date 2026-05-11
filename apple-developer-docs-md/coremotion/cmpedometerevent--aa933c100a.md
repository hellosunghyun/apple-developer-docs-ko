---
title: "CMPedometerEvent | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerevent"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.888823+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerevent#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMPedometerEvent

class

CMPedometerEvent
================

사용자의 pedestrian activity 변화입니다.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 3.0+

    class CMPedometerEvent

[주제](https://developer.apple.com/documentation/coremotion/cmpedometerevent#topics)

---------------------------------------------------------------------------------------

### [Pedometer Data](https://developer.apple.com/documentation/coremotion/cmpedometerevent#Pedometer-Data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmpedometerevent/date)

pedometer event가 기록된 날짜입니다.

[`var type: CMPedometerEventType`](https://developer.apple.com/documentation/coremotion/cmpedometerevent/type)

발생한 변경의 type입니다.

[`enum CMPedometerEventType`](https://developer.apple.com/documentation/coremotion/cmpedometereventtype)

사용자의 pedestrian activity에 발생한 변경을 나타내는 constant입니다.

### [이니셜라이저](https://developer.apple.com/documentation/coremotion/cmpedometerevent#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmpedometerevent/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmpedometerevent#relationships)

-----------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmpedometerevent#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmpedometerevent#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmpedometerevent#see-also)

-------------------------------------------------------------------------------------------

### [Pedometer 및 fitness](https://developer.apple.com/documentation/coremotion/cmpedometerevent#Pedometer-and-fitness)

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

system이 생성한 실시간 walking data를 가져오는 object입니다.

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

사용자가 도보로 이동한 거리에 대한 정보입니다.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

사용자가 device를 들고 걸으며 이동한 step 수입니다.

지원 중단됨

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

workout용 odometer data를 나타내는 class입니다.

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

1Hz로 수집한 heart rate data를 나타내는 class입니다.

현재 페이지는 CMPedometerEvent입니다
