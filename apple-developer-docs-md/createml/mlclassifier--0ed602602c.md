---
title: "MLClassifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlclassifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131859+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlclassifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLClassifier

enum

MLClassifier
============

data를 이산 category로 분류하도록 training하는 model입니다.

macOS 10.14+

    enum MLClassifier

[언급된 항목](https://developer.apple.com/documentation/createml/mlclassifier#mentions)

-----------------------------------------------------------------------------------------

[model 정확도 향상하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[개요](https://developer.apple.com/documentation/createml/mlclassifier#overview)

-------------------------------------------------------------------------------------

[`MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)
를 사용해 category를 인식하는 범용 model을 training합니다.

예를 들어 다음 입력으로 sports team이 다음 경기에서 이길지 질지를 예측하는 classifier를 만들 수 있습니다.

*   팀의 승패 비율
    
*   팀의 경기 위치
    

[`MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)
를 만들면 Create ML이 data를 검사해 자동으로 구체적인 classifier를 선택합니다(_Supporting Classifier Types_ 참고).

[주제](https://developer.apple.com/documentation/createml/mlclassifier#topics)

---------------------------------------------------------------------------------

### [classifier 생성 및 training](https://developer.apple.com/documentation/createml/mlclassifier#Creating-and-training-a-classifier)

[`init(trainingData:targetColumn:featureColumns:)`](https://developer.apple.com/documentation/createml/mlclassifier/init(trainingdata:targetcolumn:featurecolumns:))

classifier를 생성합니다.

[`var targetColumn: String`](https://developer.apple.com/documentation/createml/mlclassifier/targetcolumn)

classifier가 어떤 category를 예측할지 정의하기 위해 initialization에서 선택한 column 이름입니다.

[`var featureColumns: [String]`](https://developer.apple.com/documentation/createml/mlclassifier/featurecolumns)

classifier를 training하기 위해 initialization에서 선택한 column 이름입니다.

### [classifier 평가하기](https://developer.apple.com/documentation/createml/mlclassifier#Evaluating-a-classifier)

[`func evaluation(on:)`](https://developer.apple.com/documentation/createml/mlclassifier/evaluation(on:))

제공된 label data로 classifier를 평가합니다.

[`var trainingMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifier/trainingmetrics)

training dataset에서 classifier 성능을 측정한 값입니다.

[`var validationMetrics: MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifier/validationmetrics)

validation dataset에서 classifier 성능을 측정한 값입니다.

### [classifier 테스트하기](https://developer.apple.com/documentation/createml/mlclassifier#Testing-a-classifier)

[`func predictions(from:)`](https://developer.apple.com/documentation/createml/mlclassifier/predictions(from:))

### [classifier 저장하기](https://developer.apple.com/documentation/createml/mlclassifier#Saving-a-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlclassifier/write(to:metadata:))

app에서 사용할 Core ML model file을 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlclassifier/write(tofile:metadata:))

app에서 사용할 Core ML model file을 내보냅니다.

### [model 설명하기](https://developer.apple.com/documentation/createml/mlclassifier#Describing-a-model)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlclassifier/model)

memory에 저장된 기반 Core ML model입니다.

[`var description: String`](https://developer.apple.com/documentation/createml/mlclassifier/description)

classifier의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlclassifier/debugdescription)

debugging 출력에 적합한 classifier의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlclassifier/playgrounddescription)

playground에 표시되는 classifier 설명입니다.

### [Classifier case](https://developer.apple.com/documentation/createml/mlclassifier#Classifier-cases)

[`case decisionTree(MLDecisionTreeClassifier)`](https://developer.apple.com/documentation/createml/mlclassifier/decisiontree(_:))

data를 분할하는 규칙을 만들어 target을 예측하는 classifier입니다.

[`case randomForest(MLRandomForestClassifier)`](https://developer.apple.com/documentation/createml/mlclassifier/randomforest(_:))

data의 subset으로 training한 decision tree 모음에 기반한 classifier입니다.

[`case boostedTree(MLBoostedTreeClassifier)`](https://developer.apple.com/documentation/createml/mlclassifier/boostedtree(_:))

gradient boosting과 결합한 decision tree 모음에 기반한 classifier입니다.

[`case logisticRegression(MLLogisticRegressionClassifier)`](https://developer.apple.com/documentation/createml/mlclassifier/logisticregression(_:))

data feature의 function로 이산 target 값을 예측하는 classifier입니다.

[`case supportVector(MLSupportVectorClassifier)`](https://developer.apple.com/documentation/createml/mlclassifier/supportvector(_:))

category 간 분리를 최대화해 이진 target 값을 예측하는 classifier입니다.

Deprecated

### [지원하는 classifier type](https://developer.apple.com/documentation/createml/mlclassifier#Supporting-classifier-types)

[`struct MLDecisionTreeClassifier`](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier)

data를 분할하는 규칙을 만들어 target을 예측하는 classifier입니다.

[`struct MLRandomForestClassifier`](https://developer.apple.com/documentation/createml/mlrandomforestclassifier)

data의 subset으로 training한 decision tree 모음에 기반한 classifier입니다.

[`struct MLBoostedTreeClassifier`](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier)

gradient boosting과 결합한 decision tree 모음에 기반한 classifier입니다.

[`struct MLLogisticRegressionClassifier`](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier)

data feature의 function로 이산 target 값을 예측하는 classifier입니다.

[`struct MLSupportVectorClassifier`](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier)

category 간 분리를 최대화해 이진 target 값을 예측하는 classifier입니다.

Deprecated

### [기본 구현](https://developer.apple.com/documentation/createml/mlclassifier#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlclassifier/customdebugstringconvertible-implementations)

[API Reference: CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlclassifier/customplaygrounddisplayconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlclassifier/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlclassifier#relationships)

-----------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlclassifier#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlclassifier#see-also)

-------------------------------------------------------------------------------------

### [Tabular model](https://developer.apple.com/documentation/createml/mlclassifier#Tabular-models)

[tabular data로 model 만들기](https://developer.apple.com/documentation/CreateML/creating-a-model-from-tabular-data)

Core ML을 사용해 tabular data를 import하고 관리하면서 machine learning model을 training합니다.

[`enum MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)

연속 값을 추정하도록 training하는 model입니다.

[`struct MLRecommender`](https://developer.apple.com/documentation/createml/mlrecommender)

item 유사성, grouping, 그리고 선택적으로 item rating을 기반으로 추천하도록 training하는 model입니다.

현재 페이지: MLClassifier
