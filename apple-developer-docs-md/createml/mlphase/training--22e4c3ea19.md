---
title: "MLPhase.training | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlphase/training"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.142373+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlphase/training#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLPhase](https://developer.apple.com/documentation/createml/mlphase)
    
*   MLPhase.training

Case

MLPhase.training
================

training session이 training dataset에서 추출한 feature로 model을 training하고 있습니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    case training

[같이 보기](https://developer.apple.com/documentation/createml/mlphase/training#see-also)

-----------------------------------------------------------------------------------------

### [session phase 가져오기](https://developer.apple.com/documentation/createml/mlphase/training#Retrieving-session-phases)

[`case initialized`](https://developer.apple.com/documentation/createml/mlphase/initialized)

training session이 feature 추출과 training 전에 있는 초기 idle 상태입니다.

[`case extractingFeatures`](https://developer.apple.com/documentation/createml/mlphase/extractingfeatures)

training session이 training dataset에서 feature를 추출하고 있습니다.

[`case evaluating`](https://developer.apple.com/documentation/createml/mlphase/evaluating)

training session이 training한 model을 평가하고 있습니다.

[`case inferencing`](https://developer.apple.com/documentation/createml/mlphase/inferencing)

training session이 model을 사용해 prediction을 만들고 있습니다.

현재 페이지: MLPhase.training
