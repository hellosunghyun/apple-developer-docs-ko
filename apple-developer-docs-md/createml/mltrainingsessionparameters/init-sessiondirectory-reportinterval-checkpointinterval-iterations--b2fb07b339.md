---
title: "init(sessionDirectory:reportInterval:checkpointInterval:iterations:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsessionparameters/init(sessiondirectory:reportinterval:checkpointinterval:iterations:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.147287+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/init(sessiondirectory:reportinterval:checkpointinterval:iterations:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTrainingSessionParameters](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
    
*   init(sessionDirectory:reportInterval:checkpointInterval:iterations:)

initializer

init(sessionDirectory:reportInterval:checkpointInterval:iterations:)
====================================================================

training session용 parameter 집합을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    init(
        sessionDirectory: URL? = nil,
        reportInterval: Int = 5,
        checkpointInterval: Int = 10,
        iterations: Int = 1000
    )

[Parameters](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/init(sessiondirectory:reportinterval:checkpointinterval:iterations:)#parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`sessionDirectory`

session이 진행 상황을 저장하는 file system 위치입니다.

`reportInterval`

session이 진행 상황을 보고하기 전에 완료하는 iteration 수입니다.

`checkpointInterval`

session이 checkpoint를 저장하기 전에 완료하는 iteration 수입니다.

`iterations`

session의 전체 iteration 수입니다.

현재 페이지: init(sessionDirectory:reportInterval:checkpointInterval:iterations:)
