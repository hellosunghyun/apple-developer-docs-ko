---
title: "CMAttitude | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmattitude"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.869307+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmattitude#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMAttitude

class

CMAttitude
==========

특정 시점에서 알려진 기준 frame에 대한 device의 orientation입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 2.0+

    class CMAttitude

[개요](https://developer.apple.com/documentation/coremotion/cmattitude#overview)

-------------------------------------------------------------------------------------

`CMAttitude` class는 attitude를 나타내는 세 가지 수학적 표현을 제공합니다. rotation matrix, quaternion, Euler angle(roll, pitch, yaw 값)입니다. application에 전달되는 각 [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
object의 attitude property를 통해 `CMAttitude` object에 접근합니다. application은 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
class의 [`startDeviceMotionUpdates(using:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))
method, [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))
method, [`startDeviceMotionUpdates(using:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))
method 또는 [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
method를 호출한 결과로 이 device-motion object들을 받기 시작합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmattitude#topics)

---------------------------------------------------------------------------------

### [Euler Angle로 attitude의 수학적 표현 가져오기](https://developer.apple.com/documentation/coremotion/cmattitude#Getting-a-Mathematical-Representation-of-Attitude-as-Euler-Angles)

[`var roll: Double`](https://developer.apple.com/documentation/coremotion/cmattitude/roll)

device의 roll 값(라디안)입니다.

[`var pitch: Double`](https://developer.apple.com/documentation/coremotion/cmattitude/pitch)

device의 pitch 값(라디안)입니다.

[`var yaw: Double`](https://developer.apple.com/documentation/coremotion/cmattitude/yaw)

device의 yaw 값(라디안)입니다.

### [Rotation Matrix로 attitude의 수학적 표현 가져오기](https://developer.apple.com/documentation/coremotion/cmattitude#Getting-a-Mathematical-Representation-of-Attitude-as-a-Rotation-Matrix)

[`var rotationMatrix: CMRotationMatrix`](https://developer.apple.com/documentation/coremotion/cmattitude/rotationmatrix)

device의 attitude를 나타내는 rotation matrix를 반환합니다.

[`struct CMRotationMatrix`](https://developer.apple.com/documentation/coremotion/cmrotationmatrix)

rotation matrix를 나타내는 struct type입니다.

### [Quaternion으로 attitude의 수학적 표현 가져오기](https://developer.apple.com/documentation/coremotion/cmattitude#Getting-a-Mathematical-Representation-of-Attitude-as-a-Quaternion)

[`var quaternion: CMQuaternion`](https://developer.apple.com/documentation/coremotion/cmattitude/quaternion)

device의 attitude를 나타내는 quaternion을 반환합니다.

[`struct CMQuaternion`](https://developer.apple.com/documentation/coremotion/cmquaternion)

attitude 측정을 나타내는 quaternion type입니다.

### [attitude 변화 얻기](https://developer.apple.com/documentation/coremotion/cmattitude#Obtaining-the-Change-in-Attitude)

[`func multiply(byInverseOf: CMAttitude)`](https://developer.apple.com/documentation/coremotion/cmattitude/multiply(byinverseof:))

지정한 attitude를 기준으로 attitude 변화를 구합니다.

### [초기화 method](https://developer.apple.com/documentation/coremotion/cmattitude#Initializers)

[`init?(coder: NSCoder)`](https://developer.apple.com/documentation/coremotion/cmattitude/init(coder:))

[관계](https://developer.apple.com/documentation/coremotion/cmattitude#relationships)

-----------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/coremotion/cmattitude#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/coremotion/cmattitude#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[관련 항목](https://developer.apple.com/documentation/coremotion/cmattitude#see-also)

-------------------------------------------------------------------------------------

### [Device motion](https://developer.apple.com/documentation/coremotion/cmattitude#Device-motion)

[처리된 device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

gravity의 영향처럼 환경적 bias를 제거하도록 system이 처리한 motion data를 가져옵니다.

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

device의 attitude, rotation rate, acceleration 측정을 캡슐화합니다.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

attitude 관련 motion data의 기준 frame을 나타내는 constant입니다.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

headphone motion service를 시작하고 관리하는 object입니다.

현재 페이지는 CMAttitude입니다.
