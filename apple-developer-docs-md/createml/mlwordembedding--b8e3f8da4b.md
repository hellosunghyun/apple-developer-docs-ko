---
title: "MLWordEmbedding | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130119+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLWordEmbedding

struct

MLWordEmbedding
===============

string의 이웃을 기준으로 비슷한 string을 찾을 수 있게 해 주는 vector space 내 string map입니다.

macOS 10.15+

    struct MLWordEmbedding

[개요](https://developer.apple.com/documentation/createml/mlwordembedding#overview)

----------------------------------------------------------------------------------------

[`MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)
을 사용해 word embedding을 구성하고 file로 저장한 다음, 그 file을 Xcode project에 추가합니다. project는 runtime에 해당 word embedding file로 [`NLEmbedding`](https://developer.apple.com/documentation/NaturalLanguage/NLEmbedding)
 instance를 생성하고, 이 instance가 vector 간 거리를 바탕으로 비슷한 string을 찾습니다.

word embedding은 word embedding의 _vocabulary_ 를 이루는 string을 key로 하는 dictionary로 구성합니다. 각 string의 value는 vector를 나타내는 double array입니다. array 길이는 임의로 정할 수 있지만, 하나의 word embedding 안에서는 모든 array 길이가 같아야 합니다. array 길이가 vector space의 차원 수를 결정합니다. 예를 들어 다음 listing은 4차원이며 두 개의 string으로 구성된 vocabulary를 가진 word embedding을 만듭니다.

    let wordEmbedding = try! MLWordEmbedding(dictionary: [\
        "Hello"   : [0.0, 1.2, 5.0, 0.0],\
        "Goodbye" : [0.0, 1.3, -6.2, 0.1]\
    ])
    

[`MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)
 구성을 마쳤다면 app에 포함할 수 있도록 `.mlmodel` file로 저장합니다.

    try wordEmbedding.write(toFile: "~/Desktop/WordEmbedding.mlmodel")
    

word embedding file은 많은 string과 해당 vector를 효율적으로 저장할 수 있습니다.

[주제](https://developer.apple.com/documentation/createml/mlwordembedding#topics)

------------------------------------------------------------------------------------

### [word embedding 생성하기](https://developer.apple.com/documentation/createml/mlwordembedding#Creating-a-word-embedding)

[`init(dictionary: [String : [Double]], parameters: MLWordEmbedding.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:))

word embedding을 생성합니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct)

model configuration parameter입니다.

[`let modelParameters: MLWordEmbedding.ModelParameters`](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.property)

model configuration parameter입니다.

### [word embedding 테스트하기](https://developer.apple.com/documentation/createml/mlwordembedding#Testing-a-word-embedding)

[`func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]`](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:))

이웃을 예측합니다.

[`func distance(between: String, and: String, distanceType: NLDistanceType) -> Double`](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:))

vocabulary space에서 두 string 사이의 거리를 계산합니다.

[`enum NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType)

text embedding에서 두 위치 사이 거리를 계산하는 방법입니다.

[`func contains(String) -> Bool`](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:))

vocabulary에 지정한 string이 포함되어 있는지 나타내는 Boolean 값을 반환합니다.

[`func vector(for: String) -> [Double]?`](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:))

vocabulary에서 지정한 string과 연결된 vector에 접근합니다.

### [word embedding 저장하기](https://developer.apple.com/documentation/createml/mlwordembedding#Saving-a-word-embedding)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:))

지정한 URL에 word embedding을 Core ML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:))

지정한 file path에 word embedding을 Core ML model file로 내보냅니다.

### [word embedding 설명](https://developer.apple.com/documentation/createml/mlwordembedding#Describing-a-word-embedding)

[`let dimension: Int`](https://developer.apple.com/documentation/createml/mlwordembedding/dimension)

vocabulary embedding space의 차원 수입니다.

[`let vocabularySize: Int`](https://developer.apple.com/documentation/createml/mlwordembedding/vocabularysize)

vocabulary에 있는 string 수입니다.

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlwordembedding/model)

Core ML model file에 포함된 word embedding입니다.

[`var description: String`](https://developer.apple.com/documentation/createml/mlwordembedding/description)

word embedding의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlwordembedding/debugdescription)

debugging 중 출력하기에 적합한 word embedding의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlwordembedding/playgrounddescription)

playground에 표시하는 word embedding 설명입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlwordembedding#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordembedding/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordembedding/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordembedding/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlwordembedding#relationships)

--------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlwordembedding#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlwordembedding#see-also)

----------------------------------------------------------------------------------------

### [Text model](https://developer.apple.com/documentation/createml/mlwordembedding#Text-models)

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

natural language text를 분류하는 machine learning model을 training합니다.

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

natural language text에서 개별 단어에 tag를 지정하는 machine learning model을 training합니다.

[`struct MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)

natural language text를 분류하도록 training하는 model입니다.

[`struct MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)

natural language text를 단어 수준에서 분류하도록 training하는 word-tagging model입니다.

[`struct MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)

term과 해당 label의 모음으로, natural language text를 분석하는 tagger를 보강합니다.

현재 페이지: MLWordEmbedding
