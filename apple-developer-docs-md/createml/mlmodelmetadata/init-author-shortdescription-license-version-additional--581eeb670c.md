---
title: "init(author:shortDescription:license:version:additional:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlmodelmetadata/init(author:shortdescription:license:version:additional:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.147750+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlmodelmetadata/init(author:shortdescription:license:version:additional:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLModelMetadata](https://developer.apple.com/documentation/createml/mlmodelmetadata)
    
*   init(author:shortDescription:license:version:additional:)

initializer

init(author:shortDescription:license:version:additional:)
=========================================================

machine learning model용 새 metadata instance를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    init(
        author: String = NSFullUserName(),
        shortDescription: String = "A model trained using CreateML for use with CoreML.",
        license: String? = nil,
        version: String = "1",
        additional: [String : String]? = nil
    )

[parameter](https://developer.apple.com/documentation/createml/mlmodelmetadata/init(author:shortdescription:license:version:additional:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------------------------

`author`

model의 작성자입니다.

`shortDescription`

model의 짧은 설명입니다.

`license`

model 사용을 규정하는 license입니다.

`version`

model 버전입니다.

`additional`

임의의 key-value pair를 저장할 수 있는 dictionary입니다.

현재 페이지: init(author:shortDescription:license:version:additional:)
