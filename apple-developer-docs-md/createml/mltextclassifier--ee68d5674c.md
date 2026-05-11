---
title: "MLTextClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltextclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130705+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltextclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLTextClassifier

struct

MLTextClassifier
================

natural language text를 분류하도록 training하는 model입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+visionOS 1.0+

    struct MLTextClassifier

[언급된 문서](https://developer.apple.com/documentation/createml/mltextclassifier#mentions)

---------------------------------------------------------------------------------------------

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

[개요](https://developer.apple.com/documentation/createml/mltextclassifier#overview)

-----------------------------------------------------------------------------------------

text classifier를 사용하면 app에 포함할 machine learning model을 training해 natural language text를 분류할 수 있습니다. 이 model은 입력 text의 feature를 label과 연결해 학습하며, 입력은 문장, 단락, 전체 문서가 될 수 있습니다.

text classifier를 training한 뒤에는 Core ML model file로 저장합니다. 그런 다음 [Natural Language](https://developer.apple.com/documentation/NaturalLanguage)
 framework의 [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel)
 class instance를 사용해 model file을 app으로 읽어들입니다.

[주제](https://developer.apple.com/documentation/createml/mltextclassifier#topics)

-------------------------------------------------------------------------------------

### [text classifier 생성 및 training](https://developer.apple.com/documentation/createml/mltextclassifier#Creating-and-training-a-text-classifier)

[`init(trainingData:parameters:)`](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:parameters:))

text classifier를 생성합니다.

[`init(trainingData:textColumn:labelColumn:parameters:)`](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:))

text classifier를 생성합니다.

[`enum DataSource`](https://developer.apple.com/documentation/createml/mltextclassifier/datasource)

text classifier용 data source입니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct)

model training parameter와 validation data를 지정하는 parameter입니다.

[`let modelParameters: MLTextClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.property)

초기화 중 text classifier가 training에 사용한 configuration parameter입니다.

### [text classifier 평가하기](https://developer.apple.com/documentation/createml/mltextclassifier#Evaluating-a-text-classifier)

[`func evaluation(on:)`](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:))

evaluation metric을 계산합니다.

[`func evaluation(on:textColumn:labelColumn:)`](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:textcolumn:labelcolumn:))

evaluation metric을 계산합니다.

[`let trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mltextclassifier/trainingmetrics)

training dataset에서 classifier 성능을 측정한 값입니다.

[`let validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mltextclassifier/validationmetrics)

validation dataset에서 classifier 성능을 측정한 값입니다.

### [text classifier 테스트하기](https://developer.apple.com/documentation/createml/mltextclassifier#Testing-a-text-classifier)

[`func prediction(from: String) throws -> String`](https://developer.apple.com/documentation/createml/mltextclassifier/prediction(from:))

string을 label로 분류합니다.

[`func predictions(from:)`](https://developer.apple.com/documentation/createml/mltextclassifier/predictions(from:))

string array를 label로 분류합니다.

[`func predictionWithConfidence(from: String) throws -> [String : Double]`](https://developer.apple.com/documentation/createml/mltextclassifier/predictionwithconfidence(from:))

지정한 string에 대해 가능한 여러 label과 그 confidence score를 예측합니다.

[`func predictionsWithConfidence(from:)`](https://developer.apple.com/documentation/createml/mltextclassifier/predictionswithconfidence(from:))

지정한 array의 각 string에 대해 가능한 여러 label과 그 confidence score를 예측합니다.

### [text classifier 저장하기](https://developer.apple.com/documentation/createml/mltextclassifier#Saving-a-text-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mltextclassifier/write(to:metadata:))

지정한 URL에 text classifier를 Core ML model file로 export합니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mltextclassifier/write(tofile:metadata:))

지정한 file path에 text classifier를 Core ML model file로 export합니다.

### [text classifier 설명하기](https://developer.apple.com/documentation/createml/mltextclassifier#Describing-a-text-classifier)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mltextclassifier/model)

text classifier의 기반 Core ML model입니다.

[`var description: String`](https://developer.apple.com/documentation/createml/mltextclassifier/description)

text classifier의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mltextclassifier/debugdescription)

debugging 중 output에 적합한 text classifier의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mltextclassifier/playgrounddescription)

playground에서 사용하는 text classifier 설명입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mltextclassifier#Supporting-types)

[`enum FeatureExtractorType`](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype)

text feature extractor type입니다.

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype)

text classifier가 사용하는 algorithm type입니다.

### [Default Implementations](https://developer.apple.com/documentation/createml/mltextclassifier#Default-Implementations)

[API Reference\
\
CustomDebugStringConvertible Implementations](https://developer.apple.com/documentation/createml/mltextclassifier/customdebugstringconvertible-implementations)

[API Reference\
\
CustomPlaygroundDisplayConvertible Implementations](https://developer.apple.com/documentation/createml/mltextclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference\
\
CustomStringConvertible Implementations](https://developer.apple.com/documentation/createml/mltextclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mltextclassifier#relationships)

---------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mltextclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mltextclassifier#see-also)

-----------------------------------------------------------------------------------------

### [Text model](https://developer.apple.com/documentation/createml/mltextclassifier#Text-models)

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

natural language text를 분류하는 machine learning model을 training합니다.

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

natural language text의 개별 단어에 tag를 붙이는 machine learning model을 training합니다.

[`struct MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)

natural language text를 단어 수준에서 분류하도록 training하는 word-tagging model입니다.

[`struct MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)

natural language text를 분석하는 tagger를 보강하는 term과 label의 collection입니다.

[`struct MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)

vector space 안의 string map으로, app이 특정 string의 이웃을 살펴 유사한 string을 찾게 합니다.

현재 페이지: MLTextClassifier
