---
title: "MLModelMetadata | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlmodelmetadata"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148499+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlmodelmetadata#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLModelMetadata

struct

MLModelMetadata
===============

Core ML model file에 저장되는 model 정보입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    struct MLModelMetadata

[언급된 문서](https://developer.apple.com/documentation/createml/mlmodelmetadata#mentions)

--------------------------------------------------------------------------------------------

[text classifier model 만들기](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)

[word tagger model 만들기](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model)

[개요](https://developer.apple.com/documentation/createml/mlmodelmetadata#overview)

----------------------------------------------------------------------------------------

Core ML model을 export할 때 metadata instance를 만들고 model의 일부로 저장합니다. app에 model을 가져오면 Xcode에서 이 metadata를 확인할 수 있습니다.

[주제](https://developer.apple.com/documentation/createml/mlmodelmetadata#topics)

------------------------------------------------------------------------------------

### [metadata 만들기](https://developer.apple.com/documentation/createml/mlmodelmetadata#Creating-metadata)

[`init(author: String, shortDescription: String, license: String?, version: String, additional: [String : String]?)`](https://developer.apple.com/documentation/createml/mlmodelmetadata/init(author:shortdescription:license:version:additional:))

machine learning model용 새 metadata instance를 만듭니다.

### [metadata 접근](https://developer.apple.com/documentation/createml/mlmodelmetadata#Accessing-metadata)

[`var author: String`](https://developer.apple.com/documentation/createml/mlmodelmetadata/author)

model의 author입니다.

[`var shortDescription: String`](https://developer.apple.com/documentation/createml/mlmodelmetadata/shortdescription)

model에 대한 짧은 텍스트 설명입니다.

[`var license: String?`](https://developer.apple.com/documentation/createml/mlmodelmetadata/license)

model 사용을 규정하는 license입니다.

[`var version: String`](https://developer.apple.com/documentation/createml/mlmodelmetadata/version)

model version입니다.

[`var additional: [String : String]?`](https://developer.apple.com/documentation/createml/mlmodelmetadata/additional)

model에 관한 추가 정보를 담는 key-value 쌍을 인코딩하는 dictionary입니다.

[관계](https://developer.apple.com/documentation/createml/mlmodelmetadata#relationships)

--------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/createml/mlmodelmetadata#conforms-to)

*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/createml/mlmodelmetadata#see-also)

----------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlmodelmetadata#Supporting-types)

[`enum MLCreateError`](https://developer.apple.com/documentation/createml/mlcreateerror)

Create ML이 model training, prediction 생성, file system에 model 쓰기 등의 여러 작업을 수행하면서 throw하는 error입니다.

[`enum MLSplitStrategy`](https://developer.apple.com/documentation/createml/mlsplitstrategy)

보통 training dataset에서 validation dataset을 만들 때 사용하는 data partitioning 방식입니다.

현재 페이지는 MLModelMetadata입니다.
