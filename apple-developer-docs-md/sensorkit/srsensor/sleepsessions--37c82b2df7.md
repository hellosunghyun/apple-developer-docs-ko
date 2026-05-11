---
title: "sleepSessions | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensor/sleepsessions"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.055391+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensor/sleepsessions#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)
    
*   sleepSessions

type property

sleepSessions
=============

iOS 26.0+iPadOS 26.0+Mac Catalyst 26.0+

    static let sleepSessions: SRSensor

[설명](https://developer.apple.com/documentation/sensorkit/srsensor/sleepsessions#discussion)

----------------------------------------------------------------------------------------------------

sleep session 수집용 sensor stream입니다.

이 stream은 Sleep Sessions sensor의 sample을 저장합니다. 이 stream에서 fetch하면 `SRSleepSession` type의 object를 반환합니다.

현재 페이지: sleepSessions
