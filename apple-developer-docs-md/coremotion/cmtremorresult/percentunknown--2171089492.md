---
title: "percentUnknown | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.915277+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMTremorResult](https://developer.apple.com/documentation/coremotion/cmtremorresult)
    
*   percentUnknown

instance property

percentUnknown
==============

algorithm이 판단을 내리지 못한 시간의 비율입니다.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 5.0+

    var percentUnknown: Float { get }

[논의](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown#Discussion)

------------------------------------------------------------------------------------------------------------

활성 motion과 낮은 signal level 모두 `percentUnknown` result의 원인이 될 수 있습니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown#see-also)

--------------------------------------------------------------------------------------------------------

### [Accessing Tremor Data](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown#Accessing-Tremor-Data)

[`var percentNone: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentnone)

tremor가 감지되지 않은 시간의 비율입니다.

[`var percentSlight: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentslight)

tremor 가능성이 있었고 displacement amplitude가 slight였던 시간의 비율입니다.

[`var percentMild: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentmild)

tremor 가능성이 있었고 displacement amplitude가 mild였던 시간의 비율입니다.

[`var percentModerate: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentmoderate)

tremor 가능성이 있었고 displacement amplitude가 moderate였던 시간의 비율입니다.

[`var percentStrong: Float`](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentstrong)

tremor 가능성이 있었고 displacement amplitude가 strong이었던 시간의 비율입니다.

현재 페이지: percentUnknown
