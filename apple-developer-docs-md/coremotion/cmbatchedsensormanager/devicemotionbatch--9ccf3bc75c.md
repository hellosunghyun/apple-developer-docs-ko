---
title: "deviceMotionBatch | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionbatch"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.917455+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionbatch#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
    
*   deviceMotionBatch

instance property

deviceMotionBatch
=================

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+visionOS 1.0+watchOS 10.0+

    var deviceMotionBatch: [CMDeviceMotion]? { get }

[참고 항목](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionbatch#see-also)

-------------------------------------------------------------------------------------------------------------------

### [device-motion data 수집](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionbatch#Collecting-device-motion-data)

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates())

[`func startDeviceMotionUpdates(handler: ([CMDeviceMotion]?, (any Error)?) -> Void)`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:))

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/stopdevicemotionupdates())

[`func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates())

[`struct DeviceMotionUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isdevicemotionactive)

현재 페이지는 deviceMotionBatch입니다
