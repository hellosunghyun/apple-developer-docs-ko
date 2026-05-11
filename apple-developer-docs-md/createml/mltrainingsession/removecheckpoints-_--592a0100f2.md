---
title: "removeCheckpoints(_:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsession/removecheckpoints(_:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.156810+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsession/removecheckpoints(_:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTrainingSession](https://developer.apple.com/documentation/createml/mltrainingsession)
    
*   removeCheckpoints(\_:)

instance method

removeCheckpoints(\_:)
======================

closure 조건을 만족하는 checkpoint를 training session에서 제거합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    final func removeCheckpoints(_ predicate: (MLCheckpoint) -> Bool) throws

[Parameters](https://developer.apple.com/documentation/createml/mltrainingsession/removecheckpoints(_:)#parameters)

--------------------------------------------------------------------------------------------------------------------

`predicate`

checkpoint를 제거할지 나타내는 Boolean을 반환하는 closure입니다.

현재 페이지: removeCheckpoints(\_:)
