---
title: "CMMotionActivityManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.879428+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMotionActivityManager

class

CMMotionActivityManager
=======================

device가 저장한 motion data에 대한 access를 관리하는 object입니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+watchOS 2.0+

    class CMMotionActivityManager

[개요](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#overview)

--------------------------------------------------------------------------------------------------

motion data는 사용자가 일정 시간 동안 걷고 있는지, 뛰고 있는지, 차량에 탑승 중인지, 정지 상태인지 반영합니다. 이 class를 사용하면 현재 motion 유형이 바뀔 때 notification을 요청하거나 과거의 motion 변경 data를 수집할 수 있습니다. 예를 들어 navigation app은 현재 motion 유형의 변화를 감지해 각각에 맞는 다른 경로를 제안할 수 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#topics)

----------------------------------------------------------------------------------------------

### [activity 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#Determining-Activity-Availability)

[`class func isActivityAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/isactivityavailable())

현재 device에서 motion data를 사용할 수 있는지 나타내는 Boolean 값을 반환합니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus())

app이 저장된 motion data를 가져올 권한이 있는지 나타내는 값을 반환합니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

### [activity update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#Starting-and-Stopping-Activity-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/startactivityupdates(to:withhandler:))

현재 motion data update를 app으로 전달하기 시작합니다.

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/stopactivityupdates())

app으로 전달하던 motion update를 중지합니다.

[`typealias CMMotionActivityHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)

device와 연관된 현재 motion을 보고하는 block입니다.

### [과거 activity data 가져오기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#Getting-Historical-Activity-Data)

[`func queryActivityStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMMotionActivityQueryHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:))

지정한 기간의 과거 motion data를 수집해 반환합니다.

[`typealias CMMotionActivityQueryHandler`](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)

지정한 query interval 사이에 발생한 motion update를 보고하는 block입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#relationships)

------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#see-also)

--------------------------------------------------------------------------------------------------

### [Activity](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager#Activity)

[`class CMHeadphoneActivityManager`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)

headphone activity service를 시작하고 관리하는 object입니다.

[`class CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

단일 motion update event에 대한 data입니다.

[헤드폰에서 motion-activity data 가져오기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones)

headphone의 motion-activity 변화를 수신하도록 app을 구성합니다.

현재 페이지는 CMMotionActivityManager입니다.
