---
title: "stratifiedSplit(proportions:generator:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150883+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   stratifiedSplit(proportions:generator:)

instance method

stratifiedSplit(proportions:generator:)
=======================================

random-number generator를 사용해 data source를 strata로 나누고, label이 지정된 audio dictionary 배열을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func stratifiedSplit<RNG>(
        proportions: [Double],
        generator: inout RNG
    ) throws -> [[String : [URL]]] where RNG : RandomNumberGenerator

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------

`proportions`

각 값이 `[0.0, 1.0]` 범위에 있는 proportion 배열입니다.

`generator`

random-number generator입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:)#return-value)

-----------------------------------------------------------------------------------------------------------------------------------------------------

label이 지정된 audio file dictionary 배열입니다. 각 dictionary key는 label string이고 값은 audio-file URL 배열입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:)#see-also)

---------------------------------------------------------------------------------------------------------------------------------------------

### [data 분할하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:)#Partitioning-the-data)

[`func stratifiedSplit(proportions: [Double], seed: Int) throws -> [[String : [URL]]]`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:))

data source를 strata로 분할해 label이 지정된 audio dictionary 배열을 생성합니다.

현재 페이지: stratifiedSplit(proportions:generator:)
