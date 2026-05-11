---
title: "init(dictionary:parameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.151526+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   init(dictionary:parameters:)

initializer

init(dictionary:parameters:)
============================

word embedding을 생성합니다.

macOS 10.15+

    init(
        dictionary: [String : [Double]],
        parameters: MLWordEmbedding.ModelParameters = ModelParameters()
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:)#parameters)

-------------------------------------------------------------------------------------------------------------------------

`dictionary`

string과 해당 embedding의 dictionary입니다.

`parameters`

model parameter입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:)#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Creating a word embedding](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:)#Creating-a-word-embedding)

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct)

model configuration parameter입니다.

[`let modelParameters: MLWordEmbedding.ModelParameters`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.property)

model configuration parameter입니다.

현재 페이지: init(dictionary:parameters:)
