---
title: "Create ML | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.129146+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml#app-main)

framework

Create ML
=========

app에서 사용할 machine learning model을 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

[개요](https://developer.apple.com/documentation/createml#Overview)

------------------------------------------------------------------------

Swift와 macOS playground 같은 익숙한 도구와 함께 Create ML을 사용해 Mac에서 custom machine learning model을 만들고 training할 수 있습니다. image 인식, text에서 의미 추출, 수치 값 사이의 관계 찾기 같은 작업을 수행하도록 model을 training할 수 있습니다.

![Create ML에서 image, text 및 기타 structured data를 사용해 Core ML model을 training하는 방법을 보여 주는 다이어그램입니다.](https://docs-assets.developer.apple.com/published/eb03080ad7cc9d6f88eadc90b3bac920/create-ml-1%402x.png)

대표적인 sample을 보여 주어 pattern을 인식하도록 model을 training합니다. 예를 들어 다양한 개 image를 많이 보여 주어 개를 인식하는 model을 training할 수 있습니다. model training이 끝나면 이전에 보지 못한 data로 테스트하고, 작업을 얼마나 잘 수행하는지 평가합니다. model 성능이 충분하면 [Core ML](https://developer.apple.com/documentation/CoreML)
을 사용해 app에 통합할 준비가 된 것입니다.

![data 수집, model training, training한 model 평가로 이어지는 Create ML workflow를 보여 주는 다이어그램입니다.](https://docs-assets.developer.apple.com/published/8140ce0ea19e9ada712c516d10436651/create-ml-2%402x.png)

Create ML은 Photos와 Siri 같은 Apple 제품에 내장된 machine learning infrastructure를 활용합니다. 따라서 image classification model과 natural language model의 크기가 더 작고 training 시간도 훨씬 짧습니다.

[주제](https://developer.apple.com/documentation/createml#topics)

--------------------------------------------------------------------

### [Image model](https://developer.apple.com/documentation/createml#Image-models)

[Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)

image를 분류하는 machine learning model을 training하고 Core ML app에 추가합니다.

[`struct MLImageClassifier`](https://developer.apple.com/documentation/createml/mlimageclassifier)

image를 분류하도록 training하는 model입니다.

[`struct MLObjectDetector`](https://developer.apple.com/documentation/createml/mlobjectdetector)

image 안의 하나 이상의 object를 분류하도록 training하는 model입니다.

[`struct MLHandPoseClassifier`](https://developer.apple.com/documentation/createml/mlhandposeclassifier)

제공한 사람 손 image로 training해 hand pose classification model을 만드는 task입니다.

### [Video model](https://developer.apple.com/documentation/createml#Video-models)

[Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)

사람의 body movement를 인식하는 machine learning model을 training합니다.

[live video feed에서 human action 감지하기](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed)

일련의 video frame에서 얻은 사람의 pose data를 action-classification model로 보내 body movement를 식별합니다.

[`struct MLActionClassifier`](https://developer.apple.com/documentation/createml/mlactionclassifier)

video로 training해 사람의 body movement를 분류하는 model입니다.

[`struct MLHandActionClassifier`](https://developer.apple.com/documentation/createml/mlhandactionclassifier)

제공한 사람 손 움직임 video로 training해 hand action classification model을 만드는 task입니다.

[`struct MLStyleTransfer`](https://developer.apple.com/documentation/createml/mlstyletransfer)

한 image의 style을 다른 image나 video에 적용하도록 training하는 model입니다.

### [Text model](https://developer.apple.com/documentation/createml#Text-models)

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

natural language text를 분류하는 machine learning model을 training합니다.

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

natural language text의 개별 단어에 tag를 붙이는 machine learning model을 training합니다.

[`struct MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)

natural language text를 분류하도록 training하는 model입니다.

[`struct MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)

natural language text를 단어 수준에서 분류하도록 training하는 word-tagging model입니다.

[`struct MLGazetteer`](https://developer.apple.com/documentation/createml/mlgazetteer)

용어와 해당 label의 모음으로, natural language text를 분석하는 tagger를 보강합니다.

[`struct MLWordEmbedding`](https://developer.apple.com/documentation/createml/mlwordembedding)

vector space 안의 string map으로, string의 이웃을 살펴 비슷한 string을 app이 찾을 수 있게 합니다.

### [Sound model](https://developer.apple.com/documentation/createml#Sound-models)

[`struct MLSoundClassifier`](https://developer.apple.com/documentation/createml/mlsoundclassifier)

audio file로 training해 device에서 sound를 인식하고 식별하는 machine learning model입니다.

### [Motion model](https://developer.apple.com/documentation/createml#Motion-models)

[`struct MLActivityClassifier`](https://developer.apple.com/documentation/createml/mlactivityclassifier)

motion sensor data를 분류하도록 training하는 model입니다.

### [Tabular model](https://developer.apple.com/documentation/createml#Tabular-models)

[tabular data에서 model 만들기](https://developer.apple.com/documentation/CreateML/creating-a-model-from-tabular-data)

Core ML을 사용해 tabular data를 가져오고 관리하면서 machine learning model을 training합니다.

[`enum MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)

data를 이산적인 category로 분류하도록 training하는 model입니다.

[`enum MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)

연속적인 값을 추정하도록 training하는 model입니다.

[`struct MLRecommender`](https://developer.apple.com/documentation/createml/mlrecommender)

item 유사성, grouping, 그리고 선택적으로 item rating을 바탕으로 추천을 수행하도록 training하는 model입니다.

### [Tabular data](https://developer.apple.com/documentation/createml#Tabular-data)

[`struct MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)

machine learning model을 training하거나 평가하기 위한 data table입니다.

[`enum MLDataValue`](https://developer.apple.com/documentation/createml/mldatavalue)

data table에서 셀의 값입니다.

[API Reference\
\
Data visualizations](https://developer.apple.com/documentation/createml/data-visualizations)

playground에서 data table과 column의 image를 렌더링합니다.

### [Model accuracy](https://developer.apple.com/documentation/createml#Model-accuracy)

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

metric을 사용해 machine learning model의 성능을 조정합니다.

[`struct MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)

classifier 성능을 평가할 때 사용하는 metric입니다.

[`struct MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)

regressor 성능을 평가할 때 사용하는 metric입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger 성능을 평가할 때 사용하는 metric입니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender 성능을 평가할 때 사용하는 metric입니다.

[`struct MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)

object detector 성능을 평가할 때 사용하는 metric입니다.

### [Model training Control](https://developer.apple.com/documentation/createml#Model-training-Control)

[`class MLJob`](https://developer.apple.com/documentation/createml/mljob)

session 진행 상황을 모니터링하거나 실행을 종료하는 데 사용하는 model의 asynchronous training session 표현입니다.

[`class MLTrainingSession`](https://developer.apple.com/documentation/createml/mltrainingsession)

model의 asynchronous training session 현재 상태입니다.

[`struct MLTrainingSessionParameters`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)

training session의 configuration 설정입니다.

[`struct MLCheckpoint`](https://developer.apple.com/documentation/createml/mlcheckpoint)

feature extraction 또는 training 단계 중 특정 시점의 model asynchronous training session 상태입니다.

### [Supporting types](https://developer.apple.com/documentation/createml#Supporting-types)

[`enum MLCreateError`](https://developer.apple.com/documentation/createml/mlcreateerror)

model training, prediction 수행, file system에 model 쓰기 등 여러 작업 중 Create ML이 throw하는 error입니다.

[`struct MLModelMetadata`](https://developer.apple.com/documentation/createml/mlmodelmetadata)

Core ML model file에 저장되는 model 정보입니다.

[`enum MLSplitStrategy`](https://developer.apple.com/documentation/createml/mlsplitstrategy)

보통 training dataset에서 validation dataset을 만들 때 사용하는 data partitioning 방식입니다.

### [Articles](https://developer.apple.com/documentation/createml#Articles)

[API Reference\
\
Data visualizations](https://developer.apple.com/documentation/createml/create-ml-utilties)

playground에서 data table과 column의 image를 렌더링합니다.

[live video feed에서 human action 감지하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed)

일련의 video frame에서 얻은 사람의 pose data를 action-classification model로 보내 body movement를 식별합니다.

[Action Classifier용 training video 모으기](https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos)

action classifier를 효과적으로 training할 수 있는 고품질 예제 video를 수집합니다.

### [Functions](https://developer.apple.com/documentation/createml#Functions)

[`func show(_:)`](https://developer.apple.com/documentation/createml/show(_:))

untyped column의 streaming visualization을 생성합니다.

지원 중단됨

[`func show(_:_:)`](https://developer.apple.com/documentation/createml/show(_:_:))

두 untyped column의 streaming plot visualization을 생성합니다.

지원 중단됨

### [Enumerations](https://developer.apple.com/documentation/createml#Enumerations)

[`enum MLBoundingBoxAnchor`](https://developer.apple.com/documentation/createml/mlboundingboxanchor)

annotation 좌표가 기준점으로 사용하는 bounding box 내부 위치입니다.

[`enum MLBoundingBoxCoordinatesOrigin`](https://developer.apple.com/documentation/createml/mlboundingboxcoordinatesorigin)

annotation 좌표가 origin으로 사용하는 image 내부 위치입니다.

[`enum MLBoundingBoxUnits`](https://developer.apple.com/documentation/createml/mlboundingboxunits)

bounding box annotation이 위치와 크기를 정의할 때 사용하는 단위입니다.

현재 페이지는 Create ML입니다
