---
title: "sensorReader(_:didCompleteFetch:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044590+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:didCompleteFetch:)

instance method

sensorReader(\_:didCompleteFetch:)
==================================

완료된 fetch request를 delegate에 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        didCompleteFetch fetchRequest: SRFetchRequest
    )

[Parameters](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------

`reader`

fetch request를 완료한 reader입니다.

`fetchRequest`

완료된 fetch request입니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------

### [Reading Recorded Data](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:)#Reading-Recorded-Data)

[`func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))

fetch result를 delegate에 제공합니다.

[`func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))

fetch failure reason을 delegate에 제공합니다.

현재 페이지: sensorReader(\_:didCompleteFetch:)
