---
title: "SRSensorReaderDelegate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044300+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRSensorReaderDelegate

protocol

SRSensorReaderDelegate
======================

framework가 sensor 관련 event를 app에 알릴 때 호출하는 callback 집합입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    protocol SRSensorReaderDelegate : NSObjectProtocol

[개요](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#overview)

------------------------------------------------------------------------------------------------

sensor data에 접근하려면 object를 delegate로 할당하고 callback을 구현합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#topics)

--------------------------------------------------------------------------------------------

### [Authorization status 확인하기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#Checking-Authorization-Status)

[`func sensorReader(SRSensorReader, didChange: SRAuthorizationStatus)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:))

reader의 새로운 authorization status를 delegate에 알립니다.

### [Device 가져오기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#Fetching-Devices)

[`func sensorReader(SRSensorReader, didFetch: [SRDevice])`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:))

하나 이상의 device를 delegate에 전달합니다.

[`func sensorReader(SRSensorReader, fetchDevicesDidFailWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:))

reader가 device를 가져오지 못했을 때 이유를 delegate에 전달합니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device 표현입니다.

### [data 기록하기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#Recording-Data)

[`func sensorReaderWillStartRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))

reader가 기록을 시작할 때 delegate에 알립니다.

[`func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:))

reader가 기록하지 못했을 때 이유를 delegate에 전달합니다.

[`func sensorReaderDidStopRecording(SRSensorReader)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))

reader가 기록을 중지할 때 delegate에 알립니다.

[`func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))

reader가 기록을 중지하지 못했을 때 이유를 delegate에 전달합니다.

### [기록된 data 읽기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#Reading-Recorded-Data)

[`func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))

fetch result를 delegate에 전달합니다.

[`func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))

완료된 fetch request를 delegate에 전달합니다.

[`func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))

fetch 실패 이유를 delegate에 전달합니다.

### [Error 해석하기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#Interpreting-Errors)

[`let SRErrorDomain: String`](https://developer.apple.com/documentation/sensorkit/srerrordomain)

framework 고유의 error domain입니다.

[`struct SRError`](https://developer.apple.com/documentation/sensorkit/srerror)

SensorKit이 보고하는 error입니다.

[`enum Code`](https://developer.apple.com/documentation/sensorkit/srerror/code)

recording 또는 fetch를 중단시키는 문제 유형입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#relationships)

----------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#inherits-from)

*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#see-also)

------------------------------------------------------------------------------------------------

### [sensor event에 응답하기](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate#Responding-to-sensor-events)

[`var delegate: (any SRSensorReaderDelegate)?`](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate)

sensor 관련 event에 응답하는 object입니다.

현재 페이지: SRSensorReaderDelegate
