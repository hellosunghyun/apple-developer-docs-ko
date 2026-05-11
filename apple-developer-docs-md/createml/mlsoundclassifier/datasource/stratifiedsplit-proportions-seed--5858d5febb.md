---
title: "stratifiedSplit(proportions:seed:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.149012+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   stratifiedSplit(proportions:seed:)

instance method

stratifiedSplit(proportions:seed:)
==================================

data source를 strata로 나누어 label된 audio dictionary array를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func stratifiedSplit(
        proportions: [Double],
        seed: Int = timestampSeed()
    ) throws -> [[String : [URL]]]

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------------------

`proportions`

각 원소가 `[0.0, 1.0]` 범위에 있는 proportion array입니다.

`seed`

random-number generator용 seed입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:)#return-value)

------------------------------------------------------------------------------------------------------------------------------------------------

label된 audio file dictionary array입니다. 각 dictionary key는 label string이고 값은 audio-file URL array입니다.

[관련 항목](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:)#see-also)

----------------------------------------------------------------------------------------------------------------------------------------

### [data 분할](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:)#Partitioning-the-data)

[`func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]]`](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:))

random-number generator를 사용해 data source를 strata로 나누어 label된 audio dictionary array를 생성합니다.

현재 페이지: stratifiedSplit(proportions:seed:)
