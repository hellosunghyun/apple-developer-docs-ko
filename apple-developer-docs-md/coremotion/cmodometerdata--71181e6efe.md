---
title: "CMOdometerData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmodometerdata"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.891416+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmodometerdata#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMOdometerData

class

CMOdometerData
==============

workout용 odometer data를 나타내는 class입니다.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 1.0+

    class CMOdometerData

[개요](https://developer.apple.com/documentation/coremotion/cmodometerdata#overview)

-----------------------------------------------------------------------------------------

측정값을 가져오려면 [`speed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)
 및 [`slope`](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-96hlt)
 property를 사용합니다. 거리를 계산하려면 [`deltaDistance`](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltadistance)
 및 [`deltaAltitude`](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltaaltitude)
 property를 사용합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmodometerdata#topics)

-------------------------------------------------------------------------------------

### [speed와 slope 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata#Getting-speed-and-slope)

[`var speed: CLLocationSpeed`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speed)

초당 미터 단위로 측정한 device의 순간 속도입니다.

[`var slope: Double?`](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4)

이동 방향을 기준으로 해당 위치의 경사를 degree 단위로 나타낸 값입니다.

[`var maxAbsSlope: Double?`](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd)

모든 방향을 기준으로 해당 위치의 최대 절대 경사를 degree 단위로 나타낸 값입니다.

### [date와 time 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata#Getting-date-and-times)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmodometerdata/startdate)

device가 odometer data 기록을 시작한 시각입니다.

[`var endDate: Date`](https://developer.apple.com/documentation/coremotion/cmodometerdata/enddate)

device가 odometer data 기록을 중지한 시각입니다.

[`var gpsDate: Date`](https://developer.apple.com/documentation/coremotion/cmodometerdata/gpsdate)

해당 위치와 연결된 GPS 측정 시각입니다.

### [거리 측정하기](https://developer.apple.com/documentation/coremotion/cmodometerdata#Measuring-distances)

[`var deltaDistance: CLLocationDistance`](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltadistance)

사용자가 이전 위치 이후 이동한 거리 변화를 meter 단위로 나타낸 값입니다.

[`var deltaAltitude: CLLocationDistance`](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltaaltitude)

해당 위치와 연결된 평균 해수면 기준 고도 변화를 meter 단위로 나타낸 값입니다.

### [위치 정확도 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata#Getting-the-location-accuracy)

[`var speedAccuracy: CLLocationSpeedAccuracy`](https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy)

speed 값의 정확도입니다.

[`var verticalAccuracy: CLLocationAccuracy`](https://developer.apple.com/documentation/coremotion/cmodometerdata/verticalaccuracy)

고도 값의 유효성과 추정 오차를 meter 단위로 나타낸 값입니다.

[`var deltaDistanceAccuracy: CLLocationAccuracy`](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltadistanceaccuracy)

거리 변화 값의 정확도입니다.

### [device 가져오기](https://developer.apple.com/documentation/coremotion/cmodometerdata#Getting-the-device)

[`var originDevice: CMOdometerOriginDevice`](https://developer.apple.com/documentation/coremotion/cmodometerdata/origindevice)

data를 측정한 device입니다.

[`enum CMOdometerOriginDevice`](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice)

odometer sample이 생성된 device입니다.

### [Initializer](https://developer.apple.com/documentation/coremotion/cmodometerdata#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmodometerdata/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmodometerdata#relationships)

---------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmodometerdata#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmodometerdata#conforms-to)

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
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmodometerdata#see-also)

-----------------------------------------------------------------------------------------

### [Pedometer와 fitness](https://developer.apple.com/documentation/coremotion/cmodometerdata#Pedometer-and-fitness)

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

system이 생성한 실시간 walking data를 가져오는 object입니다.

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

사용자가 걸어서 이동한 거리에 대한 정보입니다.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

사용자의 보행 activity 변화입니다.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

사용자가 device를 들고 이동하며 걸은 step 수입니다.

Deprecated

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

1 Hz로 수집한 heart rate data를 나타내는 class입니다.

현재 페이지: CMOdometerData
