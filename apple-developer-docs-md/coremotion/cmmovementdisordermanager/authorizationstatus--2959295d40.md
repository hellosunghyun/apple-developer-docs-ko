---
title: "authorizationStatus() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.907673+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   authorizationStatus()

type method

authorizationStatus()
=====================

사용자가 app이 movement disorder data를 모니터링하고 query하도록 승인했는지를 나타내는 값입니다.

watchOS 5.0+

    class func authorizationStatus() -> CMAuthorizationStatus

[논의](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus()#Discussion)

------------------------------------------------------------------------------------------------------------------------------

app이 movement disorder data를 모니터링하거나 query하려고 처음 시도할 때 manager는 사용자에게 movement disorder data를 수집하거나 가져와도 되는지 permission을 요청합니다. permission을 요청하려면 app의 `Info.plist` 파일에 motion usage description을 설정해야 합니다. 자세한 내용은 [Provide the motion usage description](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data#Provide-the-motion-usage-description)
을 참고합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus()#see-also)

--------------------------------------------------------------------------------------------------------------------------

### [사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus()#Checking-Availablility)

[`class func isAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable())

현재 device가 movement disorder manager를 지원하는지를 나타내는 Boolean 값입니다.

[`class func version() -> String?`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version())

현재 movement disorder algorithm의 version을 설명하는 string을 반환합니다.

현재 페이지는 authorizationStatus()입니다
