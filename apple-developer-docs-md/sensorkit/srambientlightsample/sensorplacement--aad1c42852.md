---
title: "SRAmbientLightSample.SensorPlacement | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.045997+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRAmbientLightSample](https://developer.apple.com/documentation/sensorkit/srambientlightsample)
    
*   SRAmbientLightSample.SensorPlacement

enum

SRAmbientLightSample.SensorPlacement
====================================

sensor를 기준으로 light source 위치를 설명하는 방향 값입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum SensorPlacement

[주제](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#topics)

----------------------------------------------------------------------------------------------------------

### [배치 구성](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#Placement-configurations)

[`case frontBottom`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/frontbottom)

light source가 sensor의 아래쪽에 있음을 나타냅니다.

[`case frontBottomLeft`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/frontbottomleft)

light source가 sensor의 왼쪽 아래에 있음을 나타냅니다.

[`case frontBottomRight`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/frontbottomright)

light source가 sensor의 오른쪽 아래에 있음을 나타냅니다.

[`case frontLeft`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/frontleft)

light source가 sensor의 왼쪽에 있음을 나타냅니다.

[`case frontRight`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/frontright)

light source가 sensor의 오른쪽에 있음을 나타냅니다.

[`case frontTop`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/fronttop)

light source가 sensor의 위쪽에 있음을 나타냅니다.

[`case frontTopLeft`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/fronttopleft)

light source가 sensor의 왼쪽 위에 있음을 나타냅니다.

[`case frontTopRight`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/fronttopright)

light source가 sensor의 오른쪽 위에 있음을 나타냅니다.

[`case unknown`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/unknown)

sensor가 light source 위치를 판단할 수 없음을 나타냅니다.

### [initializer](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#relationships)

------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#see-also)

--------------------------------------------------------------------------------------------------------------

### [light level 측정하기](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement#Measuring-light-level)

[`var chromaticity: SRAmbientLightSample.Chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property)

sample의 light 밝기와 tint를 설명하는 좌표 쌍입니다.

[`struct Chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct)

light 밝기와 tint를 설명하는 좌표 쌍입니다.

[`var lux: Measurement<UnitIlluminance>`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/lux)

sample의 luminous flux를 설명하는 object입니다.

[`var placement: SRAmbientLightSample.SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/placement)

sensor를 기준으로 한 light의 위치입니다.

현재 페이지: SRAmbientLightSample.SensorPlacement
