---
title: "reuseExtractedFeatures(from:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsession/reuseextractedfeatures(from:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.156907+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsession/reuseextractedfeatures(from:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTrainingSession](https://developer.apple.com/documentation/createml/mltrainingsession)
    
*   reuseExtractedFeatures(from:)

instance method

reuseExtractedFeatures(from:)
=============================

다른 session이 이미 dataset에서 추출한 feature를 사용합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    final func reuseExtractedFeatures(from session: MLTrainingSession<Task>) throws

[parameter](https://developer.apple.com/documentation/createml/mltrainingsession/reuseextractedfeatures(from:)#parameters)

----------------------------------------------------------------------------------------------------------------------------

`session`

이미 feature extraction phase를 완료한 다른 training session입니다.

[설명](https://developer.apple.com/documentation/createml/mltrainingsession/reuseextractedfeatures(from:)#discussion)

----------------------------------------------------------------------------------------------------------------------------

이 method는 아직 자체 checkpoint가 없는 새 training session에서만 사용할 수 있습니다.

현재 페이지: reuseExtractedFeatures(from:)
