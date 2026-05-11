---
title: "SRElectrocardiogramSample | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.030605+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRElectrocardiogramSample

class

SRElectrocardiogramSample
=========================

sample electrocardiogram sensor data입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    class SRElectrocardiogramSample

[개요](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#overview)

---------------------------------------------------------------------------------------------------

electrocardiogram(ECG) sensor는 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
type으로 이 object들의 array를 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#topics)

-----------------------------------------------------------------------------------------------

### [ECG data 접근하기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#Accessing-ECG-data)

[`var date: Date`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/date)

session 시작 시점이 아니라 ECG sensor data recording의 시작 날짜입니다.

[`var frequency: Measurement<UnitFrequency>`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/frequency)

ECG sensor가 data를 기록하는 hertz 단위의 frequency입니다.

[`var lead: SRElectrocardiogramSample.Lead`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/lead-swift.property)

ECG data를 기록할 때 사용한 lead입니다.

[`enum Lead`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/lead-swift.enum)

ECG data를 기록할 때 사람이 사용하는 lead의 위치입니다.

[`var session: SRElectrocardiogramSession`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/session)

이 sample이 발생한 session입니다.

[`class SRElectrocardiogramSession`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession)

device가 일정 기간 동안 기록한 ECG data를 나타내는 object입니다.

[`var data: [SRElectrocardiogramData]`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/data)

sensor가 기록한 data입니다.

[`class SRElectrocardiogramData`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata)

sensor가 기록한 ECG data 표현입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#relationships)

-------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 대상](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

현재 페이지는 SRElectrocardiogramSample입니다
