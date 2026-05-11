---
title: "write(to:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.134052+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   write(to:metadata:)

instance method

write(to:metadata:)
===================

hand pose classifier를 CoreML model file로 export합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    func write(
        to fileURL: URL,
        metadata: MLModelMetadata? = nil
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:)#parameters)

---------------------------------------------------------------------------------------------------------------------

`fileURL`

file-system URL입니다.

`metadata`

model의 description, author, version, license 정보입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:)#see-also)

-----------------------------------------------------------------------------------------------------------------

### [Saving a hand pose classifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:)#Saving-a-hand-pose-classifier)

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:))

hand pose classifier를 Core ML model file로 export합니다.

현재 페이지: write(to:metadata:)
