---
title: "CMDeviceMotion | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmdevicemotion"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.869132+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMDeviceMotion

class

CMDeviceMotion
==============

device의 attitude, rotation rate, acceleration 측정값을 캡슐화한 object입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+macOS 10.15+visionOS 1.0+watchOS 2.0+

    class CMDeviceMotion

[개요](https://developer.apple.com/documentation/coremotion/cmdevicemotion#overview)

-----------------------------------------------------------------------------------------

An application receives or samples `CMDeviceMotion` objects at regular intervals after calling the [`startDeviceMotionUpdates(using:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))
 method, the [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))
 method, the [`startDeviceMotionUpdates(using:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))
 method, or the [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
 method of the [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 class.

accelerometer는 gravity와 user acceleration이라는 두 acceleration vector의 합을 측정합니다. User acceleration은 사용자가 device에 가한 acceleration입니다. Core Motion은 gyroscope와 accelerometer를 모두 사용해 device의 attitude를 추적할 수 있으므로 gravity와 user acceleration을 구분할 수 있습니다. `CMDeviceMotion` object는 두 측정값을 [`gravity`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/gravity)
 및 [`userAcceleration`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/useracceleration)
 property로 제공합니다.

[주제](https://developer.apple.com/documentation/coremotion/cmdevicemotion#topics)

-------------------------------------------------------------------------------------

### [Attitude와 Rotation Rate 가져오기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#Getting-Attitude-and-Rotation-Rate)

[`var attitude: CMAttitude`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/attitude)

device의 attitude입니다.

[`var rotationRate: CMRotationRate`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/rotationrate)

device의 rotation rate입니다.

### [Acceleration Data 가져오기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#Getting-Acceleration-Data)

[`var gravity: CMAcceleration`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/gravity)

device의 reference frame으로 표현한 gravity acceleration vector입니다.

[`var userAcceleration: CMAcceleration`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/useracceleration)

사용자가 device에 가하는 acceleration입니다.

### [보정된 Magnetic Field 가져오기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#Getting-the-Calibrated-Magnetic-Field)

[`var magneticField: CMCalibratedMagneticField`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/magneticfield)

device 기준의 magnetic field vector를 반환합니다.

[`struct CMCalibratedMagneticField`](https://developer.apple.com/documentation/coremotion/cmcalibratedmagneticfield)

보정된 magnetic field data와 calibration 정확도 추정값입니다.

[`enum CMMagneticFieldCalibrationAccuracy`](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)

magnetic field 추정값의 calibration 정확도를 나타냅니다.

### [Heading 가져오기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#Getting-the-Heading)

[`var heading: Double`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/heading)

현재 reference frame을 기준으로 한 heading angle(도 단위)입니다.

### [Sensor Location 가져오기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#Getting-the-Sensor-Location)

[`var sensorLocation: CMDeviceMotion.SensorLocation`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.property)

device-motion data를 계산하는 sensor의 위치입니다.

[`enum SensorLocation`](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum)

device의 sensor 위치를 정의합니다.

[관계](https://developer.apple.com/documentation/coremotion/cmdevicemotion#relationships)

---------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmdevicemotion#inherits-from)

*   [`CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmdevicemotion#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmdevicemotion#see-also)

-----------------------------------------------------------------------------------------

### [Device motion](https://developer.apple.com/documentation/coremotion/cmdevicemotion#Device-motion)

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

gravity의 영향 같은 환경 bias를 제거하도록 system이 처리한 motion data를 가져옵니다.

[`class CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)

특정 시점에서 알려진 reference frame을 기준으로 한 device의 orientation입니다.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

attitude 관련 motion data의 reference frame을 나타내는 constant입니다.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

headphone motion service를 시작하고 관리하는 object입니다.

현재 페이지: CMDeviceMotion
