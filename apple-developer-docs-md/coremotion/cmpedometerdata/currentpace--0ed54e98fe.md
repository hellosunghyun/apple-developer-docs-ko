---
title: "currentPace | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.898751+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   currentPace

instance property

currentPace
===========

meter당 초 단위로 측정한 사용자의 현재 pace입니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var currentPace: NSNumber? { get }

[논의](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace#Discussion)

----------------------------------------------------------------------------------------------------------

일반적인 update 동안 이 property에는 사용자의 pace가 설정됩니다. historical pedometer data query를 수행하는 경우나 사용자 pace 정보가 아직 제공되지 않는 경우에는 이 property의 값이 `nil`입니다. pace data 수집을 지원하지 않는 device에서도 이 property는 `nil`입니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace#see-also)

------------------------------------------------------------------------------------------------------

### [보행자 data 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace#Getting-the-Pedestrian-Data)

[`var numberOfSteps: NSNumber`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps)

사용자가 걸은 step 수입니다.

[`var distance: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance)

사용자가 이동한 것으로 추정되는 거리(meter)입니다.

[`var averageActivePace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace)

meter당 초 단위로 측정한 사용자의 평균 pace입니다.

[`var currentCadence: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence)

초당 step 수로 측정한 걸음 빈도입니다.

현재 페이지는 currentPace입니다
