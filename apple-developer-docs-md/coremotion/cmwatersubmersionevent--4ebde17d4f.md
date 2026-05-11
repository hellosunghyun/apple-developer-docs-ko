---
title: "CMWaterSubmersionEvent | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.876814+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMWaterSubmersionEvent

class

CMWaterSubmersionEvent
======================

device의 submersion state가 변경되었음을 나타내는 event입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    class CMWaterSubmersionEvent

[주제](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#topics)

---------------------------------------------------------------------------------------------

### [event data 접근](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#Accessing-event-data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/date)

event의 날짜와 시간입니다.

[`var state: CMWaterSubmersionEvent.State`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.property)

새로운 submersion state입니다.

[`enum State`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum)

device의 submersion state입니다.

### [초기화 method](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#relationships)

-----------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#see-also)

-------------------------------------------------------------------------------------------------

### [Water submersion](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent#Water-submersion)

[submersion data 접근](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

water-submersion manager를 사용해 Apple Watch Ultra에서 water pressure, temperature, depth data를 받습니다.

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

submersion 중 pressure와 temperature data 수집을 관리하는 object입니다.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

ambient pressure, water pressure, water temperature, submersion event update를 받는 delegate입니다.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

pressure와 depth data를 담는 update입니다.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

water temperature data를 담는 update입니다.

현재 페이지는 CMWaterSubmersionEvent입니다.
