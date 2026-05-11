---
title: "maxAbsSlope | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.911233+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata)
    
*   maxAbsSlope

instance property

maxAbsSlope
===========

해당 위치에서 모든 방향을 기준으로 측정한 최대 절대 경사이며, 단위는 도입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 10.15+visionOS 1.0+watchOS 10.0+

    var maxAbsSlope: Double? { get }

[논의](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd#Discussion)

---------------------------------------------------------------------------------------------------------------

GPS 정확도가 낮아 최대 절대 경사가 유효하지 않으면 이 property는 [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0)
입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd#see-also)

-----------------------------------------------------------------------------------------------------------

### [속도와 경사 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd#Getting-speed-and-slope)

[`var speed: CLLocationSpeed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)

device의 순간 속도이며 초당 미터 단위로 측정합니다.

[`var slope: Double?`](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4)

이동 방향 기준 해당 위치의 경사이며, 단위는 도입니다.

현재 페이지: maxAbsSlope
