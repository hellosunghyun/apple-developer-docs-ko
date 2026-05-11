---
title: "sensorReader(_:stopRecordingFailedWithError:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.037196+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:stopRecordingFailedWithError:)

instance method

sensorReader(\_:stopRecordingFailedWithError:)
==============================================

reader가 recording을 중지하지 못했을 때 delegate에 그 이유를 제공합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        stopRecordingFailedWithError error: any Error
    )

[Parameters](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------

`reader`

recording을 중지하지 못한 sensor reader입니다.

`error`

실패 원인을 설명하는 object입니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------------

### [Recording Data](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:)#Recording-Data)

[`func sensorReaderWillStartRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))

reader가 recording을 시작할 때 delegate에 알립니다.

[`func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:))

reader가 recording하지 못했을 때 delegate에 그 이유를 제공합니다.

[`func sensorReaderDidStopRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))

reader가 recording을 중지할 때 delegate에 알립니다.

현재 페이지: sensorReader(\_:stopRecordingFailedWithError:)
