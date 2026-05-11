---
title: "MLGazetteer | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlgazetteer"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130356+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlgazetteer#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLGazetteer

struct

MLGazetteer
===========

natural language text를 분석하는 tagger를 보강하는, term과 해당 label의 collection입니다.

macOS 10.15+

    struct MLGazetteer

[개요](https://developer.apple.com/documentation/createml/mlgazetteer#overview)

------------------------------------------------------------------------------------

[`MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)를 사용해 gazetteer를 구성하고 file로 저장한 다음, Xcode에서 app에 추가합니다. app은 runtime에 gazetteer file을 사용해 [`NLGazetteer`](https://developer.apple.com/documentation/NaturalLanguage/NLGazetteer) instance를 만들고, 이 instance는 [`NLTagger`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger)를 보강해 특정 term에 label을 지정합니다.

label을 key로 하는 dictionary로 gazetteer를 구성합니다. dictionary의 각 value는 해당 label에 속한 term(단어 또는 구)의 array입니다. 예를 들어 실제 행성과 가상의 행성 이름을 gazetteer에 저장할 수 있습니다.

    let planets = [        "real planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],        "fictional planet" : ["Arrakis", "Hoth", "Vulcan", "Pandora", "Tatooine", "Bajor", "Alderaan", "Romulus"]    ]
    
    
    let parameters = MLGazetteer.ModelParameters(language: .english)
    let planetGazetteer = try! MLGazetteer(dictionary: planets, parameters: parameters)
    

[`MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)를 구성한 후에는 app에 포함할 수 있도록 `.mlmodel` file로 저장합니다.

    try planetGazetteer.write(toFile: "~/Desktop/PlanetGazetteer.mlmodel")
    

gazetteer file은 많은 label과 각 label에 속한 많은 term을 효율적으로 저장할 수 있습니다.

[주제](https://developer.apple.com/documentation/createml/mlgazetteer#topics)

--------------------------------------------------------------------------------

### [gazetteer 만들기](https://developer.apple.com/documentation/createml/mlgazetteer#Creating-a-gazetteer)

[`init(dictionary: [String : [String]], parameters: MLGazetteer.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlgazetteer/init(dictionary:parameters:))

label과 term의 dictionary로 gazetteer를 생성합니다.

[`init(labeledData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLGazetteer.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlgazetteer/init(labeleddata:textcolumn:labelcolumn:parameters:))

label과 term이 들어 있는 table로 gazetteer를 생성합니다.

Deprecated

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlgazetteer/modelparameters-swift.struct)

model configuration parameter입니다.

[`let modelParameters: MLGazetteer.ModelParameters`](https://developer.apple.com/documentation/createml/mlgazetteer/modelparameters-swift.property)

model configuration parameter입니다.

### [gazetteer 테스트하기](https://developer.apple.com/documentation/createml/mlgazetteer#Testing-a-gazetteer)

[`func prediction(from: String) throws -> String`](https://developer.apple.com/documentation/createml/mlgazetteer/prediction(from:))

지정한 term의 label을 예측합니다.

[`func predictions(from:)`](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:))

지정한 term의 label을 예측합니다.

[`func predictions(from: [String]) throws -> [String]`](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:)-2rej)

지정한 term들의 label을 예측합니다.

[`func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>`](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:)-2jaui)

table column에 있는 term들의 label을 예측합니다.

Deprecated

### [gazetteer 저장하기](https://developer.apple.com/documentation/createml/mlgazetteer#Saving-a-gazetteer)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlgazetteer/write(to:metadata:))

지정한 URL에 gazetteer를 Core ML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlgazetteer/write(tofile:metadata:))

지정한 file path에 gazetteer를 Core ML model file로 내보냅니다.

### [gazetteer 설명하기](https://developer.apple.com/documentation/createml/mlgazetteer#Describing-a-gazetteer)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlgazetteer/model)

memory에 저장된 Core ML model file 안에 포함된 gazetteer입니다.

[`var description: String`](https://developer.apple.com/documentation/createml/mlgazetteer/description)

gazetteer의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlgazetteer/debugdescription)

debugging 중 출력에 적합한 gazetteer의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlgazetteer/playgrounddescription)

playground에 표시되는 gazetteer 설명입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlgazetteer#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlgazetteer/customdebugstringconvertible-implementations)

[API Reference: CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlgazetteer/customplaygrounddisplayconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlgazetteer/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlgazetteer#relationships)

----------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlgazetteer#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlgazetteer#see-also)

------------------------------------------------------------------------------------

### [text model](https://developer.apple.com/documentation/createml/mlgazetteer#Text-models)

[텍스트 분류기 model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

natural language text를 분류하는 machine learning model을 training합니다.

[단어 tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

natural language text에서 개별 단어에 tag를 지정하는 machine learning model을 training합니다.

[`struct MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)

natural language text를 분류하도록 training하는 model입니다.

[`struct MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)

natural language text를 단어 수준에서 분류하도록 training하는 word-tagging model입니다.

[`struct MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)

vector space 안의 string map으로, string의 이웃을 살펴 비슷한 string을 app이 찾을 수 있게 합니다.

현재 페이지: MLGazetteer
