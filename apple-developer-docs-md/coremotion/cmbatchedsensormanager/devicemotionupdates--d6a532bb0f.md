---
title: "CMBatchedSensorManager.DeviceMotionUpdates | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.917368+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
    
*   CMBatchedSensorManager.DeviceMotionUpdates

struct

CMBatchedSensorManager.DeviceMotionUpdates
==========================================

watchOS 10.0+

    struct DeviceMotionUpdates

[주제](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#topics)

-----------------------------------------------------------------------------------------------------------------

### [Structure](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#Structures)

[`struct Iterator`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates/iterator)

[관계](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#relationships)

-------------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#conforms-to)

*   [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#see-also)

---------------------------------------------------------------------------------------------------------------------

### [device-motion data 수집하기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates#Collecting-device-motion-data)

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates())

[`func startDeviceMotionUpdates(handler: ([CMDeviceMotion]?, (any Error)?) -> Void)`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:))

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/stopdevicemotionupdates())

[`var deviceMotionBatch: [CMDeviceMotion]?`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionbatch)

[`func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates())

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isdevicemotionactive)

현재 페이지: CMBatchedSensorManager.DeviceMotionUpdates
