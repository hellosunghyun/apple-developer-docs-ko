---
title: "MLCreateErrorDomain | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerrordomain"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.152358+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerrordomain#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLCreateErrorDomain

Global Variable

MLCreateErrorDomain
===================

Create ML error의 domain을 정의하는 global constant입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    let MLCreateErrorDomain: String

[같이 보기](https://developer.apple.com/documentation/createml/mlcreateerrordomain#see-also)

--------------------------------------------------------------------------------------------

### [error 식별](https://developer.apple.com/documentation/createml/mlcreateerrordomain#Identifying-errors)

[`case cancelled`](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled)

training session을 취소했음을 나타내는 error입니다.

[`case incompatibleParameters(parameter: String, originalValue: String, newValue: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:))

training session parameter가 호환되지 않음을 나타내는 error입니다.

[`case modifiedTrainingData`](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata)

training data가 session을 생성했을 때의 data와 다름을 나타내는 error입니다.

[`case io(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:))

I/O 실패를 나타내는 error입니다.

[`case type(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/type(reason:))

type이 없거나 올바르지 않음을 나타내는 error입니다.

[`case generic(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/generic(reason:))

다른 error 항목으로 설명되지 않는 실패를 나타내는 error입니다.

현재 페이지는 MLCreateErrorDomain입니다
