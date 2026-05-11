---
title: "Accessing submersion data | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/accessing-submersion-data"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.871991+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   submersion data에 접근하기

문서

submersion data에 접근하기
=========================

water-submersion manager를 사용해 Apple Watch Ultra에서 수압, 수온, 수심 data를 받습니다.

[개요](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#overview)

----------------------------------------------------------------------------------------------------

Apple Watch Ultra는 물에 잠긴 동안 수압, 수심, 수온 data를 수집할 수 있습니다. 하지만 app이 이 data에 접근하려면 먼저 다음 설정 단계를 수행해야 합니다.

*   submersion data 접근 권한을 부여하는 Apple 제공 entitlement를 포함합니다.
    
*   app이 submersion data 접근이 필요한 이유를 설명하는 information property list key를 제공합니다.
    
*   app에 `underwater-depth` Background Mode capability를 추가합니다.
    
*   현재 device에서 submersion manager를 사용할 수 있는지 확인합니다.
    

submersion data 모니터링을 시작하려면 [`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 를 생성하고 submersion manager에 delegate를 할당합니다. 그러면 system이 delegate로 update를 보내기 시작합니다. 이후 watch가 처음 잠겼을 때 extended runtime session을 시작하고, 다이빙 중에는 app을 touchless user interface로 전환할 수 있습니다.

### [필수 entitlement 추가하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Add-the-required-entitlement)

[`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 class를 생성하기 전에 app에 submersion data 접근을 위한 Submerged Depth and Pressure entitlement를 포함해야 합니다.

최대 수심 6m까지의 dive data에 접근하려면 app에 Shallow Depth and Pressure capability를 추가합니다. 자세한 내용은 [Adding capabilities to your app](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app)
 을 참고하세요.

최대 수심 40m를 사용하려면 전체 Submersion Depth and Pressure entitlement를 신청해야 합니다. 자세한 내용은 [the Submerged Depth and Pressure entitlement request form.](https://developer.apple.com/contact/request/submerged-depth-pressure-api-development/)
 을 참고하세요.

entitlement 없이 manager를 생성하면 system이 delegate의 [`manager(_:errorOccurred:)`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))
 method를 호출하면서 [`CMErrorNotEntitled`](https://developer.apple.com/documentation/coremotion/cmerrornotentitled)
 error를 전달하고, delegate는 더 이상 어떤 data도 받지 못합니다.

### [motion data 접근 권한 승인하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Authorize-access-to-motion-data)

system은 [`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 를 처음 생성할 때 착용자에게 motion data 접근 authorization을 자동으로 요청합니다. 하지만 manager를 생성하기 전에 app target의 information property list에 [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription)
 key를 포함하고 usage description string을 제공해야 합니다.

![Motion Usage Description key가 강조 표시된 app target의 information property list를 보여주는 Xcode 스크린샷.](https://docs-assets.developer.apple.com/published/abf9523bc09713905a9cee676772037e/media-4110816%402x.png)

system은 착용자에게 motion data 접근 authorization을 요청할 때 이 usage description을 표시합니다. usage description string을 포함하지 않으면 [`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 object를 생성하려 할 때 app이 crash됩니다.

### [underwater depth extended runtime session 지원 추가하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Add-support-for-the-underwater-depth-extended-runtime-session)

app이 계속 실행되고 화면에 남아 있도록 하려면 app의 `Info.plist` file에 `underwater-depth` Background Mode를 추가해야 합니다. 이 background mode는 dive session 동안 app이 전면 app으로 실행되게 합니다.

Project navigator에서 `Info.plist`를 Control-클릭하고 Open As > Source Code를 선택해 `Info.plist` file을 XML로 엽니다. 그런 다음 [`WKBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKBackgroundModes)
 key의 string 값을 수정해 `underwater-depth` 값을 포함하도록 합니다.

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>WKBackgroundModes</key>
        <array>
            <string>underwater-depth</string>
        </array>
    </dict>
    </plist>
    
    
    

app에 아직 `Info.plist` file이 없다면 placeholder를 추가한 뒤 다음 단계로 편집할 수 있습니다.

1.  app의 WatchKit Extension target을 선택하고 Signing & Capabilities 탭을 클릭합니다.
    
2.  Editor > Add Capability를 선택하고 Background Modes capability를 더블클릭해 Signing & Capabilities pane에 추가합니다.
    
3.  Session Type 팝업 메뉴에서 placeholder로 사용할 option을 선택합니다. Project navigator에 `Info.plist` file이 나타납니다.
    
4.  `Info.plist` file을 source code로 열고 [`WKBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKBackgroundModes)
     key의 placeholder string 값을 `underwater-depth` 값으로 바꿉니다.
    

`Info.plist` file에 `underwater-depth` Background Mode capability를 추가하면 app이 extended runtime session을 실행해 dive session 내내 전면 app으로 남을 수 있습니다. 또한 system이 착용자가 watch를 물에 잠갔을 때 자동 실행할 수 있는 app 목록에 app을 추가합니다.

대부분의 extended runtime session과 달리, app은 전면 app으로 추가 시간을 확보하기 위해 extended runtime session을 직접 시작할 필요가 없습니다. 이 key를 추가하기만 해도 system이 착용자가 app을 실행한 뒤 30분 동안 app을 자동으로 전면 app으로 유지합니다. 이 시간 동안 착용자는 잠수 전 준비를 할 수 있습니다. 이후 extended runtime session을 시작하면 dive가 끝날 때까지 app이 계속 전면 app으로 유지됩니다. watch가 10분 넘게 물 밖에 있거나 착용자가 Water Lock을 끌 때까지 session은 timeout되지 않습니다.

extended runtime session을 명시적으로 시작하지 않으면 착용자가 1m 아래로 잠수했을 때 system이 runtime session을 자동으로 시작하고, app은 [`CMWaterSubmersionMeasurement.DepthState.submergedDeep`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate/submergeddeep)
 상태로 전환합니다.

### [현재 device에서 submersion data를 사용할 수 있는지 확인하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Verify-that-the-submersion-data-is-available-on-the-current-device)

submersion manager를 만들기 전에 현재 device에서 data를 사용할 수 있는지 확인합니다.

    guard CMWaterSubmersionManager.waterSubmersionAvailable else {
        return false
    }
    

Apple Watch Ultra에서는 system이 [`waterSubmersionAvailable`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/watersubmersionavailable)
 을 [`true`](https://developer.apple.com/documentation/Swift/true)
 로 설정합니다. 다른 모든 device와 Simulator에서는 [`false`](https://developer.apple.com/documentation/Swift/false)
 로 설정합니다.

### [submersion data 모니터링 시작하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Start-monitoring-submersion-data)

submersion data 수신을 시작하려면 [`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 object를 생성하고 [`CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)
 를 할당합니다.

    // submersion manager를 생성합니다.
    submersionManager = CMWaterSubmersionManager()
    
    
    // submersion manager delegate를 할당합니다.
    submersionManager.delegate = self
    

delegate를 할당하는 즉시 data 수신이 시작됩니다. 예를 들어 delegate는 event notification과 error를 모두 받습니다.

    // event에 대응합니다.
    nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate event: CMWaterSubmersionEvent) {
    
    
        let submerged: Bool?
        switch event.state {
        case .unknown:
            logger.info("*** Received an unknown event. ***")
            submerged = nil
    
    
        case .notSubmerged:
            logger.info("*** Not Submerged Event ***")
            submerged = false
    
    
        case .submerged:
            logger.info("*** Submerged Event ***")
            submerged = true
    
    
        @unknown default:
            fatalError("*** Unknown event received: \(event.state) ***")
        }
    
    
        Task {
            await myAdd(event: event)
            if let submerged {
                await mySet(submerged: submerged)
            }
        }
    }
    
    
    // error에 대응합니다.
    nonisolated func manager(_ manager: CMWaterSubmersionManager, errorOccurred error: Error) {
        logger.error("*** An error occurred: \(error.localizedDescription) ***")
    }
    
    
    

delegate는 measurement update도 받기 시작합니다. watch가 잠기지 않은 경우 update에는 surface pressure와 submersion state data만 포함됩니다. 물에 잠기면 수압과 수심 data도 함께 받습니다. system은 watch가 잠긴 동안 초당 세 번 measurement update를 보냅니다. watch가 수면 위에 있으면 더 낮은 빈도로 update를 제공하며, watch가 움직이지 않으면 update 제공을 중단할 수 있습니다.

    nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate measurement: CMWaterSubmersionMeasurement) {
    
    
        logger.info("*** Received a depth measurement. ***")
    
    
        let currentDepth: String
        if let depth = measurement.depth {
            currentDepth = "\(depth.value) \(depth.unit)"
        } else {
            currentDepth = "None"
        }
    
    
        let currentSurfacePressure: String
        let surfacePressure = measurement.surfacePressure
        currentSurfacePressure = "\(surfacePressure.value) \(surfacePressure.unit)"
    
    
        let currentPressure: String
        if let pressure = measurement.pressure {
            currentPressure = "\(pressure.value) \(pressure.unit)"
        } else {
            currentPressure = "None"
        }
    
    
        logger.info("*** Depth: \(currentDepth) ***")
        logger.info("*** Surface Pressure: \(currentSurfacePressure) ***")
        logger.info("*** Pressure: \(currentPressure) ***")
    
    
        let submerged: Bool?
        switch measurement.submersionState {
        case .unknown:
            logger.info("*** Unknown Depth ***")
            submerged = nil
        case .notSubmerged:
            logger.info("*** Not Submerged ***")
            submerged = false
        case .submergedShallow:
            logger.info("*** Shallow Depth ***")
            submerged = true
        case .submergedDeep:
            logger.info("*** Deep Depth ***")
            submerged = true
        case .approachingMaxDepth:
            logger.info("*** Approaching Max Depth ***")
            submerged = true
        case .pastMaxDepth:
            logger.info("*** Past Max Depth ***")
            submerged = true
        case .sensorDepthError:
            logger.info("*** A depth error has occurred. ***")
            submerged = nil
        @unknown default:
            fatalError("*** An unknown measurement depth state: \(measurement.submersionState)")
        }
    
    
        Task {
            await myAdd(measurement: measurement)
            if let submerged {
                await mySet(submerged: submerged)
            }
        }
    }
    

watch는 물에 잠겼을 때 수온 data도 받습니다.

    nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate measurement: CMWaterTemperature) {
        let temp = measurement.temperature
        let uncertainty = measurement.temperatureUncertainty
        let currentTemperature = "\(temp.value) +/- \(uncertainty.value) \(temp.unit)"
    
    
        logger.info(("*** \(currentTemperature) ***"))
    
    
        Task {
            await myAdd(temperature:measurement)
        }
    }
    

수온 측정값은 정확한 값으로 수렴하는 데 시간이 걸릴 수 있습니다. system은 정확한 결과로 수렴하는 데 걸리는 시간을 추정하고, 예상 수렴값을 바탕으로 uncertainty 값을 계산합니다.

### [dive session 시작하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Start-a-dive-session)

착용자가 다이빙을 시작할 때 extended runtime session을 시작할 수 있습니다.

    func myStartDiveSession() {
        logger.info("*** Starting a dive session. ***")
    
    
    // extended runtime session을 생성합니다.
        let session = WKExtendedRuntimeSession()
    
    
    // session에 delegate를 할당합니다.
        session.delegate = self
    
    
    // session을 시작합니다.
        session.start()
    
    
        self.extendedRuntimeSession = session
        diveSessionRunning = true
    }
    

이 session은 다음 중 하나가 일어날 때까지 계속 실행됩니다.

*   [`invalidate()`](https://developer.apple.com/documentation/WatchKit/WKExtendedRuntimeSession/invalidate())
     를 호출해 session을 명시적으로 취소합니다.
    
*   착용자가 Water Lock을 끕니다.
    
*   app이 최소 10분 동안 [`CMWaterSubmersionEvent.State.notSubmerged`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum/notsubmerged)
     상태로 유지됩니다.
    

자세한 내용은 [Using extended runtime sessions](https://developer.apple.com/documentation/WatchKit/using-extended-runtime-sessions)
 을 참고하세요.

### [touchless user interface로 전환하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Transition-to-a-touchless-user-interface)

extended runtime session을 시작하면 watch에서 Water Lock이 자동으로 활성화됩니다. 그 결과 dive 동안 system은 watch의 touchscreen을 비활성화합니다. 다이빙 중에도 착용자가 app과 상호작용해야 한다면 Digital Crown이나 Action button을 사용한 interaction을 지원해야 합니다.

[`List`](https://developer.apple.com/documentation/SwiftUI/List)
, [`ScrollView`](https://developer.apple.com/documentation/SwiftUI/ScrollView)
, [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker)
 같은 많은 view는 Digital Crown에 자동으로 반응합니다. 착용자는 user interface를 바꾸지 않아도 이 요소들과 상호작용할 수 있습니다.

    struct MyPickerView: View {
    
    
        enum Action: String, CaseIterable, Identifiable {
            case none, action1, action2, action3
            var id: Self { self }
        }
    
    
        @State var selection: Action = .none
    
    
        var body: some View {
            Text(selection.rawValue)
            Picker("Action", selection: $selection) {
                ForEach(Action.allCases) { action in
                    Text(action.rawValue.capitalized)
                }
            }
        }
    }
    

[`digitalCrownRotation(_:)`](https://developer.apple.com/documentation/SwiftUI/View/digitalCrownRotation(_:))
 view modifier를 사용하면 착용자가 Digital Crown을 돌릴 때 직접 반응하도록 만들 수도 있습니다.

    struct DigitalCrown: View {
        @State private var crownValue = 0.0
    
    
        var body: some View {
            Text("\(crownValue)")
                .focusable()
                .digitalCrownRotation($crownValue,
                                      from: 1,
                                      through: 10,
                                      by: 1.0,
                                      sensitivity: .low,
                                      isHapticFeedbackEnabled: true)
        }
    }
    

Action button의 경우 [`StartDiveIntent`](https://developer.apple.com/documentation/AppIntents/StartDiveIntent)
 를 구현해 착용자가 Action button을 처음 눌렀을 때 app을 실행하고 새 dive를 준비할 수 있습니다. 그런 다음 Action button의 다음 동작을 위한 [`AppIntent`](https://developer.apple.com/documentation/AppIntents/AppIntent)
 를 donate할 수 있습니다. session 중 다른 시점에 착용자가 Action button을 누르면 다음 동작이 실행됩니다. app은 한 번에 하나의 다음 동작만 가질 수 있으며, 새 intent를 donate하면 다음 동작이 바뀝니다. 이를 통해 app의 현재 상태에 따라 다음 동작을 맞춤화할 수 있습니다.

    // app을 실행하고 dive manager를 설정하는 intent를 생성합니다.
    struct MyStartDiveSessionIntent: StartDiveIntent {
    
    
        static var title: LocalizedStringResource = "Starting a dive session."
    
    
        func perform() async throws -> some IntentResult {
            logger.debug("*** Starting a dive session. ***")
    
    
            await MyDiveManager.shared.start()
            return .result(actionButtonIntent: MyBeginDescent())
        }
    }
    
    
    // Action button의 다음 동작을 정의하는 intent를 생성합니다.
    struct MyBeginDescent: AppIntent {
    
    
        static var title: LocalizedStringResource = "Start Your Descent"
    
    
        func perform() async throws -> some IntentResult {
            logger.debug("*** Starting the descent. ***")
            await MyDiveManager.shared.beginDescent()
            return .result()
        }
    }
    
    
    

자세한 내용은 [Responding to the Action button on Apple Watch Ultra](https://developer.apple.com/documentation/AppIntents/ActionButtonArticle)
 를 참고하세요.

### [자동 dive session 처리하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Handle-automatic-dive-sessions)

extended runtime session을 명시적으로 시작하지 않으면 착용자가 1m 아래로 내려갔을 때 system이 session을 자동으로 시작합니다. 이후 이 session을 app delegate의 [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKApplicationDelegate/handle(_:)-7kiwx)
 method로 전달합니다. 이 session을 사용하려면 delegate를 추가하고 dive가 끝날 때까지 scope에 유지되는 변수에 저장합니다.

    func handle(_ extendedRuntimeSession: WKExtendedRuntimeSession) {
        // 활성 extended runtime session이 없는 상태에서 착용자가
        // 수심 1m 아래에 있기 때문에 system이 session을 시작합니다.
    
    
        let submersionSession = MySubmersionSession.shared
    
    
        // session에 delegate를 할당합니다.
        extendedRuntimeSession.delegate = submersionSession
    
    
        submersionSession.extendedRuntimeSession = extendedRuntimeSession
        submersionSession.diveSessionRunning = true
    }
    

### [자동 실행에 대응하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Respond-to-autolaunch)

Apple Watch Ultra에서는 watch가 물에 잠겼을 때 어떤 app을 실행할지 착용자가 system에 지정할 수 있습니다. 이 기능을 사용하려면 Settings > General > Auto-Launch로 이동한 뒤 When Submerged 그룹의 Auto-Launch App 설정을 선택합니다. system이 어떤 app을 실행할지도 선택할 수 있습니다.

app의 `Info.plist` file에 `underwater-depth` Background Mode capability를 추가하는 즉시 system이 app을 자동 실행 가능한 app 목록에 넣습니다. 즉, 착용자가 app을 자동 실행 app으로 설정한 뒤 다른 상호작용 없이 물에 뛰어드는 경우에도 app이 올바르게 반응해야 합니다.

예를 들어 app이 실행될 때 [`CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)
 를 설정해 둘 수 있습니다. 이렇게 하면 app이 언제나 submersion data를 받을 준비를 마칩니다. 이후 착용자가 1m 아래로 내려가면 [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKApplicationDelegate/handle(_:)-7kiwx)
 method를 사용해 자동 생성된 extended runtime session을 가져올 수 있습니다. 또는 직접 extended runtime session을 명시적으로 시작하고 싶다면 app이 [`CMWaterSubmersionEvent.State.submerged`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum/submerged)
 event를 받을 때 session을 시작할 수 있습니다.

### [submersion data 테스트하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Test-submersion-data)

submersion data는 반드시 Apple Watch Ultra에서 테스트해야 합니다. Simulator에서는 submersion manager를 생성할 수 없습니다. submersion event를 발생시키려면 Apple Watch Ultra를 최소 1피트 깊이의 물탱크에 넣어야 합니다. 가압 용기에서 테스트할 때는 watch가 물에 완전히 잠기도록 하세요.

submersion event를 발생시킬 만큼 물이 깊지 않다면 페어링된 iPhone으로 Easy Submersion mode를 활성화할 수 있습니다. phone을 Mac에 연결한 뒤 Xcode 14.2 이상에서 Debug > Induce Device Conditions > Easy Submersion > Enable Easy Submersion을 선택합니다.

[참고 항목](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#see-also)

----------------------------------------------------------------------------------------------------

### [Water submersion](https://developer.apple.com/documentation/coremotion/accessing-submersion-data#Water-submersion)

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

submersion 중 pressure와 temperature data 수집을 관리하는 object입니다.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

ambient pressure, water pressure, water temperature, submersion event에 대한 update를 받는 delegate입니다.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

device의 submersion state가 바뀌었음을 나타내는 event입니다.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

pressure와 depth data를 담은 update입니다.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

water temperature data를 담은 update입니다.

현재 페이지: Accessing submersion data
