---
title: "init(averagePrecision:meanAveragePrecision:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/init(averageprecision:meanaverageprecision:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.140796+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/init(averageprecision:meanaverageprecision:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLObjectDetectorMetrics](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics)
    
*   init(averagePrecision:meanAveragePrecision:)

이니셜라이저

init(averagePrecision:meanAveragePrecision:)
============================================

average precision과 mean average precision이 주어졌을 때 object detector용 metrics를 생성합니다.

macOS 10.15+

    init(
        averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double]),
        meanAveragePrecision: (variedIoU: Double, IoU50: Double)
    )

[파라미터](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/init(averageprecision:meanaverageprecision:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------

`averagePrecision`

이 `MLObjectDetectorMetrics`의 `averagePrecision`입니다.

`meanAveragePrecision`

이 `MLObjectDetectorMetrics`의 `meanAveragePrecision`입니다.

[설명](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/init(averageprecision:meanaverageprecision:)#discussion)

-------------------------------------------------------------------------------------------------------------------------------------------------

이 이니셜라이저는 직접 사용하지 않습니다. object detector를 training하거나 evaluation method를 사용할 때 Create ML이 이 이니셜라이저를 사용해 metrics를 생성합니다.

현재 페이지는 init(averagePrecision:meanAveragePrecision:)입니다
