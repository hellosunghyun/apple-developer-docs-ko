---
title: "maxAbsSlope | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-96ulr"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.914432+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-96ulr#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata)
    
*   maxAbsSlope

instance property

maxAbsSlope
===========

해당 위치에서 모든 방향을 기준으로 한 최대 절대 slope를 degree 단위로 나타냅니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 10.15+visionOS 1.0+watchOS 10.0+

    @property (nonatomic, strong, readonly) NSNumber * maxAbsSlope;

[설명](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-96ulr#Discussion)

---------------------------------------------------------------------------------------------------------------

GPS 정확도가 낮아 최대 절대 slope가 유효하지 않으면 이 property는 [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0)
입니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-96ulr#see-also)

-----------------------------------------------------------------------------------------------------------

### [speed와 slope 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-96ulr#Getting-speed-and-slope)

[`var speed: CLLocationSpeed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)

device의 순간 속도를 meters per second 단위로 나타냅니다.

[`slope`](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt)

이동 방향을 기준으로 한 해당 위치의 slope를 degree 단위로 나타냅니다.

현재 페이지는 maxAbsSlope입니다
