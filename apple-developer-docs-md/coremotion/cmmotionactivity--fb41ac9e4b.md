---
title: "CMMotionActivity | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionactivity"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.885454+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionactivity#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMotionActivity

class

CMMotionActivity
================

단일 motion update event의 data입니다.

iOS 7.0+iPadOS 7.0+Mac Catalyst 13.1+macOS 15.0+watchOS 2.0+

    class CMMotionActivity

[개요](https://developer.apple.com/documentation/coremotion/cmmotionactivity#overview)

-------------------------------------------------------------------------------------------

motion을 지원하는 device에서는 [`CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
 or [`CMHeadphoneActivityManager`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)
 object to request updates when the current type of motion changes. When a change occurs, the update information is packaged into a [`CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)
 object and sent to your app.

이 class의 motion 관련 property는 상호 배타적이지 않습니다. 즉, motion 관련 property가 둘 이상 [`true`](https://developer.apple.com/documentation/Swift/true)
. For example, if the user was driving in a car and the car stopped at a red light, the update event associated with that change in motion would have both the [`automotive`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/automotive)
 and [`stationary`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/stationary)
 properties set to [`true`](https://developer.apple.com/documentation/Swift/true)
. It’s also possible for all of the properties to be set to [`false`](https://developer.apple.com/documentation/Swift/false)
 when the device is in motion but the movement doesn’t correlate to walking, running, cycling, or automotive travel.

이 class의 instance는 직접 만들지 않습니다. [`CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
 object creates them and sends them to the handler block you registered. For more information about how to initiate the delivery of motion activity updates to your app, see [`CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)
.

[주제](https://developer.apple.com/documentation/coremotion/cmmotionactivity#topics)

---------------------------------------------------------------------------------------

### [motion type 가져오기](https://developer.apple.com/documentation/coremotion/cmmotionactivity#Getting-the-Type-of-Motion)

[`var stationary: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/stationary)

device가 정지 상태인지 나타내는 Boolean 값입니다.

[`var walking: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/walking)

device가 걷는 사람에게 있는지 나타내는 Boolean 값입니다.

[`var running: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/running)

device가 달리는 사람에게 있는지 나타내는 Boolean 값입니다.

[`var automotive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/automotive)

device가 자동차 안에 있는지 나타내는 Boolean 값입니다.

[`var cycling: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/cycling)

device가 자전거에 있는지 나타내는 Boolean 값입니다.

[`var unknown: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown)

motion type을 알 수 없는지 나타내는 Boolean 값입니다.

### [motion metadata 가져오기](https://developer.apple.com/documentation/coremotion/cmmotionactivity#Getting-Metadata-for-the-Motion)

[`var startDate: Date`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/startdate)

motion 변화가 발생한 시각입니다.

[`var confidence: CMMotionActivityConfidence`](https://developer.apple.com/documentation/coremotion/cmmotionactivity/confidence)

motion type 평가의 confidence입니다.

[`enum CMMotionActivityConfidence`](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence)

motion data가 정확하다고 판단하는 confidence입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmmotionactivity#relationships)

-----------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmmotionactivity#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmmotionactivity#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmmotionactivity#see-also)

-------------------------------------------------------------------------------------------

### [Activity](https://developer.apple.com/documentation/coremotion/cmmotionactivity#Activity)

[`class CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

device에 저장된 motion data에 대한 접근을 관리하는 object입니다.

[`class CMHeadphoneActivityManager`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)

headphone activity service를 시작하고 관리하는 object입니다.

[headphone에서 motion-activity data 가져오기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones)

app이 headphone의 motion-activity 변화를 수신하도록 구성합니다.

현재 페이지: CMMotionActivity
