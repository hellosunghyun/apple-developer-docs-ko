---
title: "SRDevice | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdevice"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.044129+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdevice#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRDevice

class

SRDevice
========

sample data를 제공하는 device를 나타내는 표현입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRDevice

[개요](https://developer.apple.com/documentation/sensorkit/srdevice#overview)

----------------------------------------------------------------------------------

이 class는 iOS 및 watchOS device를 지원합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srdevice#topics)

------------------------------------------------------------------------------

### [Device 정보 접근](https://developer.apple.com/documentation/sensorkit/srdevice#Accessing-Device-Information)

[`var model: String`](https://developer.apple.com/documentation/sensorkit/srdevice/model)

사용자가 정의한 device 이름입니다.

[`var name: String`](https://developer.apple.com/documentation/sensorkit/srdevice/name)

framework가 정의한 device 이름입니다.

[`var systemName: String`](https://developer.apple.com/documentation/sensorkit/srdevice/systemname)

device의 operating system입니다.

[`var systemVersion: String`](https://developer.apple.com/documentation/sensorkit/srdevice/systemversion)

device의 operating system version입니다.

[`var productType: String`](https://developer.apple.com/documentation/sensorkit/srdevice/producttype)

sample 저장에 사용된 device를 식별하는 string입니다.

### [기본 Device 접근](https://developer.apple.com/documentation/sensorkit/srdevice#Accessing-the-Primary-Device)

[`class var current: SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice/current)

app을 실행하는 device입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srdevice#relationships)

--------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srdevice#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srdevice#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srdevice#see-also)

----------------------------------------------------------------------------------

### [Device 선택](https://developer.apple.com/documentation/sensorkit/srdevice#Selecting-the-Device)

[`var device: SRDevice`](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device)

sample data를 query할 device입니다.

현재 페이지는 SRDevice입니다
