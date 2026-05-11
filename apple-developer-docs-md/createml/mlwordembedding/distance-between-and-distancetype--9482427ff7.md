---
title: "distance(between:and:distanceType:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.146826+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   distance(between:and:distanceType:)

instance method

distance(between:and:distanceType:)
===================================

vocabulary 공간에서 두 string 사이의 distance를 계산합니다.

macOS 10.15+

    func distance(
        between first: String,
        and second: String,
        distanceType: NLDistanceType = .cosine
    ) -> Double

[Parameters](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:)#parameters)

--------------------------------------------------------------------------------------------------------------------------------

`first`

embedding vocabulary에 있는 string입니다.

`second`

embedding vocabulary에 있는 또 다른 string입니다.

`distanceType`

첫 번째 string과 두 번째 string 사이의 distance를 계산할 때 사용할 metric입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:)#return-value)

------------------------------------------------------------------------------------------------------------------------------------

distance입니다.

[같이 보기](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:)#see-also)

----------------------------------------------------------------------------------------------------------------------------

### [word embedding 테스트하기](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:)#Testing-a-word-embedding)

[`func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]`](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:))

이웃을 예측합니다.

[`enum NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType)

text embedding에서 두 위치 사이 distance를 계산하는 방식입니다.

[`func contains(String) -> Bool`](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:))

vocabulary에 지정한 string이 들어 있는지 나타내는 Boolean 값을 반환합니다.

[`func vector(for: String) -> [Double]?`](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:))

vocabulary에서 지정한 string과 연결된 vector에 접근합니다.

현재 페이지: distance(between:and:distanceType:)
