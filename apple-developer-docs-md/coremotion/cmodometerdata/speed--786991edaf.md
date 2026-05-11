---
title: "speed | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata/speed"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.911412+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata)
    
*   speed

instance property

speed
=====

초당 미터 단위로 측정한 device의 순간 속도입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 10.15+visionOS 1.0+watchOS 10.0+

    var speed: CLLocationSpeed { get }

[같이 보기](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed#see-also)

-----------------------------------------------------------------------------------------------

### [Getting speed and slope](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed#Getting-speed-and-slope)

[`var slope: Double?`](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4)

이동 방향을 향한 위치의 slope이며, degree 단위로 측정합니다.

[`var maxAbsSlope: Double?`](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd)

모든 방향을 향한 위치의 최대 절대 slope이며, degree 단위로 측정합니다.

현재 페이지: speed
