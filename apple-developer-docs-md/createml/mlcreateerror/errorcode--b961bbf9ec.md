---
title: "errorCode | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror/errorcode"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.153615+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror/errorcode#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror)
    
*   errorCode

instance property

errorCode
=========

이 error의 숫자 code입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    var errorCode: Int { get }

[같이 보기](https://developer.apple.com/documentation/createml/mlcreateerror/errorcode#see-also)

------------------------------------------------------------------------------------------------

### [Describing errors in a user interface](https://developer.apple.com/documentation/createml/mlcreateerror/errorcode#Describing-errors-in-a-user-interface)

[`var errorUserInfo: [String : Any]`](https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo)

error에 대한 추가 정보를 제공하는 dictionary입니다.

[`var errorDescription: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription)

적용되는 경우, error와 그 발생 이유를 설명하는 localized되고 사람이 읽을 수 있는 description입니다.

[`var failureReason: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/failurereason)

적용되는 경우, failure의 원인을 설명하는 localized되고 사람이 읽을 수 있는 이유입니다.

현재 페이지: errorCode
