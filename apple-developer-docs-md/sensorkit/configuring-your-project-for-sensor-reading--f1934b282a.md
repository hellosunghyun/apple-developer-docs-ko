---
title: "sensor reading용 project 구성 | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.022425+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   sensor reading용 project 구성

문서

sensor reading용 project 구성
===========================================

sensor data에 접근하기 위한 system 및 사용자 permission을 얻을 수 있도록 app에 metadata를 추가합니다.

[개요](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#overview)

---------------------------------------------------------------------------------------------------------------------

Apple이 research-study app 아이디어를 승인하면, 사용자 permission을 받은 뒤 device에서 sensor data를 읽을 수 있습니다. Apple이 app을 승인하면 sensor data를 읽을 수 있게 하는 entitlement를 받습니다. 승인 조건에 따라 Apple의 privacy policy도 준수해야 합니다.

app이 사용자의 device에서 처음으로 sensor 정보를 읽으려고 하면, system이 app의 research study와 app이 수집하는 정보를 설명하는 sheet를 표시합니다. 이 sheet에서는 사용자가 개인 정보 접근을 세부 항목별로 승인할 수 있으며, app은 어떤 정보가 study에 필수인지 알려줘야 합니다. study 목적, 요청하는 sensor, privacy policy URL은 project의 `Info.plist`에 제공합니다.

자세한 내용은 [Sensor & Usage Data & Privacy](https://www.apple.com/legal/privacy/data/en/sensor-usage-data/)
 를 참고합니다.

### [sensor reader entitlement 요청](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Request-the-sensor-reader-entitlement)

SensorKit을 사용하려면 OS가 app의 code signature에 [`com.apple.developer.sensorkit.reader.allow`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensorkit.reader.allow)
 entitlement를 요구합니다. Apple은 승인된 research study에만 이 entitlement를 부여합니다. study에서 SensorKit data에 접근하려면 research proposal을 제출하고 entitlement를 요청합니다. 자세한 내용은 [Accessing SensorKit Data](https://www.researchandcare.org/resources/accessing-sensorkit-data/)
 를 참고합니다.

### [수동 provisioning profile 생성](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Create-a-manual-provisioning-profile)

Xcode는 sensor reader entitlement로 app에 code-sign하기 위해 explicit App ID가 포함된 수동 provisioning profile을 요구합니다.

explicit App ID를 만들려면 Apple Developer에 로그인한 다음, SensorKit project용 App ID를 등록하고 [Certificates, Identifiers, & Profiles](https://developer.apple.com/account/resources/certificates/list)
 페이지의 Additional Capabilities에서 sensor reader entitlement를 활성화합니다. 자세한 내용은 [Register an App ID](https://developer.apple.com/help/account/manage-identifiers/register-an-app-id)
 를 참고합니다.

수동 provisioning profile을 만들려면 sidebar에서 Profiles를 선택하고 왼쪽 위의 추가 버튼(+)을 클릭한 다음 iOS App Development profile type을 선택합니다. 자세한 내용은 [Create a development provisioning profile](https://developer.apple.com/help/account/manage-profiles/create-a-development-provisioning-profile)
 를 참고합니다.

provisioning profile은 다운로드한 뒤 Dock의 Xcode icon으로 드래그해 설치합니다. 또는 Xcode > Preferences > Accounts를 선택하고 Apple ID 및 해당 team을 선택한 뒤 Download Manual Profiles 옵션을 선택할 수 있습니다. 자세한 내용은 [Download manual provisioning profiles](https://help.apple.com/xcode/mac/current/?/deva899b4fe5#/deva899b4fe5)
 를 참고합니다.

### [signing용 Xcode 구성](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Configure-Xcode-for-signing)

project editor에서 target을 선택하고 General을 클릭해 App ID에 대응하는 bundle ID를 Xcode에 정의합니다. 자세한 내용은 [Set the bundle ID](https://help.apple.com/xcode/mac/current/#/deve21d0239c)
 를 참고합니다.

![프로젝트 target의 General 탭 스크린샷. Identity 섹션 아래의 Bundle Identifier 텍스트 필드가 provisioning profile과 연결된 App ID와 일치하는 값을 표시합니다.](https://docs-assets.developer.apple.com/published/91ee9ae6f487ded7a99f5cfb70a36b54/media-3924188%402x.png)

project에 `[Your App Name].entitlements`라는 새 property list file이 아직 없다면 추가합니다. `com.apple.developer.sensorkit.reader.allow`라는 key를 Array type으로 추가하고, app이 사용하는 각 sensor마다 string 값을 하나씩 추가합니다.

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict> 
        <key>com.apple.developer.sensorkit.reader.allow</key>
        <array> 
            <string>on-wrist</string>
            <string>ambient-light-sensor</string>
            <string>motion-accelerometer</string>
            <string>motion-rotation-rate</string>
            <string>visits</string>
            <string>pedometer</string>
            <string>device-usage</string>
            <string>messages-usage</string>
            <string>phone-usage</string>
            <string>keyboard-metrics</string> 
    </array></dict></plist>
    

위 raw property list의 code-signing entitlements file은 Xcode에서 다음과 같이 표시됩니다.

![Xcode의 code signing entitlements property list file 스크린샷. 목록의 root node에는 com.apple.developer.sensorkit.reader.allow라는 Array key가 있습니다. array에는 app이 요청하는 각 sensor에 대한 String 값이 들어 있으며, 값은 on-wrist, ambient-light-sensor, motion-accelerometer, motion-rotation-rate, visits, pedometer, device-usage, messages-usage, phone-usage, keyboard-metrics입니다.](https://docs-assets.developer.apple.com/published/0f02fccfc21f1537d4dfac88eca00fd0/media-3924189%402x.png)

수동 provisioning profile과 sensor reader entitlement로 app에 서명하려면 target의 build setting을 다음과 같이 설정합니다.

*   Code Signing Entitlements를 entitlements file로 설정합니다.
    
*   Code Signing Identity를 `Apple Developer`로 설정합니다.
    
*   Code Signing Style을 `Manual`로 설정합니다.
    
*   Provisioning Profile을 생성한 수동 provisioning profile로 설정합니다.
    

![프로젝트 target의 build settings 스크린샷. code signing entitlements 설정에는 사용자 지정 code signing entitlements file 이름이 표시됩니다. code signing identity는 iOS developer로 설정되어 있습니다. Code signing style은 manual입니다. provisioning profile build setting에는 explicit provisioning profile 이름이 표시됩니다.](https://docs-assets.developer.apple.com/published/62ff7067e9c673a6bf589fbd7215b42a/media-3924190%402x.png)

### [study 목적 설명](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Describe-the-purpose-of-your-study)

system은 사용자의 app study를 소개하는 Research Sensor & Usage Data Request sheet를 표시합니다. usage description `Info.plist` key를 사용해 app의 연구 목적을 짧게 설명합니다.

    <key>NSSensorKitUsageDescription</key>
    <string>이것은 내 app의 SensorKit usage description입니다.</string>
    

이 sheet는 App Research Purpose 배너에 연구 목적을 표시합니다.

![app의 study를 소개하는 Research Sensor & Usage Data Request sheet 스크린샷. sheet는 App Research Purpose 배너 아래에 app의 SensorKit usage description을 표시합니다.](https://docs-assets.developer.apple.com/published/87538d610da299dfd44a740a01ab3eb1/media-3928456%402x.png)

### [app의 privacy policy 연결](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Link-your-apps-privacy-policy)

project의 `Info.plist`에 [`NSSensorKitPrivacyPolicyURL`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitPrivacyPolicyURL)
 key를 사용해 privacy-policy webpage 링크를 추가합니다.

    <key>NSSensorKitPrivacyPolicyURL</key>
    <string>https://my-site.example.com/privacy-policy/</string>
    

sheet는 study 설명 아래에 app의 privacy policy 링크를 표시합니다.

![app의 study를 소개하는 Research Sensor & Usage Data Request sheet 스크린샷. app의 연구 목적 아래에서 View App Privacy Policy 링크가 강조되어 있습니다.](https://docs-assets.developer.apple.com/published/f9d7a9b0eac3c48762a1b034566ebed1/media-3683202%402x.png)

### [app이 data를 사용하는 방식 설명](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Explain-how-your-app-uses-the-data)

sheet는 app이 특정 sensor로 수집한 정보를 어떻게 사용하려는지도 설명합니다. 이 의도는 app의 `info.plist`에 sensor별 usage-detail key를 추가해 제공합니다. 예를 들어 [`accelerometer`](https://developer.apple.com/documentation/sensorkit/srsensor/accelerometer)
 property를 사용할 때는 [`SRSensorUsageMotion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMotion)
 key를 추가합니다. 다른 sensor별 usage key는 [`SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor)
 property 설명을 참고합니다.

    <key>NSSensorKitUsageDetail</key>
    <dict> 
        <key>SRSensorUsageMotion</key>
        <dict> 
            <key>Description</key> 
            <string>이 문자열은 내 app이 motion data를 사용하는 방식을 설명합니다.</string>
        </dict> 
    </dict>
    

sensor data 읽기를 시작하려면 `requestAuthorization(sensors:completion:)`를 호출하고 app이 기록할 sensor를 전달합니다.

    // ambient light 정보를 위한 sensor입니다.
    let reader = SRSensorReader(sensor: .ambientLightSensor)
    
    
    // authorization 승인 prompt를 표시합니다. 
    func requestAuthorization() {
        SRSensorReader.requestAuthorization(
            sensors [.ambientLightSensor]) { (error: Error?) in
            if let error = error {
                fatalError("Sensor authorization failed due to: \(error)") 
            } else {
                print("""
                    사용자가 authorization prompt를 닫았습니다. 
                    authorization status 변경을 기다립니다.
                """) 
            } } }
    
    
    // view를 설정합니다. 
    override func viewDidLoad() {
    
    
        // authorization status 변경을 수신합니다.
        reader.delegate = self
    }
    
    
    

app이 특정 sensor에 대해 처음 authorization을 요청할 때, sheet가 사용자 승인을 요청하고 해당 sensor의 usage-detail string을 표시합니다.

![Research Sensor & Usage Data Request sheet의 두 번째 페이지 스크린샷. “How the study will use this data” 배너 위에 “This describes how my app uses motion data.”라는 텍스트가 표시됩니다.](https://docs-assets.developer.apple.com/published/c5f5159fb33c1a5c9b45136890b92e34/media-3683199%402x.png)

### [app에 필요한 sensor 지정](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Specify-the-sensors-your-app-requires)

사용자는 sheet를 통해 Allow Collection & Sharing 또는 Don’t Allow Collection & Sharing을 탭해 각 sensor를 개별적으로 승인합니다.

![Research Sensor & Usage Data Request sheet의 두 번째 페이지 스크린샷으로, 하단의 두 버튼이 강조되어 있습니다. 위 버튼은 “Allow Collection & Sharing”이고, 아래 버튼은 “Don’t Allow Collection and Sharing”입니다.](https://docs-assets.developer.apple.com/published/9dfd6a81c4382a107e5d9faa6b9c6393/media-3683201%402x.png)

study에 하나 이상의 sensor가 필요한지 지정하면 사용자는 수집을 거부하거나, 일부만 참여하거나, 전체에 동의할 수 있습니다. study에 sensor가 필요함을 나타내려면 sensor의 usage-detail dictionary에 `Required`라는 Boolean key를 추가하고 값을 `true`로 설정합니다.

    <key>SRSensorUsageMotion</key>
    <dict> 
        ... 
        <key>Required</key> 
        <true/>
    </dict>
    

study에 선택적인 sensor 정보라면 `Required` key를 생략하거나 값을 `false`로 설정할 수 있습니다.

사용자가 필수 sensor를 승인하지 않으면 system은 study에 해당 정보가 필요하다고 경고합니다. 이 prompt에서 사용자는 Change Choice를 탭해 다시 선택하거나, 등록하지 않기를 선택할 수 있습니다.

![Research Sensor & Usage Data Request sheet의 두 번째 페이지 스크린샷. modal prompt는 사용자가 허용하지 않은 sensor가 study에 필요하다고 설명하는 텍스트와 두 개의 버튼을 표시합니다. 위 버튼은 “Don’t Enroll in Study”이고, 아래 버튼은 “Change Choice”입니다. ](https://docs-assets.developer.apple.com/published/fe9bacde05a71fb8244fb0b0c6d6c4bf/media-3683200%402x.png)

사용자가 prompt에 응답한 뒤에는 Settings > Privacy > Research Sensor & Usage Data에서 sensor별 authorization status를 나중에 조정할 수 있습니다.

[참고 항목](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#see-also)

---------------------------------------------------------------------------------------------------------------------

### [설정](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading#Setup)

[`class SRSensorReader`](https://developer.apple.com/documentation/sensorkit/srsensorreader)

사용자 authorization을 설정하고 특정 sensor의 data를 기록하는 object입니다.

현재 페이지: sensor reading용 project 구성
