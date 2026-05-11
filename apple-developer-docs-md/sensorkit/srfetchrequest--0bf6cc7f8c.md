---
title: "SRFetchRequest | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srfetchrequest"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.022847+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srfetchrequest#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRFetchRequest

class

SRFetchRequest
==============

sample query의 조건을 정의하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRFetchRequest

[개요](https://developer.apple.com/documentation/sensorkit/srfetchrequest#overview)

----------------------------------------------------------------------------------------

app은 이 class의 instance를 구성해 sensor data를 query할 device를 선택합니다. 시간 범위([`from`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)
, [`to`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to)
)는 framework가 data를 기록한 시점을 지정합니다. fetch query는 app이 먼저 [`startRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())
를 호출해 기록한 sensor data만 가져올 수 있습니다.

fetch request를 실행하려면 app이 이 class의 instance를 sensor reader의 [`fetch(_:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:))
 function에 전달합니다.

framework는 fetch request가 완료되면 sensor reader의 [`delegate`](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate)
에 [`sensorReader(_:didCompleteFetch:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))
로 알립니다. fetch가 실패하면 framework가 delegate의 [`sensorReader(_:fetching:failedWithError:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))
를 호출합니다.

SensorKit은 새로 기록된 data에 24시간 보류 기간을 둔 뒤 app이 접근할 수 있게 합니다. 이렇게 하면 사용자가 app과 공유하고 싶지 않은 data를 삭제할 기회를 얻습니다. fetch request의 시간 범위가 이 보류 기간과 겹치면 결과를 반환하지 않습니다.

[주제](https://developer.apple.com/documentation/sensorkit/srfetchrequest#topics)

------------------------------------------------------------------------------------

### [Selecting the Device](https://developer.apple.com/documentation/sensorkit/srfetchrequest#Selecting-the-Device)

[`var device: SRDevice`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device)

sample data를 query할 device입니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device 표현입니다.

### [Defining the Time Range](https://developer.apple.com/documentation/sensorkit/srfetchrequest#Defining-the-Time-Range)

[`var from: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)

이 시간 이후에 발생한 sample 정보를 fetch합니다.

[`var to: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to)

이 시간 이전에 발생한 sample 정보를 fetch합니다.

[`struct SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime)

system이 data를 기록한 시점을 설명하는 값입니다.

[`static func current() -> SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current())

현재 absolute time을 제공합니다.

[`func toCFAbsoluteTime() -> CFAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime())

absolute time을 core-foundation absolute time으로 변환합니다.

[관계](https://developer.apple.com/documentation/sensorkit/srfetchrequest#relationships)

--------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srfetchrequest#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srfetchrequest#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srfetchrequest#see-also)

----------------------------------------------------------------------------------------

### [Querying data](https://developer.apple.com/documentation/sensorkit/srfetchrequest#Querying-data)

[`class SRFetchResult`](https://developer.apple.com/documentation/sensorkit/srfetchresult)

sensor reader가 fetch한 기록된 data입니다.

현재 페이지는 SRFetchRequest입니다
