---
title: "Creating a text classifier model | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/creating-a-text-classifier-model"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.130928+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   text classifier model 만들기

문서

text classifier model 만들기
================================

natural language text를 분류하는 machine learning model을 training합니다.

[개요](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Overview)

---------------------------------------------------------------------------------------------------------

text classifier는 sentence에 담긴 sentiment처럼 natural language text의 pattern을 인식하도록 training한 machine learning model입니다.

![text string이 label에 매핑되는 방식을 보여 주는 diagram.](https://docs-assets.developer.apple.com/published/8b58fe67739dc2f7f3bb472ed54312b3/creating-a-text-classifer-model-1%402x.png)

text classifier는 이미 label을 붙여 둔 text 예시를 많이 보여 주며 training합니다. 예를 들어 movie review를 positive, negative, neutral로 미리 분류해 둘 수 있습니다.

![training data를 사용해 Create ML로 text classifier를 training하는 방식을 보여 주는 diagram.](https://docs-assets.developer.apple.com/published/928f87b97f9f6bea77d959ecc545107a/creating-a-text-classifer-model-2%402x.png)

### [data 가져오기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Import-your-data)

먼저 textual data를 모아 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
 instance로 import합니다. data table은 JSON과 CSV 형식에서 만들 수 있습니다. 또는 textual data가 file collection에 있다면, folder 이름을 label로 사용해 folder별로 정리할 수 있습니다. 이는 [Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)
 에서 사용하는 image data source와 비슷합니다.

예를 들어 sentiment별로 분류한 movie review가 들어 있는 JSON file을 생각해 보겠습니다. 각 entry에는 `text`와 `label` 두 key가 있습니다. 이 key의 값이 model training에 사용하는 input sample입니다. 아래 JSON snippet은 sentence 세 개와 각 sentiment label의 쌍을 보여 줍니다.

    // JSON file
    [\
        {\
            "text": "The movie was fantastic!",\
            "label": "positive"\
        }, {\
            "text": "Very boring. Fell asleep.",\
            "label": "negative"\
        }, {\
            "text": "It was just OK.",\
            "label": "neutral"\
        } ...\
    ]
    

macOS playground에서는 [TabularData](https://developer.apple.com/documentation/TabularData)
 framework를 사용해 data frame을 만듭니다.

    import TabularData
    
    
    let data = try DataFrame(contentsOfJSONFile: URL(fileURLWithPath: "<#/path/to/read/data.json#>"))
    

결과 data frame에는 JSON file의 key에서 가져온 _text_ 와 _label_ 두 column이 있습니다. column 이름은 의미만 분명하면 무엇이든 사용할 수 있습니다. 다른 method에서 parameter로 사용하기 때문입니다.

### [training과 evaluation을 위한 data 준비하기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Prepare-your-data-for-training-and-evaluation)

model training에 사용하는 data는 model evaluation에 사용하는 data와 달라야 합니다. [`stratifiedSplit(on:by:randomSeed:)`](https://developer.apple.com/documentation/TabularData/DataFrameProtocol/stratifiedSplit(on:by:randomSeed:)-9iauf)
 method를 사용해 data를 두 data frame으로 나눕니다. 하나는 training용이고 다른 하나는 testing용입니다. training data frame에는 대부분의 data가 들어가고, testing data frame에는 나머지 20퍼센트가 들어갑니다.

    let (trainingData, testingData) = data.stratifiedSplit(on: "text", by: 0.8)
    

### [model training parameter 선택하기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Choose-model-training-parameters)

model training parameter로 learning process를 제어할 수 있습니다. [`MLTextClassifier.ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype)
 parameter를 지정해 classifier algorithm type을 선택합니다. [`MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/maxent(revision:))
 algorithm은 빠르게 training되고 다양한 data에서 잘 동작합니다. data와 model을 탐색하는 동안 좋은 시작점이 됩니다.

transfer learning algorithm인 [`MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/transferlearning(_:revision:))
 도 선택할 수 있습니다. transfer learning model은 pre-trained model을 feature extractor로 사용하며, 여기서 [`MLTextClassifier.FeatureExtractorType`](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype)
 를 지정합니다. transfer learning model은 training 시간이 더 오래 걸릴 수 있지만, baseline model이 특정 언어의 많은 text로 이미 training되어 있어 accuracy를 높일 수 있습니다.

data에 여러 언어가 포함되어 있다면 maximum entropy algorithm [`MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/maxent(revision:))
 또는 transfer learning algorithm [`MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/transferlearning(_:revision:))
 을 선택하고, 그 [`MLTextClassifier.FeatureExtractorType`](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype)
 을 Bidirectional Encoder Representations from Transformers(BERT) embedding feature extractor [`MLTextClassifier.FeatureExtractorType.bertEmbedding`](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/bertembedding)
 으로 설정합니다.

data에 단일 언어만 포함되어 있다면 conditional random fields algorithm [`MLTextClassifier.ModelAlgorithmType.crf(revision:)`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/crf(revision:))
 또는 transfer learning algorithm [`MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/transferlearning(_:revision:))
 을 사용하고, 그 [`MLTextClassifier.FeatureExtractorType`](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype)
 을 Embeddings from Language Models(ELMo) embedding feature extractor [`MLTextClassifier.FeatureExtractorType.elmoEmbedding`](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/elmoembedding)
 으로 설정합니다.

[`MLTextClassifier.ModelParameters.ValidationData`](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum)
 parameter로 model training에서 제외할 evaluation data를 지정합니다. training 과정에서는 validation data를 사용해 model이 새로운 example을 얼마나 정확히 분류하는지 추정합니다. validation accuracy에 따라 classifier algorithm이 model 내부 값을 조정하거나, accuracy가 충분히 높으면 training을 중단할 수 있습니다. data split은 random이므로 model을 training할 때마다 결과가 달라질 수 있습니다.

    let parameters = MLTextClassifier.ModelParameters(
        validation: .split(strategy: .automatic),
        algorithm: .transferLearning(.bertEmbedding, revision: 1),
        language: .english
    )
    

### [text classifier 만들고 training하기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Create-and-train-a-text-classifier)

training data frame과 column 이름으로 [`MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)
 instance를 만듭니다.

    let sentimentClassifier = try MLTextClassifier(
        trainingData: trainingData,
        textColumn: "text",
        labelColumn: "label",
        parameters: parameters
    )
    

model(`sentimentClassifier`)이 training data와 validation data에서 얼마나 정확한지 측정하려면 model의 [`trainingMetrics`](https://developer.apple.com/documentation/createml/mltextclassifier/trainingmetrics)
 와 [`validationMetrics`](https://developer.apple.com/documentation/createml/mltextclassifier/validationmetrics)
 property에 있는 [`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
 를 사용합니다.

    // Calculate training accuracy as a percentage.
    let trainingAccuracy = (1.0 - sentimentClassifier.trainingMetrics.classificationError) * 100
    
    
    // Calculate validation accuracy as a percentage.
    let validationAccuracy = (1.0 - sentimentClassifier.validationMetrics.classificationError) * 100
    

### [classifier의 accuracy 평가하기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Evaluate-a-classifiers-accuracy)

다음으로, training된 model이 처음 보는 sentence에 대해 얼마나 잘 동작하는지 평가합니다. testing data frame을 [`evaluation(on:)`](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)-8ch4k)
 method에 전달하면 [`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
 instance를 반환합니다.

    let evaluationMetrics = sentimentClassifier.evaluation(on: testingData, textColumn: "text", labelColumn: "label")
    

evaluation accuracy를 얻으려면 반환된 [`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
 instance의 [`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
 property를 사용합니다.

    // evaluation accuracy를 percentage로 계산합니다.
    let evaluationAccuracy = (1.0 - evaluationMetrics.classificationError) * 100
    

evaluation 성능이 충분하지 않다면 data를 더 늘려 다시 training하거나 다른 조정을 해야 할 수 있습니다. model 성능 개선 방법은 [model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)
 를 참고하십시오.

### [Core ML model 저장하기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Save-a-Core-ML-model)

model 성능이 충분히 좋아지면 app에서 사용할 수 있도록 저장할 준비가 된 것입니다. [`write(to:metadata:)`](https://developer.apple.com/documentation/createml/mltextclassifier/write(to:metadata:))
 method로 Core ML model file을 disk에 기록합니다. author, version, description 같은 model 정보는 [`MLModelMetadata`](https://developer.apple.com/documentation/createml/mlmodelmetadata)
 instance로 제공합니다.

    let metadata = MLModelMetadata(author: "John Appleseed",
                                   shortDescription: "movie review sentiment를 분류하도록 training한 model",
                                   version: "1.0")
    
    
    try sentimentClassifier.write(to: URL(fileURLWithPath: "<#/path/to/save/SentimentClassifier.mlmodel#>"),
                                  metadata: metadata)
    

위 코드에서는 `fileURLWithPath:` parameter로 `SentimentClassifier.mlmodel`이라는 file 이름을 지정합니다.

### [app에 Core ML model 추가하기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Add-a-Core-ML-model-to-your-app)

Xcode에서 app을 연 상태로 `SentimentClassifier.mlmodel` file을 navigation pane으로 드래그합니다. Xcode는 model을 compile하고 app에서 사용할 `SentimentClassifier` class를 생성합니다. Xcode에서 `SentimentClassifier.mlmodel` file을 선택하면 model에 대한 추가 정보를 볼 수 있습니다.

`SentimentClassifier`에서 Natural Language framework의 [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel)
 을 만들어 training과 deployment 사이의 tokenization이 일관되게 유지되도록 합니다. 그런 다음 [`predictedLabel(for:)`](https://developer.apple.com/documentation/NaturalLanguage/NLModel/predictedLabel(for:))
 을 사용해 새로운 text input에 대한 prediction을 생성합니다.

    import NaturalLanguage
    import CoreML
    
    
    let mlModel = try SentimentClassifier(configuration: MLModelConfiguration()).model
    
    
    let sentimentPredictor = try NLModel(mlModel: mlModel)
    sentimentPredictor.predictedLabel(for: "It was the best I've ever seen!")
    

[같이 보기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#see-also)

---------------------------------------------------------------------------------------------------------

### [Text model](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model#Text-models)

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

natural language text의 개별 word에 tag를 붙이는 machine learning model을 training합니다.

[`struct MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)

natural language text를 분류하도록 training하는 model입니다.

[`struct MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)

natural language text를 word 수준에서 분류하도록 training하는 word-tagging model입니다.

[`struct MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)

natural language text를 분석하는 tagger를 보강하는 terms와 그 labels의 collection입니다.

[`struct MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)

vector space에서 string을 매핑해, app이 string의 이웃을 살펴 유사한 string을 찾을 수 있게 하는 구조입니다.

현재 페이지: Creating a text classifier model
