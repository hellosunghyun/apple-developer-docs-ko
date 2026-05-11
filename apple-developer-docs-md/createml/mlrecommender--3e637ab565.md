---
title: "MLRecommender | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlrecommender"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131947+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlrecommender#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLRecommender

struct

MLRecommender
=============

item 유사성, grouping, 그리고 선택적인 item rating을 기반으로 recommendation을 만들도록 training하는 model입니다.

macOS 10.15+

    struct MLRecommender

[개요](https://developer.apple.com/documentation/createml/mlrecommender#overview)

--------------------------------------------------------------------------------------

[`MLRecommender`](https://developer.apple.com/documentation/createml/mlrecommender)
 를 사용하면 사용자의 data를 on-device에 유지하면서, app에 포함할 machine learning model을 training해 recommendation을 제공할 수 있습니다.

recommender model은 recommendation item과 item이 속한 group에 대한 column이 포함된 tabular data로 training해 만듭니다. item rating column을 추가로 포함할 수도 있으며, 이 경우 rating이 높은 item은 낮거나 음수 rating을 가진 item보다 더 큰 가중치를 갖습니다. recommender는 training 정보를 사용해 group 안에 함께 나타나는 item이나 group 내에서 rating이 비슷한 item을 보고 유사성 pattern을 찾습니다.

recommender를 training한 뒤에는 `.mlmodel` 확장자를 가진 Core ML model file로 저장합니다. 이 model file을 Project navigator로 드래그해 Xcode project에 import합니다. runtime에는 training data의 pattern과 사용자의 item 기록을 바탕으로 recommender를 사용해 item suggestion을 제공합니다. 예를 들어 hiking app은 사용자가 이전에 걸었던 trail과 그 trail에 대한 rating을 바탕으로 다른 trail을 추천할 수 있습니다.

[주제](https://developer.apple.com/documentation/createml/mlrecommender#topics)

----------------------------------------------------------------------------------

### [recommender 생성 및 training](https://developer.apple.com/documentation/createml/mlrecommender#Creating-and-training-a-recommender)

[`init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)`](https://developer.apple.com/documentation/createml/mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:))

table과 그 안에 포함된 item column 및 user column 이름을 받아 instance를 생성합니다.

[`struct ModelParameters`](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct)

recommender model training 과정에 영향을 주는 parameter입니다.

[`let modelParameters: MLRecommender.ModelParameters`](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.property)

초기화 중 recommender가 training에 사용한 configuration parameter입니다.

[`var userIdentifierColumn: String`](https://developer.apple.com/documentation/createml/mlrecommender/useridentifiercolumn)

초기화 시 user identifier를 정의하기 위해 선택한 column 이름입니다.

[`var itemIdentifierColumn: String`](https://developer.apple.com/documentation/createml/mlrecommender/itemidentifiercolumn)

초기화 시 item identifier를 정의하기 위해 선택한 column 이름입니다.

[`var ratingColumn: String?`](https://developer.apple.com/documentation/createml/mlrecommender/ratingcolumn)

초기화 시 rating을 정의하기 위해 선택한 column 이름입니다.

### [recommender 평가하기](https://developer.apple.com/documentation/createml/mlrecommender#Evaluating-a-recommender)

[`func evaluation(on:userColumn:itemColumn:ratingColumn:cutoffs:excludingObserved:)`](https://developer.apple.com/documentation/createml/mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:))

주어진 testing data에 대한 metric을 계산합니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender의 성능을 평가할 때 사용하는 metric입니다.

### [recommender 테스트하기](https://developer.apple.com/documentation/createml/mlrecommender#Testing-a-recommender)

[`func recommendations(fromUsers:maxCount:restrictingToItems:excluding:excludingObserved:)`](https://developer.apple.com/documentation/createml/mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:))

item 유사성과 rating column을 기준으로, 주어진 user array에 대해 가장 높은 score의 item을 가져옵니다.

Deprecated

[`protocol MLIdentifier`](https://developer.apple.com/documentation/createml/mlidentifier)

Create ML framework가 machine learning identifier로 사용할 수 있는 type입니다.

Deprecated

[`func getSimilarItems(fromItems:maxCount:)`](https://developer.apple.com/documentation/createml/mlrecommender/getsimilaritems(fromitems:maxcount:))

model의 similarity type을 기준으로 상위 순위의 유사 item을 반환합니다.

Deprecated

### [recommender 저장하기](https://developer.apple.com/documentation/createml/mlrecommender#Saving-a-recommender)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlrecommender/write(to:metadata:))

주어진 URL에 recommender를 Core ML model file로 export합니다.

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlrecommender/write(tofile:metadata:))

주어진 file path에 recommender를 Core ML model file로 export합니다.

### [recommender 설명하기](https://developer.apple.com/documentation/createml/mlrecommender#Describing-a-recommender)

[`var model: MLModel`](https://developer.apple.com/documentation/createml/mlrecommender/model)

Core ML model입니다.

### [지원 type](https://developer.apple.com/documentation/createml/mlrecommender#Supporting-types)

[`enum ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mlrecommender/modelalgorithmtype)

recommender가 recommendation을 만들 때 사용할 수 있는 algorithm입니다.

[`enum SimilarityType`](https://developer.apple.com/documentation/createml/mlrecommender/similaritytype)

recommender가 item 유사성을 계산할 때 사용하는 metric입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlrecommender#see-also)

--------------------------------------------------------------------------------------

### [Tabular model](https://developer.apple.com/documentation/createml/mlrecommender#Tabular-models)

[tabular data에서 model 만들기](https://developer.apple.com/documentation/CreateML/creating-a-model-from-tabular-data)

Core ML을 사용해 tabular data를 import하고 관리하면서 machine learning model을 training합니다.

[`enum MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)

data를 이산 category로 분류하도록 training하는 model입니다.

[`enum MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)

연속 값을 추정하도록 training하는 model입니다.

현재 페이지: MLRecommender
