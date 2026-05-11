---
title: "fetchDevices() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices()"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044040+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices()#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader)
    
*   fetchDevices()

instance method

fetchDevices()
==============

이 reader의 sensor용 data를 저장하는 모든 device의 정보를 가져옵니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    func fetchDevices()

[논의](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices()#Discussion)

-----------------------------------------------------------------------------------------------------------

성공하면 framework가 [`sensorReader(_:didFetch:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:))
 를 통해 device array를 delegate에 제공합니다. 실패하면 framework가 delegate의 [`sensorReader(_:fetchDevicesDidFailWithError:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:))
 callback을 호출합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices()#see-also)

-------------------------------------------------------------------------------------------------------

### [Reading recorded data](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices()#Reading-recorded-data)

[`func fetch(SRFetchRequest)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:))

fetch request가 지정한 sample을 가져옵니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device를 표현한 class입니다.

현재 페이지: fetchDevices()
