---
title: "CMMagnetometerHandler | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900745+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMagnetometerHandler

type alias

CMMagnetometerHandler
=====================

magnetometer data를 처리하는 block callback의 type입니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    Type Alias CMMagnetometerHandler = (CMMagnetometerData?, (any Error)?) -> Void

[설명](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler#Discussion)

----------------------------------------------------------------------------------------------------

`CMMagnetometerHandler` type의 block은 처리할 magnetometer data가 있을 때 호출됩니다. 이 block은 [`startMagnetometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))
 method as the second argument. Blocks of this type return no value but take two arguments:

`magnetometerData`

세 이동 축의 magnetic-field 값을 담는 field를 가진 [`CMMagneticField`](https://developer.apple.com/documentation/coremotion/cmmagneticfield)
 structure with fields holding magnetic-field values for the three axes of movement.

`error`

magnetometer data를 제공하는 동안 발생한 error를 나타내는 object입니다. error가 발생하면 magnetometer update를 중지하고 사용자에게 문제를 알려야 합니다. error가 없으면 이 argument는 `nil`입니다. Core Motion error는 [`CMErrorDomain`](https://developer.apple.com/documentation/coremotion/cmerrordomain)
 domain and the [`CMError`](https://developer.apple.com/documentation/coremotion/cmerror)
 type.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler#see-also)

------------------------------------------------------------------------------------------------

### [Magnetometer update 관리](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler#Managing-Magnetometer-Updates)

[`var magnetometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)

system이 magnetometer data를 block handler에 전달하는 간격(초)입니다.

[`func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 magnetometer update를 시작합니다.

[`func startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())

block handler 없이 magnetometer update를 시작합니다.

[`func stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())

magnetometer update를 중지합니다.

[`var magnetometerData: CMMagnetometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)

가장 최근의 magnetometer data sample입니다.

현재 페이지: CMMagnetometerHandler
