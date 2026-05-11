---
title: "MLPhase.inferencing | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlphase/inferencing"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150795+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlphase/inferencing#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLPhase](https://developer.apple.com/documentation/createml/mlphase)
    
*   MLPhase.inferencing

case

MLPhase.inferencing
===================

training session이 model을 사용해 prediction을 수행하는 단계입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    case inferencing

[참고 항목](https://developer.apple.com/documentation/createml/mlphase/inferencing#see-also)

--------------------------------------------------------------------------------------------

### [session phase 가져오기](https://developer.apple.com/documentation/createml/mlphase/inferencing#Retrieving-session-phases)

[`case initialized`](https://developer.apple.com/documentation/createml/mlphase/initialized)

training session이 feature extraction과 training을 시작하기 전의 초기 idle 상태입니다.

[`case extractingFeatures`](https://developer.apple.com/documentation/createml/mlphase/extractingfeatures)

training session이 training dataset에서 feature를 추출하는 단계입니다.

[`case training`](https://developer.apple.com/documentation/createml/mlphase/training)

training session이 training dataset에서 추출한 feature로 model을 training하는 단계입니다.

[`case evaluating`](https://developer.apple.com/documentation/createml/mlphase/evaluating)

training session이 training한 model을 평가하는 단계입니다.

현재 페이지는 MLPhase.inferencing입니다
