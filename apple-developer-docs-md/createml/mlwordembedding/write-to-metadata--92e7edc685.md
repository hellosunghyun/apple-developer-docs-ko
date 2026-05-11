---
title: "write(to:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.143191+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   write(to:metadata:)

instance method

write(to:metadata:)
===================

word embedding을 지정한 URL에 Core ML model file로 내보냅니다.

macOS 10.15+

    func write(
        to fileURL: URL,
        metadata: MLModelMetadata? = nil
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:)#parameters)

----------------------------------------------------------------------------------------------------------------

`fileURL`

file을 기록할 file system 위치입니다.

`metadata`

내보낸 model file에 포함할 설명 정보입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:)#see-also)

------------------------------------------------------------------------------------------------------------

### [word embedding 저장하기](https://developer.apple.com/documentation/createml/mlwordembedding/write(to:metadata:)#Saving-a-word-embedding)

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlwordembedding/write(tofile:metadata:))

word embedding을 지정한 file path에 Core ML model file로 내보냅니다.

현재 페이지: write(to:metadata:)
