---
title: "MLDataTable | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mldatatable"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132227+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mldatatable#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLDataTable

struct

MLDataTable
===========

machine learning model을 training하거나 평가하기 위한 data table입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    struct MLDataTable

[언급된 문서](https://developer.apple.com/documentation/createml/mldatatable#mentions)

----------------------------------------------------------------------------------------

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

[개요](https://developer.apple.com/documentation/createml/mldatatable#overview)

------------------------------------------------------------------------------------

[`MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)
은 각 row가 관찰 가능한 feature를 가진 entity(아래 예시의 책처럼)를 나타내는 Create ML의 spreadsheet 버전입니다. table의 각 column([`MLDataColumn`](https://developer.apple.com/documentation/createml/mldatacolumn)
 또는 [`MLUntypedColumn`](https://developer.apple.com/documentation/createml/mluntypedcolumn)
)은 책의 제목이나 저자처럼 해당 entity의 관찰 가능한 feature를 나타냅니다.

![책 정보를 담은 table입니다. “Title”, “Author”라는 이름의 column이 있습니다.](https://docs-assets.developer.apple.com/published/64120429043de5dfe14896956373df1d/MLDataTable-1%402x.png)

대부분의 경우 column과 상호작용할 때는 typed [`MLDataColumn`](https://developer.apple.com/documentation/createml/mldatacolumn)
을 사용합니다. 특히 column의 내용을 직접 접근해야 할 때 유용합니다. column의 기반 type이 중요하지 않다면 [`MLUntypedColumn`](https://developer.apple.com/documentation/createml/mluntypedcolumn)
으로도 column과 상호작용할 수 있습니다.

data table을 만든 뒤에는 [`append(contentsOf:)`](https://developer.apple.com/documentation/createml/mldatatable/append(contentsof:))
, [`addColumn(_:named:)`](https://developer.apple.com/documentation/createml/mldatatable/addcolumn(_:named:)-kkbw)
, [`removeColumn(named:)`](https://developer.apple.com/documentation/createml/mldatatable/removecolumn(named:))
 같은 method로 table을 수정할 수 있습니다. 여러 subscript와 [`dropDuplicates()`](https://developer.apple.com/documentation/createml/mldatatable/dropduplicates())
 또는 [`map(_:)`](https://developer.apple.com/documentation/createml/mldatatable/map(_:)-92wrj)
 같은 method를 사용해 data table의 내용을 filter하거나 map하여 새로운 data table이나 새로운 column을 만들 수도 있습니다.

마지막으로 data table 준비가 끝나면 다음 그룹의 model을 training하고 평가하는 데 사용합니다.

*   [`MLRegressor`](https://developer.apple.com/documentation/createml/mlregressor)
    와 그 지원 type 같은 regressor
    
*   [`MLClassifier`](https://developer.apple.com/documentation/createml/mlclassifier)
    와 그 지원 type 같은 classifier
    
*   [`MLTextClassifier`](https://developer.apple.com/documentation/createml/mltextclassifier)
    와 [`MLWordTagger`](https://developer.apple.com/documentation/createml/mlwordtagger)
    같은 natural language processing type
    

[주제](https://developer.apple.com/documentation/createml/mldatatable#topics)

--------------------------------------------------------------------------------

### [Creating a data table](https://developer.apple.com/documentation/createml/mldatatable#Creating-a-data-table)

[tabular data에서 model 만들기](https://developer.apple.com/documentation/createml/creating-a-model-from-tabular-data)

Core ML을 사용해 tabular data를 import하고 관리하여 machine learning model을 training합니다.

[`init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws`](https://developer.apple.com/documentation/createml/mldatatable/init(contentsof:options:))

import한 JSON 또는 CSV 파일로 data table을 생성합니다.

[`init(dictionary: [String : any MLDataValueConvertible]) throws`](https://developer.apple.com/documentation/createml/mldatatable/init(dictionary:))

column 이름과 data value의 dictionary로 data table을 생성합니다.

[`init(namedColumns: [String : MLUntypedColumn]) throws`](https://developer.apple.com/documentation/createml/mldatatable/init(namedcolumns:))

column 이름과 untyped column의 dictionary로 data table을 생성합니다.

[`init()`](https://developer.apple.com/documentation/createml/mldatatable/init())

row와 column이 모두 없는 빈 table을 생성합니다.

[`struct ParsingOptions`](https://developer.apple.com/documentation/createml/mldatatable/parsingoptions)

CSV(comma-separated values) 파일을 machine learning model용 data table로 parsing하는 option입니다.

### [Getting the size of a data table](https://developer.apple.com/documentation/createml/mldatatable#Getting-the-size-of-a-data-table)

[`var size: (rows: Int, columns: Int)`](https://developer.apple.com/documentation/createml/mldatatable/size)

data table의 row 수와 column 수입니다.

### [Transforming rows to generate a data column](https://developer.apple.com/documentation/createml/mldatatable#Transforming-rows-to-generate-a-data-column)

[`func map(_:)`](https://developer.apple.com/documentation/createml/mldatatable/map(_:))

data table의 모든 row에 주어진 thread-safe transform을 적용해 새로운 column을 생성합니다.

### [Adding columns](https://developer.apple.com/documentation/createml/mldatatable#Adding-columns)

[`func addColumn(_:named:)`](https://developer.apple.com/documentation/createml/mldatatable/addcolumn(_:named:))

table에 untyped column을 추가합니다.

[`struct MLDataColumn`](https://developer.apple.com/documentation/createml/mldatacolumn)

data table에서 typed value를 담는 column입니다.

[`struct MLUntypedColumn`](https://developer.apple.com/documentation/createml/mluntypedcolumn)

data table에서 untyped value를 담는 column입니다.

### [Accessing columns](https://developer.apple.com/documentation/createml/mldatatable#Accessing-columns)

[`subscript(_:)`](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:))

지정한 이름의 untyped column을 가져오거나 추가합니다.

[`subscript<T>(String, T.Type) -> MLDataColumn<T>?`](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:_:))

지정한 이름과 type의 column을 가져옵니다.

### [Renaming columns](https://developer.apple.com/documentation/createml/mldatatable#Renaming-columns)

[`func renameColumn(named: String, to: String)`](https://developer.apple.com/documentation/createml/mldatatable/renamecolumn(named:to:))

기존 column의 이름을 변경합니다.

### [Removing columns](https://developer.apple.com/documentation/createml/mldatatable#Removing-columns)

[`func removeColumn(named: String)`](https://developer.apple.com/documentation/createml/mldatatable/removecolumn(named:))

지정한 이름의 column을 제거합니다.

### [Appending to a data table](https://developer.apple.com/documentation/createml/mldatatable#Appending-to-a-data-table)

[`func append(contentsOf: MLDataTable)`](https://developer.apple.com/documentation/createml/mldatatable/append(contentsof:))

지정한 data table의 내용을 이 data table 끝에 추가합니다.

### [Generating new data tables](https://developer.apple.com/documentation/createml/mldatatable#Generating-new-data-tables)

[API Reference\
\
Data table derivation operations](https://developer.apple.com/documentation/createml/data-table-derivation-operations)

기존 data table을 조작해 새로운 data table을 생성합니다.

### [Splitting a data table](https://developer.apple.com/documentation/createml/mldatatable#Splitting-a-data-table)

[`func randomSplitBySequence(proportion: Double, by: String, on: String, seed: Int) -> (MLDataTable, remaining: MLDataTable)`](https://developer.apple.com/documentation/createml/mldatatable/randomsplitbysequence(proportion:by:on:seed:))

[`func stratifiedSplit<RNG>(proportions: [Double], on: String, generator: inout RNG) throws -> MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable/stratifiedsplit(proportions:on:generator:))

user가 정의한 label column을 기준으로 stratify하면서 MLDataTable을 여러 partition으로 무작위 분할합니다.

[`func stratifiedSplit(proportions: [Double], on: String, seed: Int) throws -> MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable/stratifiedsplit(proportions:on:seed:))

user가 정의한 label column을 기준으로 stratify하면서 MLDataTable을 여러 partition으로 무작위 분할합니다.

[`func stratifiedSplitBySequence<RNG>(proportions: [Double], by: String, on: String, generator: inout RNG) throws -> MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable/stratifiedsplitbysequence(proportions:by:on:generator:))

같은 sequence의 row는 원래 순서를 유지하면서, user가 정의한 label column을 기준으로 MLDataTable을 여러 partition으로 무작위 분할합니다.

[`func stratifiedSplitBySequence(proportions: [Double], by: String, on: String, seed: Int) throws -> MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable/stratifiedsplitbysequence(proportions:by:on:seed:))

같은 sequence의 row는 원래 순서를 유지하면서, user가 정의한 label column을 기준으로 MLDataTable을 여러 partition으로 무작위 분할합니다.

### [Getting information about a data table’s rows](https://developer.apple.com/documentation/createml/mldatatable#Getting-information-about-a-data-tables-rows)

[`struct Row`](https://developer.apple.com/documentation/createml/mldatatable/row)

data table의 untyped value row입니다.

[`var rows: MLDataTable.Rows`](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.property)

table의 data row입니다.

[`struct Rows`](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct)

data table의 row collection입니다.

### [Getting information about a data table’s columns](https://developer.apple.com/documentation/createml/mldatatable#Getting-information-about-a-data-tables-columns)

[`var columnNames: MLDataTable.ColumnNames`](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.property)

data table에 있는 column의 이름입니다.

[`struct ColumnNames`](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.struct)

data table에 있는 column 이름의 collection입니다.

[`var columnTypes: [String : MLDataValue.ValueType]`](https://developer.apple.com/documentation/createml/mldatatable/columntypes)

각 column에 있는 data의 type입니다.

### [Saving a data table](https://developer.apple.com/documentation/createml/mldatatable#Saving-a-data-table)

[`func write(to: URL) throws`](https://developer.apple.com/documentation/createml/mldatatable/write(to:))

data table의 binary file을 지정한 directory URL로 export합니다.

[`func write(toDirectory: String) throws`](https://developer.apple.com/documentation/createml/mldatatable/write(todirectory:))

data table의 binary file을 지정한 directory path로 export합니다.

[`func writeCSV(to: URL) throws`](https://developer.apple.com/documentation/createml/mldatatable/writecsv(to:))

data table의 CSV file을 지정한 directory URL로 export합니다.
