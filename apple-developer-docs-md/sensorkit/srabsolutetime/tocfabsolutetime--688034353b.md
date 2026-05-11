---
title: "toCFAbsoluteTime() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime()"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.030986+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime()#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRAbsoluteTime](https://developer.apple.com/documentation/sensorkit/srabsolutetime)
    
*   toCFAbsoluteTime()

instance method

toCFAbsoluteTime()
==================

absolute time을 core-foundation absolute time으로 변환합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    func toCFAbsoluteTime() -> CFAbsoluteTime

[Return Value](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime()#return-value)

-------------------------------------------------------------------------------------------------------------------

core-foundation absolute time입니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime()#see-also)

-----------------------------------------------------------------------------------------------------------

### [시간 범위 정의](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime()#Defining-the-Time-Range)

[`var from: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)

이 시간 이후에 발생한 sample 정보를 가져옵니다.

[`var to: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to)

이 시간 이전에 발생한 sample 정보를 가져옵니다.

[`struct SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime)

system이 data를 기록한 시점을 설명하는 value입니다.

[`static func current() -> SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current())

현재 absolute time을 제공합니다.

현재 페이지는 toCFAbsoluteTime()
