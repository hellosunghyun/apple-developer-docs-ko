---
title: "sensorReader(_:startRecordingFailedWithError:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.060461+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReaderDelegate](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)
    
*   sensorReader(\_:startRecordingFailedWithError:)

instance method

sensorReader(\_:startRecordingFailedWithError:)
===============================================

reader가 recording을 시작하지 못했을 때 그 이유를 delegate에 전달합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    optional func sensorReader(
        _ reader: SRSensorReader,
        startRecordingFailedWithError error: any Error
    )

[parameter](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------------------------

`reader`

recording 시작에 실패한 sensor reader입니다.

`error`

실패 원인을 설명하는 object입니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:)#see-also)

-----------------------------------------------------------------------------------------------------------------------------------------------

### [data recording](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:)#Recording-Data)

[`func sensorReaderWillStartRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))

reader가 recording을 시작할 때 delegate에 알립니다.

[`func sensorReaderDidStopRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))

reader가 recording을 중지할 때 delegate에 알립니다.

[`func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))

reader가 recording 중지에 실패했을 때 그 이유를 delegate에 전달합니다.

현재 페이지: sensorReader(\_:startRecordingFailedWithError:)
