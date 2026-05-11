---
title: "SRTextInputSession | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srtextinputsession"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050739+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srtextinputsession#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRTextInputSession

class

SRTextInputSession
==================

특정 keyboard에서 user가 입력한 문자입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+

    class SRTextInputSession

[개요](https://developer.apple.com/documentation/sensorkit/srtextinputsession#overview)

--------------------------------------------------------------------------------------------

framework는 keyboard가 한 번 사라진 뒤 다시 표시될 때마다 이 class의 새 instance를 생성합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srtextinputsession#topics)

----------------------------------------------------------------------------------------

### [Session 식별](https://developer.apple.com/documentation/sensorkit/srtextinputsession#Identifying-the-Session)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessionidentifier)

keyboard session의 고유 식별자입니다.

### [Text Input 타이밍](https://developer.apple.com/documentation/sensorkit/srtextinputsession#Timing-Text-Input)

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/duration)

session이 지속된 시간(초)입니다.

### [Text Source 살펴보기](https://developer.apple.com/documentation/sensorkit/srtextinputsession#Inspecting-Text-Source)

[`var sessionType: SRTextInputSession.SessionType`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.property)

[`enum SessionType`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum)

session 동안 text를 입력하는 방법입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srtextinputsession#relationships)

------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srtextinputsession#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srtextinputsession#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srtextinputsession#see-also)

--------------------------------------------------------------------------------------------

### [Text Input 살펴보기](https://developer.apple.com/documentation/sensorkit/srtextinputsession#Inspecting-Text-Input)

[`var textInputSessions: [SRTextInputSession]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/textinputsessions)

application usage 중 발생하는 text input session type입니다.

현재 페이지는 SRTextInputSession입니다
