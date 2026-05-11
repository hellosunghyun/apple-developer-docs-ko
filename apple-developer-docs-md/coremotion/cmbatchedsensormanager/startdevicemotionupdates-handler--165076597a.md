---
title: "startDeviceMotionUpdates(handler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.917626+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
    
*   startDeviceMotionUpdates(handler:)

instance method

startDeviceMotionUpdates(handler:)
==================================

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+visionOS 1.0+watchOS 10.0+

    func startDeviceMotionUpdates(handler: @escaping ([CMDeviceMotion]?, (any Error)?) -> Void)

[참고 항목](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------

### [device-motion data 수집하기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:)#Collecting-device-motion-data)

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates())

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/stopdevicemotionupdates())

[`var deviceMotionBatch: [CMDeviceMotion]?`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionbatch)

[`func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates())

[`struct DeviceMotionUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isdevicemotionactive)

현재 페이지: startDeviceMotionUpdates(handler:)
