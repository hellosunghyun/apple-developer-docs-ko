---
title: "MLRegressor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlregressor"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132048+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlregressor#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLRegressor

enum

MLRegressor
===========

연속값을 추정하도록 training하는 model입니다.

macOS 10.14+

    enum MLRegressor

[언급된 문서](https://developer.apple.com/documentation/createml/mlregressor#mentions)

----------------------------------------------------------------------------------------

[model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[개요](https://developer.apple.com/documentation/createml/mlregressor#overview)

------------------------------------------------------------------------------------

[`MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)
를 사용해 가격, 시간, 온도 같은 연속값을 추정합니다.

regressor는 training 과정에서 보지 못한 output 값도 예측할 수 있다는 점에서 classifier와 다릅니다. 반면 classifier는 training data에서 제공한 category로만 input을 분류할 수 있습니다.

예를 들어 화성의 주택 가격을 추정할 때 regressor는 example 사이를 보간해 training 중에 보지 못한 가격을 추정할 수 있습니다. 아래 그림은 [Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/CoreML/integrating-a-core-ml-model-into-your-app)
 sample과 비슷한 화성 부동산 가격용 선형 regressor를 보여 줍니다.

![화성의 주택 가격 그래프와 그 사이의 연속 추정을 만드는 선형 regressor를 보여 주는 그래프](https://docs-assets.developer.apple.com/published/03ef437b3bfd8a33d85264d85eeb2de4/MLRegressor-1%402x.png)

이 경우 태양광 패널이 3개인 data point는 없지만 regressor는 주택 가격에 대해 근거 있는 prediction을 만들 수 있습니다.

[`MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)
를 만들면 Create ML이 data를 검사해 적절한 구체적 regressor를 자동으로 선택합니다. 자세한 내용은 _Supporting Regressor Types_를 참고하세요.

[주제](https://developer.apple.com/documentation/createml/mlregressor#topics)

--------------------------------------------------------------------------------

### [regressor 만들고 training하기](https://developer.apple.com/documentation/createml/mlregressor#Creating-and-training-a-regressor)

[`init(trainingData:targetColumn:featureColumns:)`](https://developer.apple.com/documentation/createml/mlregressor/init(trainingdata:targetcolumn:featurecolumns:))

regressor를 생성합니다.

[`var targetColumn: String`](https://developer.apple.com/documentation/createml/mlregressor/targetcolumn)

initializer에서 선택한 column 이름이며 regressor가 어떤 feature를 예측할지 정의합니다.

[`var featureColumns: [String]`](https://developer.apple.com/documentation/createml/mlregressor/featurecolumns)

regressor training에 사용할 column 이름입니다.

### [regressor 평가하기](https://developer.apple.com/documentation/createml/mlregressor#Evaluating-a-regressor)

[`func evaluation(on:)`](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:))

제공한 label data에서 classifier를 평가합니다.

[`var trainingMetrics: MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressor/trainingmetrics)

training data set에서 regressor 성능을 측정한 값입니다.

[`var validationMetrics: MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressor/validationmetrics)

validation data set에서 regressor 성능을 측정한 값입니다.

### [regressor 테스트하기](https://developer.apple.com/documentation/createml/mlregressor#Testing-a-regressor)

[`func predictions(from:)`](https://developer.apple.com/documentation/createml/mlregressor/predictions(from:))

### [regressor 저장하기](https://developer.apple.com/documentation/createml/mlregressor#Saving-a-regressor)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlregressor/write(to:metadata:))

app에서 사용할 Core ML model file을 내보냅니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlregressor/write(tofile:metadata:))

app에서 사용할 Core ML model file을 내보냅니다.

### [regressor 설명하기](https://developer.apple.com/documentation/createml/mlregressor#Describing-a-regressor)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlregressor/model)

memory에 저장된 기반 Core ML model입니다.

[`var description: String`](https://developer.apple.com/documentation/createml/mlregressor/description)

regressor의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mlregressor/debugdescription)

debugging 중 출력에 적합한 regressor의 text 표현입니다.

[`var playgroundDescription: Any`](https://developer.apple.com/documentation/createml/mlregressor/playgrounddescription)

playground에 표시되는 regressor 설명입니다.

### [regressor case](https://developer.apple.com/documentation/createml/mlregressor#Regressor-cases)

[`case linear(MLLinearRegressor)`](https://developer.apple.com/documentation/createml/mlregressor/linear(_:))

feature의 선형 function로 target을 추정하는 regressor입니다.

[`case decisionTree(MLDecisionTreeRegressor)`](https://developer.apple.com/documentation/createml/mlregressor/decisiontree(_:))

data를 분할하는 rule을 학습해 target을 추정하는 regressor입니다.

[`case boostedTree(MLBoostedTreeRegressor)`](https://developer.apple.com/documentation/createml/mlregressor/boostedtree(_:))

gradient boosting과 결합한 decision tree collection 기반 regressor입니다.

[`case randomForest(MLRandomForestRegressor)`](https://developer.apple.com/documentation/createml/mlregressor/randomforest(_:))

data subset으로 training한 decision tree collection 기반 regressor입니다.

### [지원하는 regressor type](https://developer.apple.com/documentation/createml/mlregressor#Supporting-regressor-types)

[`struct MLLinearRegressor`](https://developer.apple.com/documentation/createml/mllinearregressor)

feature의 선형 function로 target을 추정하는 regressor입니다.

[`struct MLDecisionTreeRegressor`](https://developer.apple.com/documentation/createml/mldecisiontreeregressor)

data를 분할하는 rule을 학습해 target을 추정하는 regressor입니다.

[`struct MLRandomForestRegressor`](https://developer.apple.com/documentation/createml/mlrandomforestregressor)

data subset으로 training한 decision tree collection 기반 regressor입니다.

[`struct MLBoostedTreeRegressor`](https://developer.apple.com/documentation/createml/mlboostedtreeregressor)

gradient boosting과 결합한 decision tree collection 기반 regressor입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mlregressor#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mlregressor/customdebugstringconvertible-implementations)

[API Reference: CustomPlaygroundDisplayConvertible 구현](https://developer.apple.com/documentation/createml/mlregressor/customplaygrounddisplayconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mlregressor/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mlregressor#relationships)

----------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlregressor#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomPlaygroundDisplayConvertible`](https://developer.apple.com/documentation/Swift/CustomPlaygroundDisplayConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlregressor#see-also)

------------------------------------------------------------------------------------

### [Tabular model](https://developer.apple.com/documentation/createml/mlregressor#Tabular-models)

[tabular data에서 model 만들기](https://developer.apple.com/documentation/CreateML/creating-a-model-from-tabular-data)

Core ML을 사용해 tabular data를 import하고 관리하면서 machine learning model을 training합니다.

[`enum MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)

data를 이산 category로 분류하도록 training하는 model입니다.

[`struct MLRecommender`](https://developer.apple.com/documentation/createml/mlrecommender)

item 유사도, grouping, 그리고 선택적으로 item rating을 기반으로 recommendation을 만들도록 training하는 model입니다.

현재 페이지: MLRegressor
