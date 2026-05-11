---
title: "MLWordEmbedding.ModelParameters | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.151338+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   MLWordEmbedding.ModelParameters

struct

MLWordEmbedding.ModelParameters
===============================

model 구성 parameter입니다.

macOS 10.15+

    struct ModelParameters

[주제](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#topics)

-----------------------------------------------------------------------------------------------------------------

### [parameter 생성](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#Creating-parameters)

[`init(language: NLLanguage?, revision: Int)`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/init(language:revision:))

model parameter를 생성합니다.

### [parameter 접근](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#Accessing-parameters)

[`var revision: Int`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/revision)

word embedding의 revision입니다.

[`var language: NLLanguage?`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/language)

word embedding의 언어입니다.

### [parameter 설명](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#Describing-parameters)

[`var description: String`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/description)

word embedding parameter의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/debugdescription)

debugging 중 출력하기에 적합한 word embedding parameter의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/playgrounddescription)

playground에 표시되는 word embedding parameter 설명입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#relationships)

-------------------------------------------------------------------------------------------------------------------------------

### [준수 대상](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#see-also)

---------------------------------------------------------------------------------------------------------------------

### [word embedding 생성](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct#Creating-a-word-embedding)

[`init(dictionary: [String : [Double]], parameters: MLWordEmbedding.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:))

word embedding을 생성합니다.

[`let modelParameters: MLWordEmbedding.ModelParameters`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.property)

model 구성 parameter입니다.

현재 페이지는 MLWordEmbedding.ModelParameters입니다
