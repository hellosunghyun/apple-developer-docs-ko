---
title: "ambientPressure | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.042557+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   ambientPressure

type property

ambientPressure
===============

pressure와 temperature metric을 제공하는 sensor입니다.

iOS 15.4+iPadOS 15.4+Mac Catalyst 15.4+

    static let ambientPressure: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure#Discussion)

------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 `[`[`CMRecordedPressureData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedPressureData)`]`입니다.

ambient pressure를 기록하는 이유를 제공하려면 information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageElevation`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageElevation)
 dictionary를 추가해야 합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure#see-also)

--------------------------------------------------------------------------------------------------

### [환경 sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure#Reading-environment-sensors)

[`static let ambientLightSensor: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor)

ambient light 정보를 제공하는 sensor입니다.

현재 페이지: ambientPressure
