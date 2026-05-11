---
title: "vector(for:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.144306+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   vector(for:)

instance method

vector(for:)
============

vocabulary에서 지정한 string에 연결된 vector에 접근합니다.

macOS 10.15+

    func vector(for text: String) -> [Double]?

[parameter](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:)#parameters)

---------------------------------------------------------------------------------------------------------

`text`

vocabulary 안의 string입니다.

[반환 값](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:)#return-value)

-------------------------------------------------------------------------------------------------------------

word embedding에 해당 string이 있으면 그에 연결된 vector를 반환하고, 없으면 `nil`을 반환합니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:)#see-also)

-----------------------------------------------------------------------------------------------------

### [word embedding 테스트하기](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:)#Testing-a-word-embedding)

[`func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]`](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:))

neighbor를 예측합니다.

[`func distance(between: String, and: String, distanceType: NLDistanceType) -> Double`](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:))

vocabulary space에서 두 string 사이의 distance를 계산합니다.

[`enum NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType)

text embedding 안 두 위치 사이의 distance를 계산하는 방식입니다.

[`func contains(String) -> Bool`](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:))

vocabulary에 지정한 string이 포함되어 있는지 나타내는 Boolean 값을 반환합니다.

현재 페이지: vector(for:)
