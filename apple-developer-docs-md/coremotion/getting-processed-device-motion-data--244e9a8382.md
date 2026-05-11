---
title: "Getting processed device-motion data | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.868301+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   processed device-motion data 가져오기

문서

processed device-motion data 가져오기
====================================

gravity의 영향처럼 환경에서 생기는 bias를 제거하도록 system이 처리한 motion data를 가져옵니다.

[개요](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#overview)

---------------------------------------------------------------------------------------------------------------

Core Motion framework는 accelerometer, gyroscope, magnetometer를 포함한 여러 hardware sensor의 raw data에 접근할 수 있게 해줍니다. raw data는 유용하지만 때로는 필요하지 않은 추가 정보도 포함합니다. 예를 들어 raw accelerometer data에는 gravity로 인한 acceleration과 device motion으로 인한 acceleration이 모두 들어 있습니다. device 고유의 acceleration만 얻으려면 raw data 값에서 gravitational acceleration을 제거해야 합니다. 이 data를 제거하려면 추가 정보와 처리 시간이 더 필요합니다.

원하는 data를 더 쉽게 얻을 수 있도록 device-motion service는 raw data를 처리하고 다음 값을 제공합니다.

*   3차원 공간에서의 device attitude(orientation)
    
*   bias가 제거된 device rotation rate
    
*   현재 gravity vector
    
*   device 고유의 acceleration(gravity 제외)
    
*   현재 magnetic field vector
    

device-motion service는 여러 sensor의 정보를 조합해 위 결과를 제공합니다. device-motion service는 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
, [`CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)
, [`CMBatchedSensorManager`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
에서 사용할 수 있습니다. accelerometer나 gyroscope data 없이는 app이 동작할 수 없다면 app의 required device capabilities 목록에 해당 hardware를 포함하도록 업데이트합니다. required device capabilities를 지정하는 방법은 [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiredDeviceCapabilities)
를 참고합니다.

### [motion data 사용 가능 여부 확인](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#Check-for-the-availability-of-motion-data)

device-motion data는 여러 이유로 제공되지 않을 수 있으므로 시작하기 전에 service가 사용 가능한지 확인합니다. `CMMotionManager`의 [`isDeviceMotionAvailable`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable)
 property 값을 확인해 `true`인지 확인합니다. 값이 `false`이면 service를 시작해도 app에는 data가 전달되지 않습니다.

### [attitude data를 해석할 reference frame 선택](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#Choose-a-frame-of-reference-for-interpreting-attitude-data)

device의 attitude는 device 각 축을 기준으로 얼마나 회전했는지를 뜻합니다. device-motion service는 알려진 device orientation을 기준으로 한 attitude 값을 보고하며, 이를 device의 frame of reference라고도 부릅니다. device-motion service를 시작할 때 Core Motion이 사용할 frame of reference를 지정합니다.

기본 frame of reference는 [`xArbitraryZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)
이며, 이 값은 z축을 지면과 수직으로 두고 x축과 y축을 공간에서의 현재 device orientation에 맞춥니다. 이 옵션이나 [`xArbitraryCorrectedZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)
 옵션을 사용하면 device의 초기 시작 위치를 기준으로 변화를 측정할 수 있습니다. 예를 들어 골프 스윙 분석 app은 사람의 골프 스윙을 측정하기 위해 이 frame of reference를 사용할 수 있습니다. compass나 navigation app이라면 각각 특정 magnetic north와 true north를 기준으로 device orientation을 보고하는 [`xMagneticNorthZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical)
 또는 [`xTrueNorthZVertical`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical)
 frame of reference를 선택합니다.

device-motion service를 시작할 때 원하는 reference frame을 지정합니다. `CMMotionManager` object는 선택한 frame of reference를 [`attitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe)
 property에 저장하고 기본 선택으로 사용합니다.

device orientation이 frame of reference orientation과 일치하면 보고된 `CMAttitude`의 [`roll`](https://developer.apple.com/documentation/coremotion/cmattitude/roll)
, [`pitch`](https://developer.apple.com/documentation/coremotion/cmattitude/pitch)
, [`yaw`](https://developer.apple.com/documentation/coremotion/cmattitude/yaw)
 회전 값은 모두 `0`이 됩니다. 사용자가 device를 회전하면 roll, pitch, yaw 값이 frame of reference를 기준으로 한 회전량(라디안)을 나타냅니다. 다음 그림은 각 축 기준으로 이 값을 해석하는 방법을 보여 줍니다. 회전 값의 범위는 -π부터 π까지입니다.

![x, y, z축을 기준으로 rotation rate를 측정하는 gyroscope](https://docs-assets.developer.apple.com/published/64b92fc751671c47e15435b373ffc1bf/media-4251993%402x.png)

서로 다른 device type의 coordinate axis에 대한 정보는 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 또는 [`CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)
를 참고합니다.

### [device-motion update 시작](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#Start-device-motion-updates)

device-motion data 수집을 시작하려면 `CMMotionManager` object를 만들고 적절한 method 중 하나를 호출합니다. Core Motion은 device-motion update를 처리하는 두 가지 옵션을 제공합니다.

*   closure를 사용해 일정한 stream의 update를 처리합니다.
    
*   필요할 때 update를 처리합니다.
    

두 옵션 모두 `CMMotionManager` type의 [`deviceMotionUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)
 property를 사용해 system update 빈도를 지정해야 합니다. 최대 update 빈도는 hardware에 따라 다르지만 보통 최소 100 Hz입니다. hardware가 지원하는 수준보다 더 큰 update 빈도를 지정하면 Core Motion은 대신 최대 빈도를 사용합니다.

다음 예제는 device-motion service가 초당 50회 update를 전달하고 magnetic north를 기준으로 attitude data를 전달하도록 구성합니다. closure 없이 device motion을 시작하는 경우에는 `CMMotionManager`의 [`deviceMotion`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)
 property를 정기적으로 확인하는 책임이 사용자에게 있습니다. 이 예제는 timer를 설정해 property 값을 확인하고 최신 data를 app content에 반영합니다.

    func startDeviceMotion() {
        if motion.isDeviceMotionAvailable {
            self.motion.deviceMotionUpdateInterval = 1.0 / 50.0
            self.motion.showsDeviceMovementDisplay = true
            self.motion.startDeviceMotionUpdates(using: .xMagneticNorthZVertical)
            
            // Configure a timer to fetch the motion data.
            self.timer = Timer(fire: Date(), interval: (1.0 / 50.0), repeats: true,
                               block: { (timer) in
                                if let data = self.motion.deviceMotion {
                                    // Get the attitude relative to the magnetic north reference frame.
                                    let x = data.attitude.pitch
                                    let y = data.attitude.roll
                                    let z = data.attitude.yaw
                                    
        // app에서 motion data를 사용합니다.
                                }
            })
            
            // Add the timer to the current run loop.
            RunLoop.current.add(self.timer!, forMode: RunLoop.Mode.default)
        }
    }
    

지속적으로 들어오는 event stream을 처리하려면 [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue)
 object와 [`CMDeviceMotionHandler`](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)
 type의 closure를 사용해 device-motion service를 시작합니다. Core Motion이 새 data 값을 받을 때마다 operation queue에서 closure를 실행합니다. 각 data 값에는 [`timestamp`](https://developer.apple.com/documentation/coremotion/cmlogitem/timestamp)
 값이 함께 제공되며, 이를 사용해 data의 시의성을 확인하고 특정 기준보다 오래된 data를 버릴 수 있습니다. 다음 예제는 operation queue를 사용해 초당 60회의 update를 처리합니다.

    func startQueuedUpdates() {
       if motion.isDeviceMotionAvailable {
          self.motion.deviceMotionUpdateInterval = 1.0 / 60.0
          self.motion.showsDeviceMovementDisplay = true
          self.motion.startDeviceMotionUpdates(using: .xMagneticNorthZVertical, 
                   to: self.queue, withHandler: { (data, error) in
             // Make sure the data is valid before accessing it.
             if let validData = data {
                // Get the attitude relative to the magnetic north reference frame. 
                let roll = validData.attitude.roll
                let pitch = validData.attitude.pitch
                let yaw = validData.attitude.yaw
    
    
        // app에서 motion data를 사용합니다.
             }
          })
       }
    }
    
    
    

### [device-motion update 중지](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#Stop-device-motion-updates)

device battery 수명에 미치는 영향을 최소화하려면 motion data가 더 이상 필요 없을 때 항상 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 object의 [`stopDeviceMotionUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopdevicemotionupdates())
 method를 호출합니다. device-motion service는 특수 hardware를 사용해 motion data를 수집하며, 이 hardware를 실행하면 추가 전력이 소모됩니다. 특히 다음 경우에는 service를 중지합니다.

*   app이 비활성화되거나 background로 들어갈 때
    
*   사용자가 motion data가 필요한 기능과 상호작용을 멈췄을 때
    
*   app이 필요한 motion data를 모두 얻는 즉시
    

app이 constant motion update를 필요로 하지 않는다면 device-motion service를 시작하고, 필요한 data를 가져온 뒤, 즉시 service를 중지합니다. 꼭 필요한 시간보다 오래 service를 실행하지 마십시오.

[참고 항목](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#see-also)

---------------------------------------------------------------------------------------------------------------

### [Device motion](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data#Device-motion)

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

device의 attitude, rotation rate, acceleration 측정을 캡슐화한 값입니다.

[`class CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)

특정 시점에서 알려진 frame of reference를 기준으로 한 device orientation입니다.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

attitude 관련 motion data의 frame of reference를 나타내는 constant입니다.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

headphone motion service를 시작하고 관리하는 object입니다.

현재 페이지는 Getting processed device-motion data입니다
