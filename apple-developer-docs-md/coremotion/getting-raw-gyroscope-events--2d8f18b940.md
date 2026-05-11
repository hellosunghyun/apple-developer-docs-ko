---
title: "Getting raw gyroscope events | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.870536+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   raw gyroscope event 가져오기

문서

raw gyroscope event 가져오기
============================

onboard gyroscope에서 data를 가져옵니다.

[개요](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#overview)

-------------------------------------------------------------------------------------------------------

gyroscope는 device가 공간 축을 중심으로 회전하는 속도를 측정합니다. 많은 iOS device에는 3축 gyroscope가 있으며, 다음 그림에 나온 세 축 각각의 rotation value를 제공합니다. rotation value는 해당 축을 기준으로 초당 radian 단위로 측정합니다. rotation value는 회전 방향에 따라 양수일 수도 음수일 수도 있습니다.

![gyroscope가 x, y, z축을 기준으로 rotation rate를 측정하는 모습](https://docs-assets.developer.apple.com/published/cd1feafe8399d86e120bf5f723a12459/media-2904021%402x.png)

Core Motion framework의 class를 사용해 raw gyroscope data에 접근합니다. 구체적으로는 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 class가 gyroscope hardware를 활성화하는 interface를 제공합니다. hardware를 활성화할 때는 app에 가장 적합한 interface를 선택합니다. 필요할 때만 gyroscope data를 pull할 수도 있고, framework가 일정한 간격으로 app에 update를 push하도록 요청할 수도 있습니다. 각 방식은 configuration 단계가 다르고 적합한 use case도 다릅니다.

gyroscope interface가 제공하는 raw rotation rate data는 temperature 같은 다른 요인의 bias를 받을 수 있습니다. app에 bias가 없는 rotation value가 필요하다면 대신 device-motion interface를 사용합니다. device-motion interface는 특수 algorithm을 사용해 bias를 제거하고 더 정밀한 rotation value를 제공합니다. 자세한 내용은 [processed device-motion data 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)
를 참고하십시오.

device type별 coordinate axis 정보는 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
를 참고하십시오.

### [gyroscope data 사용 가능 여부 확인하기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#Check-for-the-availability-of-gyroscope-data)

여러 이유로 gyroscope data를 사용할 수 없을 수 있으므로, 가져오기 전에 먼저 data가 사용 가능한지 확인합니다. `CMMotionManager`의 [`isGyroAvailable`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroavailable)
 property 값을 확인해 `true`인지 점검합니다. `false`라면 update를 시작해도 app에 어떤 data도 전달되지 않습니다.

### [필요할 때만 gyroscope data 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#Get-gyroscope-data-only-when-you-need-it)

game처럼 자체 schedule에 따라 gyroscope data를 처리하는 app은 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
의 [`startGyroUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())
 method를 사용해 rotation data 전달을 시작합니다. 이 method를 호출하면 system이 gyroscope hardware를 활성화하고 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 object의 [`gyroData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)
 property를 업데이트하기 시작합니다. 하지만 system은 그 property가 업데이트될 때 별도로 알려주지 않습니다. rotation data가 필요할 때 직접 property 값을 확인해야 합니다.

gyroscope update 전달을 시작하기 전에 [`gyroUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)
 property에 값을 할당해 update 주기를 지정합니다. 요청할 수 있는 최대 주파수는 hardware에 따라 다르지만 보통 최소 100 Hz 이상입니다. hardware가 지원하는 범위를 넘는 주파수를 요청하면 Core Motion이 대신 지원 가능한 최대값을 사용합니다.

다음 예제는 초당 50회 gyroscope update가 일어나도록 설정하는 method를 보여 줍니다. 이어서 같은 주기로 update를 가져오고 data를 처리하는 timer도 설정합니다. timer를 더 낮은 주기로 동작하게 할 수도 있지만, 실제로 쓰지 않는 update를 hardware가 더 많이 생성하게 되어 전력을 낭비할 수 있습니다.

    func startGyros() {
       if motion.isGyroAvailable {
          self.motion.gyroUpdateInterval = 1.0 / 50.0
          self.motion.startGyroUpdates()
    
    
          // accelerometer data를 가져올 timer를 설정합니다.
          self.timer = Timer(fire: Date(), interval: (1.0/50.0), 
                 repeats: true, block: { (timer) in
             // gyro data를 가져옵니다.
             if let data = self.motion.gyroData {
                let x = data.rotationRate.x
                let y = data.rotationRate.y
                let z = data.rotationRate.z
    
    
                // app에서 gyroscope data를 사용합니다. 
             }
          })
    
    
          // 현재 run loop에 timer를 추가합니다.
          RunLoop.current.add(self.timer!, forMode: .defaultRunLoopMode)
       }
    }
    
    
    func stopGyros() {
       if self.timer != nil {
          self.timer?.invalidate()
          self.timer = nil
    
    
          self.motion.stopGyroUpdates()
       }
    }
    

### [지속적인 gyroscope update stream 처리하기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#Process-a-steady-stream-of-gyroscope-updates)

움직임 pattern 분석처럼 모든 gyroscope data를 빠짐없이 수집하려면 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
의 [`startGyroUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))
 method를 사용합니다. 이 method는 지정한 queue에서 handler block을 실행해 새로운 rotation value 집합이 생길 때마다 app으로 push합니다. block이 queue에 쌓이므로 app이 잠시 바빠서 update를 바로 처리하지 못하더라도 모든 gyroscope data를 받을 수 있습니다.

gyroscope update 전달을 시작하기 전에 [`gyroUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)
 property에 값을 할당해 update 주기를 지정합니다. 요청할 수 있는 최대 주파수는 hardware에 따라 다르지만 보통 최소 100 Hz 이상입니다. hardware가 지원하는 범위를 넘는 주파수를 요청하면 Core Motion이 대신 지원 가능한 최대값을 사용합니다.

다음 예제는 [MotionGraphs](https://developer.apple.com/library/archive/samplecode/MotionGraphs/Introduction/Intro.html#//apple_ref/doc/uid/DTS40012333)
 sample code project의 method를 보여 줍니다. 더 많은 문맥이 필요하면 이 project를 직접 확인할 수 있습니다. 이 app은 내장 gyroscope에서 받은 rotation data를 실시간 graph로 표시합니다. 사용자는 slider로 gyroscope update 주기를 조정하고, slider 값이 바뀌면 예제에 나온 `startUpdatesWithSliderValue:` method가 호출됩니다. 이 method는 새 주기로 gyroscope update를 다시 시작합니다. 새 sample을 받을 때마다 지정된 block이 main thread에 queue됩니다. 그 block이 app의 graph view와 label을 새로운 rotation value로 업데이트합니다.

    static const NSTimeInterval gyroMin = 0.01;
    - (void)startUpdatesWithSliderValue:(int)sliderValue {
       // update interval을 결정합니다
       NSTimeInterval delta = 0.005;
       NSTimeInterval updateInterval = gyroMin + delta * sliderValue;
    
    
       // CMMotionManager를 생성합니다
       CMMotionManager *mManager = [(APLAppDelegate *)\
                [[UIApplication sharedApplication] delegate] sharedManager];
       APLGyroGraphViewController * __weak weakSelf = self;
    
    
       // gyroscope를 사용할 수 있는지 확인합니다
       if ([mManager isGyroAvailable] == YES) {
          // motion manager에 update interval을 할당합니다
          [mManager setGyroUpdateInterval:updateInterval];
          [mManager startGyroUpdatesToQueue:[NSOperationQueue mainQueue] \
                   withHandler:^(CMGyroData *gyroData, NSError *error) {\
             [weakSelf.graphView addX:gyroData.rotationRate.x \
                      y:gyroData.rotationRate.y \
                      z:gyroData.rotationRate.z];\
             [weakSelf setLabelValueX:gyroData.rotationRate.x \
                      y:gyroData.rotationRate.y \
                      z:gyroData.rotationRate.z];\
          }];
       }
       self.updateIntervalLabel.text = [NSString stringWithFormat:@"%f", updateInterval];
    }
    - (void)stopUpdates{
       CMMotionManager *mManager = [(APLAppDelegate *)\
                [[UIApplication sharedApplication] delegate] sharedManager];
       if ([mManager isGyroActive] == YES) {
          [mManager stopGyroUpdates];
       }
    }
    

[같이 보기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#see-also)

-------------------------------------------------------------------------------------------------------

### [Gyroscope](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events#Gyroscopes)

[`class CMGyroData`](https://developer.apple.com/documentation/coremotion/cmgyrodata)

device rotation rate의 단일 측정값입니다.

현재 페이지: Getting raw gyroscope events
