---
title: "CMGyroHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmgyrohandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.872527+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmgyrohandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMGyroHandler

type alias

CMGyroHandler
=============

gyroscope data를 처리하는 block callback type입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    typealias CMGyroHandler = (CMGyroData?, (any Error)?) -> Void

[논의](https://developer.apple.com/documentation/coremotion/cmgyrohandler#Discussion)

--------------------------------------------------------------------------------------------

Blocks of type `CMGyroHandler` are called when there is gyroscope data to process. You pass the block into [`startGyroUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))
 as the second argument. Blocks of this type return no value but take two arguments:

`gyroData`

An object that encapsulates a [`CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmrotationrate)
 structure with fields holding rotation-rate values for the three axes of movement.

`error`

An error object representing an error encountered in providing gyroscope data. If an error occurs, you should stop gyroscope updates and inform the user of the problem. If there is no error, this argument is `nil`. Core Motion errors are of the [`CMErrorDomain`](https://developer.apple.com/documentation/coremotion/cmerrordomain)
 domain and the [`CMError`](https://developer.apple.com/documentation/coremotion/cmerror)
 type.

[같이 보기](https://developer.apple.com/documentation/coremotion/cmgyrohandler#see-also)

----------------------------------------------------------------------------------------

### [Gyroscope Update 관리하기](https://developer.apple.com/documentation/coremotion/cmgyrohandler#Managing-Gyroscope-Updates)

[`var gyroUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)

block handler에 gyroscope update를 제공하는 간격(초)입니다.

[`func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 gyroscope update를 시작합니다.

[`func startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())

handler 없이 gyroscope update를 시작합니다.

[`func stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())

gyroscope update를 중지합니다.

[`var gyroData: CMGyroData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)

가장 최근 gyroscope data sample입니다.

현재 페이지: CMGyroHandler
