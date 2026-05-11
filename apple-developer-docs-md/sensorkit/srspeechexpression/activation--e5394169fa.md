---
title: "activation | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.055534+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRSpeechExpression](https://developer.apple.com/documentation/sensorkit/srspeechexpression)
    
*   activation

instance property

activation
==========

speaker의 energy 또는 activation 수준입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    var activation: Double { get }

[논의](https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation#Discussion)

-----------------------------------------------------------------------------------------------------------

이 property의 범위는 `-1`부터 `1`까지이며, 음수 값은 negative sentiment를 나타내고 양수 값은 positive sentiment를 나타냅니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation#see-also)

-------------------------------------------------------------------------------------------------------

### [Getting speech analytics](https://developer.apple.com/documentation/sensorkit/srspeechexpression/activation#Getting-speech-analytics)

[`var confidence: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/confidence)

speaker의 confidence 수준입니다.

[`var mood: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/mood)

speaker가 일반적인 speech와 비교해 얼마나 어눌하고, 피곤하거나, 지친 것처럼 들리는지를 나타냅니다.

[`var valence: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/valence)

speaker의 positive 또는 negative emotion이나 sentiment 정도입니다.

[`var dominance: Double`](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance)

speaker가 얼마나 강하게 또는 약하게 들리는지의 정도입니다.

현재 페이지: activation
