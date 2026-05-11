---
title: "CMPedometerData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmpedometerdata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.888692+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmpedometerdata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMPedometerData

class

CMPedometerData
===============

사용자가 걸어서 이동한 거리 정보입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+watchOS 2.0+

    class CMPedometerData

[개요](https://developer.apple.com/documentation/coremotion/cmpedometerdata#overview)

------------------------------------------------------------------------------------------

이 class의 instance는 직접 만들지 않습니다. 대신 [`CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)
 object를 사용해 system에 pedometer data를 요청합니다. 각 요청의 data는 이 class의 instance로 패키징되어 pedometer object에 등록한 handler로 전달됩니다.

[주제](https://developer.apple.com/documentation/coremotion/cmpedometerdata#topics)

--------------------------------------------------------------------------------------

### [날짜 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata#Getting-the-Dates)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/startdate)

pedometer data의 시작 시간입니다.

[`var endDate: Date`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/enddate)

pedometer data의 종료 시간입니다.

### [보행 data 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata#Getting-the-Pedestrian-Data)

[`var numberOfSteps: NSNumber`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/numberofsteps)

사용자가 걸은 step 수입니다.

[`var distance: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance)

사용자가 이동한 추정 거리(미터)입니다.

[`var averageActivePace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace)

사용자의 평균 pace이며, 단위는 미터당 초입니다.

[`var currentPace: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace)

사용자의 현재 pace이며, 단위는 미터당 초입니다.

[`var currentCadence: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence)

step를 밟는 속도이며, 단위는 초당 step 수입니다.

### [층수 가져오기](https://developer.apple.com/documentation/coremotion/cmpedometerdata#Getting-the-Floor-Counts)

[`var floorsAscended: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended)

걸어서 올라간 대략적인 층수입니다.

[`var floorsDescended: NSNumber?`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsdescended)

걸어서 내려간 대략적인 층수입니다.

### [initializer](https://developer.apple.com/documentation/coremotion/cmpedometerdata#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmpedometerdata/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmpedometerdata#relationships)

----------------------------------------------------------------------------------------------------

### [상속 관계](https://developer.apple.com/documentation/coremotion/cmpedometerdata#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmpedometerdata#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmpedometerdata#see-also)

------------------------------------------------------------------------------------------

### [Pedometer와 fitness](https://developer.apple.com/documentation/coremotion/cmpedometerdata#Pedometer-and-fitness)

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

system이 생성하는 실시간 walking data를 가져오는 object입니다.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

사용자의 보행 activity 변화입니다.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

device와 함께 사용자가 걸은 step 수입니다.

Deprecated

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

workout용 odometer data를 나타내는 class입니다.

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

1 Hz로 수집한 heart rate data를 나타내는 class입니다.

현재 페이지: CMPedometerData
