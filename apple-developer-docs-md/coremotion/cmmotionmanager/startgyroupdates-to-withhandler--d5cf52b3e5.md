---
title: "startGyroUpdates(to:withHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900466+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   startGyroUpdates(to:withHandler:)

instance method

startGyroUpdates(to:withHandler:)
=================================

operation queue에서 지정한 handler와 함께 gyroscope update를 시작합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    func startGyroUpdates(
        to queue: OperationQueue,
        withHandler handler: @escaping CMGyroHandler
    )

[parameter](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------

`queue`

caller가 제공하는 operation queue입니다. 처리된 event가 높은 빈도로 도착할 수 있으므로 main operation queue 사용은 권장하지 않습니다.

`handler`

새로운 gyroscope data를 처리하기 위해 각 update마다 호출되는 block입니다. 이 block은 [`CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)
 type을 준수해야 합니다.

[언급된 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)#mentions)

--------------------------------------------------------------------------------------------------------------------------------

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)#Discussion)

--------------------------------------------------------------------------------------------------------------------------------

app이 gyroscope update를 더 이상 처리하지 않으려면 [`stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())
를 호출해야 합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)#see-also)

----------------------------------------------------------------------------------------------------------------------------

### [Gyroscope Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:)#Managing-Gyroscope-Updates)

[`var gyroUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)

block handler에 gyroscope update를 제공하는 간격(초)입니다.

[`func startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())

handler 없이 gyroscope update를 시작합니다.

[`func stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())

gyroscope update를 중지합니다.

[`var gyroData: CMGyroData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)

최신 gyroscope data sample입니다.

[`typealias CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

gyroscope data를 처리하는 block callback의 type입니다.

현재 페이지: startGyroUpdates(to:withHandler:)
