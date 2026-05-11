---
title: "identifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.873133+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMRecordedAccelerometerData](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)
    
*   identifier

instance property

identifier
==========

accelerometer data의 고유 identifier입니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var identifier: UInt64 { get }

[논의](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier#Discussion)

---------------------------------------------------------------------------------------------------------------------

Accelerometer data는 batch 단위로 기록되며 각 batch에 고유 identifier가 할당됩니다. 이 property에는 이 sample이 기록된 batch의 identifier가 들어 있습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier#see-also)

-----------------------------------------------------------------------------------------------------------------

### [Getting the Accelerometer Data](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier#Getting-the-Accelerometer-Data)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/startdate)

sensor sample이 기록된 wall clock 시간입니다.

현재 페이지: identifier
