---
title: "MLCreateError | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcreateerror"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148387+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcreateerror#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLCreateError

enum

MLCreateError
=============

Create ML이 model training, prediction 생성, model을 file system에 기록하는 작업 등 여러 operation을 수행하는 동안 발생시키는 error입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    enum MLCreateError

[주제](https://developer.apple.com/documentation/createml/mlcreateerror#topics)

----------------------------------------------------------------------------------

### [Identifying errors](https://developer.apple.com/documentation/createml/mlcreateerror#Identifying-errors)

[`case cancelled`](https://developer.apple.com/documentation/createml/mlcreateerror/cancelled)

training session을 취소했음을 나타내는 error입니다.

[`case incompatibleParameters(parameter: String, originalValue: String, newValue: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:))

training session parameter가 호환되지 않음을 나타내는 error입니다.

[`case modifiedTrainingData`](https://developer.apple.com/documentation/createml/mlcreateerror/modifiedtrainingdata)

training data가 session을 만들었을 때의 data와 다름을 나타내는 error입니다.

[`case io(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/io(reason:))

I/O failure를 나타내는 error입니다.

[`case type(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/type(reason:))

누락되었거나 잘못된 type을 나타내는 error입니다.

[`case generic(reason: String)`](https://developer.apple.com/documentation/createml/mlcreateerror/generic(reason:))

다른 error로 분류되지 않는 failure를 나타내는 error입니다.

[`let MLCreateErrorDomain: String`](https://developer.apple.com/documentation/createml/mlcreateerrordomain)

Create ML error의 domain을 정의하는 global constant입니다.

### [Describing errors](https://developer.apple.com/documentation/createml/mlcreateerror#Describing-errors)

[`var description: String`](https://developer.apple.com/documentation/createml/mlcreateerror/description)

error에 대한 사람이 읽을 수 있는 설명입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlcreateerror/debugdescription)

debugging 중 출력하기 적합한, 사람이 읽을 수 있는 error 설명입니다.

### [Describing errors in a user interface](https://developer.apple.com/documentation/createml/mlcreateerror#Describing-errors-in-a-user-interface)

[`var errorCode: Int`](https://developer.apple.com/documentation/createml/mlcreateerror/errorcode)

이 error의 숫자 code입니다.

[`var errorUserInfo: [String : Any]`](https://developer.apple.com/documentation/createml/mlcreateerror/erroruserinfo)

error에 대한 추가 정보를 제공하는 dictionary입니다.

[`var errorDescription: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/errordescription)

가능한 경우 error와 그 발생 이유를 localized된 사람이 읽을 수 있는 형태로 설명합니다.

[`var failureReason: String?`](https://developer.apple.com/documentation/createml/mlcreateerror/failurereason)

가능한 경우 failure의 원인을 localized된 사람이 읽을 수 있는 형태로 설명합니다.

### [Default Implementations](https://developer.apple.com/documentation/createml/mlcreateerror#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlcreateerror/customdebugstringconvertible-implementations)

[API Reference: CustomNSError 구현](https://developer.apple.com/documentation/createml/mlcreateerror/customnserror-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlcreateerror/customstringconvertible-implementations)

[API Reference: LocalizedError 구현](https://developer.apple.com/documentation/createml/mlcreateerror/localizederror-implementations)

[관계](https://developer.apple.com/documentation/createml/mlcreateerror#relationships)

------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlcreateerror#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomNSError`](https://developer.apple.com/documentation/Foundation/CustomNSError)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Error`](https://developer.apple.com/documentation/Swift/Error)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`LocalizedError`](https://developer.apple.com/documentation/Foundation/LocalizedError)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlcreateerror#see-also)

--------------------------------------------------------------------------------------

### [Supporting types and constants](https://developer.apple.com/documentation/createml/mlcreateerror#Supporting-types-and-constants)

[`let MLCreateErrorDomain: String`](https://developer.apple.com/documentation/createml/mlcreateerrordomain)

Create ML error의 domain을 정의하는 global constant입니다.

현재 페이지: MLCreateError
