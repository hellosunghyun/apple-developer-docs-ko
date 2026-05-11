---
title: "CMFallDetectionEvent | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionevent"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.898320+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMFallDetectionEvent

class

CMFallDetectionEvent
====================

fall detection event에 대한 data를 포함하는 object입니다.

watchOS 7.2+

    class CMFallDetectionEvent

[주제](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#topics)

-------------------------------------------------------------------------------------------

### [Fall data에 접근하기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#Accessing-Fall-Data)

[`var resolution: CMFallDetectionEvent.UserResolution`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/resolution)

event의 resolution입니다.

[`enum UserResolution`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution)

fall detection event에 대한 user resolution입니다.

### [event 날짜 가져오기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#Getting-the-event-date)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/date)

event의 시각과 날짜입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#relationships)

---------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#see-also)

-----------------------------------------------------------------------------------------------

### [Fall detection](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent#Fall-detection)

[`class CMFallDetectionManager`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)

fall detection event를 관리하는 object입니다.

[`protocol CMFallDetectionDelegate`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)

fall detection event 정보와 authorization status 변경을 받는 delegate입니다.

[`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription)

fall detection event data 접근 권한을 요청하는 이유를 사용자에게 설명하는 메시지입니다.

현재 페이지: CMFallDetectionEvent
