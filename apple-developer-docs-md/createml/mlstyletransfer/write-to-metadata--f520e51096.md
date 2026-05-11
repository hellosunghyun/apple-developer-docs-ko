---
title: "write(to:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.137696+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer)
    
*   write(to:metadata:)

instance method

write(to:metadata:)
===================

style transfer model을 file system의 지정한 위치에 Core ML model file로 내보냅니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+visionOS 1.0+

    func write(
        to fileURL: URL,
        metadata: MLModelMetadata? = .init()
    ) throws

[parameter](https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:)#parameters)

----------------------------------------------------------------------------------------------------------------

`fileURL`

model을 저장할 file system 위치의 URL입니다.

`metadata`

내보낸 model file에 포함할 설명 정보입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:)#see-also)

------------------------------------------------------------------------------------------------------------

### [style transfer model 저장하기](https://developer.apple.com/documentation/createml/mlstyletransfer/write(to:metadata:)#Saving-a-style-transfer-model)

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlstyletransfer/write(tofile:metadata:))

style transfer model을 해당 file path에 Core ML model file로 내보냅니다.

현재 페이지: write(to:metadata:)
