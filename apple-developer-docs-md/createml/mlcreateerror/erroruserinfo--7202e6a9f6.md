---
title: "errorUserInfo | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.153712+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror)
    
*   errorUserInfo

instance property

errorUserInfo
=============

error에 대한 추가 정보를 제공하는 dictionary입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    var errorUserInfo: [String : Any] { get }

[관련 항목](https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo#see-also)

----------------------------------------------------------------------------------------------------

### [user interface에서 error 설명](https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo#Describing-errors-in-a-user-interface)

[`var errorCode: Int`](https://developer.apple.com/documentation/createml/mlcreateerror/errorcode)

이 error의 numeric code입니다.

[`var errorDescription: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription)

가능한 경우 error와 발생 이유를 설명하는 localized human-readable description입니다.

[`var failureReason: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/failurereason)

가능한 경우 failure의 원인을 설명하는 localized human-readable reason입니다.

현재 페이지는 errorUserInfo
