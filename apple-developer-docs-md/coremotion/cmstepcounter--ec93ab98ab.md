---
title: "CMStepCounter | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmstepcounter"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891526+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmstepcounter#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMStepCounter Deprecated

class

CMStepCounter
=============

device와 함께 사용자가 걸은 step 수입니다.

iOS 7.0–8.0DeprecatediPadOS 7.0–8.0DeprecatedMac Catalyst 13.1–13.1DeprecatedvisionOS 1.0–1.0Deprecated

    class CMStepCounter

[개요](https://developer.apple.com/documentation/coremotion/cmstepcounter#overview)

----------------------------------------------------------------------------------------

적절한 내장 hardware가 있는 device에서는 step 정보가 수집되어 저장되며, 이를 바탕으로 query를 실행해 사용자의 최근 physical activity를 확인할 수 있습니다. 이 class를 사용하면 현재 step data와 historical data를 모두 수집할 수 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmstepcounter#topics)

------------------------------------------------------------------------------------

### [step counting 사용 가능 여부 판단](https://developer.apple.com/documentation/coremotion/cmstepcounter#Determining-Step-Counting-Availability)

[`class func isStepCountingAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable())

현재 device에서 step-counting 지원이 가능한지를 나타내는 Boolean 값을 반환합니다.

### [step counting update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmstepcounter#Starting-and-Stopping-Step-Counting-Updates)

[`func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/startstepcountingupdates(to:updateon:withhandler:))

현재 step-counting data delivery를 app으로 시작합니다.

[`func stopStepCountingUpdates()`](https://developer.apple.com/documentation/coremotion/cmstepcounter/stopstepcountingupdates())

app으로 전달되는 step-counting update를 중지합니다.

[`typealias CMStepUpdateHandler`](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)

update가 시작된 이후 기록된 step 수를 보고하는 block입니다.

### [historical step counting data 가져오기](https://developer.apple.com/documentation/coremotion/cmstepcounter#Getting-Historical-Step-Counting-Data)

[`func queryStepCountStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMStepQueryHandler)`](https://developer.apple.com/documentation/coremotion/cmstepcounter/querystepcountstarting(from:to:to:withhandler:))

지정한 기간의 historical step count data를 수집해 반환합니다.

[`typealias CMStepQueryHandler`](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)

query operation의 step 수를 보고하는 block입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmstepcounter#relationships)

--------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmstepcounter#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 대상](https://developer.apple.com/documentation/coremotion/cmstepcounter#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmstepcounter#see-also)

----------------------------------------------------------------------------------------

### [Pedometer 및 fitness](https://developer.apple.com/documentation/coremotion/cmstepcounter#Pedometer-and-fitness)

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

system이 생성한 실시간 walking data를 가져오는 object입니다.

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

사용자가 도보로 이동한 거리에 대한 정보입니다.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

사용자의 보행 activity 변화입니다.

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

workout용 odometer data를 나타내는 class입니다.

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

1 Hz로 수집한 heart rate data를 나타내는 class입니다.

현재 페이지는 CMStepCounter입니다
