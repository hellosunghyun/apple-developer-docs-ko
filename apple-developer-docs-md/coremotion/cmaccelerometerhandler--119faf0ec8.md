---
title: "CMAccelerometerHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899631+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAccelerometerHandler

type 별칭

CMAccelerometerHandler
======================

accelerometer data를 처리하는 block callback의 type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    typealias CMAccelerometerHandler = (CMAccelerometerData?, (any Error)?) -> Void

[설명](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler#Discussion)

-----------------------------------------------------------------------------------------------------

`CMAccelerometerHandler` type의 block은 처리할 accelerometer data가 있을 때 호출됩니다. 이 block을 [`startAccelerometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))
의 두 번째 argument로 전달합니다. 이 type의 block은 값을 반환하지 않으며 두 개의 argument를 받습니다.

`accelerometerData`

세 개의 movement axis에 대한 acceleration 값을 담은 field가 있는 [`CMAcceleration`](https://developer.apple.com/documentation/coremotion/cmacceleration)
struct를 캡슐화한 object입니다.

`error`

accelerometer update를 제공하는 과정에서 발생한 error를 나타내는 error object입니다. error가 발생하면 accelerometer update를 중지하고 사용자에게 문제를 알려야 합니다. error가 없으면 이 argument는 `nil`입니다. Core Motion error는 [`CMErrorDomain`](https://developer.apple.com/documentation/coremotion/cmerrordomain)
domain과 [`CMError`](https://developer.apple.com/documentation/coremotion/cmerror)
type을 사용합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler#see-also)

-------------------------------------------------------------------------------------------------

### [Accelerometer Update 관리](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler#Managing-Accelerometer-Updates)

[`var accelerometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)

block handler에 accelerometer update를 제공하는 간격(초)입니다.

[`func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))

operation queue와 지정한 handler로 accelerometer update를 시작합니다.

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())

handler 없이 accelerometer update를 시작합니다.

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())

accelerometer update를 중지합니다.

[`var accelerometerData: CMAccelerometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)

가장 최근의 accelerometer data sample입니다.

현재 페이지는 CMAccelerometerHandler입니다.
