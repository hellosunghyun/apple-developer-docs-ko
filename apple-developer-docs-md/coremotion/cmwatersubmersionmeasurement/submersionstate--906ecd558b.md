---
title: "submersionState | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.881978+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionMeasurement](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)
    
*   submersionState

instance property

submersionState
===============

깊이 상태입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    var submersionState: CMWaterSubmersionMeasurement.DepthState { get }

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [data에 접근하기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate#Accessing-the-data)

[`var date: Date`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/date)

system이 measurement를 기록한 시각과 날짜입니다.

[`var depth: Measurement<UnitLength>?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depth)

수중 깊이입니다.

[`var pressure: Measurement<UnitPressure>?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure)

수압입니다.

[`var surfacePressure: Measurement<UnitPressure>`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/surfacepressure)

수면의 기압입니다.

[`enum DepthState`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate)

device의 수중 깊이를 기준으로 한 상태입니다.

현재 페이지: submersionState
