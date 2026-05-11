---
title: "to | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srfetchrequest/to"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.033575+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRFetchRequest](https://developer.apple.com/documentation/sensorkit/srfetchrequest)
    
*   to

instance property

to
==

이 시각 이전에 발생한 sample 정보를 fetch합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var to: SRAbsoluteTime { get set }

[설명](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to#Discussion)

-----------------------------------------------------------------------------------------------

framework는 app이 이 property의 value를 정의하도록 요구합니다. app이 이 property를 정의하지 않으면 framework는 [`SRError.Code.fetchRequestInvalid`](https://developer.apple.com/documentation/sensorkit/srerror/code/fetchrequestinvalid)
를 [`sensorReader(_:fetching:failedWithError:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))
를 통해 reader delegate에 전달해 fetch에 응답합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to#see-also)

-------------------------------------------------------------------------------------------

### [시간 범위 정의](https://developer.apple.com/documentation/sensorkit/srfetchrequest/to#Defining-the-Time-Range)

[`var from: SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/from)

이 시각 이후에 발생한 sample 정보를 fetch합니다.

[`struct SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime)

system이 data를 기록한 시점을 설명하는 value입니다.

[`static func current() -> SRAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current())

현재 absolute time을 제공합니다.

[`func toCFAbsoluteTime() -> CFAbsoluteTime`](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime())

absolute time을 core-foundation absolute time으로 변환합니다.

현재 페이지: to
