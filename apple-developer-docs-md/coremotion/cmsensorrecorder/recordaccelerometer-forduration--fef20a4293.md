---
title: "recordAccelerometer(forDuration:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.877514+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)
    
*   recordAccelerometer(forDuration:)

instance method

recordAccelerometer(forDuration:)
=================================

지정한 시간 동안 accelerometer data 기록을 시작합니다.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.1+watchOS 2.0+

    func recordAccelerometer(forDuration duration: TimeInterval)

[Parameters](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:)#parameters)

---------------------------------------------------------------------------------------------------------------------------------

`duration`

data를 기록할 시간(초)입니다. 최대 43,200초(12시간)까지 지정할 수 있습니다.

[논의](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:)#Discussion)

---------------------------------------------------------------------------------------------------------------------------------

이 method를 호출하면 system이 50Hz sample rate로 accelerometer data 캡처를 시작합니다. 앱이 suspend되거나 종료되어도 system은 지정한 시간 동안 data를 기록합니다. 수집된 data는 최대 3일 동안 앱에서 계속 접근할 수 있습니다.

현재 페이지: recordAccelerometer(forDuration:)
