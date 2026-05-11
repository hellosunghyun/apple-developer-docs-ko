---
title: "gyroUpdateInterval | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900371+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   gyroUpdateInterval

instance property

gyroUpdateInterval
==================

block handler에 gyroscope update를 제공하는 초 단위 interval입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    var gyroUpdateInterval: TimeInterval { get set }

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval#mentions)

-----------------------------------------------------------------------------------------------------------------

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

[논의](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval#Discussion)

-----------------------------------------------------------------------------------------------------------------

system은 [`startGyroUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))
 에 지정한 block handler에 이 property 값으로 결정되는 일정한 interval로 gyroscope(즉, rotation rate) update를 제공합니다. interval 단위는 초입니다. 이 property 값에는 최소값과 최대값 제한이 있으며, 최대값은 hardware가 지원하는 최대 주파수에 따라 결정됩니다. app이 gyroscope data interval에 민감하다면, 전달된 [`CMGyroData`](https://developer.apple.com/documentation/coremotion/cmgyrodata)
 instance의 timestamp를 항상 확인해 실제 update interval을 판단해야 합니다.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval#see-also)

-------------------------------------------------------------------------------------------------------------

### [Managing Gyroscope Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval#Managing-Gyroscope-Updates)

[`func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 gyroscope update를 시작합니다.

[`func startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())

handler 없이 gyroscope update를 시작합니다.

[`func stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())

gyroscope update를 중지합니다.

[`var gyroData: CMGyroData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)

최신 gyroscope data sample입니다.

[`typealias CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

gyroscope data를 처리하는 block callback type입니다.

현재 페이지: gyroUpdateInterval
