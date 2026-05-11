---
title: "startGyroUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.901016+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startGyroUpdates()

instance method

startGyroUpdates()
==================

handler 없이 gyroscope update를 시작합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startGyroUpdates()

[언급 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates()#mentions)

-----------------------------------------------------------------------------------------------------------------

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates()#Discussion)

-----------------------------------------------------------------------------------------------------------------

최신 gyroscope data는 [`gyroData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)
 property로 가져올 수 있습니다. app이 더 이상 gyroscope update를 처리하지 않아야 하면 [`stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())
 를 호출해야 합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates()#see-also)

-------------------------------------------------------------------------------------------------------------

### [Gyroscope update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates()#Managing-Gyroscope-Updates)

[`var gyroUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)

block handler에 gyroscope update를 전달하는 간격(초)입니다.

[`func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))

operation queue에서 지정한 handler와 함께 gyroscope update를 시작합니다.

[`func stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())

gyroscope update를 중지합니다.

[`var gyroData: CMGyroData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)

최신 gyroscope data sample입니다.

[`typealias CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

gyroscope data를 처리하는 block callback의 type입니다.

현재 페이지는 startGyroUpdates()
