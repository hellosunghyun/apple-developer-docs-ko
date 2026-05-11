---
title: "SRError.Code.promptDeclined | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.059905+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
    
*   *   [SRError](https://developer.apple.com/documentation/sensorkit/srerror)
        
*   [SRError.Code](https://developer.apple.com/documentation/sensorkit/srerror/code)
    
*   SRError.Code.promptDeclined

case

SRError.Code.promptDeclined
===========================

사용자가 sensor 승인 workflow를 취소할 때 발생합니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    case promptDeclined

[설명](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined#Discussion)

---------------------------------------------------------------------------------------------------------

[`requestAuthorization(sensors:completion:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))
은 사용자가 Cancel을 눌러 prompt를 거부하면 이 error를 completion closure에 전달합니다. 사용자가 argument sensor에 대한 접근을 이미 허용했거나 거부한 뒤에 이 function을 호출하면 framework도 prompt를 취소합니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined#see-also)

-----------------------------------------------------------------------------------------------------

### [error](https://developer.apple.com/documentation/sensorkit/srerror/code/promptdeclined#Errors)

[`case dataInaccessible`](https://developer.apple.com/documentation/sensorkit/srerror/code/datainaccessible)

app이 sensor data에 접근할 수 없을 때 발생합니다.

[`case fetchRequestInvalid`](https://developer.apple.com/documentation/sensorkit/srerror/code/fetchrequestinvalid)

app이 fetch request를 잘못 구성했을 때 발생합니다.

[`case invalidEntitlement`](https://developer.apple.com/documentation/sensorkit/srerror/code/invalidentitlement)

app에 필요한 entitlement가 없을 때 발생합니다.

[`case noAuthorization`](https://developer.apple.com/documentation/sensorkit/srerror/code/noauthorization)

사용자가 Settings app에서 sensor access를 거부할 때 발생합니다.

현재 페이지는 SRError.Code.promptDeclined입니다
