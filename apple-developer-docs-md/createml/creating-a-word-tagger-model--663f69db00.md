---
title: "Creating a word tagger model | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/creating-a-word-tagger-model"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130576+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   word tagger model 만들기

Article

word tagger model 만들기
============================

natural language text에서 개별 단어에 tag를 지정하는 machine learning model을 training합니다.

[개요](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#overview)

-----------------------------------------------------------------------------------------------------

_word tagger_는 natural language text를 단어 수준에서 분류하도록 training한 machine learning model입니다.

word tagger는 이미 tag한 단어가 들어 있는 문장 예시를 여러 개 보여 주어 training합니다. 예를 들어 _iPad_, _iPhone_ 같은 Apple 제품명이 여기에 해당합니다.

### [data 가져오기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Import-your-data)

먼저 text data를 모아 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
 instance로 가져옵니다. JSON과 CSV 형식에서 data table을 만들 수 있습니다.

예를 들어, tag를 지정한 단어가 들어 있는 문장을 담은 JSON 파일을 생각해 보겠습니다. 각 entry에는 `tokens`와 `labels`라는 key 쌍이 들어 있습니다.

*   `tokens` key의 값은 각 문장에 들어 있는 단어와 구두점의 array입니다.
    
*   `labels`의 값은 각 token에 대응하는 label, 즉 tag의 array입니다.
    

두 array의 길이는 같으며, 각 token과 해당 label이 일대일로 매핑됩니다.

아래 JSON snippet은 tokenized sentence 세 쌍과 그에 연결된 label을 보여 줍니다.

    // JSON file
    [\
        {\
            "tokens": ["AirPods", "are", "a", "fantastic", "Apple", "product", "."],\
            "labels": ["PROD", "NONE", "NONE", "NONE", "ORG", "NONE", "NONE"]\
        },\
        {\
            "tokens": ["The", "iPhone", "takes", "stunning", "photos", "."],\
            "labels": ["NONE", "PROD", "NONE", "NONE", "NONE", "NONE"]\
        },\
        {\
            "tokens": ["Start", "building", "a", "native", "Mac", "app", "from", "your", "current", "iPad", "app", "using", "Mac", "Catalyst", "."],\
            "labels": ["NONE", "NONE", "NONE", "NONE", "PROD", "NONE", "NONE", "NONE", "NONE", "PROD", "NONE", "NONE", "PROD", "PROD", "NONE"]\
        }\
    ]
    

macOS playground에서는 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
의 [`init(contentsOf:options:)`](https://developer.apple.com/documentation/createml/mldatatable/init(contentsof:options:))
 method를 사용해 data table을 만듭니다.

    import CreateML
    
    
    let data = try MLDataTable(contentsOf:
        URL(fileURLWithPath: "<#/path/to/read/data.json#>"))
    

생성된 data table에는 JSON 파일의 key에서 가져온 `tokens`와 `labels`라는 두 column이 있습니다. column 이름은 다른 method의 parameter로 사용할 예정이므로, 의미만 분명하다면 무엇이든 괜찮습니다.

이렇게 모은 data는 model training과 evaluation이라는 두 핵심 작업에 사용합니다.

### [training과 evaluation용 data 준비하기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Prepare-your-data-for-training-and-evaluation)

word tagger model을 training한 뒤에는 tag 지정 작업을 얼마나 잘하는지 평가해야 합니다. model 성능을 테스트하려면 data의 일부를 testing dataset으로 따로 분리합니다. training data와 testing data는 겹치지 않도록 완전히 분리해야 합니다. 이렇게 해야 testing data를 바탕으로 계산한 metric이 classifier가 처음 보는 예시에서 얼마나 잘 동작하는지 보여 줍니다.

일반적으로 testing dataset은 training dataset보다 훨씬 작습니다. 보통 전체 data의 약 80%로 model을 training하고 20%로 test합니다. 하지만 더 중요한 점은 testing data의 품질입니다. 실제 예시에 최대한 가깝고, 분포가 고르며, 균형이 잘 맞아야 합니다. 가장 좋은 data를 testing data로 사용합니다.

dataset에서 training data와 testing data를 만드는 한 가지 방법은 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
의 [`randomSplit(by:seed:)`](https://developer.apple.com/documentation/createml/mldatatable/randomsplit(by:seed:))
 method를 사용하는 것입니다. 이 method는 data를 두 table로 나누며, 하나는 training용이고 다른 하나는 testing용입니다. `0.8` split을 지정하면 전체 data의 80%를 담은 training data table과 나머지 20%를 담은 testing data table을 만들 수 있습니다.

    let (trainingData, testingData) = data.randomSplit(by: 0.8, seed: 5)
    

[`randomSplit(by:seed:)`](https://developer.apple.com/documentation/createml/mldatatable/randomsplit(by:seed:))
는 dataset을 빠르게 나누는 방법이지만, training dataset과 testing dataset을 직접 따로 만드는 것도 고려해 볼 만합니다. 그렇게 하면 testing data의 품질을 더 확실히 보장할 수 있습니다.

### [word tagger 만들고 training하기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Create-and-train-the-word-tagger)

training data table과 column 이름을 사용해 [`MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)
 instance를 만듭니다. training은 즉시 시작됩니다.

    let wordTagger = try MLWordTagger(trainingData: trainingData,
                                 tokenColumn: "tokens",
                                 labelColumn: "labels")
    

word tagger training에서는 training 진행 상황을 추적하기 위해 training data의 작은 일부를 validation dataset으로 따로 둬야 합니다. validation data를 사용하면 model이 아직 training하지 않은 예시에서 성능이 어떤지 training process가 판단할 수 있습니다. validation accuracy에 따라 training algorithm이 model 내부 값을 조정하거나, accuracy가 충분히 높으면 training process를 중단할 수도 있습니다.

training data와 validation data도 겹치지 않도록 완전히 분리해야 합니다. 이 split을 직접 만들고 싶다면 training data의 약 5~10%를 validation data로 따로 떼어 두고, custom model parameter를 설정해 전달할 수 있습니다. 직접 split하지 않으면 Create ML이 training phase 동안 model 진행 상황을 검증할 수 있도록 training data의 일부를 자동으로 분리합니다. data가 무작위로 나뉘기 때문에 model을 training할 때마다 결과가 달라질 수 있습니다.

model이 training data와 validation data에서 얼마나 정확하게 동작했는지 확인하려면 model의 [`trainingMetrics`](https://developer.apple.com/documentation/createml/mlwordtagger/trainingmetrics)
와 [`validationMetrics`](https://developer.apple.com/documentation/createml/mlwordtagger/validationmetrics)
 property에 있는 [`taggingError`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/taggingerror)
 property를 사용합니다.

    // Training accuracy as a percentage
    let trainingAccuracy = (1.0 - wordTagger.trainingMetrics.taggingError) * 100
    
    
    // Validation accuracy as a percentage
    let validationAccuracy = (1.0 - wordTagger.validationMetrics.taggingError) * 100
    

### [tagger accuracy 평가하기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Evaluate-the-taggers-accuracy)

다음으로, training된 model이 한 번도 보지 못한 문장으로 test해 성능을 평가합니다. testing data table을 [`evaluation(on:tokenColumn:labelColumn:)`](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:tokencolumn:labelcolumn:)-31x1l)
 method에 전달하면 [`MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)
 instance가 반환됩니다.

    let evaluationMetrics = wordTagger.evaluation(on: testingData,
                                                  tokenColumn: "tokens",
                                                  labelColumn: "labels")
    

evaluation accuracy를 구하려면 반환된 [`MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)
 instance의 [`taggingError`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/taggingerror)
 property를 사용합니다.

    // Evaluation accuracy as a percentage
    let evaluationAccuracy = (1.0 - evaluationMetrics.taggingError) * 100
    

evaluation 성능이 충분하지 않다면 더 많은 data로 다시 training하거나 다른 조정을 해야 할 수 있습니다. model 성능을 개선하는 방법은 `Improving Your Model’s Accuracy`를 참고합니다.

### [Core ML model 저장하기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Save-the-Core-ML-model)

model 성능이 충분히 좋아졌다면 앱에서 사용할 수 있도록 저장할 준비가 된 것입니다. [`write(to:metadata:)`](https://developer.apple.com/documentation/createml/mltextclassifier/write(to:metadata:))
 method를 사용해 Core ML model 파일(이 예시에서는 `AppleTagger.mlmodel`)을 디스크에 기록합니다. model의 작성자, 버전, 설명 같은 정보는 [`MLModelMetadata`](https://developer.apple.com/documentation/createml/mlmodelmetadata)
 instance로 전달합니다.

    let metadata = MLModelMetadata(author: "Jane Appleseed",
                                   shortDescription: "Apple 제품에 tag를 지정하도록 training한 model입니다.",
                                   version: "1.0")
    
    
    try wordTagger.write(to: URL(fileURLWithPath: "<#/path/to/save/AppleTagger.mlmodel#>"),
                                  metadata: metadata)
    

### [앱에 model 추가하기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Add-the-model-to-your-app)

앱을 Xcode에서 연 상태에서 `AppleTagger.mlmodel` 파일을 navigation pane으로 끌어옵니다. Xcode는 model을 컴파일하고 앱에서 사용할 `AppleTagger` class를 생성합니다. model에 대한 추가 정보는 Xcode에서 `AppleTagger.mlmodel` 파일을 선택해 확인합니다.

training과 deployment 사이에서 tokenization이 일관되도록 `AppleTagger`로부터 Natural Language framework의 [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel)
을 만듭니다. 그리고 기존 [`NLTagScheme`](https://developer.apple.com/documentation/NaturalLanguage/NLTagScheme)
 또는 custom [`NLTagScheme`](https://developer.apple.com/documentation/NaturalLanguage/NLTagScheme)
을 사용해 문장이나 문단에 tag를 지정할 수 있도록 model을 [`NLTagger`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger)
에 연결합니다.

    import NaturalLanguage 
    import CoreML
    
    
    let text = "The iPad is my favorite Apple product."
    
    
    do {
        let mlModel = try AppleTagger(configuration: MLModelConfiguration()).model
    
    
        let customModel = try NLModel(mlModel: mlModel)
        let customTagScheme = NLTagScheme("Apple")
        
        let tagger = NLTagger(tagSchemes: [.nameType, customTagScheme])
        tagger.string = text
        tagger.setModels([customModel], forTagScheme: customTagScheme)
        
        tagger.enumerateTags(in: text.startIndex..<text.endIndex, unit: .word, 
                             scheme: customTagScheme, options: .omitWhitespace) { tag, tokenRange  in
            if let tag = tag {
                print("\(text[tokenRange]): \(tag.rawValue)")
            }
            return true
        }
    } catch {
        print(error)
    }
    

[같이 보기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#see-also)

-----------------------------------------------------------------------------------------------------

### [Text model](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model#Text-models)

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

natural language text를 분류하는 machine learning model을 training합니다.

[`struct MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)

natural language text를 분류하도록 training하는 model입니다.

[`struct MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)

natural language text를 단어 수준에서 분류하도록 training하는 word-tagging model입니다.

[`struct MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)

용어와 해당 label의 collection으로, natural language text를 분석하는 tagger를 보강합니다.

[`struct MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)

vector space의 string map으로, string의 이웃을 살펴 비슷한 string을 앱에서 찾을 수 있게 합니다.

현재 페이지: word tagger model 만들기
