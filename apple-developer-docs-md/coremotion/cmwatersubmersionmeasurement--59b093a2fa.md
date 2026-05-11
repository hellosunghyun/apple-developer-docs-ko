---
title: "CMWaterSubmersionMeasurement | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.879318+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMWaterSubmersionMeasurement

class

CMWaterSubmersionMeasurement
============================

pressure와 depth에 관한 data를 포함한 update입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    class CMWaterSubmersionMeasurement

[주제](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#topics)

---------------------------------------------------------------------------------------------------

### [data 접근](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#Accessing-the-data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/date)

system이 measurement를 기록한 시각과 날짜입니다.

[`var depth: Measurement<UnitLength>?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depth)

수중 depth입니다.

[`var pressure: Measurement<UnitPressure>?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure)

수압입니다.

[`var surfacePressure: Measurement<UnitPressure>`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/surfacepressure)

수면 위 기압입니다.

[`var submersionState: CMWaterSubmersionMeasurement.DepthState`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate)

depth state입니다.

[`enum DepthState`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate)

device의 수중 depth를 기준으로 한 state입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#relationships)

-----------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#see-also)

-------------------------------------------------------------------------------------------------------

### [수중 submersion](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement#Water-submersion)

[submersion data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

water-submersion manager를 사용해 Apple Watch Ultra에서 수압, 온도, depth data를 받습니다.

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

submersion 중 pressure와 temperature data 수집을 관리하는 object입니다.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

ambient pressure, water pressure, water temperature, submersion event update를 받는 delegate입니다.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

device의 submersion state가 변경되었음을 나타내는 event입니다.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

water temperature에 관한 data를 포함한 update입니다.

현재 페이지는 CMWaterSubmersionMeasurement입니다
