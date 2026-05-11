---
title: "isStepCountingAvailable() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.907579+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
    
*   *   [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)
        
*   isStepCountingAvailable() Deprecated

type method

isStepCountingAvailable()
=========================

현재 device에서 step-counting support를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

iOS 7.0–8.0DeprecatediPadOS 7.0–8.0DeprecatedMac Catalyst 13.1–13.1DeprecatedvisionOS 1.0–1.0Deprecated

    class func isStepCountingAvailable() -> Bool

[Return Value](https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable()#return-value)

--------------------------------------------------------------------------------------------------------------------------

step-counting support를 사용할 수 있으면 [`true`](https://developer.apple.com/documentation/Swift/true)
, 그렇지 않으면 [`false`](https://developer.apple.com/documentation/Swift/false)
입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable()#Discussion)

----------------------------------------------------------------------------------------------------------------------

step-counting support는 모든 iOS device에서 제공되지 않습니다. 현재 device에서 support를 사용할 수 있는지 확인하려면 이 method를 사용합니다.

현재 페이지는 isStepCountingAvailable()입니다
