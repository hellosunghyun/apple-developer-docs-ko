---
title: "MLDataValue.DictionaryType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.138757+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLDataValue](https://developer.apple.com/documentation/createml/mldatavalue)
    
*   MLDataValue.DictionaryType

struct

MLDataValue.DictionaryType
==========================

이름이 지정된 data value의 dictionary입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    struct DictionaryType

[주제](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#topics)

-----------------------------------------------------------------------------------------------

### [Dictionary Type 생성하기](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#Creating-a-dictionary-type)

[`init([MLDataValue : MLDataValue])`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(_:))

[`init<S>(uniqueKeysWithValues: S)`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(uniquekeyswithvalues:))

[`typealias Key`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/key)

[`typealias Value`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/value)

### [Element 가져오기](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#Getting-an-element)

[`subscript(MLDataValue.DictionaryType.Key) -> MLDataValue.DictionaryType.Value?`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/subscript(_:))

### [기본 구현](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#Default-Implementations)

[API Reference\
\
MLDataValueConvertible Implementations](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/mldatavalueconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#relationships)

-------------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#conforms-to)

*   [`Collection`](https://developer.apple.com/documentation/Swift/Collection)
    
*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`MLDataValueConvertible`](https://developer.apple.com/documentation/createml/mldatavalueconvertible)
    
*   [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence)
    

[같이 보기](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#see-also)

---------------------------------------------------------------------------------------------------

### [Dictionary Value 접근하기](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype#Accessing-dictionary-values)

[`var dictionaryValue: MLDataValue.DictionaryType?`](https://developer.apple.com/documentation/createml/mldatavalue/dictionaryvalue)

기본 dictionary입니다.

현재 페이지: MLDataValue.DictionaryType
