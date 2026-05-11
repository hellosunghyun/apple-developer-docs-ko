---
title: "CMWaterTemperature | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatertemperature"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.879536+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatertemperature#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMWaterTemperature

class

CMWaterTemperature
==================

water temperature data를 담은 update입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    class CMWaterTemperature

[주제](https://developer.apple.com/documentation/coremotion/cmwatertemperature#topics)

-----------------------------------------------------------------------------------------

### [data 접근](https://developer.apple.com/documentation/coremotion/cmwatertemperature#Accessing-the-data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmwatertemperature/date)

system이 measurement를 기록한 시간과 날짜입니다.

[`var temperature: Measurement<UnitTemperature>`](https://developer.apple.com/documentation/coremotion/cmwatertemperature/temperature)

water temperature입니다.

[`var temperatureUncertainty: Measurement<UnitTemperature>`](https://developer.apple.com/documentation/coremotion/cmwatertemperature/temperatureuncertainty)

water temperature measurement의 uncertainty 양입니다.

### [Initializer](https://developer.apple.com/documentation/coremotion/cmwatertemperature#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmwatertemperature/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmwatertemperature#relationships)

-------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmwatertemperature#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmwatertemperature#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmwatertemperature#see-also)

---------------------------------------------------------------------------------------------

### [Water submersion](https://developer.apple.com/documentation/coremotion/cmwatertemperature#Water-submersion)

[잠수 data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

water-submersion manager를 사용해 Apple Watch Ultra에서 water pressure, temperature, depth data를 받습니다.

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

잠수 중 pressure 및 temperature data 수집을 관리하는 object입니다.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

ambient pressure, water pressure, water temperature, submersion event에 대한 update를 받는 delegate입니다.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

device의 잠수 상태가 바뀌었음을 나타내는 event입니다.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

pressure와 depth data를 담은 update입니다.

현재 페이지: CMWaterTemperature
