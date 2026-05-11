---
title: "init(trainingData:parameters:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/init(trainingdata:parameters:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133433+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/init(trainingdata:parameters:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   init(trainingData:parameters:)

이니셜라이저

init(trainingData:parameters:)
==============================

data source로 표현된 training dataset으로 style transfer model을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    init(
        trainingData: MLStyleTransfer.DataSource,
        parameters: MLStyleTransfer.Model파라미터 = .init()
    ) throws

[파라미터](https://developer.apple.com/documentation/createml/mlstyletransfer/init(trainingdata:parameters:)#parameters)

---------------------------------------------------------------------------------------------------------------------------

`trainingData`

data source로 표현된 style image와 content image입니다.

`parameters`

An [`MLStyleTransfer.Model파라미터`](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters)
instance로, training session용 model을 구성할 때 사용합니다.

현재 페이지는 init(trainingData:parameters:)입니다
