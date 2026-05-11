---
title: "pressure | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.902928+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionMeasurement](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)
    
*   pressure

instance property

pressure
========

수압입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    var pressure: Measurement<UnitPressure>? { get }

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure#see-also)

----------------------------------------------------------------------------------------------------------------

### [Accessing the data](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure#Accessing-the-data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/date)

system이 measurement를 기록한 시간과 날짜입니다.

[`var depth: Measurement<UnitLength>?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depth)

수중 depth입니다.

[`var surfacePressure: Measurement<UnitPressure>`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/surfacepressure)

수면의 기압입니다.

[`var submersionState: CMWaterSubmersionMeasurement.DepthState`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate)

depth state입니다.

[`enum DepthState`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate)

device의 수중 depth를 기반으로 한 state입니다.

현재 페이지: pressure
