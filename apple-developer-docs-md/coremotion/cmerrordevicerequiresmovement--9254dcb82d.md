---
title: "CMErrorDeviceRequiresMovement | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmerrordevicerequiresmovement"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.892514+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmerrordevicerequiresmovement#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMErrorDeviceRequiresMovement

Global Variable

CMErrorDeviceRequiresMovement
=============================

motion data를 sample링하려면 device가 움직여야 합니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

    var CMErrorDeviceRequiresMovement: CMError { get }

[같이 보기](https://developer.apple.com/documentation/coremotion/cmerrordevicerequiresmovement#see-also)

--------------------------------------------------------------------------------------------------------

### [Errors](https://developer.apple.com/documentation/coremotion/cmerrordevicerequiresmovement#Errors)

[`var CMErrorInvalidAction: CMError`](https://developer.apple.com/documentation/coremotion/cmerrorinvalidaction)

지정한 action이 올바르지 않습니다.

[`var CMErrorInvalidParameter: CMError`](https://developer.apple.com/documentation/coremotion/cmerrorinvalidparameter)

지정한 parameter가 올바르지 않습니다.

[`var CMErrorMotionActivityNotAuthorized: CMError`](https://developer.apple.com/documentation/coremotion/cmerrormotionactivitynotauthorized)

app이 현재 motion activity support를 사용할 권한을 받지 않았습니다.

[`var CMErrorMotionActivityNotAvailable: CMError`](https://developer.apple.com/documentation/coremotion/cmerrormotionactivitynotavailable)

현재 device에서는 motion activity support를 사용할 수 없습니다.

[`var CMErrorMotionActivityNotEntitled: CMError`](https://developer.apple.com/documentation/coremotion/cmerrormotionactivitynotentitled)

app에 요청한 activity용 entitlement가 없습니다.

[`var CMErrorNilData: CMError`](https://developer.apple.com/documentation/coremotion/cmerrornildata)

Core Motion이 data를 반환하지 않았습니다.

[`var CMErrorNULL: CMError`](https://developer.apple.com/documentation/coremotion/cmerrornull)

error가 발생하지 않았습니다.

[`var CMErrorNotAuthorized: CMError`](https://developer.apple.com/documentation/coremotion/cmerrornotauthorized)

app이 Core Motion framework를 사용할 권한을 받지 않았습니다.

[`var CMErrorNotAvailable: CMError`](https://developer.apple.com/documentation/coremotion/cmerrornotavailable)

요청한 service를 이 device에서 사용할 수 없습니다.

[`var CMErrorNotEntitled: CMError`](https://developer.apple.com/documentation/coremotion/cmerrornotentitled)

app에 필요한 entitlement가 없습니다.

[`var CMErrorSize: CMError`](https://developer.apple.com/documentation/coremotion/cmerrorsize)

data 크기가 올바르지 않습니다.

[`var CMErrorTrueNorthNotAvailable: CMError`](https://developer.apple.com/documentation/coremotion/cmerrortruenorthnotavailable)

이 device에서는 true north를 사용할 수 없습니다.

[`var CMErrorUnknown: CMError`](https://developer.apple.com/documentation/coremotion/cmerrorunknown)

알 수 없는 error가 발생했습니다.

현재 페이지: CMErrorDeviceRequiresMovement
