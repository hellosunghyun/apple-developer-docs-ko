---
title: "averageActivePace | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.898653+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   averageActivePace

instance property

averageActivePace
=================

초당 meter가 아니라 meter당 초 단위로 측정한 사용자의 평균 pace입니다.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.1+macOS 10.15+watchOS 3.0+

    var averageActivePace: NSNumber? { get }

[논의](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace#Discussion)

----------------------------------------------------------------------------------------------------------------

일반적인 update 동안에는 [`startUpdates(from:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmpedometer/startupdates(from:withhandler:))
가 호출된 이후의 사용자의 평균 active pace가 이 property에 설정됩니다. historical query를 수행할 때는 [`startDate`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/startdate)
와 [`endDate`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/enddate)
 사이의 평균 active pace가 설정됩니다.

이 property는 사용자가 활동한 구간에서만 pace를 평균 내며, 비활동 구간은 모두 제외합니다. historical pedometer data query를 수행하는 중에 정보가 없으면(예를 들어 사용자가 `startDate`와 `endDate` 사이에 움직이지 않은 경우) 이 property 값은 `nil`입니다. pace data 수집을 지원하지 않는 device에서도 이 property는 `nil`입니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace#see-also)

------------------------------------------------------------------------------------------------------------

### [보행자 data 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace#Getting-the-Pedestrian-Data)

[`var numberOfSteps: NSNumber`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps)

사용자가 걸은 step 수입니다.

[`var distance: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance)

사용자가 이동한 것으로 추정되는 거리(meter)입니다.

[`var currentPace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace)

meter당 초 단위로 측정한 사용자의 현재 pace입니다.

[`var currentCadence: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence)

초당 step 수로 측정한 걸음 빈도입니다.

현재 페이지는 averageActivePace입니다
