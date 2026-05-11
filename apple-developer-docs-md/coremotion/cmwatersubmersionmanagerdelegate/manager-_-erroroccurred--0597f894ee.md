---
title: "manager(_:errorOccurred:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.901307+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)
    
*   manager(\_:errorOccurred:)

instance method

manager(\_:errorOccurred:)
==========================

error가 발생하면 delegate에 알립니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    func manager(
        _ manager: CMWaterSubmersionManager,
        errorOccurred error: any Error
    )

**Required**

[parameter](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------

`manager`

water submersion data용 manager입니다.

`error`

error 정보를 담은 error object입니다.

[언급된 항목](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)#mentions)

-----------------------------------------------------------------------------------------------------------------------------------------

[잠수 data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

[설명](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------

error에 대응하려면 이 method를 구현합니다.

    // Respond to errors.
    nonisolated func manager(_ manager: CMWaterSubmersionManager, errorOccurred error: Error) {
        logger.error("*** An error occurred: \(error.localizedDescription) ***")
    }
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)#see-also)

-------------------------------------------------------------------------------------------------------------------------------------

### [update 받기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:)#Receiving-updates)

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6)

water submersion event가 발생하면 delegate에 알립니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb)

새 pressure 및 depth measurement 집합을 delegate에 제공합니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua)

업데이트된 water temperature data를 delegate에 제공합니다.

**Required**

현재 페이지: manager(\_:errorOccurred:)
