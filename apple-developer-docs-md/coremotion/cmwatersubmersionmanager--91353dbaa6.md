---
title: "CMWaterSubmersionManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.872213+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMWaterSubmersionManager

class

CMWaterSubmersionManager
========================

잠수 중 pressure 및 temperature data 수집을 관리하는 object입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    class CMWaterSubmersionManager

[언급된 항목](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#mentions)

-------------------------------------------------------------------------------------------------------

[잠수 data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

[개요](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#overview)

---------------------------------------------------------------------------------------------------

이 class를 사용하면 Apple Watch Ultra에서 실시간 depth, water pressure, water temperature data를 받을 수 있습니다.

먼저 app target의 information property list에서 [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription)
 key를 사용해 usage description을 지정합니다. 실시간 잠수 data에 접근하려면 entitlement도 포함해야 합니다.

최대 수심 6 m의 다이빙 data에 접근하려면 app에 Shallow Depth and Pressure capability를 추가합니다. 자세한 내용은 [Adding capabilities to your app](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app)
을 참고하세요.

최대 수심 40 m를 사용하려면 전체 Submerged Depth and Pressure entitlement를 신청해야 합니다. 자세한 내용은 [Express interest in the Submerged Depth and Pressure API](https://developer.apple.com/contact/request/submerged-depth-pressure-api/)
를 참고하세요.

다음으로 잠수 data를 사용할 수 있는지 확인합니다.

    guard CMWaterSubmersionManager.waterSubmersionAvailable else {
        return false
    }
    

[`waterSubmersionAvailable`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/watersubmersionavailable)
 property가 [`true`](https://developer.apple.com/documentation/Swift/true)
이면 [`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 object를 생성하고 delegate를 할당합니다.

    // Instantiate the submersion manager.
    submersionManager = CMWaterSubmersionManager()
    
    
    
    
    // Assign the submersion manager delegate.
    submersionManager.delegate = self
    

그러면 delegate가 system의 update를 받기 시작합니다. 자세한 내용은 [잠수 data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)
를 참고하세요.

[주제](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#topics)

-----------------------------------------------------------------------------------------------

### [delegate 설정](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#Setting-the-delegate)

[`var delegate: (any CMWaterSubmersionManagerDelegate)?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/delegate)

잠수 data와 event에 대한 update를 받는 object입니다.

### [사용 가능 여부와 권한 확인](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#Checking-availability-and-authorization)

[`class var waterSubmersionAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/watersubmersionavailable)

현재 device가 submersion manager를 지원하는지 나타내는 Boolean value입니다.

[`class var authorizationStatus: CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus)

app이 잠수 data를 받을 사용자 권한이 있는지 나타내는 value입니다.

### [최대 수심 접근](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#Accessing-the-maximum-depth)

[`var maximumDepth: Measurement<UnitLength>?`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/maximumdepth)

water submersion manager가 지원하는 최대 수심입니다.

[관계](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#relationships)

-------------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#see-also)

---------------------------------------------------------------------------------------------------

### [Water submersion](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager#Water-submersion)

[잠수 data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

water-submersion manager를 사용해 Apple Watch Ultra에서 water pressure, temperature, depth data를 받습니다.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

ambient pressure, water pressure, water temperature, submersion event에 대한 update를 받는 delegate입니다.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

device의 잠수 상태가 바뀌었음을 나타내는 event입니다.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

pressure와 depth data를 담은 update입니다.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

water temperature data를 담은 update입니다.

현재 페이지: CMWaterSubmersionManager
