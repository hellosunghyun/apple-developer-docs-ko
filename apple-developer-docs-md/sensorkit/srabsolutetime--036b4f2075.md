---
title: "SRAbsoluteTime | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srabsolutetime"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.033442+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srabsolutetime#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRAbsoluteTime

struct

SRAbsoluteTime
==============

system이 data를 기록한 시점을 설명하는 value입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    struct SRAbsoluteTime

[설명](https://developer.apple.com/documentation/sensorkit/srabsolutetime#Discussion)

--------------------------------------------------------------------------------------------

이 value는 재부팅 이후에도 계속 추적하는 [`mach_continuous_time`](https://developer.apple.com/documentation/kernel/1646199-mach_continuous_time)
과 달리, 단조 증가하는 device별 시간을 추적합니다.

Although a fetch can query a [`device`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device)
 other than a phone (such as a paired watch), the framework consistently describes time according to the phone. Any fetch results from a paired watch are in the phone’s version of [`SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime)
.

[주제](https://developer.apple.com/documentation/sensorkit/srabsolutetime#topics)

------------------------------------------------------------------------------------

### [Absolute Time 생성](https://developer.apple.com/documentation/sensorkit/srabsolutetime#Creating-an-Absolute-Time)

[`init(CFTimeInterval)`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/init(_:))

raw value에서 absolute time을 생성합니다.

[`init(rawValue: CFTimeInterval)`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/init(rawvalue:))

raw value에서 absolute time을 생성합니다.

### [현재 Absolute Time 접근](https://developer.apple.com/documentation/sensorkit/srabsolutetime#Accessing-the-Current-Absolute-Time)

[`static func current() -> SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current())

현재 absolute time을 제공합니다.

### [Absolute Time 변환](https://developer.apple.com/documentation/sensorkit/srabsolutetime#Converting-Absolute-Times)

[`func toCFAbsoluteTime() -> CFAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime())

absolute time을 core-foundation absolute time으로 변환합니다.

[관계](https://developer.apple.com/documentation/sensorkit/srabsolutetime#relationships)

--------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srabsolutetime#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srabsolutetime#see-also)

----------------------------------------------------------------------------------------

### [시간 범위 정의](https://developer.apple.com/documentation/sensorkit/srabsolutetime#Defining-the-Time-Range)

[`var from: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)

이 시간 이후에 발생한 sample 정보를 가져옵니다.

[`var to: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to)

이 시간 이전에 발생한 sample 정보를 가져옵니다.

[`static func current() -> SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current())

현재 absolute time을 제공합니다.

[`func toCFAbsoluteTime() -> CFAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime())

absolute time을 core-foundation absolute time으로 변환합니다.

현재 페이지는 SRAbsoluteTime
