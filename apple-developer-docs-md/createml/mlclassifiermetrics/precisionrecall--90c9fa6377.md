---
title: "precisionRecall | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.135262+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLClassifierMetrics](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
    
*   precisionRecall

instance property

precisionRecall
===============

각 class의 precision 및 recall 백분율을 나열한 data table입니다.

iOS 15.0–17.0DeprecatediPadOS 15.0–17.0DeprecatedMac Catalyst 15.0–17.0DeprecatedmacOS 10.14–14.0DeprecatedtvOS 16.0–17.0DeprecatedvisionOS 1.0+

    var precisionRecall: MLDataTable { get }

[언급된 문서](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall#mentions)

----------------------------------------------------------------------------------------------------------------

[Model 정확도 높이기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[논의](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall#discussion)

----------------------------------------------------------------------------------------------------------------

precision과 recall은 각 class별로 계산하는 metric입니다. 이 둘을 함께 보면 label을 너무 넓게 적용하는 경우와 해당 label의 example을 놓치는 경우 사이의 tradeoff를 파악할 수 있습니다.

precision은 model이 주어진 category에 적절할 때만 label을 얼마나 정확히 적용했는지를 나타냅니다. 즉 false positive가 적을수록 precision이 높습니다.

recall은 model이 category와 관련된 모든 example을 얼마나 잘 찾아냈는지를 나타냅니다. 즉 false negative가 적을수록 recall이 높습니다.

![](https://docs-assets.developer.apple.com/published/7855eb855befe83b05e51d97fbcc6a95/MLClassifierMetrics-precisionRecall-1%402x.png)

아래 그림은 각 example이 “Elephant” category의 precision 및 recall 백분율에 어떻게 반영되는지 보여줍니다.

![Elephant category의 실제 label과 예측 label을 보여 주는 표입니다.](https://docs-assets.developer.apple.com/published/d2e3bf7a61ae75d3205a71b3d78cee9d/MLClassifierMetrics-precisionRecall-2%402x.png)

“Elephant”는 true label, 즉 올바른 label로는 한 번만 나타나지만 예측은 두 번 발생합니다. 이 두 번째 예측은 precision 오류입니다. precision과 recall을 보면 [`classificationError`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)
.

보다 model이 어떤 방식으로 실수하는지 훨씬 잘 파악할 수 있습니다.

“Elephant” example이 다른 어떤 category로 label되었는지 확인하려면 [`confusion`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)
 property.

[같이 보기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall#see-also)

------------------------------------------------------------------------------------------------------------

### [model 이해하기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall#Understanding-the-model)

[`var classificationError: Double`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)

잘못 label된 example의 비율입니다.

[`var confusion: MLDataTable`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)

각 classification category의 실제 label과 예측 label을 비교하는 표입니다.

[`var confusionDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe)

각 class의 실제 label과 예측 label을 비교하는 data frame입니다.

[`var precisionRecallDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecalldataframe)

각 class의 precision 및 recall 백분율을 나열한 data frame입니다.

현재 페이지: precisionRecall
