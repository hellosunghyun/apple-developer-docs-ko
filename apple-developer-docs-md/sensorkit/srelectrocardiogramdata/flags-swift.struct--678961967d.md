---
title: "SRElectrocardiogramData.Flags | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.034734+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRElectrocardiogramData](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata)
    
*   SRElectrocardiogramData.Flags

struct

SRElectrocardiogramData.Flags
=============================

sample ECG data를 읽는 동안 발생하는 sensor context 또는 event입니다.

iOS 17.4+iPadOS 17.4+Mac Catalyst 17.4+

    struct Flags

[주제](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#topics)

----------------------------------------------------------------------------------------------------------------

### [context 또는 event 가져오기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#Getting-context-or-events)

[`static var crownTouched: SRElectrocardiogramData.Flags`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct/crowntouched)

사람이 crown을 터치할 때 system이 ECG data를 기록합니다.

[`static var signalInvalid: SRElectrocardiogramData.Flags`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct/signalinvalid)

ECG data에 유효하지 않은 sensor signal이 발생합니다.

### [flag 초기화](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#Initializing-flags)

[`init(rawValue: UInt)`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct/init(rawvalue:))

ECG flags struct를 초기화합니다.

[관계](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#relationships)

------------------------------------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`ExpressibleByArrayLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByArrayLiteral)
    
*   [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    
*   [`SetAlgebra`](https://developer.apple.com/documentation/Swift/SetAlgebra)
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#see-also)

--------------------------------------------------------------------------------------------------------------------

### [electrocardiogram 세부 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct#Getting-electrocardiogram-details)

[`var flags: SRElectrocardiogramData.Flags`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.property)

[`var value: Measurement<UnitElectricPotentialDifference>`](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/value)

microvolt 단위의 electrocardiogram data입니다.

현재 페이지는 SRElectrocardiogramData.Flags입니다
