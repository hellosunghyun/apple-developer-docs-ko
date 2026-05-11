---
title: "MLPhase | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlphase"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.143677+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlphase#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   MLPhase

enum

MLPhase
=======

training session의 가능한 상태입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    enum MLPhase

[주제](https://developer.apple.com/documentation/createml/mlphase#topics)

----------------------------------------------------------------------------

### [session phase 가져오기](https://developer.apple.com/documentation/createml/mlphase#Retrieving-session-phases)

[`case initialized`](https://developer.apple.com/documentation/createml/mlphase/initialized)

feature 추출과 training을 시작하기 전의 초기 idle 상태입니다.

[`case extractingFeatures`](https://developer.apple.com/documentation/createml/mlphase/extractingfeatures)

training session이 training dataset에서 feature를 추출하는 중입니다.

[`case training`](https://developer.apple.com/documentation/createml/mlphase/training)

training session이 training dataset에서 추출한 feature로 model을 training하는 중입니다.

[`case evaluating`](https://developer.apple.com/documentation/createml/mlphase/evaluating)

training session이 training한 model을 평가하는 중입니다.

[`case inferencing`](https://developer.apple.com/documentation/createml/mlphase/inferencing)

training session이 model을 사용해 prediction을 만드는 중입니다.

[관계](https://developer.apple.com/documentation/createml/mlphase#relationships)

------------------------------------------------------------------------------------------

### [준수하는 protocol](https://developer.apple.com/documentation/createml/mlphase#conforms-to)

*   [`Copyable`](https://developer.apple.com/documentation/Swift/Copyable)
    
*   [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable)
    
*   [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Escapable`](https://developer.apple.com/documentation/Swift/Escapable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[같이 보기](https://developer.apple.com/documentation/createml/mlphase#see-also)

--------------------------------------------------------------------------------

### [training session progress 확인하기](https://developer.apple.com/documentation/createml/mlphase#Checking-a-training-sessions-progress)

[`var phase: MLPhase`](https://developer.apple.com/documentation/createml/mltrainingsession/phase)

training session의 현재 상태입니다.

[`var iteration: Int`](https://developer.apple.com/documentation/createml/mltrainingsession/iteration)

training session phase의 iteration 번호입니다.

[`var checkpoints: [MLCheckpoint]`](https://developer.apple.com/documentation/createml/mltrainingsession/checkpoints)

지금까지 training session이 만든 checkpoint 배열입니다.

현재 페이지: MLPhase
