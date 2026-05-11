---
title: "gyroData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.901109+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   gyroData

instance property

gyroData
========

가장 최근의 gyroscope data sample입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var gyroData: CMGyroData? { get }

[언급된 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata#mentions)

-------------------------------------------------------------------------------------------------------

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata#Discussion)

-------------------------------------------------------------------------------------------------------

gyroscope data를 사용할 수 없으면 이 property의 값은 `nil`입니다. [`startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())를 호출한 뒤 gyroscope data를 받는 app은 이 property의 값을 주기적으로 확인하고 gyroscope data를 처리합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata#see-also)

---------------------------------------------------------------------------------------------------

### [Gyroscope Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata#Managing-Gyroscope-Updates)

[`var gyroUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)

block handler에 gyroscope update를 전달하는 간격(초)입니다.

[`func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))

operation queue에서 지정한 handler와 함께 gyroscope update를 시작합니다.

[`func startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())

handler 없이 gyroscope update를 시작합니다.

[`func stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())

gyroscope update를 중단합니다.

[`typealias CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

gyroscope data를 처리하는 block callback의 type입니다.

현재 페이지는 gyroData입니다
