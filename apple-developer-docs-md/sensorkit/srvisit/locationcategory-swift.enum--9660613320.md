---
title: "SRVisit.LocationCategory | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.038327+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRVisit](https://developer.apple.com/documentation/sensorkit/srvisit)
    
*   SRVisit.LocationCategory

enum

SRVisit.LocationCategory
========================

location의 type입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    enum LocationCategory

[주제](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#topics)

---------------------------------------------------------------------------------------------------------

### [category](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#Categories)

[`case gym`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum/gym)

user의 gym입니다.

[`case home`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum/home)

user의 집입니다.

[`case school`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum/school)

user의 학교입니다.

[`case unknown`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum/unknown)

user가 자주 방문하지만 type을 알 수 없는 location입니다.

[`case work`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum/work)

user의 직장입니다.

### [이니셜라이저](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#relationships)

-----------------------------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#see-also)

-------------------------------------------------------------------------------------------------------------

### [Visit 정보 접근](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum#Accessing-Visit-Information)

[`var arrivalDateInterval: DateInterval`](https://developer.apple.com/documentation/sensorkit/srvisit/arrivaldateinterval)

user가 관심 location에 도착한 시간 범위입니다.

[`var departureDateInterval: DateInterval`](https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval)

user가 관심 location에서 떠난 시간 범위입니다.

[`var distanceFromHome: CLLocationDistance`](https://developer.apple.com/documentation/sensorkit/srvisit/distancefromhome)

home category location으로부터의 거리입니다.

[`var locationCategory: SRVisit.LocationCategory`](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.property)

location의 type입니다.

현재 페이지는 SRVisit.LocationCategory입니다
