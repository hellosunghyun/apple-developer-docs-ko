---
title: "sessionDirectory | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.147478+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTrainingSessionParameters](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
    
*   sessionDirectory

instance property

sessionDirectory
================

session이 진행 상황을 저장하는 file system 위치입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    let sessionDirectory: URL?

[같이 보기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory#see-also)

---------------------------------------------------------------------------------------------------------------------

### [Configuring the session’s parameters](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory#Configuring-the-sessions-parameters)

[`var reportInterval: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/reportinterval)

session이 진행 상황을 보고하기 전에 완료하는 iteration 수입니다.

[`var checkpointInterval: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/checkpointinterval)

session이 checkpoint를 저장하기 전에 완료하는 iteration 수입니다.

[`var iterations: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations)

training session의 최대 iteration 수입니다.

현재 페이지: sessionDirectory
