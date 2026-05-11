---
title: "encode(to:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.149408+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLCheckpoint](https://developer.apple.com/documentation/createml/mlcheckpoint)
    
*   encode(to:)

instance method

encode(to:)
===========

checkpoint를 encoder에 encode합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    func encode(to encoder: any Encoder) throws

[parameter](https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:)#parameters)

-----------------------------------------------------------------------------------------------------

`encoder`

data를 기록할 encoder입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:)#see-also)

-------------------------------------------------------------------------------------------------

### [checkpoint encode 및 decode하기](https://developer.apple.com/documentation/createml/mlcheckpoint/encode(to:)#Encoding-and-decoding-a-checkpoint)

[`init(from: any Decoder) throws`](https://developer.apple.com/documentation/createml/mlcheckpoint/init(from:))

decoder에서 decode해 새 checkpoint를 만듭니다.

현재 페이지: encode(to:)
