---
title: "ambientLightSensor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.046963+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   ambientLightSensor

type property

ambientLightSensor
==================

ambient light 정보를 제공하는 sensor입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    static let ambientLightSensor: SRSensor

[논의](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor#Discussion)

---------------------------------------------------------------------------------------------------------

이 sensor의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type은 [`SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)
입니다.

information property list의 [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail)
 key에 [`SRSensorUsageAmbientLightSensor`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageAmbientLightSensor)
 dictionary를 추가해 ambient light를 기록하는 이유를 제공해야 합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor#see-also)

-----------------------------------------------------------------------------------------------------

### [환경 sensor 읽기](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor#Reading-environment-sensors)

[`static let ambientPressure: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure)

pressure와 temperature metric을 제공하는 sensor입니다.

현재 페이지: ambientLightSensor
