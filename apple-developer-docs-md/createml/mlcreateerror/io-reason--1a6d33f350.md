---
title: "MLCreateError.io(reason:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.151164+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror)
    
*   MLCreateError.io(reason:)

case

MLCreateError.io(reason:)
=========================

I/O failure를 나타내는 error입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    case io(reason: String)

[참고 항목](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:)#see-also)

--------------------------------------------------------------------------------------------------

### [error 식별](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:)#Identifying-errors)

[`case cancelled`](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled)

training session을 취소했음을 나타내는 error입니다.

[`case incompatibleParameters(parameter: String, originalValue: String, newValue: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:))

training session parameter가 서로 호환되지 않음을 나타내는 error입니다.

[`case modifiedTrainingData`](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata)

training data가 session 생성 시점의 data와 달라졌음을 나타내는 error입니다.

[`case type(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/type(reason:))

type이 없거나 올바르지 않음을 나타내는 error입니다.

[`case generic(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/generic(reason:))

다른 error로 분류되지 않는 failure를 나타내는 error입니다.

[`let MLCreateErrorDomain: String`](https://developer.apple.com/documentation/createml/mlcreateerrordomain)

Create ML error의 domain을 정의하는 전역 constant입니다.

현재 페이지: MLCreateError.io(reason:)
