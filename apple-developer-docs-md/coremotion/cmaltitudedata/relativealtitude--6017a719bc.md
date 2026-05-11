---
title: "relativeAltitude | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaltitudedata/relativealtitude"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.873886+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaltitudedata/relativealtitude#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMAltitudeData](https://developer.apple.com/documentation/coremotion/cmaltitudedata)
    
*   relativeAltitude

instance property

relativeAltitude
================

처음 보고된 event 이후의 altitude 변화량(미터)입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+watchOS 2.0+

    var relativeAltitude: NSNumber { get }

[논의](https://developer.apple.com/documentation/coremotion/cmaltitudedata/relativealtitude#Discussion)

--------------------------------------------------------------------------------------------------------------

altimeter object에 처음 전달되는 altitude event에서는 이 property의 값이 `0`입니다. 이후 event에는 처음 보고된 event를 기준으로 한 altitude의 상대적 변화량이 들어 있습니다. 예를 들어 첫 번째 event와 두 번째 event 사이에 altitude가 5미터 변했다면, 두 번째 event에서 이 property의 값은 `5`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmaltitudedata/relativealtitude#see-also)

----------------------------------------------------------------------------------------------------------

### [Altitude Data 가져오기](https://developer.apple.com/documentation/coremotion/cmaltitudedata/relativealtitude#Getting-the-Altitude-Data)

[`var pressure: NSNumber`](https://developer.apple.com/documentation/coremotion/cmaltitudedata/pressure)

기록된 pressure(kilopascal)입니다.

현재 페이지: relativeAltitude
