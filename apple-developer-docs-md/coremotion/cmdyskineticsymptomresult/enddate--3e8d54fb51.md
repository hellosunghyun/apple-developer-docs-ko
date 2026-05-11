---
title: "endDate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.913724+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMDyskineticSymptomResult](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)
    
*   endDate

instance property

endDate
=======

result의 종료 시각과 날짜입니다.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.1+watchOS 5.0+

    var endDate: Date { get }

[논의](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate#Discussion)

----------------------------------------------------------------------------------------------------------------

result의 `endDate`는 항상 [`startDate`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/startdate)
보다 1분 이내로 뒤에 있습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate#see-also)

------------------------------------------------------------------------------------------------------------

### [시간 간격 읽기](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate#Reading-the-Time-Interval)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/startdate)

result의 시작 시각과 날짜입니다.

현재 페이지: endDate
