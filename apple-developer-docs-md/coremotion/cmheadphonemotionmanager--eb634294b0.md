---
title: "CMHeadphoneMotionManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.869558+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMHeadphoneMotionManager

class

CMHeadphoneMotionManager
========================

headphone motion service를 시작하고 관리하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+macOS 14.0+watchOS 7.0+

    class CMHeadphoneMotionManager

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#mentions)

-------------------------------------------------------------------------------------------------------

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[개요](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#overview)

---------------------------------------------------------------------------------------------------

이 class는 headphone motion update를 app에 전달합니다. manager의 instance를 사용해 device가 motion을 지원하는지 확인하고, update를 시작하고 중지합니다. motion update를 받아 응답하려면 [`CMHeadphoneMotionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate)
 protocol을 채택합니다. 이 class를 사용하기 전에 [`isDeviceMotionAvailable`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/isdevicemotionavailable)
 를 확인해 기능을 사용할 수 있는지 확인합니다.

### [좌표축 식별하기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#Identify-the-coordinate-axes)

attitude data를 해석하려면 device 좌표축의 방향을 알아야 합니다. 다음 그림은 motion을 지원하는 Apple headphone의 양의 x축, 양의 y축, 양의 z축을 보여 줍니다.

![양쪽 device의 양의 x축, 양의 y축, 양의 z축을 나타내는 레이블이 포함된 AirPods Max와 AirPods Pro 그림입니다.](https://docs-assets.developer.apple.com/published/4f7825123ffe36ae9788ba56f7f92bd7/media-4302074%402x.png)

[주제](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#topics)

-----------------------------------------------------------------------------------------------

### [사용 가능 여부 확인하기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#Checking-Availability)

[`var isDeviceMotionAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/isdevicemotionavailable)

현재 device가 headphone motion manager를 지원하는지 나타내는 Boolean 값입니다.

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/isdevicemotionactive)

headphone motion manager가 활성 상태인지 나타내는 Boolean 값입니다.

[`var isConnectionStatusActive: Bool`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/isconnectionstatusactive)

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/authorizationstatus())

headphone motion 모니터링의 authorization status를 반환합니다.

### [Update 시작 및 중지](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#Starting-and-Stopping-Updates)

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates())

device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMHeadphoneMotionManager.DeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:))

handler와 함께 device-motion update를 시작합니다.

[`func startConnectionStatusUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startconnectionstatusupdates())

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`func stopConnectionStatusUpdates()`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/stopconnectionstatusupdates())

### [Delegate 가져오기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#Getting-the-Delegate)

[`var delegate: (any CMHeadphoneMotionManagerDelegate)?`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/delegate)

headphone motion manager event를 수신하는 object입니다.

[`protocol CMHeadphoneMotionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate)

headphone 연결 및 연결 해제를 위한 interface를 정의하는 method 집합입니다.

### [Device-Motion 정보 가져오기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#Getting-Device-Motion-Information)

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotion)

가장 최근의 device-motion data입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#relationships)

-------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#see-also)

---------------------------------------------------------------------------------------------------

### [Device motion](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager#Device-motion)

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

gravity 효과 같은 환경 bias를 제거하도록 system이 처리한 motion data를 가져옵니다.

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

device의 attitude, rotation rate, acceleration 측정값을 캡슐화합니다.

[`class CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)

특정 시점의 알려진 기준 frame에 대한 device의 방향입니다.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

attitude 관련 motion data의 기준 frame을 나타내는 constant입니다.

현재 페이지: CMHeadphoneMotionManager
