---
title: "manager(_:didUpdate:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.878306+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)
    
*   manager(\_:didUpdate:)

instance method

manager(\_:didUpdate:)
======================

delegate에 업데이트된 수온 data를 제공합니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    func manager(
        _ manager: CMWaterSubmersionManager,
        didUpdate measurement: CMWaterTemperature
    )

**Required**

[Parameters](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

`manager`

water submersion data를 위한 manager입니다.

`measurement`

수온과 measurement의 uncertainty 정보를 담은 data object입니다.

[논의](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua#Discussion)

-------------------------------------------------------------------------------------------------------------------------------------------

수온 update를 받으려면 이 method를 구현합니다. system은 잠수 중에는 초당 세 번 temperature update를 보냅니다. 수면 위에 있을 때는 더 느린 속도로 update를 제공하며, device가 움직이지 않으면 update 제공을 중단할 수 있습니다.

    nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate measurement: CMWaterTemperature) {
        let temp = measurement.temperature
        let uncertainty = measurement.temperatureUncertainty
        let currentTemperature = "\(temp.value) +/- \(uncertainty.value) \(temp.unit)"
    
    
        logger.info(("*** \(currentTemperature) ***"))
    
    
        Task {
            await myAdd(temperature:measurement)
        }
    }
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua#see-also)

---------------------------------------------------------------------------------------------------------------------------------------

### [update 받기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua#Receiving-updates)

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6)

water submersion event가 발생하면 delegate에 알립니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb)

delegate에 새로운 pressure 및 depth measurement 집합을 제공합니다.

**Required**

[`func manager(CMWaterSubmersionManager, errorOccurred: any Error)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))

error가 발생하면 delegate에 알립니다.

**Required**

현재 페이지: manager(\_:didUpdate:)
