---
title: "numberOfSteps | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.892420+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   numberOfSteps

instance property

numberOfSteps
=============

사용자가 걸은 step 수입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var numberOfSteps: NSNumber { get }

[관련 항목](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps#see-also)

--------------------------------------------------------------------------------------------------------

### [보행 data 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps#Getting-the-Pedestrian-Data)

[`var distance: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance)

사용자가 이동한 것으로 추정되는 거리(미터)입니다.

[`var averageActivePace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace)

사용자의 평균 pace를 초/미터 단위로 나타낸 값입니다.

[`var currentPace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace)

사용자의 현재 pace를 초/미터 단위로 나타낸 값입니다.

[`var currentCadence: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence)

step이 발생하는 속도를 step/초 단위로 나타낸 값입니다.

현재 페이지: numberOfSteps
