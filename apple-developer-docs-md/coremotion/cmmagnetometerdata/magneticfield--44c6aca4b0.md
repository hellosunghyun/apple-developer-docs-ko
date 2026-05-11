---
title: "magneticField | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.881313+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMagnetometerData](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)
    
*   magneticField

instance property

magneticField
=============

magnetometer가 측정한 magnetic field를 반환합니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var magneticField: CMMagneticField { get }

[논의](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield#Discussion)

---------------------------------------------------------------------------------------------------------------

이 property의 값은 device가 관측한 전체 magnetic field이며, 지구의 geomagnetic field에 device 자체와 주변 환경이 만들어내는 bias가 더해진 값입니다.

이 값은 "raw" magnetic-field 값입니다. device가 만든 bias와 경우에 따라 주변 field의 bias까지 걸러내는 [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
의 [`magneticField`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/magneticfield)
 property가 제공하는 calibrated 값과는 다릅니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield#see-also)

-----------------------------------------------------------------------------------------------------------

### [Field 강도 가져오기](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata/magneticfield#Getting-the-Field-Strength)

[`struct CMMagneticField`](https://developer.apple.com/documentation/coremotion/cmmagneticfield)

3축 magnetometer data를 포함하는 struct입니다.

현재 페이지는 magneticField입니다
