---
title: "write(toFile:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.143090+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   write(toFile:metadata:)

instance method

write(toFile:metadata:)
=======================

word embedding을 지정한 file path에 Core ML model file로 내보냅니다.

macOS 10.15+

    func write(
        toFile path: String,
        metadata: MLModelMetadata? = nil
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:)#parameters)

--------------------------------------------------------------------------------------------------------------------

`path`

model file을 기록할 file system path입니다.

`metadata`

내보낸 model file에 포함할 설명 정보입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:)#see-also)

----------------------------------------------------------------------------------------------------------------

### [word embedding 저장하기](https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:)#Saving-a-word-embedding)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:))

word embedding을 지정한 URL에 Core ML model file로 내보냅니다.

현재 페이지: write(toFile:metadata:)
