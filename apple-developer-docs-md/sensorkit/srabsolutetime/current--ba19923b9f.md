---
title: "current() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srabsolutetime/current()"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.031152+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current()#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRAbsoluteTime](https://developer.apple.com/documentation/sensorkit/srabsolutetime)
    
*   current()

type method

current()
=========

현재 absolute time을 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static func current() -> SRAbsoluteTime

[Return Value](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current()#return-value)

----------------------------------------------------------------------------------------------------------

현재 device의 absolute time입니다.

[논의](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current()#Discussion)

------------------------------------------------------------------------------------------------------

각 device는 자체 absolute time을 가집니다. 이 function은 [`current`](https://developer.apple.com/documentation/sensorkit/srdevice/current)
 device의 absolute time을 반환합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current()#see-also)

--------------------------------------------------------------------------------------------------

### [시간 범위 정의](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current()#Defining-the-Time-Range)

[`var from: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)

이 시각 이후에 발생한 sample 정보를 가져옵니다.

[`var to: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to)

이 시각 이전에 발생한 sample 정보를 가져옵니다.

[`struct SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime)

system이 data를 기록하는 시점을 설명하는 값입니다.

[`func toCFAbsoluteTime() -> CFAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime())

absolute time을 core-foundation absolute time으로 변환합니다.

현재 페이지는 current()입니다
