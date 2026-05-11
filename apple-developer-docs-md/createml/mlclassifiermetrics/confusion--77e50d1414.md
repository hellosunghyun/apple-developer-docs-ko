---
title: "confusion | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.135431+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLClassifierMetrics](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
    
*   confusion

instance property

confusion
=========

각 classification category의 실제 label과 예측 label을 비교한 table입니다.

iOS 15.0–17.0사용 중단iPadOS 15.0–17.0사용 중단Mac Catalyst 15.0–17.0사용 중단macOS 10.14–14.0사용 중단tvOS 16.0–17.0사용 중단visionOS 1.0+

    var confusion: MLDataTable { get }

[언급된 문서](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion#mentions)

----------------------------------------------------------------------------------------------------------

[model 정확도 높이기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)

[설명](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion#discussion)

----------------------------------------------------------------------------------------------------------

confusion data table은 category 사이에서 example이 어떻게 잘못 label되었는지 설명합니다. 각 row에는 가능한 category 조합마다 true label, predicted label, count가 들어 있습니다. 예를 들어 아래 table은 “business”가 113회 올바르게 “business”로 label되었고, “business”가 2회 “entertainment”와 혼동되었다는 것을 보여줍니다.

![true label과 predicted label별 row가 들어 있는 confusion table 형식을 보여 주는 표](https://docs-assets.developer.apple.com/published/c9b7730d227217804dd88adf475e1069/MLClassifierMetrics-confusion-1%402x.png)

model 성능을 더 잘 이해하려면 이 data table을 사용해 주어진 data set에서 model이 어떤 category를 가장 많이 혼동하는지, 즉 어떤 실수를 가장 많이 하는지 확인할 수 있습니다. 예를 들어 아래 code listing은 가장 자주 발생하는 실수를 찾는 방법을 보여줍니다.

    let confusion = model.validationMetrics.confusion
    
    
    // Filter for rows which contain mistakes.
    let errors = confusion[confusion["True Label"] != confusion["Predicted"]]
    let mostCommonError = errors.rows.max { row1, row2 in
        row1["Count", Int.self]! < row2["Count", Int.self]!
    }
print(mostCommonError ?? "confusion table이 비어 있습니다.")
    // ["Predicted": "tech", "True Label": "business", "Count": 9]
    

이 data를 살펴보는 또 다른 유용한 방법은 matrix를 사용해 실제 label과 예측 label을 비교하는 것입니다. [`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
는 matrix 형식을 직접 표시합니다.

    print(model.validationMetrics)
    // ...
    // ******CONFUSION MATRIX******
    // ----------------------------------
    // True\Pred business entertainment politics sport tech
    // business 113 2 3 0 9
    // entertainment 1 183 3 2 3
    // politics 6 8 116 0 3
    // sport 0 6 1 135 3
    // tech 2 7 3 0 129
    // ...
    

이 예시에서 왼쪽 위 count는 business example 113개가 올바르게 “business”로 label되었음을 보여줍니다. 두 번째 열은 business example 2개에 대해 “entertainment”가 예측되었음을 보여줍니다. 두 번째 행은 entertainment example 1개가 “business”로 잘못 label되었음을 보여줍니다.

[관련 항목](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion#see-also)

------------------------------------------------------------------------------------------------------

### [model 이해하기](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusion#Understanding-the-model)

[`var classificationError: Double`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/classificationerror)

잘못 label된 example의 비율입니다.

[`var precisionRecall: MLDataTable`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)

각 class의 precision 및 recall 백분율을 나열한 data table입니다.

[`var confusionDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe)

각 class의 실제 label과 예측 label을 비교한 data frame입니다.

[`var precisionRecallDataFrame: DataFrame`](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecalldataframe)

각 class의 precision 및 recall 백분율을 나열한 data frame입니다.

현재 페이지: confusion
