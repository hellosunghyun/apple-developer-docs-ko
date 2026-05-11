---
title: "errorDescription | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror/errordescription"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.153817+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror)
    
*   errorDescription

instance property

errorDescription
================

가능한 경우 error와 발생 원인을 localized된 사람이 읽을 수 있는 형태로 설명합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    var errorDescription: String? { get }

[참고 항목](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription#see-also)

-------------------------------------------------------------------------------------------------------

### [user interface에서 error 설명](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription#Describing-errors-in-a-user-interface)

[`var errorCode: Int`](https://developer.apple.com/documentation/createml/mlcreateerror/errorcode)

이 error의 숫자 code입니다.

[`var errorUserInfo: [String : Any]`](https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo)

error에 대한 추가 정보를 제공하는 dictionary입니다.

[`var failureReason: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/failurereason)

가능한 경우 failure의 원인을 localized된 사람이 읽을 수 있는 형태로 제공합니다.

현재 페이지는 errorDescription입니다
