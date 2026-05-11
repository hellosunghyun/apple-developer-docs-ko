---
title: "stopRecording() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording()"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043856+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording()#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   stopRecording()

instance method

stopRecording()
===============

sensor data recording을 중지합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    func stopRecording()

[설명](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording()#Discussion)

------------------------------------------------------------------------------------------------------------

이 function은 framework에 이 reader의 sensor recording을 중지하도록 요청합니다. framework는 이 device와 페어링된 모든 device에서 recording합니다. framework가 recording하는 전체 device 목록을 얻으려면 [`fetchDevices()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())
 를 호출합니다.

framework는 같은 app 안의 여러 reader 또는 같은 system의 서로 다른 app에서 하나의 sensor를 동시에 recording할 수 있게 합니다. 따라서 이 function은 caller가 reader의 sensor recording에 대한 관심을 포기한다는 의미를 가집니다.

성공하면 framework는 delegate의 [`sensorReaderDidStopRecording(_:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))
 callback을 호출합니다. 실패하면 framework는 delegate의 [`sensorReader(_:stopRecordingFailedWithError:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))
 를 호출합니다.

이 function이 성공하려면 reader가 authorization을 받아야 합니다([`authorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)
 참고).

[참고 항목](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording()#see-also)

--------------------------------------------------------------------------------------------------------

### [sensor data recording](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording()#Recording-sensor-data)

[`func startRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())

sensor data recording을 시작합니다.

현재 페이지: stopRecording()
