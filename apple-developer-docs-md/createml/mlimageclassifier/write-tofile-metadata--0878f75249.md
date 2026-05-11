---
title: "write(toFile:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.134541+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLImageClassifier](https://developer.apple.com/documentation/createml/mlimageclassifier)
    
*   write(toFile:metadata:)

instance method

write(toFile:metadata:)
=======================

image classifier를 file path에 Core ML model file로 export합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+visionOS 1.0+

    func write(
        toFile path: String,
        metadata: MLModelMetadata? = nil
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:)#parameters)

----------------------------------------------------------------------------------------------------------------------

`path`

model을 저장할 file system 위치 path입니다.

`metadata`

export한 model file에 포함할 설명 정보입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:)#see-also)

------------------------------------------------------------------------------------------------------------------

### [Saving an image classifier](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:)#Saving-an-image-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:))

image classifier를 file system의 위치에 Core ML model file로 export합니다.

현재 페이지: write(toFile:metadata:)
