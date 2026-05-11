---
title: "MLSplitStrategy | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsplitstrategy"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148626+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsplitstrategy#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLSplitStrategy

enum

MLSplitStrategy
===============

보통 training dataset에서 validation dataset을 만들 때 사용하는 data 분할 방식입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+tvOS 16.0+visionOS 1.0+

    enum MLSplitStrategy

[주제](https://developer.apple.com/documentation/createml/mlsplitstrategy#topics)

------------------------------------------------------------------------------------

### [data 분할하기](https://developer.apple.com/documentation/createml/mlsplitstrategy#Partitioning-data)

[`case automatic`](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic)

Create ML이 training dataset 중 validation dataset에 사용할 양을 자동으로 결정합니다.

[`case fixed(ratio: Double, seed: Int?)`](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:))

Create ML이 ratio를 기준으로 training dataset의 일부를 사용해 validation dataset을 생성합니다.

[`func resolve(count: Int) -> (ratio: Double, seed: Int)`](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:))

특정 element count에 맞게 이 split strategy를 해석합니다.

### [random seed 만들기](https://developer.apple.com/documentation/createml/mlsplitstrategy#Creating-a-random-seed)

[`func timestampSeed() -> Int`](https://developer.apple.com/documentation/createml/timestampseed())

현재 system time을 기준으로 숫자를 반환합니다.

[관계](https://developer.apple.com/documentation/createml/mlsplitstrategy#relationships)

--------------------------------------------------------------------------------------------------

### [준수 대상](https://developer.apple.com/documentation/createml/mlsplitstrategy#conforms-to)

*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/createml/mlsplitstrategy#see-also)

----------------------------------------------------------------------------------------

### [지원 type](https://developer.apple.com/documentation/createml/mlsplitstrategy#Supporting-types)

[`enum MLCreateError`](https://developer.apple.com/documentation/createml/mlcreateerror)

model training, prediction 수행, file system에 model 쓰기 등 다양한 작업 중 Create ML이 throw하는 error입니다.

[`struct MLModelMetadata`](https://developer.apple.com/documentation/createml/mlmodelmetadata)

Core ML model file에 저장되는 model 정보입니다.

현재 페이지는 MLSplitStrategy입니다
