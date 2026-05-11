---
title: "floorsAscended | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900185+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   floorsAscended

instance property

floorsAscended
==============

걸어서 올라간 층수의 대략적인 수입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var floorsAscended: NSNumber? { get }

[설명](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended#Discussion)

-------------------------------------------------------------------------------------------------------------

이 값은 사용자가 계단을 걸어 오르거나 뛰어 올라간 층수만 반영하며, 엘리베이터나 기타 보조 수단으로 올라간 층수는 반영하지 않습니다. 한 층의 높이는 약 3m입니다. 현재 device가 floor counting을 지원하지 않으면 이 property의 값은 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended#see-also)

---------------------------------------------------------------------------------------------------------

### [층수 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended#Getting-the-Floor-Counts)

[`var floorsDescended: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended)

걸어서 내려간 층수의 대략적인 수입니다.

현재 페이지: floorsAscended
