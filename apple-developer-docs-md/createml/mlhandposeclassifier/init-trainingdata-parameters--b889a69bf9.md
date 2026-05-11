---
title: "init(trainingData:parameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/init(trainingdata:parameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.138047+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/init(trainingdata:parameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   init(trainingData:parameters:)

initializer

init(trainingData:parameters:)
==============================

synchronous training session을 시작해 hand pose classifier를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    init(
        trainingData: MLHandPoseClassifier.DataSource,
        parameters: MLHandPoseClassifier.ModelParameters = ModelParameters()
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/init(trainingdata:parameters:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------

`trainingData`

[`MLHandPoseClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource)
 instance입니다.

`parameters`

training session용 model을 구성할 때 사용하는 [`MLHandPoseClassifier.ModelParameters`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct)
 instance입니다.

현재 페이지: init(trainingData:parameters:)
