---
title: "averagePrecision | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.140884+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLObjectDetectorMetrics](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)
    
*   averagePrecision

instance property

averagePrecision
================

서로 다른 threshold에서의 average precision dictionary 두 개입니다.

macOS 10.15+

    var averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double]) { get }

[Parameters](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision#parameters)

---------------------------------------------------------------------------------------------------------------------

`variedIoU`

intersection-over-union metric에서 50%부터 95%까지 다양한 threshold에 대한 모든 class의 average precision 값입니다. dictionary의 key는 각 object의 label입니다.

`IoU50`

intersection-over-union metric의 50% threshold에서 모든 class의 average precision 값입니다. dictionary의 key는 각 object의 label입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision#see-also)

-----------------------------------------------------------------------------------------------------------------

### [model 평가하기](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision#Assessing-the-model)

[`var meanAveragePrecision: (variedIoU: Double, IoU50: Double)`](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/meanaverageprecision)

서로 다른 threshold에서의 mean-average precision 두 개입니다.

현재 페이지: averagePrecision
