---
title: "SRDeletionReason | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeletionreason"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045531+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeletionreason#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRDeletionReason

enum

SRDeletionReason
================

framework가 sample을 삭제하는 이유입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum SRDeletionReason

[주제](https://developer.apple.com/documentation/sensorkit/srdeletionreason#topics)

--------------------------------------------------------------------------------------

### [Reasons](https://developer.apple.com/documentation/sensorkit/srdeletionreason#Reasons)

[`case ageLimit`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/agelimit)

sample이 framework의 보관 한도를 넘겼음을 나타냅니다.

[`case lowDiskSpace`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/lowdiskspace)

system의 disk space가 부족함을 나타냅니다.

[`case noInterestedClients`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients)

sensor에 활성 stakeholder가 없음을 나타냅니다.

[`case systemInitiated`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/systeminitiated)

system이 삭제를 요청했음을 나타냅니다.

[`case userInitiated`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/userinitiated)

user가 삭제를 요청했음을 나타냅니다.

### [initializer](https://developer.apple.com/documentation/sensorkit/srdeletionreason#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srdeletionreason#relationships)

----------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srdeletionreason#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeletionreason#see-also)

------------------------------------------------------------------------------------------

### [Accessing the Deletion Reason](https://developer.apple.com/documentation/sensorkit/srdeletionreason#Accessing-the-Deletion-Reason)

[`var reason: SRDeletionReason`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord/reason)

framework가 sample을 삭제한 이유입니다.

현재 페이지: SRDeletionReason
