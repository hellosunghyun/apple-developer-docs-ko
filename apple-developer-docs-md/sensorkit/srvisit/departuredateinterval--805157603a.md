---
title: "departureDateInterval | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.037833+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRVisit](https://developer.apple.com/documentation/sensorkit/srvisit)
    
*   departureDateInterval

instance property

departureDateInterval
=====================

사용자가 관심 위치를 떠난 시점을 포함하는 시간 범위입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    var departureDateInterval: DateInterval { get }

[관련 항목](https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval#see-also)

-------------------------------------------------------------------------------------------------------

### [visit 정보 접근](https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval#Accessing-Visit-Information)

[`var arrivalDateInterval: DateInterval`](https://developer.apple.com/documentation/sensorkit/srvisit/arrivaldateinterval)

사용자가 관심 위치에 도착한 시점을 포함하는 시간 범위입니다.

[`var distanceFromHome: CLLocationDistance`](https://developer.apple.com/documentation/sensorkit/srvisit/distancefromhome)

해당 위치와 home category 위치 사이의 거리입니다.

[`var locationCategory: SRVisit.LocationCategory`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.property)

위치의 type입니다.

[`enum LocationCategory`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum)

위치 type입니다.

현재 페이지는 departureDateInterval입니다.
