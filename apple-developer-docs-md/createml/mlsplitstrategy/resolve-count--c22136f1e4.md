---
title: "resolve(count:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.151993+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSplitStrategy](https://developer.apple.com/documentation/createml/mlsplitstrategy)
    
*   resolve(count:)

instance method

resolve(count:)
===============

특정 element count에 대해 이 split strategy를 해석합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    func resolve(count: Int) -> (ratio: Double, seed: Int)

[parameter](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:)#parameters)

------------------------------------------------------------------------------------------------------------

`count`

split하는 collection의 element 수입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:)#return-value)

----------------------------------------------------------------------------------------------------------------

사용할 split 비율과 random seed입니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:)#see-also)

--------------------------------------------------------------------------------------------------------

### [data 분할](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:)#Partitioning-data)

[`case automatic`](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic)

Create ML이 training dataset 중 validation dataset에 사용할 양을 자동으로 결정합니다.

[`case fixed(ratio: Double, seed: Int?)`](https://developer.apple.com/documentation/createml/mlsplitstrategy/fixed(ratio:seed:))

Create ML이 ratio를 기준으로 training dataset의 일부를 사용해 validation dataset을 만듭니다.

현재 페이지: resolve(count:)
