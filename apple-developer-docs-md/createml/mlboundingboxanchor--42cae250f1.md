---
title: "MLBoundingBoxAnchor | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlboundingboxanchor"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150351+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlboundingboxanchor#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLBoundingBoxAnchor

enum

MLBoundingBoxAnchor
===================

annotation 좌표가 기준점으로 사용하는 bounding box 내부 위치입니다.

macOS 10.15+

    enum MLBoundingBoxAnchor

[주제](https://developer.apple.com/documentation/createml/mlboundingboxanchor#topics)

----------------------------------------------------------------------------------------

### [anchor 지정하기](https://developer.apple.com/documentation/createml/mlboundingboxanchor#Designating-anchors)

[`case center`](https://developer.apple.com/documentation/createml/mlboundingboxanchor/center)

bounding box 중심점의 anchor입니다.

[`case topLeft`](https://developer.apple.com/documentation/createml/mlboundingboxanchor/topleft)

bounding box 왼쪽 위 모서리의 anchor입니다.

[`case bottomLeft`](https://developer.apple.com/documentation/createml/mlboundingboxanchor/bottomleft)

bounding box 왼쪽 아래 모서리의 anchor입니다.

[관계](https://developer.apple.com/documentation/createml/mlboundingboxanchor#relationships)

------------------------------------------------------------------------------------------------------

### [준수 protocol](https://developer.apple.com/documentation/createml/mlboundingboxanchor#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlboundingboxanchor#see-also)

--------------------------------------------------------------------------------------------

### [Bounding box annotation](https://developer.apple.com/documentation/createml/mlboundingboxanchor#Bounding-box-annotations)

[`case boundingBox(units: MLBoundingBoxUnits, origin: MLBoundingBoxCoordinatesOrigin, anchor: MLBoundingBoxAnchor)`](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:))

image 안의 object 주위 사각형을 정의하는 annotation type입니다.

[`enum MLBoundingBoxUnits`](https://developer.apple.com/documentation/createml/mlboundingboxunits)

bounding box annotation이 위치와 크기를 정의할 때 사용하는 단위입니다.

[`enum MLBoundingBoxCoordinatesOrigin`](https://developer.apple.com/documentation/createml/mlboundingboxcoordinatesorigin)

annotation 좌표가 원점으로 사용하는 image 내부 위치입니다.

현재 페이지: MLBoundingBoxAnchor
