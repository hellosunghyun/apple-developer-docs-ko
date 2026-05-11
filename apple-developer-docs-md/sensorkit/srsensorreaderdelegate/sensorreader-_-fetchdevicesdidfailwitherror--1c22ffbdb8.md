---
title: "sensorReader(_:fetchDevicesDidFailWithError:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.060784+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:fetchDevicesDidFailWithError:)

instance method

sensorReader(\_:fetchDevicesDidFailWithError:)
==============================================

reader가 device를 가져오지 못했을 때 그 이유를 delegate에 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        fetchDevicesDidFailWithError error: any Error
    )

[Parameters](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------

`reader`

device를 가져오지 못한 reader입니다.

`error`

실패 원인을 설명하는 object입니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------------

### [Fetching Devices](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:)#Fetching-Devices)

[`func sensorReader(SRSensorReader, didFetch: [SRDevice])`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:))

하나 이상의 device를 delegate에 제공합니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device의 표현입니다.

현재 페이지: sensorReader(\_:fetchDevicesDidFailWithError:)
