---
title: "CMOdometerOriginDevice | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerorigindevice"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.893541+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMOdometerOriginDevice

enum

CMOdometerOriginDevice
======================

odometer sample이 시작된 device입니다.

iOS 15.4+iPadOS 15.4+Mac Catalyst 15.4+macOS 10.15+visionOS 1.0+watchOS 8.4+

    enum CMOdometerOriginDevice

[주제](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#topics)

---------------------------------------------------------------------------------------------

### [device origin](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#Device-origins)

[`case unknown`](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice/unknown)

odometer sample의 origin을 알 수 없습니다.

[`case local`](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice/local)

odometer sample의 origin이 sample을 요청한 동일한 device입니다.

[`case remote`](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice/remote)

odometer sample의 origin이 local device와 페어링된 device입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#relationships)

-----------------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#see-also)

-------------------------------------------------------------------------------------------------

### [device 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice#Getting-the-device)

[`var originDevice: CMOdometerOriginDevice`](https://developer.apple.com/documentation/coremotion/cmodometerdata/origindevice)

data를 측정한 device입니다.

현재 페이지는 CMOdometerOriginDevice입니다
