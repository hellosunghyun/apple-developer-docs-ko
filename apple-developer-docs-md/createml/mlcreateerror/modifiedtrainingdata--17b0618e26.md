---
title: "MLCreateError.modifiedTrainingData | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150976+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror)
    
*   MLCreateError.modifiedTrainingData

Case

MLCreateError.modifiedTrainingData
==================================

session을 생성했을 때의 data와 현재 training data가 다름을 나타내는 error입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    case modifiedTrainingData

[같이 보기](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata#see-also)

-----------------------------------------------------------------------------------------------------------

### [error 식별하기](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata#Identifying-errors)

[`case cancelled`](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled)

training session을 취소했음을 나타내는 error입니다.

[`case incompatibleParameters(parameter: String, originalValue: String, newValue: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:))

training session parameter가 서로 호환되지 않음을 나타내는 error입니다.

[`case io(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:))

I/O 실패를 나타내는 error입니다.

[`case type(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/type(reason:))

type이 누락되었거나 잘못되었음을 나타내는 error입니다.

[`case generic(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/generic(reason:))

다른 error로 분류되지 않는 실패를 나타내는 error입니다.

[`let MLCreateErrorDomain: String`](https://developer.apple.com/documentation/createml/mlcreateerrordomain)

Create ML error의 domain을 정의하는 전역 constant입니다.

현재 페이지: MLCreateError.modifiedTrainingData
