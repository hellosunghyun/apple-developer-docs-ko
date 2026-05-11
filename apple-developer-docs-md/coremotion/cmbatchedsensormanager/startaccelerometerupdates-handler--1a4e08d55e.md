---
title: "startAccelerometerUpdates(handler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.917025+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
    
*   startAccelerometerUpdates(handler:)

instance method

startAccelerometerUpdates(handler:)
===================================

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+visionOS 1.0+watchOS 10.0+

    func startAccelerometerUpdates(handler: @escaping ([CMAccelerometerData]?, (any Error)?) -> Void)

[같이 보기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------

### [accelerometer data 수집하기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:)#Collecting-accelerometer-data)

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates())

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/stopaccelerometerupdates())

[`var accelerometerBatch: [CMAccelerometerData]?`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch)

[`func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates())

[`struct AccelerometerUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates)

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isaccelerometeractive)

현재 페이지: startAccelerometerUpdates(handler:)
