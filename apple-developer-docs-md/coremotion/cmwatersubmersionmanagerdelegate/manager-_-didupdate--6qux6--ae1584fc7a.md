---
title: "manager(_:didUpdate:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.878557+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)
    
*   manager(\_:didUpdate:)

instance method

manager(\_:didUpdate:)
======================

water submersion event가 발생하면 delegate에 알립니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    func manager(
        _ manager: CMWaterSubmersionManager,
        didUpdate event: CMWaterSubmersionEvent
    )

**Required**

[parameter](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

`manager`

water submersion data용 manager입니다.

`event`

submersion state가 변경되었음을 나타내는 event입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6#Discussion)

-------------------------------------------------------------------------------------------------------------------------------------------

device의 submersion state 변경에 대응하려면 이 method를 구현합니다.

    nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate event: CMWaterSubmersionEvent) {
    
    
        let submerged: Bool?
        switch event.state {
        case .unknown:
            logger.info("*** Received an unknown event ***")
            submerged = nil
    
    
        case .notSubmerged:
            logger.info("*** Not Submerged Event ***")
            submerged = false
    
    
        case .submerged:
            logger.info("*** Submerged Event ***")
            submerged = true
    
    
        @unknown default:
            fatalError("*** unknown event received: \(event.state) ***")
        }
    
    
        Task {
            await myAdd(event: event)
            if let submerged {
                await mySet(submerged: submerged)
            }
        }
    }
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6#see-also)

---------------------------------------------------------------------------------------------------------------------------------------

### [Receiving updates](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6#Receiving-updates)

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb)

새 pressure 및 depth 측정값 집합을 delegate에 전달합니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua)

업데이트된 water temperature data를 delegate에 전달합니다.

**Required**

[`func manager(CMWaterSubmersionManager, errorOccurred: any Error)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))

error가 발생하면 delegate에 알립니다.

**Required**

현재 페이지: manager(\_:didUpdate:)
