---
title: "speedAccuracy | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.910666+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata)
    
*   speedAccuracy

instance property

speedAccuracy
=============

speed 값의 accuracy입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 10.15+visionOS 1.0+watchOS 10.0+

    var speedAccuracy: CLLocationSpeedAccuracy { get }

[논의](https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy#Discussion)

-----------------------------------------------------------------------------------------------------------

이 property는 [`speed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)
 property의 accuracy를 나타냅니다. 이 property가 `0` 또는 양수를 포함하면 `speed` property의 값은 지정한 meters per second 범위만큼의 오차를 가집니다. 이 property가 음수를 포함하면 `speed` property의 값은 유효하지 않습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy#see-also)

-------------------------------------------------------------------------------------------------------

### [Getting the location accuracy](https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy#Getting-the-location-accuracy)

[`var verticalAccuracy: CLLocationAccuracy`](https://developer.apple.com/documentation/coremotion/cmodometerdata/verticalaccuracy)

altitude 값의 유효성과 추정 불확실성을 meters 단위로 나타냅니다.

[`var deltaDistanceAccuracy: CLLocationAccuracy`](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltadistanceaccuracy)

거리 변화 값의 accuracy입니다.

현재 페이지: speedAccuracy
