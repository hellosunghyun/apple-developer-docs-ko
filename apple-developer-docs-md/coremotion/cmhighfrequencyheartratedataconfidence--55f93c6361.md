---
title: "CMHighFrequencyHeartRateDataConfidence | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.912991+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMHighFrequencyHeartRateDataConfidence

enum

CMHighFrequencyHeartRateDataConfidence
======================================

heart rate data의 정확도에 대한 confidence level입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+visionOS 1.0+watchOS 10.0+

    enum CMHighFrequencyHeartRateDataConfidence

[주제](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#topics)

-------------------------------------------------------------------------------------------------------------

### [confidence level](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#Levels-of-confidence)

[`case low`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence/low)

heart rate data에 대한 confidence level이 낮습니다.

[`case medium`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence/medium)

heart rate data에 대한 confidence level이 중간입니다.

[`case high`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence/high)

heart rate data에 대한 confidence level이 높습니다.

[`case highest`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence/highest)

heart rate data에 대한 가장 높은 confidence level입니다.

### [초기화 method](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence/init(rawvalue:))

[관계](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#relationships)

---------------------------------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#see-also)

-----------------------------------------------------------------------------------------------------------------

### [heart rate data 접근](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence#Accessing-heart-rate-data)

[`var heartRate: Double`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/heartrate)

heart rate 값(BPM 단위)입니다.

[`var confidence: CMHighFrequencyHeartRateDataConfidence`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/confidence)

heart rate 값의 confidence level입니다.

현재 페이지는 CMHighFrequencyHeartRateDataConfidence입니다.
