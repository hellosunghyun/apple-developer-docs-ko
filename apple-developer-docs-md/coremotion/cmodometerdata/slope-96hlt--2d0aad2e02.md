---
title: "slope | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.912897+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata)
    
*   slope

instance property

slope
=====

이동 방향을 기준으로 해당 위치의 경사를 도 단위로 측정한 값입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 10.15+visionOS 1.0+watchOS 10.0+

    @property (nonatomic, strong, readonly) NSNumber * slope;

[논의](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt#Discussion)

---------------------------------------------------------------------------------------------------------

경사 값이 유효하지 않으면 이 property는 [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0)
입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt#see-also)

-----------------------------------------------------------------------------------------------------

### [Getting speed and slope](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt#Getting-speed-and-slope)

[`var speed: CLLocationSpeed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)

device의 순간 속도를 meters per second 단위로 측정한 값입니다.

[`maxAbsSlope`](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-96ulr)

모든 방향을 기준으로 해당 위치의 최대 절대 경사를 도 단위로 측정한 값입니다.

현재 페이지: slope
