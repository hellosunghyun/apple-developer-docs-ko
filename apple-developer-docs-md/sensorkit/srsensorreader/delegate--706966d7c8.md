---
title: "delegate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044218+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   delegate

instance property

delegate
========

sensor 관련 event에 응답하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    weak var delegate: (any SRSensorReaderDelegate)? { get set }

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate#see-also)

-------------------------------------------------------------------------------------------------

### [sensor event에 응답하기](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate#Responding-to-sensor-events)

[`protocol SRSensorReaderDelegate`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)

framework가 app에 sensor 관련 event를 알리기 위해 호출하는 callback 집합입니다.

현재 페이지: delegate
