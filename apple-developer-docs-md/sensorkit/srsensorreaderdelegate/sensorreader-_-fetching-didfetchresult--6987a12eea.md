---
title: "sensorReader(_:fetching:didFetchResult:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044683+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:fetching:didFetchResult:)

instance method

sensorReader(\_:fetching:didFetchResult:)
=========================================

delegate에 fetch result를 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        fetching fetchRequest: SRFetchRequest,
        didFetchResult result: SRFetchResult<AnyObject>
    ) -> Bool

[parameter](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

`reader`

fetch가 result를 제공하는 sensor reader입니다.

`fetchRequest`

완료된 fetch request입니다.

`result`

fetch request의 result입니다.

[설명](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:)#Discussion)

---------------------------------------------------------------------------------------------------------------------------------------------

framework는 app이 reader의 sensor를 바탕으로 result type을 알고 있다고 가정합니다. sensor별 result type 목록은 [Sample types](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#Sample-types)
.

fetch가 여러 result를 생성하면 framework는 각 result마다 이 callback을 한 번씩 호출합니다.

이 function 범위 안에서 fetch result를 재사용하려면 strong reference를 할당하지 말고 `fetchResult`의 복사본을 만듭니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------

### [기록된 data 읽기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:)#Reading-Recorded-Data)

[`func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))

delegate에 완료된 fetch request를 제공합니다.

[`func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))

delegate에 fetch 실패 이유를 제공합니다.

현재 페이지: sensorReader(\_:fetching:didFetchResult:)
