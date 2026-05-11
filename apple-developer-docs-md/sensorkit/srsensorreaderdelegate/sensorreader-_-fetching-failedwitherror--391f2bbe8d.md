---
title: "sensorReader(_:fetching:failedWithError:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045906+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:fetching:failedWithError:)

instance method

sensorReader(\_:fetching:failedWithError:)
==========================================

delegate에 fetch 실패 이유를 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        fetching fetchRequest: SRFetchRequest,
        failedWithError error: any Error
    )

[파라미터](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:)#parameters)

----------------------------------------------------------------------------------------------------------------------------------------------

`reader`

fetch가 실패한 sensor reader입니다.

`fetchRequest`

원래의 fetch request입니다.

`error`

실패 원인을 설명하는 object입니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------

### [기록된 data 읽기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:)#Reading-Recorded-Data)

[`func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))

delegate에 fetch result를 제공합니다.

[`func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))

delegate에 완료된 fetch request를 제공합니다.

현재 페이지: sensorReader(\_:fetching:failedWithError:)
