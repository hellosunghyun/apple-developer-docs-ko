---
title: "prediction(from:maxCount:maxDistance:distanceType:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.148285+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding)
    
*   prediction(from:maxCount:maxDistance:distanceType:)

instance method

prediction(from:maxCount:maxDistance:distanceType:)
===================================================

neighbor를 예측합니다.

macOS 10.15+

    func prediction(
        from text: String,
        maxCount: Int = 10,
        maxDistance: Double = 2.0,
        distanceType: NLDistanceType = .cosine
    ) throws -> [(text: String, distance: Double)]

[Parameters](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)#parameters)

------------------------------------------------------------------------------------------------------------------------------------------------

`text`

embedding vocabulary 안에 있는 string입니다.

`maxCount`

neighboring string의 최대 개수입니다.

`maxDistance`

허용되는 최대 neighbor distance입니다.

`distanceType`

입력 string과 neighbor 사이의 distance를 평가할 때 사용할 distance formula type입니다.

[Return Value](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)#return-value)

----------------------------------------------------------------------------------------------------------------------------------------------------

neighboring string과 각 string이 입력 string까지 가지는 distance의 array입니다.

[논의](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)#discussion)

------------------------------------------------------------------------------------------------------------------------------------------------

distance 값은 [`NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType)
이 정하는 formula로 계산합니다. 예를 들어 [`NLDistanceType.cosine`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType/cosine)
을 사용할 수 있습니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)#see-also)

--------------------------------------------------------------------------------------------------------------------------------------------

### [word embedding 테스트](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:)#Testing-a-word-embedding)

[`func distance(between: String, and: String, distanceType: NLDistanceType) -> Double`](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:))

vocabulary space에서 두 string 사이의 distance를 계산합니다.

[`enum NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType)

text embedding 안의 두 위치 사이 distance를 계산하는 방식입니다.

[`func contains(String) -> Bool`](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:))

vocabulary에 지정한 string이 포함되어 있는지를 나타내는 Boolean 값을 반환합니다.

[`func vector(for: String) -> [Double]?`](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:))

vocabulary에서 지정한 string과 연결된 vector에 접근합니다.

현재 페이지는 prediction(from:maxCount:maxDistance:distanceType:)입니다
