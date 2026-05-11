---
title: "accelerometerData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900928+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   accelerometerData

instance property

accelerometerData
=================

가장 최근의 accelerometer data sample입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var accelerometerData: CMAccelerometerData? { get }

[언급된 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata#mentions)

----------------------------------------------------------------------------------------------------------------

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata#Discussion)

----------------------------------------------------------------------------------------------------------------

accelerometer data를 사용할 수 없으면 이 property의 값은 `nil`입니다. [`startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())
를 호출한 뒤 accelerometer data를 받고 있는 app은 이 property의 값을 주기적으로 확인하고 acceleration data를 처리합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata#see-also)

------------------------------------------------------------------------------------------------------------

### [Accelerometer update 관리하기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata#Managing-Accelerometer-Updates)

[`var accelerometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)

block handler에 accelerometer update를 제공하는 간격(초)입니다.

[`func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 accelerometer update를 시작합니다.

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())

handler 없이 accelerometer update를 시작합니다.

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())

accelerometer update를 중지합니다.

[`typealias CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

accelerometer data를 처리하는 block callback의 type입니다.

현재 페이지: accelerometerData
