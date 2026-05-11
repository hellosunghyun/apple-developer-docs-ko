---
title: "startRecording() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording()"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043756+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording()#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   startRecording()

instance method

startRecording()
================

sensor data recording을 시작합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    func startRecording()

[설명](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording()#Discussion)

-------------------------------------------------------------------------------------------------------------

이 function은 framework에 이 reader의 sensor recording을 시작하라고 지시합니다. framework는 이 device와 pairing된 모든 device에서 recording합니다. framework가 recording하는 전체 device 목록을 얻으려면 [`fetchDevices()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())
를 호출합니다.

framework는 같은 app 안이든 같은 system의 다른 app이든 여러 reader가 하나의 sensor를 동시에 recording하도록 허용합니다. 이 function을 여러 번 호출해도 framework는 sensor recording이 활성 상태인지 확인만 합니다.

성공하면 framework는 delegate의 [`sensorReaderWillStartRecording(_:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))
callback을 호출합니다. 실패하면 framework는 delegate의 [`sensorReader(_:startRecordingFailedWithError:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:))
를 호출합니다.

이 function이 성공하려면 reader에 authorization이 있어야 합니다([`authorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)
 참고).

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording()#see-also)

---------------------------------------------------------------------------------------------------------

### [sensor data recording](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording()#Recording-sensor-data)

[`func stopRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording())

sensor data recording을 중지합니다.

현재 페이지는 startRecording()입니다.
