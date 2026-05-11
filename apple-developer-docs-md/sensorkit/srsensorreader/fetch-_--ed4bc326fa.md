---
title: "fetch(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:)"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.043948+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:)#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   fetch(\_:)

instance method

fetch(\_:)
==========

fetch request가 지정한 sample을 가져옵니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    func fetch(_ request: SRFetchRequest)

[파라미터](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:)#parameters)

------------------------------------------------------------------------------------------------------

`request`

sample을 가져올 device와 관심 있는 sample 기간을 설명하는 object입니다.

[설명](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:)#설명)

------------------------------------------------------------------------------------------------------

app은 caller의 sensor data에 접근할 때 이 function를 호출합니다.

Upon success, the framework delivers results in the form of _samples_ via the delegate’s [`sensorReader(_:fetching:didFetchResult:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))
callback으로 결과를 전달합니다. 이 function가 여러 sample을 반환하면 framework는 delegate를 여러 번 호출합니다.

The framework returns sensor data only for the argument fetch-object’s device, and that’s dated only within the argument fetch-object’s time window. Within that window, this function returns only the data that the framework recorded (see [`startRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())
), and that the framework hasn’t deleted (see [`SRDeletionRecord`](https://developer.apple.com/documentation/sensorkit/srdeletionrecord)
).

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:)#see-also)

--------------------------------------------------------------------------------------------------

### [기록된 data 읽기](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:)#Reading-recorded-data)

[`func fetchDevices()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())

이 reader의 sensor data를 저장하는 모든 device의 정보를 가져옵니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device의 표현입니다.

현재 페이지: fetch(\_:)
