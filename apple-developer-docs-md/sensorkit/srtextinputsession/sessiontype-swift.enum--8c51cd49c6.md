---
title: "SRTextInputSession.SessionType | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.051614+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRTextInputSession](https://developer.apple.com/documentation/sensorkit/srtextinputsession)
    
*   SRTextInputSession.SessionType

enum

SRTextInputSession.SessionType
==============================

session 동안 text를 입력하는 방법입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+

    enum SessionType

[개요](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#overview)

-------------------------------------------------------------------------------------------------------------------

이 class는 [`sessionType`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.property)
 property에 사용할 수 있는 option을 정의합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#topics)

---------------------------------------------------------------------------------------------------------------

### [입력 소스](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#Sources)

[`case dictation`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum/dictation)

session에 spoken text가 포함되어 있음을 나타냅니다.

[`case keyboard`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum/keyboard)

session에 keyboard input으로 입력한 text가 포함되어 있음을 나타냅니다.

[`case pencil`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum/pencil)

session에 Apple Pencil로 그린 text가 포함되어 있음을 나타냅니다.

[`case thirdPartyKeyboard`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum/thirdpartykeyboard)

session에 third-party keyboard에서 입력한 text가 포함되어 있음을 나타냅니다.

### [initializer](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#Initializers)

[`init?(rawValue: Int)`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum/init(rawvalue:))

[관계](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#relationships)

-----------------------------------------------------------------------------------------------------------------------------

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#conforms-to)

*   [`BitwiseCopyable`](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#see-also)

-------------------------------------------------------------------------------------------------------------------

### [text 소스 확인](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum#Inspecting-Text-Source)

[`var sessionType: SRTextInputSession.SessionType`](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.property)

현재 페이지는 SRTextInputSession.SessionType입니다
