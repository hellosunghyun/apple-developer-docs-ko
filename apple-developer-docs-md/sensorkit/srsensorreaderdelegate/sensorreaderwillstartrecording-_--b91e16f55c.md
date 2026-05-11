---
title: "sensorReaderWillStartRecording(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.060554+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReaderWillStartRecording(\_:)

instance method

sensorReaderWillStartRecording(\_:)
===================================

reader가 recording을 시작할 때 delegate에 알립니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReaderWillStartRecording(_ reader: SRSensorReader)

[파라미터](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------

`reader`

recording을 시작하는 reader입니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------

### [data recording](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:)#Recording-Data)

[`func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:))

reader가 recording에 실패했을 때 delegate에 이유를 제공합니다.

[`func sensorReaderDidStopRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))

reader가 recording을 중지할 때 delegate에 알립니다.

[`func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))

reader가 recording 중지에 실패했을 때 delegate에 이유를 제공합니다.

현재 페이지는 sensorReaderWillStartRecording(\_:)입니다
