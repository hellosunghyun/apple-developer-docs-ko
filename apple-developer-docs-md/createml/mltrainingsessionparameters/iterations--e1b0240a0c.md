---
title: "iterations | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.157663+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLTrainingSessionParameters](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)
    
*   iterations

instance property

iterations
==========

training session의 최대 iteration 수입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 11.0+tvOS 16.0+visionOS 1.0+

    var iterations: Int

[논의](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations#discussion)

-------------------------------------------------------------------------------------------------------------------

각 iteration은 training data 전체를 한 번 통과하는 것으로, epoch라고도 부릅니다. training이 수렴하면 iteration 수가 이보다 적어도 중지될 수 있습니다. 이 제한은 재개한 training session에도 적용됩니다. 원래 제한을 넘어 training을 계속하려면 재개 전에 제한을 늘립니다.

[같이 보기](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations#see-also)

---------------------------------------------------------------------------------------------------------------

### [session parameter 구성](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations#Configuring-the-sessions-parameters)

[`let sessionDirectory: URL?`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory)

session이 진행 상태를 저장하는 file system 위치입니다.

[`var reportInterval: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/reportinterval)

session이 진행 상태를 보고하기 전에 완료하는 iteration 수입니다.

[`var checkpointInterval: Int`](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/checkpointinterval)

session이 checkpoint를 저장하기 전에 완료하는 iteration 수입니다.

현재 페이지는 iterations입니다
