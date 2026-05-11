---
title: "stopGyroUpdates() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899076+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   stopGyroUpdates()

instance method

stopGyroUpdates()
=================

gyroscope update를 중지합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func stopGyroUpdates()

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates()#see-also)

------------------------------------------------------------------------------------------------------------

### [Gyroscope Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates()#Managing-Gyroscope-Updates)

[`var gyroUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)

block handler에 gyroscope update를 제공하는 간격(초)입니다.

[`func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))

operation queue에서 지정한 handler와 함께 gyroscope update를 시작합니다.

[`func startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())

handler 없이 gyroscope update를 시작합니다.

[`var gyroData: CMGyroData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)

최신 gyroscope data sample입니다.

[`typealias CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

gyroscope data를 처리하는 block callback의 type입니다.

현재 페이지: stopGyroUpdates()
