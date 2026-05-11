---
title: "CMPedometerEventType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometereventtype"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891217+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMPedometerEventType

enum

CMPedometerEventType
====================

사용자의 보행 activity에 발생한 변화를 나타내는 constant입니다.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 3.0+

    enum CMPedometerEventType

[주제](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#topics)

-------------------------------------------------------------------------------------------

### [enum case](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#Enumeration-Cases)

[`case pause`](https://developer.apple.com/documentation/coremotion/cmpedometereventtype/pause)

사용자의 보행 activity가 중단되었습니다.

[`case resume`](https://developer.apple.com/documentation/coremotion/cmpedometereventtype/resume)

사용자의 보행 activity가 다시 시작되었습니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmpedometereventtype/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#relationships)

---------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#see-also)

-----------------------------------------------------------------------------------------------

### [Pedometer Data](https://developer.apple.com/documentation/coremotion/cmpedometereventtype#Pedometer-Data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmpedometerevent/date)

pedometer event가 기록된 날짜입니다.

[`var type: CMPedometerEventType`](https://developer.apple.com/documentation/coremotion/cmpedometerevent/type)

발생한 변화의 type입니다.

현재 페이지는 CMPedometerEventType입니다
