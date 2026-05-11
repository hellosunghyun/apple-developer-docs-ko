---
title: "Getting raw accelerometer events | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.869664+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   raw accelerometer event 가져오기

문서

raw accelerometer event 가져오기
================================

내장 accelerometer에서 data를 가져옵니다.

[개요](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#overview)

-----------------------------------------------------------------------------------------------------------

accelerometer는 한 축을 따라 속도가 변하는 값을 측정합니다. 모든 iOS device에는 3축 accelerometer가 있으며, 다음 그림에 보이는 세 축 각각의 acceleration 값을 전달합니다. accelerometer가 보고하는 값은 중력 가속도를 단위로 측정하며, `1.0`은 주어진 방향으로 초당 9.8m/s의 acceleration을 나타냅니다. acceleration 값은 방향에 따라 양수일 수도 음수일 수도 있습니다.

![Accelerometer는 x축, y축, z축을 따라 속도 변화를 측정합니다](https://docs-assets.developer.apple.com/published/92a6d07674e95cb45de48f62e3247fdd/media-2904020%402x.png)

raw accelerometer data는 Core Motion framework의 class를 사용해 접근합니다. 특히 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 class가 accelerometer hardware를 활성화하는 interface를 제공합니다. hardware를 활성화할 때는 app에 가장 적합한 interface를 선택합니다. 필요할 때만 accelerometer data를 pull할 수도 있고, framework에 일정 간격으로 update를 app에 push하도록 요청할 수도 있습니다. 각 방식은 설정 단계가 다르고 적합한 사용 사례도 다릅니다.

서로 다른 device type의 좌표축 정보는 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 를 참고합니다.

### [Accelerometer Data 사용 가능 여부 확인하기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#Check-for-the-availability-of-accelerometer-data)

accelerometer data는 여러 이유로 사용할 수 없을 수 있으므로, 가져오기 전에 사용 가능한지 확인합니다. `CMMotionManager`의 [`isAccelerometerAvailable`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeravailable)
 property 값을 확인해 `true`인지 점검합니다. `false`이면 update를 시작해도 app에 data가 전달되지 않습니다.

### [필요할 때만 accelerometer data 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#Get-accelerometer-data-only-when-you-need-it)

game처럼 자체 schedule에 따라 accelerometer data를 처리하는 app은 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 의 [`startAccelerometerUpdates()`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())
 method를 사용해 accelerometer data 전달을 시작합니다. 이 method를 호출하면 system이 accelerometer hardware를 활성화하고 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 object의 [`accelerometerData`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)
 property를 업데이트하기 시작합니다. 하지만 system은 이 property가 업데이트될 때 알려 주지 않습니다. accelerometer data가 필요할 때 직접 property 값을 확인해야 합니다.

accelerometer update 전달을 시작하기 전에 [`accelerometerUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)
 property에 값을 할당해 update 빈도를 지정합니다. 요청할 수 있는 최대 빈도는 hardware에 따라 다르지만 보통 최소 100Hz입니다. hardware가 지원하는 수준보다 높은 빈도를 요청하면 Core Motion은 지원 가능한 최대값을 대신 사용합니다.

다음 예제는 accelerometer update가 초당 50회 발생하도록 설정하는 method를 보여 줍니다. 이어서 같은 빈도로 update를 가져와 data를 처리하는 timer를 설정합니다. timer를 더 낮은 빈도로 설정할 수도 있지만, 실제로 사용하지 않는 update를 hardware가 더 많이 생성하게 되어 전력을 낭비합니다.

    let motion = CMMotionManager()
    
    
    func startAccelerometers() {
       // Make sure the accelerometer hardware is available. 
       if self.motion.isAccelerometerAvailable {
          self.motion.accelerometerUpdateInterval = 1.0 / 50.0  // 50 Hz
          self.motion.startAccelerometerUpdates()
    
    
          // Configure a timer to fetch the data.
          self.timer = Timer(fire: Date(), interval: (1.0/50.0), 
                repeats: true, block: { (timer) in
             // Get the accelerometer data.
             if let data = self.motion.accelerometerData {
                let x = data.acceleration.x
                let y = data.acceleration.y
                let z = data.acceleration.z
    
    
        // app에서 accelerometer data를 사용합니다.
             }
          })
    
    
          // Add the timer to the current run loop.
          RunLoop.current.add(self.timer!, forMode: .defaultRunLoopMode)
       }
    }
    

### [지속적으로 들어오는 accelerometer data 처리하기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#Process-a-steady-stream-of-accelerometer-data)

들어오는 accelerometer data를 모두 캡처하려면, 예를 들어 움직임 패턴을 분석하려는 경우 [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)
 의 [`startAccelerometerUpdates(to:withHandler:)`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))
 method를 사용합니다. 이 method는 지정한 queue에서 handler block을 실행해 새 accelerometer 값 집합을 app으로 push합니다. 이 block이 queue에 들어가기 때문에 app이 잠시 바빠 update를 처리하지 못해도 accelerometer data를 모두 받을 수 있습니다.

accelerometer update 전달을 시작하기 전에 [`accelerometerUpdateInterval`](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)
 property에 값을 할당해 update 빈도를 지정합니다. 요청할 수 있는 최대 빈도는 hardware에 따라 다르지만 보통 최소 100Hz입니다. hardware가 지원하는 수준보다 높은 빈도를 요청하면 Core Motion은 지원 가능한 최대값을 대신 사용합니다.

다음 예제는 [MotionGraphs](https://developer.apple.com/library/archive/samplecode/MotionGraphs/Introduction/Intro.html#//apple_ref/doc/uid/DTS40012333)
 sample code project의 method를 보여 줍니다. 더 많은 맥락은 해당 project를 살펴보면 됩니다. 이 app은 accelerometer data의 실시간 그래프를 표시합니다. 사용자는 slider를 사용해 accelerometer update 빈도를 설정하며, 값이 바뀌면 예제에 나온 `startUpdatesWithSliderValue:` method가 호출됩니다. 이 method는 새 빈도로 accelerometer update를 다시 시작합니다. 새 sample을 받을 때마다 지정한 block이 main thread에 queue됩니다. 그 block은 app의 graph view와 label을 새 accelerometer 값으로 업데이트합니다.

    static const NSTimeInterval accelerometerMin = 0.01;
    - (void)startUpdatesWithSliderValue:(int)sliderValue {
        // Determine the update interval.
        NSTimeInterval delta = 0.005;
        NSTimeInterval updateInterval = accelerometerMin + delta * sliderValue;
    // CMMotionManager object를 만듭니다.
        CMMotionManager *mManager = [(APLAppDelegate *)\
                [[UIApplication sharedApplication] delegate] sharedManager];
        APLAccelerometerGraphViewController * __weak weakSelf = self;
        // Check whether the accelerometer is available.
        if ([mManager isAccelerometerAvailable] == YES) {
            // Assign the update interval to the motion manager.
            [mManager setAccelerometerUpdateInterval:updateInterval];
            [mManager startAccelerometerUpdatesToQueue:[NSOperationQueue mainQueue]\
                   withHandler:^(CMAccelerometerData *accelerometerData, NSError *error) {\
            [weakSelf.graphView addX:accelerometerData.acceleration.x \
                      y:accelerometerData.acceleration.y \
                      z:accelerometerData.acceleration.z];\
            [weakSelf setLabelValueX:accelerometerData.acceleration.x \
                      y:accelerometerData.acceleration.y \
                      z:accelerometerData.acceleration.z];\
          }];
       }
       self.updateIntervalLabel.text = [NSString stringWithFormat:@"%f", updateInterval];
    }
    - (void)stopUpdates {
       CMMotionManager *mManager = [(APLAppDelegate *)\
                [[UIApplication sharedApplication] delegate] sharedManager];
       if ([mManager isAccelerometerActive] == YES) {
          [mManager stopAccelerometerUpdates];
       }
    }
    

[같이 보기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#see-also)

-----------------------------------------------------------------------------------------------------------

### [Accelerometer](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events#Accelerometers)

[`class CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

device의 3개 accelerometer에서 얻은 data sample입니다.

[`class CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

device가 기록한 accelerometer data 한 건입니다.

[`class CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

device에서 accelerometer data를 수집하고 가져오는 object입니다.

[`class CMSensorDataList`](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

system이 기록한 accelerometer data 목록입니다.

현재 페이지: raw accelerometer event 가져오기
