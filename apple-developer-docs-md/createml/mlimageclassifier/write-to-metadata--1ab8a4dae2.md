---
title: "write(to:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.134659+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLImageClassifier](https://developer.apple.com/documentation/createml/mlimageclassifier)
    
*   write(to:metadata:)

instance method

write(to:metadata:)
===================

image classifier를 Core ML model file로 export해 file system의 위치에 저장합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+visionOS 1.0+

    func write(
        to fileURL: URL,
        metadata: MLModelMetadata? = nil
    ) throws

[parameter](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:)#parameters)

------------------------------------------------------------------------------------------------------------------

`fileURL`

model을 저장할 file system 위치 URL입니다.

`metadata`

export된 model file에 포함할 설명용 정보입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:)#see-also)

--------------------------------------------------------------------------------------------------------------

### [image classifier 저장하기](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:)#Saving-an-image-classifier)

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:))

image classifier를 Core ML model file로 export해 file path에 저장합니다.

현재 페이지: write(to:metadata:)
