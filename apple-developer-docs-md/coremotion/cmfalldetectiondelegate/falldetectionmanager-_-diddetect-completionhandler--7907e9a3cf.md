---
title: "fallDetectionManager(_:didDetect:completionHandler:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:)"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.914228+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:)#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMFallDetectionDelegate](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)
    
*   fallDetectionManager(\_:didDetect:completionHandler:)

instance method

fallDetectionManager(\_:didDetect:completionHandler:)
=====================================================

fall detection event가 발생했음을 알립니다.

watchOS 7.2+

    optional func fallDetectionManager(
        _ fallDetectionManager: CMFallDetectionManager,
        didDetect event: CMFallDetectionEvent,
        completionHandler handler: @escaping @Sendable () -> Void
    )

    optional func fallDetectionManager(
        _ fallDetectionManager: CMFallDetectionManager,
        didDetect event: CMFallDetectionEvent
    ) async

[Parameter](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

`fallDetectionManager`

이 event의 fall detection manager입니다.

`event`

event 관련 data를 담은 object입니다.

`handler`

event용 completion handler입니다. event 처리를 마치는 즉시 이 handler를 호출합니다.

[설명](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:)#Discussion)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

사용자가 fall detection을 허용했다면, fall detection event가 발생할 때 system이 app을 깨우거나 실행합니다. app에는 background에서 잠시 실행할 시간이 주어집니다. 시간이 만료되기 전에 event를 처리하고 completion handler를 호출해야 하며, 그렇지 않으면 system이 app을 중단합니다.

또한 사용자가 app을 실행할 때마다, system은 최근에 fall event가 발생했는지 확인합니다. 발생한 적이 있으면 이 method를 호출합니다.

예를 들어 app이 crash된 뒤 다시 실행되는 경우처럼, app이 같은 event를 여러 번 받을 수 있다는 점에 유의합니다. app이 이미 그 event를 받았는지 판단하려면 항상 event의 [`date`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/date)
 property를 확인합니다. system은 서로 다른 fall event가 서로 다른 `date` 값을 갖도록 보장합니다.

현재 페이지: fallDetectionManager(\_:didDetect:completionHandler:)
