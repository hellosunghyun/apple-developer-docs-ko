---
title: "MLWordTagger | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordtagger"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130458+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordtagger#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLWordTagger

struct

MLWordTagger
============

word 단위로 natural language text를 분류하도록 training하는 word-tagging model입니다.

macOS 10.14+

    struct MLWordTagger

[다음 문서에서 언급됨](https://developer.apple.com/documentation/createml/mlwordtagger#mentions)

-----------------------------------------------------------------------------------------

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

[개요](https://developer.apple.com/documentation/createml/mlwordtagger#overview)

-------------------------------------------------------------------------------------

[`MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)
를 사용해 제품 이름이나 관심 지점처럼 app과 관련된 content를 식별하는 custom word tagger를 만듭니다.

custom word tagger를 [Natural Language](https://developer.apple.com/documentation/NaturalLanguage)
 framework에서 사용하려면 model file로 저장한 뒤 [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel)
로 가져옵니다. 그런 다음 [`setModels(_:forTagScheme:)`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger/setModels(_:forTagScheme:))
 method를 사용해 custom [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel)
을 [`NLTagger`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger)
에 추가합니다.

[주제](https://developer.apple.com/documentation/createml/mlwordtagger#topics)

---------------------------------------------------------------------------------

### [word tagger 생성 및 training](https://developer.apple.com/documentation/createml/mlwordtagger#Creating-and-training-a-word-tagger)

[`init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws`](https://developer.apple.com/documentation/createml/mlwordtagger/init(trainingdata:parameters:))

word tagger를 만듭니다.

[`init(trainingData:tokenColumn:labelColumn:parameters:)`](https://developer.apple.com/documentation/createml/mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:))

word tagger를 만듭니다.

[`typealias Token`](https://developer.apple.com/documentation/createml/mlwordtagger/token)

word tagger의 token type으로, string입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct)

model training parameter와 validation data를 지정하는 parameter입니다.

[`let modelParameters: MLWordTagger.ModelParameters`](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.property)

word tagger가 초기화 중 training에 사용한 configuration parameter입니다.

### [word tagger 평가](https://developer.apple.com/documentation/createml/mlwordtagger#Evaluating-a-word-tagger)

[`func evaluation(on:tokenColumn:labelColumn:)`](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:tokencolumn:labelcolumn:))

evaluation metric을 계산합니다.

[`func evaluation(on: [(tokens: [MLWordTagger.Token], labels: [String])]) -> MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:))

evaluation metric을 계산합니다.

[`let trainingMetrics: MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtagger/trainingmetrics)

training data set에서 tagger 성능을 측정한 값입니다.

[`let validationMetrics: MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtagger/validationmetrics)

validation data set에서 tagger 성능을 측정한 값입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger 성능을 평가할 때 사용하는 metric입니다.

### [word tagger 테스트](https://developer.apple.com/documentation/createml/mlwordtagger#Testing-a-word-tagger)

[`func prediction(from:)`](https://developer.apple.com/documentation/createml/mlwordtagger/prediction(from:))

input string의 tag를 예측합니다.

[`func predictions(from:)`](https://developer.apple.com/documentation/createml/mlwordtagger/predictions(from:))

input string에서 label sequence, token 위치, token 길이를 예측합니다.

[`func predictionWithConfidence(from:)`](https://developer.apple.com/documentation/createml/mlwordtagger/predictionwithconfidence(from:))

input string의 tag와 confidence score를 예측합니다.

### [word tagger 저장](https://developer.apple.com/documentation/createml/mlwordtagger#Saving-a-word-tagger)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlwordtagger/write(to:metadata:))

word tagger를 지정한 URL에 Core ML model file로 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlwordtagger/write(tofile:metadata:))

word tagger를 지정한 file path에 Core ML model file로 내보냅니다.

### [word tagger 설명](https://developer.apple.com/documentation/createml/mlwordtagger#Describing-a-word-tagger)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlwordtagger/model)

word tagger의 기반 Core ML model입니다.

[`var description: String`](https://developer.apple.com/documentation/createml/mlwordtagger/description)

word tagger의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlwordtagger/debugdescription)

debugging 중 출력하기에 적합한 word tagger의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlwordtagger/playgrounddescription)

playground에서의 word tagger 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlwordtagger#Supporting-types)

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mlwordtagger/featureextractortype)

transfer-learning algorithm 옵션으로 word tagger를 training할 때 사용할 수 있는 feature extractor입니다.

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlwordtagger/modelalgorithmtype)

algorithm type입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlwordtagger#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordtagger/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordtagger/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mlwordtagger/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlwordtagger#relationships)

-----------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlwordtagger#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlwordtagger#see-also)

-------------------------------------------------------------------------------------

### [text model](https://developer.apple.com/documentation/createml/mlwordtagger#Text-models)

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

natural language text를 분류하는 machine learning model을 training합니다.

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

natural language text의 개별 word에 tag를 지정하는 machine learning model을 training합니다.

[`struct MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)

natural language text를 분류하도록 training하는 model입니다.

[`struct MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)

용어와 그 label의 collection으로, natural language text를 분석하는 tagger를 보강합니다.

[`struct MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)

vector space 안의 string map으로, app이 어떤 string의 이웃을 살펴 비슷한 string을 찾도록 해 줍니다.

현재 페이지는 MLWordTagger입니다
