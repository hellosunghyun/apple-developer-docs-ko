---
title: "sensorReader(_:didChange:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044405+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:didChange:)

instance method

sensorReader(\_:didChange:)
===========================

reader의 새 authorization status를 delegate에 알립니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        didChange authorizationStatus: SRAuthorizationStatus
    )

[Parameters](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------

`reader`

authorization 상태가 바뀐 sensor reader입니다.

`authorizationStatus`

framework가 sensor reader를 authorize했는지 나타내는 flag입니다.

현재 페이지: sensorReader(\_:didChange:)
