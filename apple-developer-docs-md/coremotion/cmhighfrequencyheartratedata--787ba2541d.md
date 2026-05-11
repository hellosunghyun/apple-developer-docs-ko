---
title: "CMHighFrequencyHeartRateData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891626+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMHighFrequencyHeartRateData

class

CMHighFrequencyHeartRateData
============================

1 Hz로 수집한 heart rate data를 나타내는 class입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+watchOS 10.0+

    class CMHighFrequencyHeartRateData

[개요](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#overview)

-------------------------------------------------------------------------------------------------------

data를 가져오려면 [`heartRate`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/heartrate)
 property를 사용하고, 정확도는 [`confidence`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/confidence)
 property로 확인합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#topics)

---------------------------------------------------------------------------------------------------

### [Accessing heart rate data](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#Accessing-heart-rate-data)

[`var heartRate: Double`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/heartrate)

BPM 단위의 heart rate 값입니다.

[`var confidence: CMHighFrequencyHeartRateDataConfidence`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/confidence)

heart rate 값의 confidence level입니다.

[`enum CMHighFrequencyHeartRateDataConfidence`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence)

heart rate data 정확도에 대한 confidence level입니다.

### [Getting the sample date](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#Getting-the-sample-date)

[`var date: Date?`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/date)

heart rate 값이 발생한 시각입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#relationships)

-----------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#see-also)

-------------------------------------------------------------------------------------------------------

### [Pedometer and fitness](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata#Pedometer-and-fitness)

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

system이 생성하는 실시간 walking data를 가져오는 object입니다.

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

사용자가 걸어서 이동한 거리에 대한 정보입니다.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

사용자의 보행 activity 변화입니다.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

device를 들고 사용자가 걸은 step 수입니다.

Deprecated

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

workout용 odometer data를 나타내는 class입니다.

현재 페이지는 CMHighFrequencyHeartRateData입니다
