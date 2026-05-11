---
title: "currentCadence | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900095+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   currentCadence

instance property

currentCadence
==============

steps per second 단위로 측정한 step 속도입니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var currentCadence: NSNumber? { get }

[논의](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence#Discussion)

-------------------------------------------------------------------------------------------------------------

정기 update 중에는 이 property에 사용자의 cadence가 설정됩니다. 과거 pedometer data를 query하거나 사용자 cadence 정보를 아직 사용할 수 없으면 이 property 값은 `nil`입니다. cadence data 수집을 지원하지 않는 device에서도 이 property는 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence#see-also)

---------------------------------------------------------------------------------------------------------

### [Getting the Pedestrian Data](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence#Getting-the-Pedestrian-Data)

[`var numberOfSteps: NSNumber`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps)

사용자가 걸은 step 수입니다.

[`var distance: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance)

사용자가 이동한 것으로 추정되는 거리(미터)입니다.

[`var averageActivePace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace)

seconds per meter 단위로 측정한 사용자의 평균 pace입니다.

[`var currentPace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace)

seconds per meter 단위로 측정한 사용자의 현재 pace입니다.

현재 페이지: currentCadence
