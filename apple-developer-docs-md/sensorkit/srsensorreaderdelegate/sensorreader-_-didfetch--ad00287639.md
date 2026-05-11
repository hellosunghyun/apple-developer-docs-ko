---
title: "sensorReader(_:didFetch:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.060365+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:didFetch:)

instance method

sensorReader(\_:didFetch:)
==========================

delegate에 하나 이상의 device를 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        didFetch devices: [SRDevice]
    )

[parameter](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:)#parameters)

------------------------------------------------------------------------------------------------------------------------------

`reader`

device를 가져온 sensor reader입니다.

`devices`

가져온 device입니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:)#see-also)

--------------------------------------------------------------------------------------------------------------------------

### [device 가져오기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:)#Fetching-Devices)

[`func sensorReader(SRSensorReader, fetchDevicesDidFailWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:))

reader가 device를 가져오지 못했을 때 그 이유를 delegate에 제공합니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device 표현입니다.

현재 페이지는 sensorReader(\_:didFetch:)
