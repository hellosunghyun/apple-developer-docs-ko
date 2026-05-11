---
title: "magnetometerUpdateInterval | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.900556+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
    
*   magnetometerUpdateInterval

instance property

magnetometerUpdateInterval
==========================

system이 block handler에 magnetometer data를 전달하는 간격(초)입니다.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.1+watchOS 2.0+

    var magnetometerUpdateInterval: TimeInterval { get set }

[설명](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval#Discussion)

-------------------------------------------------------------------------------------------------------------------------

system은 [`startMagnetometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))
에 지정한 block handler에 이 property 값으로 결정되는 규칙적인 간격으로 magnetometer data를 제공합니다. 간격 단위는 초입니다. 이 property 값은 최소값과 최대값으로 제한되며, 최대값은 hardware가 지원하는 최대 frequency에 따라 결정됩니다. app이 magnetometer data 간격에 민감하다면 전달된 [`CMMagnetometerData`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)
instance의 timestamp를 항상 확인해 실제 update interval을 판단해야 합니다.

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Magnetometer Update 관리](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval#Managing-Magnetometer-Updates)

[`func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))

operation queue와 지정한 handler로 magnetometer update를 시작합니다.

[`func startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())

block handler 없이 magnetometer update를 시작합니다.

[`func stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())

magnetometer update를 중지합니다.

[`var magnetometerData: CMMagnetometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)

가장 최근의 magnetometer data sample입니다.

[`typealias CMMagnetometerHandler`](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

magnetometer data를 처리하는 block callback의 type입니다.

현재 페이지는 magnetometerUpdateInterval입니다.
