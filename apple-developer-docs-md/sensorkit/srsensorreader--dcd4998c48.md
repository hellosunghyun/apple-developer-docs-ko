---
title: "SRSensorReader | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsensorreader"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.022701+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsensorreader#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRSensorReader

class

SRSensorReader
==============

특정 sensor에 대해 사용자 authorization을 설정하고 data를 기록하는 object입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRSensorReader

[개요](https://developer.apple.com/documentation/sensorkit/srsensorreader#overview)

----------------------------------------------------------------------------------------

reader를 사용해 특정 sensor의 data를 얻으려면 app이 [`init(sensor:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/init(sensor:))
로 이 class의 instance를 만들고, `Sensors`에서 사용할 수 있는 sensor 하나를 전달합니다.

reader는 사용 전에 사용자의 authorization이 필요한 특정 sensor용 data stream입니다. app이 [`requestAuthorization(sensors:completion:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))
를 호출하면 OS가 해당 sensor 사용 승인 여부를 사용자에게 묻고, 사용자 응답에 따라 app의 authorization을 결정합니다. [`requestAuthorization(sensors:completion:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))
호출 결과 authorization status가 바뀌면 framework는 [`sensorReader(_:didChange:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:))
callback으로 delegate에 알립니다. reader의 [`authorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)
가 [`SRAuthorizationStatus.authorized`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus/authorized)
이면 app은 recording을 시작해 sensor data 수집을 시작합니다.

app이 [`startRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())
을 호출하면 framework는 다른 app이나 system process의 요청으로 이미 실행 중인 경우가 아니라면 reader의 sensor를 시작합니다. app은 활성 sensor에 대해 이전 7일간 기록된 data에 접근할 수 있습니다. app이 [`stopRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording())
을 호출하면 sensor에 대한 stakeholdership을 relinquish합니다. sensor에 app 또는 system stakeholder가 더 이상 없으면 framework는 sensor를 비활성화하고, 이에 따라 data recording도 중지합니다.

sensor의 data를 fetch하려면 request object를 [`fetch(_:)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:))
function에 전달합니다. [`SRFetchRequest`](https://developer.apple.com/documentation/sensorkit/srfetchrequest)
는 data의 시점을 정의하는 time range와 data를 수집할 phone 또는 watch 같은 device를 지정합니다. [`fetchDevices()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())
를 사용해 사용할 수 있는 device를 나열하고, Defining the Time Range의 time convenience-function을 사용해 time range를 지정합니다.

fetch query가 성공하면 framework는 [`sensorReader(_:didCompleteFetch:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))
로 delegate에 알립니다. delegate는 [`sensorReader(_:fetching:didFetchResult:)`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))
에서 _sample_ 형태의 sensor data를 받습니다. fetch result의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
type은 reader의 sensor에 따라 달라집니다. sensor와 sample의 매핑은 [Sample types](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample#Sample-types)
를 참고합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srsensorreader#topics)

------------------------------------------------------------------------------------

### [사용자 authorization 확인하기](https://developer.apple.com/documentation/sensorkit/srsensorreader#Checking-user-authorization)

[`var authorizationStatus: SRAuthorizationStatus`](https://developer.apple.com/documentation/sensorkit/srsensorreader/authorizationstatus)

사용자가 app이 이 reader의 sensor에 접근하도록 동의했는지에 대한 상태입니다.

[`class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/requestauthorization(sensors:completion:))

하나 이상의 sensor를 읽을 사용자 permission을 요청합니다.

[`enum SRAuthorizationStatus`](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus)

사용자가 app의 특정 sensor 읽기를 승인했는지 model링하는 상태입니다.

### [sensor reader 만들기](https://developer.apple.com/documentation/sensorkit/srsensorreader#Creating-a-sensor-reader)

[`init(sensor: SRSensor)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/init(sensor:))

새 sensor reader object를 초기화합니다.

[`struct SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensor)

app이 읽을 수 있는 sensor입니다.

[`var sensor: SRSensor`](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor)

이 object가 읽는 특정 sensor입니다.

### [sensor data 기록하기](https://developer.apple.com/documentation/sensorkit/srsensorreader#Recording-sensor-data)

[`func startRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())

sensor data recording을 시작합니다.

[`func stopRecording()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording())

sensor data recording을 중지합니다.

### [기록된 data 읽기](https://developer.apple.com/documentation/sensorkit/srsensorreader#Reading-recorded-data)

[`func fetch(SRFetchRequest)`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:))

fetch request가 지정한 sample을 fetch합니다.

[`func fetchDevices()`](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())

이 reader의 sensor에 대한 data를 저장하는 모든 device의 device 정보를 가져옵니다.

[`class SRDevice`](https://developer.apple.com/documentation/sensorkit/srdevice)

sample data를 제공하는 device 표현입니다.

### [sensor event에 응답하기](https://developer.apple.com/documentation/sensorkit/srsensorreader#Responding-to-sensor-events)

[`var delegate: (any SRSensorReaderDelegate)?`](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate)

sensor 관련 event에 응답하는 object입니다.

[`protocol SRSensorReaderDelegate`](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)

framework가 호출해 app에 sensor 관련 event를 알리는 callback 집합입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srsensorreader#relationships)

--------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srsensorreader#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수 protocol](https://developer.apple.com/documentation/sensorkit/srsensorreader#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[같이 보기](https://developer.apple.com/documentation/sensorkit/srsensorreader#see-also)

----------------------------------------------------------------------------------------

### [설정](https://developer.apple.com/documentation/sensorkit/srsensorreader#Setup)

[sensor reading을 위해 project 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)

sensor data에 접근하기 위한 system 및 사용자 permission을 얻도록 app에 metadata를 추가합니다.

현재 페이지: SRSensorReader
