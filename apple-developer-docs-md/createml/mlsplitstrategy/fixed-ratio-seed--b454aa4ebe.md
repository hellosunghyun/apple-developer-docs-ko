---
title: "MLSplitStrategy.fixed(ratio:seed:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.151891+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSplitStrategy](https://developer.apple.com/documentation/createml/mlsplitstrategy)
    
*   MLSplitStrategy.fixed(ratio:seed:)

Case

MLSplitStrategy.fixed(ratio:seed:)
==================================

Create ML은 ratio를 기준으로 training dataset의 일부를 사용해 validation dataset을 만듭니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+tvOS 16.0+visionOS 1.0+

    case fixed(
        ratio: Double,
        seed: Int?
    )

[논의](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:)#discussion)

---------------------------------------------------------------------------------------------------------------

ratio는 validation에 사용할 training data의 양을 정하는 `[0.0, 1.0]` 범위의 값입니다. seed 값은 여러 invocation에서 일관된 결과를 얻는 데 사용할 수 있습니다. seed가 nil이면 매 invocation마다 split이 무작위로 결정됩니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:)#see-also)

-----------------------------------------------------------------------------------------------------------

### [data 분할하기](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:)#Partitioning-data)

[`case automatic`](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic)

Create ML이 training dataset 중 어느 정도를 validation dataset에 사용할지 자동으로 결정합니다.

[`func resolve(count: Int) -> (ratio: Double, seed: Int)`](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:))

특정 element count에 대해 이 split strategy를 해석합니다.

현재 페이지: MLSplitStrategy.fixed(ratio:seed:)
