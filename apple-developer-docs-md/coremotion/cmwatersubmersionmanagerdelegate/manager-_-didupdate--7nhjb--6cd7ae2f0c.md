---
title: "manager(_:didUpdate:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.878421+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMWaterSubmersionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)
    
*   manager(\_:didUpdate:)

instance method

manager(\_:didUpdate:)
======================

delegate에 새로운 pressure 및 depth measurement 세트를 제공합니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    func manager(
        _ manager: CMWaterSubmersionManager,
        didUpdate measurement: CMWaterSubmersionMeasurement
    )

**Required**

[파라미터](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

`manager`

water submersion data를 관리하는 manager입니다.

`measurement`

pressure와 depth 정보를 담은 data object입니다.

[설명](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb#설명)

-------------------------------------------------------------------------------------------------------------------------------------------

업데이트된 surface pressure, water pressure, depth data를 받으려면 이 method를 구현합니다. system은 잠수 중일 때 초당 세 번 measurement update를 보냅니다. 수면 위에 있을 때는 더 느린 속도로 update를 제공하며, device가 움직이지 않으면 update 제공을 중단할 수 있습니다.

    nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate measurement: CMWaterSubmersionMeasurement) {
    
    
        logger.info("*** Received a depth measurement ***")
    
    
        let currentDepth: String
        if let depth = measurement.depth {
            currentDepth = "\(depth.value) \(depth.unit)"
        } else {
            currentDepth = "None"
        }
    
    
        let currentSurfacePressure: String
        let surfacePressure = measurement.surfacePressure
        currentSurfacePressure = "\(surfacePressure.value) \(surfacePressure.unit)"
    
    
        let currentPressure: String
        if let pressure = measurement.pressure {
            currentPressure = "\(pressure.value) \(pressure.unit)"
        } else {
            currentPressure = "None"
        }
    
    
        logger.info("*** Depth: \(currentDepth) ***")
        logger.info("*** Surface Pressure: \(currentSurfacePressure) ***")
        logger.info("*** Pressure: \(currentPressure) ***")
    
    
        let submerged: Bool?
        switch measurement.submersionState {
        case .unknown:
            logger.info("*** Unknown Depth ***")
            submerged = nil
        case .notSubmerged:
            logger.info("*** Not Submerged ***")
            submerged = false
        case .submergedShallow:
            logger.info("*** Shallow Depth ***")
            submerged = true
        case .submergedDeep:
            logger.info("*** Deep Depth ***")
            submerged = true
        case .approachingMaxDepth:
            logger.info("*** Approaching Max Depth ***")
            submerged = true
        case .pastMaxDepth:
            logger.info("*** Past Max Depth ***")
            submerged = true
        case .sensorDepthError:
            logger.info("*** A depth error has occurred. ***")
            submerged = nil
        @unknown default:
            fatalError("*** An unknown measurement depth state: \(measurement.submersionState)")
        }
    
    
        Task {
            await myAdd(measurement: measurement)
            if let submerged {
                await mySet(submerged: submerged)
            }
        }
    }
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb#see-also)

---------------------------------------------------------------------------------------------------------------------------------------

### [update 받기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb#Receiving-updates)

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6)

water submersion event가 발생하면 delegate에 알립니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua)

delegate에 업데이트된 water temperature data를 제공합니다.

**Required**

[`func manager(CMWaterSubmersionManager, errorOccurred: any Error)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))

error가 발생하면 delegate에 알립니다.

**Required**

현재 페이지: manager(\_:didUpdate:)
