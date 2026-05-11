---
title: "chromaticity | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.046624+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRAmbientLightSample](https://developer.apple.com/documentation/sensorkit/srambientlightsample)
    
*   chromaticity

instance property

chromaticity
============

sample의 light 밝기와 tint를 설명하는 coordinate 쌍입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var chromaticity: SRAmbientLightSample.Chromaticity { get }

[참고 항목](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property#see-also)

--------------------------------------------------------------------------------------------------------------------------

### [light level 측정](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property#Measuring-light-level)

[`struct Chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct)

light 밝기와 tint를 설명하는 coordinate 쌍입니다.

[`var lux: Measurement<UnitIlluminance>`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/lux)

sample의 luminous flux를 설명하는 object입니다.

[`var placement: SRAmbientLightSample.SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/placement)

sensor를 기준으로 한 light 위치입니다.

[`enum SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement)

sensor를 기준으로 light source 위치를 설명하는 방향 값입니다.

현재 페이지는 chromaticity입니다
