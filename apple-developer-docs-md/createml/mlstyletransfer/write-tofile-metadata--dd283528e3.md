---
title: "write(toFile:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.139885+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   write(toFile:metadata:)

instance method

write(toFile:metadata:)
=======================

style transfer model을 file path의 Core ML model file로 export합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    func write(
        toFile path: String,
        metadata: MLModelMetadata? = .init()
    ) throws

[파라미터](https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:)#parameters)

--------------------------------------------------------------------------------------------------------------------

`path`

model을 저장할 file system 위치 경로입니다.

`metadata`

export한 model file에 포함할 설명 정보입니다.

[관련 항목](https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:)#see-also)

----------------------------------------------------------------------------------------------------------------

### [style transfer model 저장하기](https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:)#Saving-a-style-transfer-model)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:))

style transfer model을 file system 위치의 Core ML model file로 export합니다.

현재 페이지는 write(toFile:metadata:)입니다.
