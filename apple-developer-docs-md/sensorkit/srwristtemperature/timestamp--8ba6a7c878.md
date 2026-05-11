---
title: "timestamp | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srwristtemperature/timestamp"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.032740+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srwristtemperature/timestamp#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRWristTemperature](https://developer.apple.com/documentation/sensorkit/srwristtemperature)
    
*   timestamp

instance property

timestamp
=========

device가 temperature를 기록한 date와 time입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var timestamp: Date { get }

[참고 항목](https://developer.apple.com/documentation/sensorkit/srwristtemperature/timestamp#see-also)

------------------------------------------------------------------------------------------------------

### [temperature 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srwristtemperature/timestamp#Getting-temperature-information)

[`var value: Measurement<UnitTemperature>`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/value)

celsius 단위의 temperature sensor 값입니다.

[`var errorEstimate: Measurement<UnitTemperature>`](https://developer.apple.com/documentation/sensorkit/srwristtemperature/errorestimate)

temperature 측정의 error 양에 대한 추정치입니다.

현재 페이지: timestamp
