---
title: "CMFallDetectionManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.897530+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMFallDetectionManager

class

CMFallDetectionManager
======================

fall detection event를 관리하는 object입니다.

watchOS 7.2+

    class CMFallDetectionManager

[개요](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#overview)

-------------------------------------------------------------------------------------------------

Series 4 이후의 Apple Watch는 착용자가 넘어졌는지 감지하고, 필요한 경우 응급 service에 연락할 수 있습니다. `CMFallDetectionManager`를 사용하면 app이 사용자의 authorization을 요청하고, 이런 _fall detection event_ 알림을 받을 delegate를 설정할 수 있습니다. 자세한 내용은 [Use fall detection with Apple Watch](https://support.apple.com/en-us/HT208944)
를 참고하십시오.

`CMFallDetectionManager`를 사용하려면 Apple의 entitlement가 필요합니다. entitlement를 신청하려면 [Fall Detection Entitlement Request](https://developer.apple.com/contact/request/fall-detection-api)
를 참고하십시오. 이 entitlement를 사용하면 추가 capability 없이도 app을 background에서 실행할 수 있습니다. 다만 app에 필요하다면 다른 background mode용 capability를 추가할 수 있습니다.

app에서 fall을 감지하는 방법은 두 가지입니다. HealthKit에서 [`numberOfTimesFallen`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/numberOfTimesFallen)
 sample을 query하거나, Core Motion의 `CMFallDetectionManager`를 사용할 수 있습니다.

### [fall 감지 및 대응](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Detect-and-Respond-to-Falls)

Core Motion fall detection manager는 app이 적시에 fall에 반응해 넘어지는 사람을 도와야 하는 경우 특히 유용합니다.

fall detection manager는 다음을 제공합니다.

*   app에 실시간으로 알립니다
    
*   모든 fall event를 app에 알립니다
    
*   app이 fall에 대응할 수 있도록 background runtime을 제공합니다
    

### [시간 경과에 따른 fall 감지 및 모니터링](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Detect-and-Monitor-Falls-Over-Time)

HealthKit sample은 더 긴 기간 동안 fall을 모니터링하는 app에 특히 유용합니다. fall event와 HealthKit이 sample을 업데이트하는 시점 사이에 지연이 있을 수 있기 때문입니다.

HealthKit은 다음을 제공합니다.

*   fall을 감지한 device뿐 아니라, 사용자의 HealthKit data에 접근할 수 있는 모든 device에서 사용할 수 있는 sample
    
*   넘어졌던 사람이 fall을 확인했거나 system이 fall을 응급 service로 escalated한 경우의 fall sample. 사용자가 fall alert를 dismiss하면 HealthKit은 그 fall을 기록하지 않습니다.
    

### [manager 생성](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Create-the-Manager)

fall detection 알림을 받으려면 먼저 현재 device에서 이 기능을 사용할 수 있는지 확인합니다. 사용할 수 있다면 manager를 만들고 delegate를 설정합니다.

    if CMFallDetectionManager.isAvailable  {
        
        // manager를 생성합니다.
        let manager = CMFallDetectionManager()
        
        // CMFallDetectionDelegte protocol을 채택한 delegate를 할당합니다.
        manager.delegate = myDelegate
        
        // manager reference를 유지합니다.
        myManager = manager
    }
    

delegate는 가능한 한 이르게, 이상적으로는 extension delegate의 [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/applicationDidFinishLaunching())
 method에서 설정합니다. background에서 app을 실행할 때 system이 app의 user interface를 생성하지 않을 수 있으므로, interface controller가 활성화될 때처럼 user interface code나 SwiftUI의 [`ScenePhase`](https://developer.apple.com/documentation/SwiftUI/ScenePhase)
 state 변경에 반응하는 코드에서 delegate를 설정할 수 없습니다.

### [user authorization 요청](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Request-User-Authorization)

user interface가 로드된 후 이전에 승인을 요청했는지 확인합니다. 아직 요청하지 않았다면 [`requestAuthorization(handler:)`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:))
를 호출해 요청을 시작합니다.

    // 사용자에게 fall detection event 알림 authorization을
    // 이미 요청했는지 확인합니다.
    if myManager?.authorizationStatus == .notDetermined {
        
        // authorization을 요청합니다.
        myManager?.requestAuthorization { (authorizationStatus) in
            
            // authorization status에 대응합니다.
        }
    }
    

사용자가 app을 승인한 경우에만 delegate가 fall detection event 알림을 받습니다. 사용자는 언제든지 Settings > Privacy > Fall Detection에서 app의 authorization state를 변경할 수 있습니다.

delegate를 설정하고 사용자가 authorization을 부여하면 app은 최근 fall event를 확인합니다. system이 event를 찾으면 delegate의 [`fallDetectionManager(_:didDetect:completionHandler:)`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:))
 method를 호출하고 가장 최근 event를 전달합니다. 이후 실행에서는 app이 계속 승인된 상태이고 system이 최근 fall event를 감지한 경우, delegate를 설정하자마자 system이 `fallDetectionManager(_:didDetect:completionHandler:)`를 호출합니다.

system은 새로운 fall detection event에 대응할 수 있도록 background에서 app을 깨우기도 합니다. system은 app이 event에 대응하고 completion handler를 호출할 수 있도록 짧은 시간만 제공합니다. app이 이 시간을 초과하면 system이 app을 suspend할 수 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#topics)

---------------------------------------------------------------------------------------------

### [사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Checking-Availability)

[`class var isAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/isavailable)

현재 device가 fall detection을 지원하는지 나타내는 Boolean 값입니다.

### [authorization 요청](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Requesting-Authorization)

[`func requestAuthorization(handler: (CMAuthorizationStatus) -> Void)`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/requestauthorization(handler:))

fall detection event 알림을 받기 위한 authorization을 요청합니다.

[`var authorizationStatus: CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/authorizationstatus)

fall detection event 알림 수신에 대한 authorization status입니다.

[`enum CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmauthorizationstatus)

motion 관련 기능의 authorization status입니다.

### [event 처리](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Handling-Events)

[`var delegate: (any CMFallDetectionDelegate)?`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager/delegate)

fall detection event 알림을 받을 수 있는 delegate입니다.

[`protocol CMFallDetectionDelegate`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)

fall detection event 정보와 authorization status 변경을 받는 delegate입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#relationships)

-----------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#see-also)

-------------------------------------------------------------------------------------------------

### [fall detection](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager#Fall-detection)

[`protocol CMFallDetectionDelegate`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)

fall detection event 정보와 authorization status 변경을 받는 delegate입니다.

[`class CMFallDetectionEvent`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)

fall detection event data를 담는 object입니다.

[`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription)

app이 fall detection event data 접근 permission을 요청하는 이유를 사용자에게 설명하는 메시지입니다.

현재 페이지는 CMFallDetectionManager입니다
