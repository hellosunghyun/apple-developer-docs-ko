---
title: "init(from:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(from:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.154774+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(from:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLDataValue](https://developer.apple.com/documentation/createml/mldatavalue)
    
*   *   [MLDataValue](https://developer.apple.com/documentation/createml/mldatavalue)
        
*   [MLDataValue.DictionaryType](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype)
    
*   init(from:)

이니셜라이저

init(from:)
===========

다른 dictionary에서 data-value dictionary를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    init?(from dataValue: MLDataValue)

[설명](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(from:)#discussion)

-------------------------------------------------------------------------------------------------------------------

이 이니셜라이저를 사용해 다른 data-value dictionary instance에서 [`MLDataValue.DictionaryType`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype)
을 생성합니다. [`dictionaryValue`](https://developer.apple.com/documentation/createml/mldatavalue/dictionaryvalue)
에서 `nil`이 아닌 값을 가져오거나 [`type`](https://developer.apple.com/documentation/createml/mldatavalue/type)
property를 확인해 data value의 underlying type을 확인할 수 있습니다.

현재 페이지는 init(from:)입니다
