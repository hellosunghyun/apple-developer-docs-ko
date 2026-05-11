---
title: "MLDataValue | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mldatavalue"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132138+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mldatavalue#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLDataValue

enum

MLDataValue
===========

data table의 cell 값입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    enum MLDataValue

[개요](https://developer.apple.com/documentation/createml/mldatavalue#overview)

------------------------------------------------------------------------------------

[`MLDataValue`](https://developer.apple.com/documentation/createml/mldatavalue)
enum은 table에 training data를 저장할 때 사용하는 기본 type입니다. classifier는 evaluation metric 같은 정보를 저장할 때 data value를 사용합니다. data value는 Create ML에서 사용할 수 있는 모든 data type을 감쌉니다.

`data value` 안의 실제 정보에 접근하려면 type의 enum case에 대응하는 property를 사용하면 됩니다. data value wrapper에 어떤 kind의 값이 들어 있는지 확실하지 않다면 switch 문으로 값을 unwrap하거나 [`type`](https://developer.apple.com/documentation/createml/mldatavalue/type)
property 값을 확인합니다.

[주제](https://developer.apple.com/documentation/createml/mldatavalue#topics)

--------------------------------------------------------------------------------

### [type과 data value 사이 변환하기](https://developer.apple.com/documentation/createml/mldatavalue#Converting-between-types-and-data-values)

[`protocol MLDataValueConvertible`](https://developer.apple.com/documentation/createml/mldatavalueconvertible)

data value로, 그리고 data value에서 자신을 변환할 수 있는 type입니다.

### [data value 만들기](https://developer.apple.com/documentation/createml/mldatavalue#Creating-a-data-value)

[`case int(Int)`](https://developer.apple.com/documentation/createml/mldatavalue/int(_:))

integer 값입니다.

[`case double(Double)`](https://developer.apple.com/documentation/createml/mldatavalue/double(_:))

double 값입니다.

[`case string(String)`](https://developer.apple.com/documentation/createml/mldatavalue/string(_:))

string 값입니다.

[`case dictionary(MLDataValue.DictionaryType)`](https://developer.apple.com/documentation/createml/mldatavalue/dictionary(_:))

이름이 지정된 data value의 dictionary입니다.

[`case sequence(MLDataValue.SequenceType)`](https://developer.apple.com/documentation/createml/mldatavalue/sequence(_:))

data value의 sequence입니다.

[`case multiArray(MLDataValue.MultiArrayType)`](https://developer.apple.com/documentation/createml/mldatavalue/multiarray(_:))

data value의 다차원 array입니다.

### [type 살펴보기](https://developer.apple.com/documentation/createml/mldatavalue#Inspecting-the-type)

[`var type: MLDataValue.ValueType`](https://developer.apple.com/documentation/createml/mldatavalue/type)

data value가 감싸는 실제 값의 kind입니다.

[`enum ValueType`](https://developer.apple.com/documentation/createml/mldatavalue/valuetype)

`MLDataValue wraps`가 지원하는 실제 type을 설명하는 enum입니다.

### [numeric 값 접근하기](https://developer.apple.com/documentation/createml/mldatavalue#Accessing-numeric-values)

[`var intValue: Int?`](https://developer.apple.com/documentation/createml/mldatavalue/intvalue)

실제 integer 값입니다.

[`var doubleValue: Double?`](https://developer.apple.com/documentation/createml/mldatavalue/doublevalue)

실제 double 값입니다.

### [string 값 접근하기](https://developer.apple.com/documentation/createml/mldatavalue#Accessing-string-values)

[`var stringValue: String?`](https://developer.apple.com/documentation/createml/mldatavalue/stringvalue)

실제 string 값입니다.

### [dictionary 값 접근하기](https://developer.apple.com/documentation/createml/mldatavalue#Accessing-dictionary-values)

[`var dictionaryValue: MLDataValue.DictionaryType?`](https://developer.apple.com/documentation/createml/mldatavalue/dictionaryvalue)

실제 dictionary입니다.

[`struct DictionaryType`](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype)

이름이 지정된 data value의 dictionary입니다.

### [array 값 접근하기](https://developer.apple.com/documentation/createml/mldatavalue#Accessing-array-values)

[`var sequenceValue: MLDataValue.SequenceType?`](https://developer.apple.com/documentation/createml/mldatavalue/sequencevalue)

실제 sequence입니다.

[`struct SequenceType`](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype)

data value의 sequence입니다.

[`var multiArrayValue: MLDataValue.MultiArrayType?`](https://developer.apple.com/documentation/createml/mldatavalue/multiarrayvalue)

실제 다차원 array입니다.

[`struct MultiArrayType`](https://developer.apple.com/documentation/createml/mldatavalue/multiarraytype)

data value의 다차원 array입니다.

### [data value 비교하기](https://developer.apple.com/documentation/createml/mldatavalue#Comparing-data-values)

[`static func == (MLDataValue, MLDataValue) -> Bool`](https://developer.apple.com/documentation/createml/mldatavalue/==(_:_:))

두 data value가 같은 실제 값을 감싸고 있는지 나타내는 Boolean 값을 반환합니다.

### [data value 설명하기](https://developer.apple.com/documentation/createml/mldatavalue#Describing-a-data-value)

[`var description: String`](https://developer.apple.com/documentation/createml/mldatavalue/description)

data value의 텍스트 표현입니다.

[`var debugDescription: String`](https://developer.apple.com/documentation/createml/mldatavalue/debugdescription)

debugging 중 출력하기에 적합한 data value의 텍스트 표현입니다.

### [error 처리하기](https://developer.apple.com/documentation/createml/mldatavalue#Handling-errors)

[`case invalid`](https://developer.apple.com/documentation/createml/mldatavalue/invalid)

유효하지 않은 값입니다.

[`var isValid: Bool`](https://developer.apple.com/documentation/createml/mldatavalue/isvalid)

data value가 유효한지 나타내는 Boolean 값입니다.

### [기본 구현](https://developer.apple.com/documentation/createml/mldatavalue#Default-Implementations)

[API Reference: CustomDebugStringConvertible 구현](https://developer.apple.com/documentation/createml/mldatavalue/customdebugstringconvertible-implementations)

[API Reference: CustomStringConvertible 구현](https://developer.apple.com/documentation/createml/mldatavalue/customstringconvertible-implementations)

[API Reference: Equatable 구현](https://developer.apple.com/documentation/createml/mldatavalue/equatable-implementations)

[관계](https://developer.apple.com/documentation/createml/mldatavalue#relationships)

----------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mldatavalue#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    

[같이 보기](https://developer.apple.com/documentation/createml/mldatavalue#see-also)

------------------------------------------------------------------------------------

### [tabular data](https://developer.apple.com/documentation/createml/mldatavalue#Tabular-data)

[`struct MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)

machine learning model을 training하거나 평가하기 위한 data table입니다.

[API Reference: data visualization 항목](https://developer.apple.com/documentation/createml/data-visualizations)

playground에서 data table과 column의 image를 렌더링합니다.

현재 페이지: MLDataValue
