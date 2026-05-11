---
title: "accelerometerBatch | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.916753+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
    
*   accelerometerBatch

instance property

accelerometerBatch
==================

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+visionOS 1.0+watchOS 10.0+

    var accelerometerBatch: [CMAccelerometerData]? { get }

[참고 항목](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch#see-also)

--------------------------------------------------------------------------------------------------------------------

### [accelerometer data 수집하기](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch#Collecting-accelerometer-data)

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates())

[`func startAccelerometerUpdates(handler: ([CMAccelerometerData]?, (any Error)?) -> Void)`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:))

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/stopaccelerometerupdates())

[`func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates())

[`struct AccelerometerUpdates`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates)

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isaccelerometeractive)

현재 페이지는 accelerometerBatch입니다
