---
title: "predictions(from:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.134162+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   predictions(from:)

instance method

predictions(from:)
==================

URL array의 각 image에 대한 hand pose prediction array를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    func predictions(from images: [URL]) throws -> [[(label: String, confidence: Double)]]

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)#parameters)

--------------------------------------------------------------------------------------------------------------------

`images`

image file URL array입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)#return-value)

------------------------------------------------------------------------------------------------------------------------

prediction tuple array들의 array입니다.

[논의](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)#discussion)

--------------------------------------------------------------------------------------------------------------------

각 prediction은 분류 label과 그 label에 대한 model의 confidence를 짝지은 tuple array로 구성됩니다. 이 method는 prediction array의 array를 반환하며, 바깥 array의 각 element는 `images`의 해당 URL element에 대한 prediction입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)#see-also)

----------------------------------------------------------------------------------------------------------------

### [Testing a hand pose classifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:)#Testing-a-hand-pose-classifier)

[`func prediction(from: URL) throws -> [(label: String, confidence: Double)]`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:))

image에 대한 hand pose prediction을 생성합니다.

현재 페이지는 predictions(from:)입니다
