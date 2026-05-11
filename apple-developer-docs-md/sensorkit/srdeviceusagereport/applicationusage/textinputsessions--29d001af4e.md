---
title: "textInputSessions | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050649+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
    
*   *   [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
        
*   [SRDeviceUsageReport.ApplicationUsage](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)
    
*   textInputSessions

instance property

textInputSessions
=================

application usage 중 발생하는 text input session type입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+

    var textInputSessions: [SRTextInputSession] { get }

[설명](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions#Discussion)

------------------------------------------------------------------------------------------------------------------------------------

이 property에는 사용자가 app에서 text를 입력할 때 framework가 기록하는 text와 input source가 들어 있습니다. text-input session은 사용자가 keyboard를 띄울 때 시작되고 keyboard가 사라질 때 끝납니다. 다만 framework는 20단어보다 적은 text-input session을 이후 text-input session과 합쳐 최소 20단어에 도달할 때까지 결합합니다. framework는 input mode([`inputModes`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/inputmodes)
)를 분리해서, 한 input mode가 다른 mode의 text-input session(예: Spanish-Mexico)과 결합되지 않도록 합니다.

[관련 항목](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions#see-also)

--------------------------------------------------------------------------------------------------------------------------------

### [text input 확인하기](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions#Inspecting-Text-Input)

[`class SRTextInputSession`](https://developer.apple.com/documentation/sensorkit/srtextinputsession)

특정 keyboard에 대해 사용자가 입력한 문자입니다.

현재 페이지: textInputSessions
