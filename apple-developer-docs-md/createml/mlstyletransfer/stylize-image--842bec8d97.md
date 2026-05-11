---
title: "stylize(image:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133337+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   stylize(image:)

instance method

stylize(image:)
===============

model이 학습한 style을 image에 적용합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    func stylize(image: CGImage) throws -> CGImage?

[Parameters](https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:)#parameters)

------------------------------------------------------------------------------------------------------------

`image`

model이 자신의 style을 적용할 입력 image입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:)#return-value)

----------------------------------------------------------------------------------------------------------------

model의 style을 적용해 stylize한 `CGImage` type의 image입니다.

[논의](https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:)#discussion)

------------------------------------------------------------------------------------------------------------

현재 페이지: stylize(image:)
