---
title: "dominance | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.032348+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechExpression](https://developer.apple.com/documentation/sensorkit/srspeechexpression)
    
*   dominance

instance property

dominance
=========

화자가 얼마나 강하거나 유약하게 들리는지를 나타내는 정도입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var dominance: Double { get }

[논의](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance#Discussion)

----------------------------------------------------------------------------------------------------------

이 property는 `-1`부터 `1`까지의 범위입니다. 음수 값은 부정적인 sentiment를, 양수 값은 긍정적인 sentiment를 나타냅니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance#see-also)

------------------------------------------------------------------------------------------------------

### [Getting speech analytics](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance#Getting-speech-analytics)

[`var confidence: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/confidence)

화자의 confidence 수준입니다.

[`var mood: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/mood)

일반적인 speech와 비교해 화자가 얼마나 혀가 꼬였거나, 피곤하거나, 지친 듯 들리는지를 나타냅니다.

[`var valence: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/valence)

화자의 감정 또는 sentiment가 얼마나 긍정적이거나 부정적인지를 나타내는 정도입니다.

[`var activation: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation)

화자의 energy 또는 activation 수준입니다.

현재 페이지: dominance
