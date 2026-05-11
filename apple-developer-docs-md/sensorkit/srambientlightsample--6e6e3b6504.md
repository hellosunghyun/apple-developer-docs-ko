---
title: "SRAmbientLightSample | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srambientlightsample"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.023016+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srambientlightsample#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRAmbientLightSample

class

SRAmbientLightSample
====================

사용자 환경의 ambient light 양입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRAmbientLightSample

[개요](https://developer.apple.com/documentation/sensorkit/srambientlightsample#overview)

----------------------------------------------------------------------------------------------

The [`ambientLightSensor`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor)
 sensor provides this class as its [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type.

[주제](https://developer.apple.com/documentation/sensorkit/srambientlightsample#topics)

------------------------------------------------------------------------------------------

### [light level 측정](https://developer.apple.com/documentation/sensorkit/srambientlightsample#Measuring-light-level)

[`var chromaticity: SRAmbientLightSample.Chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.property)

sample의 light brightness와 tint를 설명하는 coordinate pair입니다.

[`struct Chromaticity`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct)

light brightness와 tint를 설명하는 coordinate pair입니다.

[`var lux: Measurement<UnitIlluminance>`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/lux)

sample의 luminous flux를 설명하는 object입니다.

[`var placement: SRAmbientLightSample.SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/placement)

sensor를 기준으로 한 light의 위치입니다.

[`enum SensorPlacement`](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement)

sensor를 기준으로 light source 위치를 설명하는 directional value입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srambientlightsample#relationships)

--------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srambientlightsample#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srambientlightsample#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srambientlightsample#see-also)

----------------------------------------------------------------------------------------------

### [data 해석](https://developer.apple.com/documentation/sensorkit/srambientlightsample#Interpreting-data)

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app, 또는 website를 사용하는 빈도와 상대적 duration입니다.

[`class SRKeyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)

device keyboard의 configuration과 사용 pattern입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object와의 사용자 interaction입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안 사용자의 Messages app activity를 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안 사용자의 phone activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

사용자의 일상 이동 루틴 진행 상태입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목에 있는 watch의 configuration입니다.

현재 페이지는 SRAmbientLightSample
