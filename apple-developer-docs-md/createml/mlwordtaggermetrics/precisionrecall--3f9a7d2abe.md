---
title: "precisionRecall | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecall"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142587+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecall#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordTaggerMetrics](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)
    
*   *   [MLWordTaggerMetrics](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)
        
*   precisionRecall Deprecated

instance property

precisionRecall
===============

각 category의 precision 및 recall 백분율을 나열한 data table입니다.

macOS 10.14–14.0Deprecated

    var precisionRecall: MLDataTable { get }

[참고 항목](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecall#see-also)

------------------------------------------------------------------------------------------------------------

### [tagger 성능 분석](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecall#Analyzing-the-taggers-performance)

[`var taggingError: Double`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/taggingerror)

잘못 태깅된 example 비율입니다.

[`var confusion: MLDataTable`](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/confusion)

각 tagging category에 대해 실제 label과 예측 label을 비교하는 table입니다.

Deprecated

현재 페이지: precisionRecall
