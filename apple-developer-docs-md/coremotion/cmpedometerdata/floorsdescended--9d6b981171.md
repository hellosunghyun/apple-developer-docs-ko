---
title: "floorsDescended | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900272+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
    
*   floorsDescended

instance property

floorsDescended
===============

걸어서 내려간 층 수의 대략적인 값입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    var floorsDescended: NSNumber? { get }

[설명](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended#Discussion)

--------------------------------------------------------------------------------------------------------------

이 값에는 사용자가 계단을 걸어 내려가거나 뛰어 내려가며 내려간 층만 반영되며, 엘리베이터나 그 밖의 보조 수단으로 내려간 층은 반영되지 않습니다. 한 층의 높이는 약 3미터입니다. 현재 device가 floor counting을 지원하지 않으면 이 property 값은 `nil`입니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended#see-also)

----------------------------------------------------------------------------------------------------------

### [층 수 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended#Getting-the-Floor-Counts)

[`var floorsAscended: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended)

걸어서 올라간 층 수의 대략적인 값입니다.

현재 페이지는 floorsDescended입니다.
