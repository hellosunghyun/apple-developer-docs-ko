---
title: "Creating a model from tabular data | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132532+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLDataTable](https://developer.apple.com/documentation/createml/mldatatable)
    
*   tabular data로 model 만들기

Sample Code

tabular data로 model 만들기
==================================

Core ML을 사용해 tabular data를 import하고 관리하여 machine learning model을 training합니다.

[Download](https://docs-assets.developer.apple.com/published/ecccf72f7716/CreatingAModelFromTabularData.zip)

Xcode 10.1+

[개요](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Overview)

-----------------------------------------------------------------------------------------------------------

이 sample playground는 [Create ML](https://developer.apple.com/documentation/CreateML)
 framework를 사용해 regressor와 classifier인 두 개의 [Core ML](https://developer.apple.com/documentation/CoreML)
 model을 training합니다.

![data가 Create ML로 들어가 Core ML model file을 생성하는 data 흐름을 보여주는 다이어그램.](https://docs-assets.developer.apple.com/published/38976948d8275d3ec653e82667c6e840/tabular-data-flow%402x.png)

playground는 화성 주거 data가 들어 있는 CSV file을 data table로 import합니다. data table에는 화성의 habitat에 대한 다음 column 정보가 들어 있습니다:

*   Price
    
*   크기(에이커 단위 면적)
    
*   온실 수
    
*   태양광 패널 수
    
*   주요 용도
    

playground는 각 model에 관련된 column 묶음을 사용해 regressor model과 classifier model을 training합니다. training이 끝나면 regressor는 habitat의 가격을 예측할 준비가 되고, classifier는 habitat의 용도를 예측할 준비가 됩니다.

마지막으로 playground는 각 model을 file로 저장해 app에 통합할 수 있게 합니다.

### [data import](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Import-the-data)

원하는 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
 initializer를 사용해 data를 data table로 import합니다. 이 sample에서는 playground에 포함된 CSV file 내용으로 첫 번째 data table을 초기화합니다.

    /// playground의 `Resources` folder에 있는 CSV file로 data table을 만듭니다.
    let csvFile = Bundle.main.url(forResource: "MarsHabitats", withExtension: "csv")!
    let dataTable = try MLDataTable(contentsOf: csvFile)
    

console에서 내용을 보기 좋게 출력한 sample을 보려면 data table을 `print()`에 전달합니다.

    print(dataTable)
    

    // 출력 예시...
    /*
     Columns:
         solar_panels    float
         greenhouses     float
         size            integer
         price           integer
         purpose         string
     Rows: 400
     Data:
     +-------------+-------------+-------------+-------------+-------------+
     | solarPanels | greenhouses | size        | price       | purpose     |
     +-------------+-------------+-------------+-------------+-------------+
     | 5           | 2.5         | 430         | 1500        | farm        |
     | 12          | 3           | 470         | 2990        | general     |
     | 20          | 2           | 460         | 2950        | power       |
     | 8           | 3           | 315         | 1990        | farm        |
     | 7.5         | 1.5         | 245         | 1500        | general     |
     +-------------+-------------+-------------+-------------+-------------+
     [400 rows x 5 columns]
     */
    

### [관련 model data 분리](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Isolate-the-relevant-model-data)

필요하면 model에 관련된 column만 포함하는 새 data table을 생성합니다.

예를 들어 가격을 예측할 때 playground의 regressor에는 원래 다섯 개 column 중 네 개만 필요합니다:

*   `price`
    
*   `solarPanels`
    
*   `greenhouses`
    
*   `size`
    

playground는 첫 번째 data table의 [`subscript(_:)`](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:))
에 column 이름 배열을 전달해 regressor에 맞춘 새 data table을 생성합니다.

    let regressorColumns = ["price", "solarPanels", "greenhouses", "size"]
    let regressorTable = dataTable[regressorColumns]
    

habitat의 용도를 예측하려면 classifier에도 비슷한 column 묶음이 필요합니다:

*   `purpose`
    
*   `solarPanels`
    
*   `greenhouses`
    
*   `size`
    

    let classifierColumns = ["purpose", "solarPanels", "greenhouses", "size"]
    let classifierTable = dataTable[classifierColumns]
    

### [training용 data와 evaluation용 data 나누기](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Divide-the-data-for-training-and-evaluation)

training 후 model을 evaluation할 계획이라면 data table의 일부 row를 training data와 분리해 evaluation용으로 남겨 둡니다. training에 사용하지 않은 data로 model을 evaluation하면 model의 실제 환경 성능을 더 잘 반영할 수 있습니다.

playground는 [`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
의 [`randomSplit(by:seed:)`](https://developer.apple.com/documentation/createml/mldatatable/randomsplit(by:seed:))
 method를 사용해 model마다 두 개의 data table을 만듭니다. 하나는 evaluation용이고 다른 하나는 training용입니다. 이 method는 원본 data table의 row를 무작위로 나눠 생성한 두 개의 새 data table tuple을 반환합니다. tuple의 첫 번째 data table 크기는 `0.0`과 `1.0` 사이 부동소수점 값인 `proportion` parameter로 결정합니다. tuple의 두 번째 data table에는 나머지 data row가 들어 있습니다.

이 예제에서 playground는 각 model data row의 20%를 evaluation용으로 남기고 나머지 80%를 training에 사용합니다.

    let (regressorEvaluationTable, regressorTrainingTable) = regressorTable.randomSplit(by: 0.20, seed: 5)
    let (classifierEvaluationTable, classifierTrainingTable) = classifierTable.randomSplit(by: 0.20, seed: 5)
    

model이 evaluation과 training에 각각 얼마나 많은 data를 필요로 하는지는 app마다 다릅니다. 일반적으로 더 많은 example로 model을 training할수록 성능이 좋아집니다.

### [regressor training](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Train-the-regressor)

playground는 training data table과 target column 이름을 initializer에 전달해 regressor를 training합니다. `targetColumn` parameter는 model이 prediction에서 어떤 정보를 제공할지 결정합니다. playground는 model의 target column으로 `price`를 지정해 regressor가 habitat의 가격을 예측하도록 합니다.

    let regressor = try MLRegressor(trainingData: regressorTable, targetColumn: "price")
    

training 중 [Create ML](https://developer.apple.com/documentation/createml)
은 training phase에서 model 진행 상황을 검증하는 데 사용할 training data의 일부를 자동으로 분리합니다. training process는 validation data를 기준으로 model 성능을 판단합니다. validation 정확도에 따라 training algorithm은 model 내부 값을 조정하거나 정확도가 충분히 높으면 training process를 중단할 수도 있습니다. 분할은 무작위로 이뤄지므로 model을 training할 때마다 결과가 달라질 수 있습니다.

### [regressor evaluation](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Evaluate-the-regressor)

regressor가 training과 validation 동안 얼마나 정확하게 동작했는지 보려면 playground가 [`trainingMetrics`](https://developer.apple.com/documentation/createml/mlregressor/trainingmetrics)
와 [`validationMetrics`](https://developer.apple.com/documentation/createml/mlregressor/validationmetrics)
 property의 [`maximumError`](https://developer.apple.com/documentation/createml/mlregressormetrics/maximumerror)
 property를 가져옵니다.

    /// prediction과 기대 값 사이 거리 중 가장 큰 값입니다.
    let worstTrainingError = regressor.trainingMetrics.maximumError
    let worstValidationError = regressor.validationMetrics.maximumError
    

playground는 evaluation data table을 전달해 regressor 성능을 evaluation합니다.

    /// regressor를 evaluation합니다.
    let regressorEvalutation = regressor.evaluation(on: regressorEvaluationTable)
    
    
    /// prediction과 기대 값 사이 거리 중 가장 큰 값입니다.
    let worstEvaluationError = regressorEvalutation.maximumError
    

regressor의 evaluation 성능이 충분하지 않다면 다음이 필요할 수 있습니다:

*   더 많은 data row로 다시 training합니다.
    
*   다른 구체적인 regressor type을 선택합니다([`MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)
    .
    
*   다른 조정을 수행합니다([model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)
    ).
    

### [classifier training](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Train-the-classifier)

playground는 habitat의 용도를 예측하도록 classifier를 training합니다. 이를 위해 training data table의 `purpose` column을 classifier target으로 사용합니다.

    let classifier = try MLClassifier(trainingData: classifierTrainingTable,
                                      targetColumn: "purpose")
    

classifier는 training data에 들어 있는 값만 예측할 수 있으며, training data 범위를 넘는 숫자 값도 예측할 수 있는 regressor와 다릅니다. 예를 들어 playground의 classifier는 `purpose` column에 있는 값이 `"power"`, `"farm"`, `"general"`뿐이므로 이 값만 예측할 수 있습니다.

### [classifier evaluation](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Evaluate-the-classifier)

classifier가 training과 validation 동안 얼마나 정확하게 동작했는지 보려면 playground가 [`trainingMetrics`](https://developer.apple.com/documentation/createml/mlclassifier/trainingmetrics)
와 [`validationMetrics`](https://developer.apple.com/documentation/createml/mlclassifier/validationmetrics)
 property의 [`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
 property를 가져옵니다.

    /// classifier training accuracy를 백분율로 나타냅니다.
    let trainingError = classifier.trainingMetrics.classificationError
    let trainingAccuracy = (1.0 - trainingError) * 100
    
    
    /// classifier validation accuracy를 백분율로 나타냅니다.
    let validationError = classifier.validationMetrics.classificationError
    let validationAccuracy = (1.0 - validationError) * 100
    

regressor와 마찬가지로 playground는 evaluation data table을 전달해 classifier 성능을 evaluation합니다.

    /// classifier를 evaluation합니다.
    let classifierEvaluation = classifier.evaluation(on: classifierEvaluationTable)
    
    
    /// classifier evaluation accuracy를 백분율로 나타냅니다.
    let evaluationError = classifierEvaluation.classificationError
    let evaluationAccuracy = (1.0 - evaluationError) * 100
    

classifier의 evaluation 성능이 충분하지 않다면 다음이 필요할 수 있습니다:

*   더 많은 data row로 다시 training합니다.
    
*   다른 구체적인 classifier type을 선택합니다([`MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)
    ).
    
*   다른 조정을 수행합니다([model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)
    ).
    

### [model 저장](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Save-the-model)

model 성능에 만족하면 나중에 app에서 사용할 수 있도록 file로 저장합니다. playground는 [`write(to:metadata:)`](https://developer.apple.com/documentation/createml/mlregressor/write(to:metadata:))
 method를 사용해 metadata와 함께 price regressor를 사용자 desktop에 저장합니다.

    let regressorMetadata = MLModelMetadata(author: "Maria Ruiz",
                                            shortDescription: "Predicts the price of a habitat on Mars.",
                                            version: "1.0")
    /// Save the trained regressor model to the Desktop.
    try regressor.write(to: desktopPath.appendingPathComponent("MarsHabitatPricer.mlmodel"),
                        metadata: regressorMetadata)
    

playground는 같은 방식으로 purpose classifier도 사용자 desktop에 저장합니다.

    let classifierMetadata = MLModelMetadata(author: "Maria Ruiz",
                                             shortDescription: "Predicts the purpose of a habitat on Mars.",
                                             version: "1.0")
    
    
    /// Save the trained classifier model to the Desktop.
    try classifier.write(to: desktopPath.appendingPathComponent("MarsHabitatPurposeClassifier.mlmodel"),
                         metadata: classifierMetadata)
    

### [model을 app에 추가](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Add-the-model-to-an-app)

model을 app에 추가하는 방법은 [Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/CoreML/integrating-a-core-ml-model-into-your-app)
을 참고합니다.

[같이 보기](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#see-also)

-----------------------------------------------------------------------------------------------------------

### [data table 만들기](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data#Creating-a-data-table)

[`init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws`](https://developer.apple.com/documentation/createml/mldatatable/init(contentsof:options:))

import한 JSON 또는 CSV file로 data table을 만듭니다.

[`init(dictionary: [String : any MLDataValueConvertible]) throws`](https://developer.apple.com/documentation/createml/mldatatable/init(dictionary:))

column 이름과 data 값 dictionary로 data table을 만듭니다.

[`init(namedColumns: [String : MLUntypedColumn]) throws`](https://developer.apple.com/documentation/createml/mldatatable/init(namedcolumns:))

column 이름과 untyped column dictionary로 data table을 만듭니다.

[`init()`](https://developer.apple.com/documentation/createml/mldatatable/init())

row와 column이 없는 빈 table을 만듭니다.

[`struct ParsingOptions`](https://developer.apple.com/documentation/createml/mldatatable/parsingoptions)

comma-separated values(CSV) file을 machine learning model용 data table로 parsing하는 옵션입니다.

현재 페이지는 tabular data로 model 만들기입니다
