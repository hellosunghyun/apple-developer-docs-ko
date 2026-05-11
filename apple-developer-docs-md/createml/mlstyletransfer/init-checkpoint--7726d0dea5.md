---
title: "init(checkpoint:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/init(checkpoint:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.136798+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/init(checkpoint:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   init(checkpoint:)

initializer

init(checkpoint:)
=================

training session checkpoint에서 style transfer model을 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    init(checkpoint: MLCheckpoint) throws

[Parameters](https://developer.apple.com/documentation/createml/mlstyletransfer/init(checkpoint:)#parameters)

--------------------------------------------------------------------------------------------------------------

`checkpoint`

style transfer training session의 checkpoint입니다.

[논의](https://developer.apple.com/documentation/createml/mlstyletransfer/init(checkpoint:)#discussion)

--------------------------------------------------------------------------------------------------------------

style transfer model의 training session에서 나온 checkpoint는 [`phase`](https://developer.apple.com/documentation/createml/mlcheckpoint/phase)
property가 [`MLPhase.training`](https://developer.apple.com/documentation/createml/mlphase/training)
인 경우에만 사용할 수 있습니다.

현재 페이지: init(checkpoint:)
