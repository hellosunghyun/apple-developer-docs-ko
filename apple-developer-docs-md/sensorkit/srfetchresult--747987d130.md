---
title: "SRFetchResult | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srfetchresult"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.023776+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srfetchresult#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRFetchResult

class

SRFetchResult
=============

sensor reader가 fetch한 기록 data입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRFetchResult<SampleType> where SampleType : AnyObject

[개요](https://developer.apple.com/documentation/sensorkit/srfetchresult#overview)

---------------------------------------------------------------------------------------

sensor reader의 [`delegate`](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate)
는 fetch 요청이 성공적으로 끝나면 [`sensorReader(_:didCompleteFetch:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))
에서 이 class의 instance를 받습니다.

result는 sample 형태이며, type은 reader의 sensor에 따라 달라집니다. sensor별 sample type 목록은 [Sample types](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#Sample-types)
를 참고하십시오.

[주제](https://developer.apple.com/documentation/sensorkit/srfetchresult#topics)

-----------------------------------------------------------------------------------

### [sample data](https://developer.apple.com/documentation/sensorkit/srfetchresult#Sampling-Data)

[`var sample: SampleType`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)

sensor reader가 fetch한 recording입니다.

[`var timestamp: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchresult/timestamp)

framework가 sample을 기록한 시각입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srfetchresult#relationships)

-------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srfetchresult#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srfetchresult#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srfetchresult#see-also)

---------------------------------------------------------------------------------------

### [data query](https://developer.apple.com/documentation/sensorkit/srfetchresult#Querying-data)

[`class SRFetchRequest`](https://developer.apple.com/documentation/sensorkit/srfetchrequest)

sample query의 조건을 정의하는 object입니다.

현재 페이지는 SRFetchResult입니다.
