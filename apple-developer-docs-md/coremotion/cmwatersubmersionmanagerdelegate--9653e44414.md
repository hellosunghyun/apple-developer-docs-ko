---
title: "CMWaterSubmersionManagerDelegate | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.876657+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMWaterSubmersionManagerDelegate

protocol

CMWaterSubmersionManagerDelegate
================================

ambient pressure, water pressure, water temperature, submersion event update를 받는 delegate입니다.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+visionOS 1.0+watchOS 9.0+

    protocol CMWaterSubmersionManagerDelegate : NSObjectProtocol

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#mentions)

---------------------------------------------------------------------------------------------------------------

[submersion data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

[개요](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#overview)

-----------------------------------------------------------------------------------------------------------

system은 app에 업데이트된 data를 전달하기 위해 delegate method를 호출합니다. watch가 잠수 상태가 아닐 때 app은 event, measurement, error message를 받습니다. 다만 measurement update에는 surface pressure와 submersion state data만 포함됩니다. 잠수 후에는 measurement update에 depth와 water pressure data가 포함됩니다. watch는 water temperature update도 받기 시작합니다.

watch가 잠수 중일 때 system은 measurement update와 temperature update를 초당 세 번 보냅니다. watch가 수면 위에 있을 때는 더 느린 속도로 update를 제공하며, watch가 움직이지 않으면 update 제공을 중단할 수도 있습니다.

[주제](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#topics)

-------------------------------------------------------------------------------------------------------

### [Receiving updates](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#Receiving-updates)

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6)

water submersion event가 발생하면 delegate에 알립니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb)

새 pressure 및 depth measurement 집합을 delegate에 제공합니다.

**Required**

[`func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua)

업데이트된 water temperature data를 delegate에 제공합니다.

**Required**

[`func manager(CMWaterSubmersionManager, errorOccurred: any Error)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))

error가 발생하면 delegate에 알립니다.

**Required**

[관계](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#relationships)

---------------------------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#inherits-from)

*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#see-also)

-----------------------------------------------------------------------------------------------------------

### [Water submersion](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate#Water-submersion)

[submersion data 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

water-submersion manager를 사용해 Apple Watch Ultra에서 water pressure, temperature, depth data를 받습니다.

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

submersion 중 pressure와 temperature data 수집을 관리하는 object입니다.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

device의 submersion state가 바뀌었음을 나타내는 event입니다.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

pressure와 depth data를 담은 update입니다.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

water temperature data를 담은 update입니다.

현재 페이지: CMWaterSubmersionManagerDelegate
