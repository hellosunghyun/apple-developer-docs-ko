---
title: "Model 정확도 향상 | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132342+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   Model 정확도 향상

Article

Model 정확도 향상
===============================

machine learning model의 성능을 조정할 때 metrics를 사용합니다.

[개요](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#Overview)

--------------------------------------------------------------------------------------------------------

model을 평가하고 개선하려면 먼저 여러 data set 전반의 성능을 확인합니다. 각 dataset의 metrics를 보면 어떤 변경이 model 정확도에 가장 큰 영향을 주는지 판단할 수 있습니다.

하나의 metric만으로는 model 성능 전체를 파악할 수 없습니다. model을 개선하려면 training, validation, testing data set 간의 metrics를 비교합니다([`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
 or [`MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)
에 따라 model type이 달라집니다). 예를 들어 [Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)
 article에서 다루는 accuracy는 각 data set의 [`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
 metric에서 계산됩니다.

model을 만든 뒤 testing data를 로드하면 code로도 이 값들에 접근할 수 있습니다:

    print("Training Metrics\n", model.trainingMetrics)
    print("Validation Metrics\n", model.validationMetrics)
    
    
    let evaluationMetrics = model.evaluation(on: testData)
    print("Evaluation Metrics\n", evaluationMetrics)
    

이 경우 [`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
, [`precisionRecall`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)
, and [`confusion`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)
 같은 classifier용 metric과 [`maximumError`](https://developer.apple.com/documentation/createml/mlregressormetrics/maximumerror)
 and [`rootMeanSquaredError`](https://developer.apple.com/documentation/createml/mlregressormetrics/rootmeansquarederror)
 같은 regressor용 metric이 출력됩니다. 각 data set의 값을 보고 model에서 개선이 필요한 부분을 판단합니다.

### [Model의 training accuracy 높이기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#Improve-Your-Models-Training-Accuracy)

model의 training accuracy가 낮다면 현재 model configuration이 data의 복잡성을 포착하지 못한다는 뜻입니다.

training parameter를 조정해 보십시오. image data를 다룰 때는 `MLImageClassifierBuilder` playground UI에서 최대 iteration 수를 두 배로 늘립니다(기본값은 10).

![MLImageClassifierBuilder playground UI에서 최대 iteration 수를 20으로 설정한 화면.](https://docs-assets.developer.apple.com/published/d5d3381985df49dadf5207e31a918ee5/improving-your-model-s-accuracy-1%402x.png)

natural language data라면 다른 underlying algorithm을 시도합니다([`MLTextClassifier.ModelAlgorithmType`](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype)
 참고). 더 일반적인 작업에서는 [`MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)
 가 결정하는 type 대신 다른 underlying model을 사용합니다(_Supporting Classifier Types_ 참고). [`MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)
 도 마찬가지입니다(_Supporting Regressor Types_ 참고).

### [Model의 validation accuracy 높이기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#Improve-Your-Models-Validation-Accuracy)

validation set에서 model accuracy가 낮거나 model을 training할 때마다 큰 폭으로 오르내린다면 더 많은 data가 필요합니다. 이미 수집한 example에서 추가 input data를 생성할 수 있는데, 이를 _data augmentation_이라고 합니다. image data에서는 crop, rotation, blur, exposure adjustment 같은 작업을 조합해 하나의 image를 여러 example로 만들 수 있습니다.

![코끼리 image 하나에 crop, rotate, blur, expose 같은 augmentation을 적용해 여러 image가 되는 모습을 보여 주는 그림.](https://docs-assets.developer.apple.com/published/8ebb9a01db59e838cba566133acf4ffe/improving-your-model-s-accuracy-2%402x.png)

data가 충분히 많아도 validation accuracy가 training accuracy보다 여전히 크게 낮을 수 있습니다. 이 경우 model은 \_overfitting\_ 상태이며, 다른 example에는 일반적으로 적용되지 않는 training set의 세부 사항을 너무 많이 학습하고 있다는 뜻입니다. 이런 경우에는 model이 training data를 과도하게 학습하지 않도록 training iteration 수를 줄여야 합니다.

### [Model의 evaluation accuracy 높이기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#Improve-Your-Models-Evaluation-Accuracy)

testing data에서의 model accuracy가 training 또는 validation accuracy보다 낮다면, 보통 model을 training한 data와 evaluation에 제공한 testing data 사이에 의미 있는 차이가 있다는 뜻입니다.

예를 들어 [`MLImageClassifier`](https://developer.apple.com/documentation/createml/mlimageclassifier)
 를 실내 고양이 image로 많이 training했는데 testing은 실외 고양이 image만 사용했다고 가정해 보겠습니다. 조명, exposure, background 차이 때문에 testing data에서 좋은 결과가 나오기 어렵습니다. 사람에게는 분명해 보이는 image 차이도 충분한 training data가 없으면 model이 구분하기 어렵습니다.

이 문제를 해결하려면 training set에 더 다양한 data를 포함해야 합니다. 일반적으로 example이 많을수록 성능이 높아지지만, testing data만큼 다양한 example을 model에 보여 주는 것도 중요합니다.

[관련 항목](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#see-also)

--------------------------------------------------------------------------------------------------------

### [Model 정확도](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy#Model-accuracy)

[`struct MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)

classifier 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLRegressorMetrics`](https://developer.apple.com/documentation/createml/mlregressormetrics)

regressor 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLWordTaggerMetrics`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)

word tagger 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLRecommenderMetrics`](https://developer.apple.com/documentation/createml/mlrecommendermetrics)

recommender 성능을 평가할 때 사용하는 metrics입니다.

[`struct MLObjectDetectorMetrics`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)

object detector 성능을 평가할 때 사용하는 metrics입니다.

현재 페이지는 Model 정확도 향상
