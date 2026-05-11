---
title: "prediction(from:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.134297+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   prediction(from:)

instance method

prediction(from:)
=================

image에 대한 hand pose prediction을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    func prediction(from image: URL) throws -> [(label: String, confidence: Double)]

[parameter](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)#parameters)

-------------------------------------------------------------------------------------------------------------------

`image`

image file URL입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)#return-value)

-----------------------------------------------------------------------------------------------------------------------

prediction tuple 배열입니다.

[논의](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)#discussion)

-------------------------------------------------------------------------------------------------------------------

각 prediction은 classification label과 그 label에 대한 model의 confidence를 짝지은 tuple 배열로 구성됩니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)#see-also)

---------------------------------------------------------------------------------------------------------------

### [hand pose classifier 테스트](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:)#Testing-a-hand-pose-classifier)

[`func predictions(from: [URL]) throws -> [[(label: String, confidence: Double)]]`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:))

URL 배열의 각 image에 대한 hand pose prediction 배열을 생성합니다.

현재 페이지는 prediction(from:)입니다
