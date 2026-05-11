---
title: "SRAmbientLightSample.Chromaticity | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.046281+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRAmbientLightSample](https://developer.apple.com/documentation/sensorkit/srambientlightsample)
    
*   SRAmbientLightSample.Chromaticity

struct

SRAmbientLightSample.Chromaticity
=================================

빛의 밝기와 색조를 설명하는 좌표 쌍입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    struct Chromaticity

[개요](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#overview)

------------------------------------------------------------------------------------------------------------------------

[`SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)
 class는 [`chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property)
 property를 통해 이 structure instance에 대한 read-only access를 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#topics)

--------------------------------------------------------------------------------------------------------------------

### [Chromaticity 만들기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#Creating-a-Chromaticity)

[`init()`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct/init())

chromaticity instance를 생성합니다.

[`init(x: Float32, y: Float32)`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct/init(x:y:))

argument 좌표 쌍으로 chromaticity instance를 생성합니다.

### [chromaticity 설정하기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#Setting-chromaticity)

[`var x: Float32`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct/x)

chromaticity x값입니다.

[`var y: Float32`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct/y)

chromaticity y값입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#relationships)

----------------------------------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#see-also)

------------------------------------------------------------------------------------------------------------------------

### [광량 측정하기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct#Measuring-light-level)

[`var chromaticity: SRAmbientLightSample.Chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property)

sample의 빛 밝기와 색조를 설명하는 좌표 쌍입니다.

[`var lux: Measurement<UnitIlluminance>`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/lux)

sample의 luminous flux를 설명하는 object입니다.

[`var placement: SRAmbientLightSample.SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/placement)

sensor를 기준으로 한 빛의 위치입니다.

[`enum SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement)

sensor를 기준으로 광원의 위치를 설명하는 방향 값입니다.

현재 페이지: SRAmbientLightSample.Chromaticity
