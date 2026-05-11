---
title: "device | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srfetchrequest/device"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045816+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRFetchRequest](https://developer.apple.com/documentation/sensorkit/srfetchrequest)
    
*   device

instance property

device
======

sample data를 query할 device입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var device: SRDevice { get set }

[설명](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device#Discussion)

---------------------------------------------------------------------------------------------------

app이 이 property 값을 정의하지 않으면 framework가 현재 device를 query합니다. 사용 가능한 device 목록을 가져오려면 app이 sensor reader에서 [`fetchDevices()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())
를 호출합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device#see-also)

-----------------------------------------------------------------------------------------------

### [Device 선택](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device#Selecting-the-Device)

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device 표현입니다.

현재 페이지는 device입니다
