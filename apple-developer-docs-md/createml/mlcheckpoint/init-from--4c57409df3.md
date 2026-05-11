---
title: "init(from:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.149516+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCheckpoint](https://developer.apple.com/documentation/createml/mlcheckpoint)
    
*   init(from:)

initializer

init(from:)
===========

decoder에서 decode하여 새 checkpoint를 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    init(from decoder: any Decoder) throws

[Parameters](https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:)#parameters)

-----------------------------------------------------------------------------------------------------

`decoder`

data를 읽어올 decoder입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:)#see-also)

-------------------------------------------------------------------------------------------------

### [checkpoint 인코딩 및 디코딩하기](https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:)#Encoding-and-decoding-a-checkpoint)

[`func encode(to: any Encoder) throws`](https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:))

checkpoint를 encoder에 encode합니다.

현재 페이지: init(from:)
