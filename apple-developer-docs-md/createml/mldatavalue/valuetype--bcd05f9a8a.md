---
title: "MLDataValue.ValueType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mldatavalue/valuetype"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.139131+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLDataValue](https://developer.apple.com/documentation/createml/mldatavalue)
    
*   MLDataValue.ValueType

enum

MLDataValue.ValueType
=====================

`MLDataValue wraps`가 지원하는 기반 type을 설명하는 enum입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    enum ValueType

[주제](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#topics)

------------------------------------------------------------------------------------------

### [지원되는 값](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#Supported-values)

[`case int`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/int)

integer type입니다.

[`case double`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/double)

double type입니다.

[`case string`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/string)

string type입니다.

[`case dictionary`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/dictionary)

dictionary type입니다.

[`case sequence`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/sequence)

sequence type입니다.

[`case multiArray`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/multiarray)

다차원 type입니다.

[`case invalid`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/invalid)

invalid type입니다.

### [data value type 설명하기](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#Describing-a-data-value-type)

[`var description: String`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/description)

data value type의 text 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/debugdescription)

debugging 출력에 적합한 data value type의 text 표현입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/customdebugstringconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mldatavalue/valuetype/customstringconvertible-implementations)

[관계](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#relationships)

--------------------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    

[관련 항목](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#see-also)

----------------------------------------------------------------------------------------------

### [type 확인하기](https://developer.apple.com/documentation/createml/mldatavalue/valuetype#Inspecting-the-type)

[`var type: MLDataValue.ValueType`](https://developer.apple.com/documentation/createml/mldatavalue/type)

data value가 wrap하는 기반 값의 종류입니다.

현재 페이지: MLDataValue.ValueType
