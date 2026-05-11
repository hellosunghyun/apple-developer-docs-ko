---
title: "distance | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.898543+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   distance

instance property

distance
========

사용자가 이동한 추정 거리(미터 단위)입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var distance: NSNumber? { get }

[설명](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance#Discussion)

-------------------------------------------------------------------------------------------------------

이 값은 걷거나 달릴 때 이동한 거리를 반영합니다. 현재 device에서 distance estimation을 지원하지 않으면 이 property의 값은 `nil`일 수 있습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance#see-also)

---------------------------------------------------------------------------------------------------

### [보행 data 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance#Getting-the-Pedestrian-Data)

[`var numberOfSteps: NSNumber`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps)

사용자가 걸은 step 수입니다.

[`var averageActivePace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace)

사용자의 평균 pace로, 미터당 초 단위로 측정합니다.

[`var currentPace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace)

사용자의 현재 pace로, 미터당 초 단위로 측정합니다.

[`var currentCadence: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence)

step이 발생하는 속도로, 초당 step 수로 측정합니다.

현재 페이지: distance
