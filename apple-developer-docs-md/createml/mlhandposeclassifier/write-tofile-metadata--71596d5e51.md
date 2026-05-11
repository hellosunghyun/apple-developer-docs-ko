---
title: "write(toFile:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.141562+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier)
    
*   write(toFile:metadata:)

instance method

write(toFile:metadata:)
=======================

hand pose classifier를 Core ML model file로 export합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    func write(
        toFile path: String,
        metadata: MLModelMetadata? = nil
    ) throws

[파라미터](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:)#parameters)

-------------------------------------------------------------------------------------------------------------------------

`path`

file-system path입니다.

`metadata`

model의 설명, 작성자, version, license 정보입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:)#see-also)

---------------------------------------------------------------------------------------------------------------------

### [hand pose classifier 저장](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(tofile:metadata:)#Saving-a-hand-pose-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:))

hand pose classifier를 CoreML model file로 export합니다.

현재 페이지는 write(toFile:metadata:)입니다
