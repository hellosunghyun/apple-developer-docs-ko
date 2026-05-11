---
title: "contains(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144556+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   contains(\_:)

instance method

contains(\_:)
=============

vocabulary에 지정한 string이 포함되어 있는지 나타내는 Boolean 값을 반환합니다.

macOS 10.15+

    func contains(_ text: String) -> Bool

[Parameters](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:)#parameters)

---------------------------------------------------------------------------------------------------------

`text`

vocabulary에서 찾을 string입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:)#return-value)

-------------------------------------------------------------------------------------------------------------

string을 vocabulary에서 찾았으면 `true`, 아니면 false입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:)#see-also)

-----------------------------------------------------------------------------------------------------

### [word embedding 테스트하기](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:)#Testing-a-word-embedding)

[`func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]`](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:))

이웃 항목을 예측합니다.

[`func distance(between: String, and: String, distanceType: NLDistanceType) -> Double`](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:))

vocabulary space에서 두 string 사이의 거리를 계산합니다.

[`enum NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType)

text embedding의 두 위치 사이 거리를 계산하는 방법입니다.

[`func vector(for: String) -> [Double]?`](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:))

vocabulary에서 지정한 string에 연결된 vector에 접근합니다.

현재 페이지: contains(\_:)
