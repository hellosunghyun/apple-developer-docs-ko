---
title: "SRElectrocardiogramData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.032856+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRElectrocardiogramData

class

SRElectrocardiogramData
=======================

sensor가 기록한 ECG data를 나타내는 표현입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    class SRElectrocardiogramData

[주제](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#topics)

---------------------------------------------------------------------------------------------

### [electrocardiogram 세부 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#Getting-electrocardiogram-details)

[`var flags: SRElectrocardiogramData.Flags`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.property)

[`struct Flags`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct)

sample ECG data를 읽는 동안 발생하는 sensor context 또는 event입니다.

[`var value: Measurement<UnitElectricPotentialDifference>`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/value)

microvolt 단위의 electrocardiogram data입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#relationships)

-----------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#conforms-to)

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
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#see-also)

-------------------------------------------------------------------------------------------------

### [Accessing ECG data](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata#Accessing-ECG-data)

[`var date: Date`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/date)

session 시작 시점이 아니라 ECG sensor data recording의 시작 날짜입니다.

[`var frequency: Measurement<UnitFrequency>`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/frequency)

ECG sensor가 data를 기록하는 hertz 단위의 주파수입니다.

[`var lead: SRElectrocardiogramSample.Lead`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/lead-swift.property)

ECG data를 기록할 때 사용한 lead입니다.

[`enum Lead`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/lead-swift.enum)

ECG data를 기록할 때 사람이 사용하는 lead 위치입니다.

[`var session: SRElectrocardiogramSession`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/session)

이 sample이 발생한 session입니다.

[`class SRElectrocardiogramSession`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession)

device가 일정 기간 동안 기록한 ECG data를 나타내는 object입니다.

[`var data: [SRElectrocardiogramData]`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/data)

sensor가 기록한 data입니다.

현재 페이지는 SRElectrocardiogramData입니다
