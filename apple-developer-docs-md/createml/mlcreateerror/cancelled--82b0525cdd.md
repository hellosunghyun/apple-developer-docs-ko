---
title: "MLCreateError.cancelled | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror/cancelled"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.147620+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror)
    
*   MLCreateError.cancelled

Case

MLCreateError.cancelled
=======================

training session을 취소했음을 나타내는 error입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    case cancelled

[같이 보기](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled#see-also)

------------------------------------------------------------------------------------------------

### [error 식별하기](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled#Identifying-errors)

[`case incompatibleParameters(parameter: String, originalValue: String, newValue: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:))

training session parameter가 서로 호환되지 않음을 나타내는 error입니다.

[`case modifiedTrainingData`](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata)

training data가 session을 만들 때의 data와 다름을 나타내는 error입니다.

[`case io(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:))

I/O 실패를 나타내는 error입니다.

[`case type(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/type(reason:))

type이 없거나 올바르지 않음을 나타내는 error입니다.

[`case generic(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/generic(reason:))

다른 error로 분류되지 않는 실패를 나타내는 error입니다.

[`let MLCreateErrorDomain: String`](https://developer.apple.com/documentation/createml/mlcreateerrordomain)

Create ML error의 domain을 정의하는 global constant입니다.

현재 페이지: MLCreateError.cancelled
