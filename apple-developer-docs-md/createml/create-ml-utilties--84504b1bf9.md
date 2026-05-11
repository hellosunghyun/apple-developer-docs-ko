---
title: "Data visualizations | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/create-ml-utilties"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150001+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/create-ml-utilties#app-main)

컬렉션

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   data visualization

API 컬렉션

data visualization
===================

data table과 column의 image를 playground에 렌더링합니다.

[주제](https://developer.apple.com/documentation/createml/create-ml-utilties#topics)

---------------------------------------------------------------------------------------

### [Table visualization](https://developer.apple.com/documentation/createml/create-ml-utilties#Table-visualizations)

[`func show(MLDataTable) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:)-2dkfz)

data table의 streaming visualization을 생성합니다.

Deprecated

### [Column visualization](https://developer.apple.com/documentation/createml/create-ml-utilties#Column-visualizations)

[`func show<Element>(MLDataColumn<Element>) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:)-5r938)

data column의 streaming visualization을 생성합니다.

Deprecated

[`func show(MLUntypedColumn) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:)-9645r)

untyped column의 streaming visualization을 생성합니다.

Deprecated

### [Plot visualization](https://developer.apple.com/documentation/createml/create-ml-utilties#Plot-visualizations)

[`func show<ElementX, ElementY>(MLDataColumn<ElementX>, MLDataColumn<ElementY>) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:_:)-537qb)

두 data column의 streaming plot visualization을 생성합니다.

Deprecated

[`func show(MLUntypedColumn, MLUntypedColumn) -> any MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/show(_:_:)-2tmbf)

두 untyped column의 streaming plot visualization을 생성합니다.

Deprecated

### [Visualization protocol](https://developer.apple.com/documentation/createml/create-ml-utilties#Visualization-protocols)

[`protocol MLVisualizable`](https://developer.apple.com/documentation/createml/mlvisualizable)

machine learning type의 image visualization입니다.

[`protocol MLStreamingVisualizable`](https://developer.apple.com/documentation/createml/mlstreamingvisualizable)

machine learning type용 image visualization sequence입니다.

현재 페이지: data visualization
