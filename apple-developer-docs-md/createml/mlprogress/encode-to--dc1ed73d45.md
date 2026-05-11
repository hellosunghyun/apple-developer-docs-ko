---
title: "encode(to:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlprogress/encode(to:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.158886+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlprogress/encode(to:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLProgress](https://developer.apple.com/documentation/createml/mlprogress)
    
*   encode(to:)

instance method

encode(to:)
===========

progress 값을 지정한 encoder에 encoding합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    func encode(to encoder: any Encoder) throws

[Parameters](https://developer.apple.com/documentation/createml/mlprogress/encode(to:)#parameters)

---------------------------------------------------------------------------------------------------

`encoder`

data를 기록할 encoder입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlprogress/encode(to:)#see-also)

-----------------------------------------------------------------------------------------------

### [session progress encoding 및 decoding](https://developer.apple.com/documentation/createml/mlprogress/encode(to:)#Encoding-and-decoding-a-sessions-progress)

[`init(from: any Decoder) throws`](https://developer.apple.com/documentation/createml/mlprogress/init(from:))

지정한 decoder에서 decoding해 progress instance를 만듭니다.

현재 페이지: encode(to:)
