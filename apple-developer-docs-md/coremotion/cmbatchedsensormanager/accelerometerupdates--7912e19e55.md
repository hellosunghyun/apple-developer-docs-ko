---
title: "CMBatchedSensorManager.AccelerometerUpdates | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.899997+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
    
*   CMBatchedSensorManager.AccelerometerUpdates

struct

CMBatchedSensorManager.AccelerometerUpdates
===========================================

watchOS 10.0+

    struct AccelerometerUpdates

[주제](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#topics)

------------------------------------------------------------------------------------------------------------------

### [Structure](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#Structures)

[`struct Iterator`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates/iterator)

[관계](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#relationships)

--------------------------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#conforms-to)

*   [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#see-also)

----------------------------------------------------------------------------------------------------------------------

### [accelerometer data 수집하기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates#Collecting-accelerometer-data)

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates())

[`func startAccelerometerUpdates(handler: ([CMAccelerometerData]?, (any Error)?) -> Void)`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:))

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/stopaccelerometerupdates())

[`var accelerometerBatch: [CMAccelerometerData]?`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch)

[`func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates())

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isaccelerometeractive)

현재 페이지: CMBatchedSensorManager.AccelerometerUpdates
