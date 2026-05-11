---
title: "accelerometerUpdateInterval | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899315+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   accelerometerUpdateInterval

instance property

accelerometerUpdateInterval
===========================

block handler에 accelerometer update를 전달하는 간격(초)입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var accelerometerUpdateInterval: TimeInterval { get set }

[언급 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval#mentions)

--------------------------------------------------------------------------------------------------------------------------

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval#Discussion)

--------------------------------------------------------------------------------------------------------------------------

system은 이 property 값으로 정해진 일정한 간격마다 [`startAccelerometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))
 에 지정한 block handler로 accelerometer update를 전달합니다. 간격 단위는 초입니다. 이 property 값에는 최소값과 최대값 제한이 있으며, 최대값은 hardware가 지원하는 최대 주파수로 결정됩니다. app이 acceleration data 간격에 민감하다면, 실제 update 간격은 전달된 [`CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)
 instance의 timestamp를 항상 확인해 판단해야 합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval#see-also)

----------------------------------------------------------------------------------------------------------------------

### [관련 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval#Related-Documentation)

[UIKit app용 event handling guide](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)

### [Accelerometer update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval#Managing-Accelerometer-Updates)

[`func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 accelerometer update를 시작합니다.

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())

handler 없이 accelerometer update를 시작합니다.

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())

accelerometer update를 중지합니다.

[`var accelerometerData: CMAccelerometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)

가장 최근의 accelerometer data sample입니다.

[`typealias CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

accelerometer data를 처리하는 block callback의 type입니다.

현재 페이지는 accelerometerUpdateInterval입니다
