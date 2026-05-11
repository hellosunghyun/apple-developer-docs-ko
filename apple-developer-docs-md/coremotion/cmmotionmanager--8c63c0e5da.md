---
title: "CMMotionManager | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmotionmanager"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.868852+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmotionmanager#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   CMMotionManager

class

CMMotionManager
===============

motion service를 시작하고 관리하는 object입니다.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.1+visionOS 1.0+watchOS 2.0+

    class CMMotionManager

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmotionmanager#mentions)

----------------------------------------------------------------------------------------------

[raw accelerometer event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

[raw gyroscope event 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

[processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

[개요](https://developer.apple.com/documentation/coremotion/cmmotionmanager#overview)

------------------------------------------------------------------------------------------

[`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 object를 사용해 기기 내장 sensor가 감지한 움직임을 보고하는 service를 시작합니다. 이 object로 다음 네 가지 motion data를 받을 수 있습니다.

*   **Accelerometer data**: 3차원 공간에서 기기의 순간 가속도를 나타냅니다.
    
*   **Gyroscope data**: 기기의 세 주축을 기준으로 한 순간 회전을 나타냅니다.
    
*   **Magnetometer data**: 지구 자기장에 대한 기기의 방향을 나타냅니다.
    
*   **Device-motion data**: 사용자가 기기에 가한 가속도, attitude, rotation rate, calibration된 자기장 기준 방향, 중력 기준 방향처럼 motion과 관련된 핵심 특성을 나타냅니다. 이 data는 Core Motion의 sensor fusion algorithm이 제공합니다.
    

처리된 device-motion data는 기기의 attitude, rotation rate, calibration된 자기장, 중력 방향, 그리고 사용자가 기기에 더한 가속도 양을 제공합니다.

지정한 update interval로 live sensor data를 받을 수도 있고, sensor가 data를 수집해 나중에 가져오도록 할 수도 있습니다. 어느 방식을 사용하든 data가 더 이상 필요 없을 때는 적절한 stop method([`stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())
, [`stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())
, [`stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())
, [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
)를 호출합니다.

### [Receive regular motion updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Receive-regular-motion-updates)

특정 interval로 motion data를 받으려면 app이 operation queue([`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue)
 instance)와 해당 update를 처리할 특정 type의 block handler를 받는 start method를 호출합니다. motion data는 block handler로 전달됩니다. update 빈도는 interval property 값으로 결정됩니다.

*   **Accelerometer.** update interval을 지정하려면 [`accelerometerUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)
     property를 설정합니다. [`startAccelerometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))
     method를 호출하고 [`CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)
    type의 block을 전달합니다. accelerometer data는 [`CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)
     object로 block에 전달됩니다.
    
*   **Gyroscope.** update interval을 지정하려면 [`gyroUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)
     property를 설정합니다. [`startGyroUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))
     method를 호출하고 [`CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)
    type의 block을 전달합니다. rotation-rate data는 [`CMGyroData`](https://developer.apple.com/documentation/coremotion/cmgyrodata)
     object로 block에 전달됩니다.
    
*   **Magnetometer.** update interval을 지정하려면 [`magnetometerUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)
     property를 설정합니다. [`startMagnetometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))
     method를 호출하고 [`CMMagnetometerHandler`](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)
    type의 block을 전달합니다. magnetic-field data는 [`CMMagnetometerData`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)
     object로 block에 전달됩니다.
    
*   **Device motion.** update interval을 지정하려면 [`deviceMotionUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)
     property를 설정합니다. [`startDeviceMotionUpdates(using:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))
    또는 [`startDeviceMotionUpdates(using:to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))
     또는 [`startDeviceMotionUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))
     method를 호출하고 [`CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)
    type의 block을 전달합니다. 첫 번째 method를 사용하면 attitude estimate에 사용할 reference frame을 지정할 수 있습니다. rotation-rate data는 [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
     object로 block에 전달됩니다.
    

### [Sample motion data periodically](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Sample-motion-data-periodically)

주기적으로 motion data를 sample하려면 parameter를 받지 않는 method로 motion service를 시작하고, 주기적으로 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
의 property에 접근합니다. 이 방식은 game 같은 app에 권장됩니다. accelerometer data를 block으로 처리하면 추가 overhead가 생기고, 대부분의 game app은 frame을 render할 때 최신 motion data sample만 필요하기 때문입니다.

*   **Accelerometer.** [`startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())
     를 호출해 update를 시작하고 [`accelerometerData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)
     property를 읽어 [`CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)
     object에 주기적으로 접근합니다.
    
*   **Gyroscope.** [`startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())
     를 호출해 update를 시작하고 [`gyroData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)
     property를 읽어 [`CMGyroData`](https://developer.apple.com/documentation/coremotion/cmgyrodata)
     object에 주기적으로 접근합니다.
    
*   **Magnetometer.** [`startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())
     를 호출해 update를 시작하고 [`magnetometerData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)
     property를 읽어 [`CMMagnetometerData`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)
     object에 주기적으로 접근합니다.
    
*   **Device motion.** [`startDeviceMotionUpdates(using:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))
     또는 [`startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())
     method를 호출해 update를 시작하고 [`deviceMotion`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)
     property를 읽어 [`CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)
     object에 주기적으로 접근합니다. [`startDeviceMotionUpdates(using:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))
     method를 사용하면 attitude estimate용 reference frame을 지정할 수 있습니다.
    

### [Determine hardware availability and state](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Determine-hardware-availability-and-state)

hardware feature(예: gyroscope)가 기기에서 사용할 수 없으면, 해당 feature와 관련된 start method를 호출해도 아무 동작도 하지 않습니다. hardware feature를 사용할 수 있는지 또는 활성 상태인지 확인하려면 적절한 property를 검사합니다. 예를 들어 gyroscope data는 [`isGyroAvailable`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroavailable)
 또는 [`isGyroActive`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive)
 property 값을 확인합니다.

### [Identify the coordinate axes of the device](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Identify-the-coordinate-axes-of-the-device)

accelerometer, gyroscope, 또는 attitude 정보를 해석하려면 기기 coordinate axis의 방향을 알아야 합니다. 다음 그림은 motion 기능을 지원하는 Apple 기기에서 양의 x-axis, 양의 y-axis, 양의 z-axis를 보여줍니다.

![iPhone, iPad, Apple Watch, Apple Vision Pro에 양의 x-axis, 양의 y-axis, 양의 z-axis를 표시한 그림입니다.](https://docs-assets.developer.apple.com/published/b702f8aa95f1359d3b1b7a05b575569b/media-4302073%402x.png)

[주제](https://developer.apple.com/documentation/coremotion/cmmotionmanager#topics)

--------------------------------------------------------------------------------------

### [Determining the Availability of Services](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Determining-the-Availability-of-Services)

[`var isDeviceMotionAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable)

device에서 device-motion service를 사용할 수 있는지 나타내는 Boolean 값입니다.

[`var isAccelerometerAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeravailable)

device에서 accelerometer를 사용할 수 있는지 나타내는 Boolean 값입니다.

[`var isGyroAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroavailable)

device에서 gyroscope를 사용할 수 있는지 나타내는 Boolean 값입니다.

[`var isMagnetometerAvailable: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeravailable)

device에서 magnetometer를 사용할 수 있는지 나타내는 Boolean 값입니다.

### [Determining Which Services Are Active](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Determining-Which-Services-Are-Active)

[`var isDeviceMotionActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)

app이 device-motion service의 update를 받고 있는지 판단하는 Boolean 값입니다.

[`var isAccelerometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive)

accelerometer update가 현재 진행 중인지 나타내는 Boolean 값입니다.

[`var isGyroActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive)

gyroscope update가 현재 진행 중인지 판단하는 Boolean 값입니다.

[`var isMagnetometerActive: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive)

magnetometer update가 현재 진행 중인지 판단하는 Boolean 값입니다.

### [Managing Device Motion Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Managing-Device-Motion-Updates)

[`var showsDeviceMovementDisplay: Bool`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)

device-movement display를 표시할지 제어합니다.

[`var deviceMotionUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)

block handler에 device-motion update를 제공하는 초 단위 interval입니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))

지정한 reference frame과 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))

지정한 block handler를 사용해 operation queue에서 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:))

reference frame을 사용해 block handler 없이 device-motion update를 시작합니다.

[`func startDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates())

block handler 없이 device-motion update를 시작합니다.

[`func stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())

device-motion update를 중지합니다.

[`var deviceMotion: CMDeviceMotion?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)

최신 device-motion data sample입니다.

[`typealias CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

device-motion data를 처리하는 block callback type입니다.

### [Managing Accelerometer Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Managing-Accelerometer-Updates)

[`var accelerometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)

block handler에 accelerometer update를 제공하는 초 단위 interval입니다.

[`func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 accelerometer update를 시작합니다.

[`func startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())

handler 없이 accelerometer update를 시작합니다.

[`func stopAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())

accelerometer update를 중지합니다.

[`var accelerometerData: CMAccelerometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)

최신 accelerometer data sample입니다.

[`typealias CMAccelerometerHandler`](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

accelerometer data를 처리하는 block callback type입니다.

### [Managing Gyroscope Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Managing-Gyroscope-Updates)

[`var gyroUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)

block handler에 gyroscope update를 제공하는 초 단위 interval입니다.

[`func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 gyroscope update를 시작합니다.

[`func startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())

handler 없이 gyroscope update를 시작합니다.

[`func stopGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())

gyroscope update를 중지합니다.

[`var gyroData: CMGyroData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)

최신 gyroscope data sample입니다.

[`typealias CMGyroHandler`](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

gyroscope data를 처리하는 block callback type입니다.

### [Managing Magnetometer Updates](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Managing-Magnetometer-Updates)

[`var magnetometerUpdateInterval: TimeInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)

system이 block handler에 magnetometer data를 전달하는 초 단위 interval입니다.

[`func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates(to:withhandler:))

지정한 handler와 함께 operation queue에서 magnetometer update를 시작합니다.

[`func startMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())

block handler 없이 magnetometer update를 시작합니다.

[`func stopMagnetometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())

magnetometer update를 중지합니다.

[`var magnetometerData: CMMagnetometerData?`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)

최신 magnetometer data sample입니다.

[`typealias CMMagnetometerHandler`](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

magnetometer data를 처리하는 block callback type입니다.

### [Accessing Attitude Reference Frames](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Accessing-Attitude-Reference-Frames)

[`var attitudeReferenceFrame: CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe)

현재 사용 중인 reference frame 또는 기본 attitude reference frame을 반환합니다.

[`class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/availableattitudereferenceframes())

현재 device의 attitude를 보고하는 데 사용할 수 있는 reference frame의 bitmask를 반환합니다.

### [Understanding Errors](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Understanding-Errors)

[`let CMErrorDomain: String`](https://developer.apple.com/documentation/coremotion/cmerrordomain)

Core Motion의 error domain입니다.

[`struct CMError`](https://developer.apple.com/documentation/coremotion/cmerror)

motion error를 정의합니다.

[관계](https://developer.apple.com/documentation/coremotion/cmmotionmanager#relationships)

----------------------------------------------------------------------------------------------------

### [상속 대상](https://developer.apple.com/documentation/coremotion/cmmotionmanager#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/coremotion/cmmotionmanager#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/coremotion/cmmotionmanager#see-also)

------------------------------------------------------------------------------------------

### [Essentials](https://developer.apple.com/documentation/coremotion/cmmotionmanager#Essentials)

[Core Motion 업데이트](https://developer.apple.com/documentation/Updates/CoreMotion)

Core Motion의 중요한 변경 사항을 알아봅니다.

현재 페이지: CMMotionManager
