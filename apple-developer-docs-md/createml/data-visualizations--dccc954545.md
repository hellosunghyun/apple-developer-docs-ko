---
title: "Data visualizations | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/data-visualizations"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.132445+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/data-visualizations#app-main)

컬렉션

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   Data visualizations

API 컬렉션

Data visualizations
===================

playground에서 data table과 column의 image를 렌더링합니다.

[주제](https://developer.apple.com/documentation/createml/data-visualizations#topics)

----------------------------------------------------------------------------------------

### [table 시각화](https://developer.apple.com/documentation/createml/data-visualizations#Table-visualizations)

[`func show(MLDataTable) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:)-2dkfz)

data table의 streaming visualization을 생성합니다.

Deprecated

### [column 시각화](https://developer.apple.com/documentation/createml/data-visualizations#Column-visualizations)

[`func show<Element>(MLDataColumn<Element>) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:)-5r938)

data column의 streaming visualization을 생성합니다.

Deprecated

[`func show(MLUntypedColumn) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:)-9645r)

untyped column의 streaming visualization을 생성합니다.

Deprecated

### [plot 시각화](https://developer.apple.com/documentation/createml/data-visualizations#Plot-visualizations)

[`func show<ElementX, ElementY>(MLDataColumn<ElementX>, MLDataColumn<ElementY>) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:_:)-537qb)

두 data column의 streaming plot visualization을 생성합니다.

Deprecated

[`func show(MLUntypedColumn, MLUntypedColumn) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:_:)-2tmbf)

두 untyped column의 streaming plot visualization을 생성합니다.

Deprecated

### [visualization protocol](https://developer.apple.com/documentation/createml/data-visualizations#Visualization-protocols)

[`protocol MLVisualizable`](https://developer.apple.com/documentation/createml/mlvisualizable)

machine learning type의 image visualization입니다.

[`protocol MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/mlstreamingvisualizable)

machine learning type용 image visualization sequence입니다.

[같이 보기](https://developer.apple.com/documentation/createml/data-visualizations#see-also)

--------------------------------------------------------------------------------------------

### [tabular data](https://developer.apple.com/documentation/createml/data-visualizations#Tabular-data)

[`struct MLDataTable`](https://developer.apple.com/documentation/createml/mldatatable)

machine learning model을 training하거나 평가하기 위한 data table입니다.

[`enum MLDataValue`](https://developer.apple.com/documentation/createml/mldatavalue)

data table cell의 값입니다.

현재 페이지는 Data visualizations입니다
