---
title: "MLSplitStrategy.automatic | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150523+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSplitStrategy](https://developer.apple.com/documentation/createml/mlsplitstrategy)
    
*   MLSplitStrategy.automatic

케이스

MLSplitStrategy.automatic
=========================

Create ML이 training dataset 중 얼마를 validation dataset으로 사용할지 자동으로 결정합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+tvOS 16.0+visionOS 1.0+

    case automatic

[설명](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic#discussion)

------------------------------------------------------------------------------------------------------

Create ML은 크기에 따라 training dataset에서 최대 10%를 분할해 validation dataset을 만듭니다.

| Training samples | % used for validation |
| --- | --- |
| < 50 | None |
| 50 to 199 | 10% |
| ≥ 200 | 5%  |

[같이 보기](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic#see-also)

--------------------------------------------------------------------------------------------------

### [Data 분할하기](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic#Partitioning-data)

[`case fixed(ratio: Double, seed: Int?)`](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:))

비율에 따라 training dataset의 일부를 사용해 validation dataset을 만듭니다.

[`func resolve(count: Int) -> (ratio: Double, seed: Int)`](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:))

특정 element count에 대해 이 split strategy를 해석합니다.

현재 페이지: MLSplitStrategy.automatic
