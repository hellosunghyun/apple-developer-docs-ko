---
title: "sensorReaderDidStopRecording(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.037096+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReaderDidStopRecording(\_:)

instance method

sensorReaderDidStopRecording(\_:)
=================================

reader가 recording을 중지하면 delegate에 알립니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReaderDidStopRecording(_ reader: SRSensorReader)

[Parameters](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------------

`reader`

recording을 중지한 reader입니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:)#see-also)

---------------------------------------------------------------------------------------------------------------------------------

### [Recording Data](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:)#Recording-Data)

[`func sensorReaderWillStartRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))

reader가 recording을 시작하면 delegate에 알립니다.

[`func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:))

reader가 recording에 실패했을 때 그 이유를 delegate에 제공합니다.

[`func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))

reader가 recording 중지에 실패했을 때 그 이유를 delegate에 제공합니다.

현재 페이지는 sensorReaderDidStopRecording(\_:)입니다
