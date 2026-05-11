---
title: "slope | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.911324+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata)
    
*   slope

instance property

slope
=====

이동 방향 위치의 slope를 도 단위로 나타낸 값입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 10.15+visionOS 1.0+watchOS 10.0+

    var slope: Double? { get }

[설명](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4#Discussion)

---------------------------------------------------------------------------------------------------------

If the slope measurement is invalid, this property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0)
.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4#see-also)

-----------------------------------------------------------------------------------------------------

### [speed와 slope 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4#Getting-speed-and-slope)

[`var speed: CLLocationSpeed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)

device의 순간 속도를 미터/초 단위로 나타낸 값입니다.

[`var maxAbsSlope: Double?`](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd)

해당 위치에서 모든 방향 기준의 최대 절대 slope를 도 단위로 나타낸 값입니다.

현재 페이지: slope
