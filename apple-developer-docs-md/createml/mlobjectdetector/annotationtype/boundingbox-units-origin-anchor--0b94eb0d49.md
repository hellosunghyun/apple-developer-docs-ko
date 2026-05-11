---
title: "MLObjectDetector.AnnotationType.boundingBox(units:origin:anchor:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.163876+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLObjectDetector](https://developer.apple.com/documentation/createml/mlobjectdetector)
    
*   *   [MLObjectDetector](https://developer.apple.com/documentation/createml/mlobjectdetector)
        
*   [MLObjectDetector.AnnotationType](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype)
    
*   MLObjectDetector.AnnotationType.boundingBox(units:origin:anchor:)

Case

MLObjectDetector.AnnotationType.boundingBox(units:origin:anchor:)
=================================================================

image 안의 object 주변에 사각형을 정의하는 annotation type입니다.

macOS 10.15+

    case boundingBox(
        units: MLBoundingBoxUnits = .pixel,
        origin: MLBoundingBoxCoordinatesOrigin = .topLeft,
        anchor: MLBoundingBoxAnchor = .center
    )

[논의](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:)#discussion)

----------------------------------------------------------------------------------------------------------------------------------------------

bounding box annotation을 사용하려면 annotation을 어떻게 해석할지 Create ML에 알려야 합니다.

*   [`MLBoundingBoxUnits`](https://developer.apple.com/documentation/createml/mlboundingboxunits)를 사용해 bounding box coordinate 단위를 지정합니다.
    
*   [`MLBoundingBoxAnchor`](https://developer.apple.com/documentation/createml/mlboundingboxanchor)를 사용해 coordinate가 가리키는 bounding box 내부 위치를 지정합니다.
    
*   [`MLBoundingBoxCoordinatesOrigin`](https://developer.apple.com/documentation/createml/mlboundingboxcoordinatesorigin)을 사용해 annotation이 origin으로 사용할 image 부분을 지정합니다.
    

[Formatting a Bounding Box JSON Annotation File](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:)#Formatting-a-Bounding-Box-JSON-Annotation-File)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

JSON file의 최상위에는 다음 JSON object 구조의 array가 있어야 합니다.

| Name | Type | Value |
| --- | --- | --- |
| `imagefilename` | String | image file의 이름입니다. |
| `annotation` | Array | annotation JSON object의 array입니다. |

`annotation` array의 각 JSON object는 다음 JSON object 구조를 가져야 합니다.

| Name | Type | Value |
| --- | --- | --- |
| `label` | String | annotation한 object의 이름입니다. |
| `coordinates` | JSON object | object의 위치와 image에서 차지하는 영역입니다. |

`coordinate` JSON object는 다음 구조를 가져야 합니다. image의 origin은 왼쪽 위 모서리입니다. `x`\-값은 왼쪽에서 오른쪽으로 증가하고 `y`\-값은 위에서 아래로 증가합니다.

| Name | Type | Value |
| --- | --- | --- |
| `x` | Number | `MLBoundingBoxCoordinatesOrigin`이 정의하는 annotation origin의 `x`\-coordinate입니다. |
| `y` | Number | `MLBoundingBoxCoordinatesOrigin`이 정의하는 annotation origin의 `y`\-coordinate입니다. |
| `width` | Number | annotation bounding box의 너비입니다. |
| `height` | Number | annotation bounding box의 높이입니다. |

예를 들어 다음 JSON file은 최상위 array에 image file 하나(`"cat and dog.png"`)를 포함하며, 여기에 annotation 두 개가 있어 올바른 구조를 이룹니다.

    // JSON file
      [{\
        "imagefilename": "cat and dog.png",\
        "annotation":\
        [\
          {\
            "label": "cat",\
            "coordinates":\
            {\
              "y": 2.0,\
              "x": 3.9,\
              "height": 40.1,\
              "width": 20.0\
            }\
          }, {\
            "label": "dog",\
            "coordinates":\
            {\
              "y": 40.0,\
              "x": 38.9,\
              "height": 100.1,\
              "width": 70.0\
            }\
          }\
        ]\
      },\
      ... ]
    

일반적인 annotation JSON file은 최상위 array에 각 image file마다 하나씩 훨씬 많은 object를 포함합니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:)#see-also)

------------------------------------------------------------------------------------------------------------------------------------------

### [bounding box annotation](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:)#Bounding-box-annotations)

[`enum MLBoundingBoxUnits`](https://developer.apple.com/documentation/createml/mlboundingboxunits)

bounding box annotation이 위치와 크기를 정의할 때 사용하는 단위입니다.

[`enum MLBoundingBoxAnchor`](https://developer.apple.com/documentation/createml/mlboundingboxanchor)

annotation coordinate가 기준점으로 사용하는 bounding box 내부 위치입니다.

[`enum MLBoundingBoxCoordinatesOrigin`](https://developer.apple.com/documentation/createml/mlboundingboxcoordinatesorigin)

annotation coordinate가 origin으로 사용하는 image 내부 위치입니다.

현재 페이지는 MLObjectDetector.AnnotationType.boundingBox(units:origin:anchor:)입니다
