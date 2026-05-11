---
title: "sessionIdentifiers | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.031674+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRKeyboardMetrics](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics)
    
*   sessionIdentifiers

instance property

sessionIdentifiers
==================

sample에 metrics를 보고하는 keyboard session의 identifier입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    var sessionIdentifiers: [String] { get }

[설명](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers#Discussion)

------------------------------------------------------------------------------------------------------------------

keyboard session은 system이 keyboard를 표시할 때 시작하고 dismiss할 때 끝납니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers#see-also)

--------------------------------------------------------------------------------------------------------------

### [Keyboard configuration 및 session 확인](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers#Inspecting-Keyboard-Configuration-and-Sessions)

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/duration)

report가 다루는 duration입니다.

[`var keyboardIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/keyboardidentifier)

keyboard list에서 keyboard의 identifier입니다.

[`var version: String`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/version)

keyboard metrics의 version입니다.

[`var width: Measurement<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/width)

report에 포함된 keyboard의 너비(mm)입니다.

[`var height: Measurement<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/height)

report에 포함된 keyboard의 높이(mm)입니다.

[`var inputModes: [String]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/inputmodes)

session에서 활성화된 keyboard language입니다.

현재 페이지는 sessionIdentifiers
