---
title: "CMHeadphoneActivityManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.885330+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMHeadphoneActivityManager

class

CMHeadphoneActivityManager
==========================

headphone activity service를 시작하고 관리하는 object입니다.

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+macOS 15.0+watchOS 11.0+

    class CMHeadphoneActivityManager

[개요](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#overview)

-----------------------------------------------------------------------------------------------------

이 class는 app에 headphone activity update를 전달합니다. manager instance를 사용해 device가 headphone activity update를 지원하는지 확인하고, update를 시작하거나 중지합니다. 이 class를 사용하기 전에 [`isActivityAvailable`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable)
 및 [`isStatusAvailable`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable)
 를 확인해 기능을 사용할 수 있는지 먼저 점검합니다.

이 class는 [`CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
 와 유사한 정보를 제공하지만, activity 정보의 출처가 device motion이 아니라 headphone motion이라는 점이 다릅니다.

[주제](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#topics)

-------------------------------------------------------------------------------------------------

### [사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#Checking-Availability)

[`var isActivityAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable)

현재 device가 headphone activity를 지원하는지 나타내는 Boolean 값입니다.

[`var isActivityActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityactive)

headphone motion activity가 활성 상태인지 나타내는 Boolean 값입니다.

[`var isStatusAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusavailable)

현재 device가 headphone status를 지원하는지 나타내는 Boolean 값입니다.

[`var isStatusActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isstatusactive)

headphone status가 활성 상태인지 나타내는 Boolean 값입니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus())

headphone activity 모니터링의 authorization status를 반환합니다.

### [update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#Starting-and-Stopping-Updates)

[`func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startactivityupdates(to:withhandler:))

headphone activity update를 시작하고, 지정한 queue를 통해 지정한 handler에 data를 제공합니다.

[`func stopActivityUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopactivityupdates())

headphone activity update를 중지합니다.

[`func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/startstatusupdates(to:withhandler:))

headphone status update를 시작하고, 지정한 queue를 통해 지정한 handler에 data를 제공합니다.

[`func stopStatusUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/stopstatusupdates())

headphone status update를 중지합니다.

### [지원 type](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#Supporting-Types)

[`enum Status`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/status)

Headphone 연결 status update입니다.

[`typealias ActivityHandler`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler)

headphone motion activity data를 사용할 수 있을 때 호출되는 handler의 type입니다.

[`typealias StatusHandler`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/statushandler)

status update와 함께 호출되는 handler의 type입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#relationships)

---------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#see-also)

-----------------------------------------------------------------------------------------------------

### [Activity](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager#Activity)

[`class CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

device에 저장된 motion data에 대한 access를 관리하는 object입니다.

[`class CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

단일 motion update event의 data입니다.

[headphones에서 motion-activity data 가져오기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones)

app이 headphones의 motion-activity 변화를 수신하도록 구성합니다.

현재 페이지: CMHeadphoneActivityManager
