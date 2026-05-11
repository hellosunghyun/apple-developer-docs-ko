---
title: "confusionDataFrame | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.135567+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLClassifierMetrics](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
    
*   confusionDataFrame

instance property

confusionDataFrame
==================

각 class의 실제 label과 예측된 label을 비교하는 data frame입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+macOS 14.0+tvOS 17.0+visionOS 1.0+

    var confusionDataFrame: DataFrame { get }

[논의](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe#discussion)

-------------------------------------------------------------------------------------------------------------------

confusion data frame은 category 사이에서 example이 어떻게 잘못 label되었는지 설명합니다. 각 row에는 실제 label, 예측된 label, 그리고 그 조합에 해당하는 instance 수가 들어 있습니다. 예를 들어 아래 표는 “business”가 113번 “business”로 올바르게 label되었고, 2번은 “entertainment”로 혼동되었음을 보여 줍니다.

![실제 label과 예측된 label의 row를 포함하는 confusion matrix 형식을 보여 주는 표](https://docs-assets.developer.apple.com/published/c9b7730d227217804dd88adf475e1069/MLClassifierMetrics-confusion-1%402x.png)

[같이 보기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe#see-also)

---------------------------------------------------------------------------------------------------------------

### [model 이해하기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe#Understanding-the-model)

[`var classificationError: Double`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)

잘못 label된 example의 비율입니다.

[`var precisionRecall: MLDataTable`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)

각 class의 precision 및 recall 백분율을 나열한 data table입니다.

[`var confusion: MLDataTable`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion)

각 classification category의 실제 label과 예측된 label을 비교하는 table입니다.

[`var precisionRecallDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecalldataframe)

각 class의 precision 및 recall 백분율을 나열한 data frame입니다.

현재 페이지: confusionDataFrame
