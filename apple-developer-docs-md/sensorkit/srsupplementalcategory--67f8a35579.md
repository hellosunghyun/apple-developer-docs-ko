---
title: "SRSupplementalCategory | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srsupplementalcategory"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.050354+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRSupplementalCategory

class

SRSupplementalCategory
======================

app category에 추가 context를 제공하는 더 자세한 category입니다.

iOS 16.4+iPadOS 16.4+Mac Catalyst 16.4+

    class SRSupplementalCategory

[개요](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#overview)

------------------------------------------------------------------------------------------------

supplemental category를 사용하면 [`SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)
안의 app usage data가 가진 세부 관계를 해석할 수 있습니다. device usage report에는 [`SRDeviceUsageReport.CategoryKey`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/categorykey)
가 정의하는 상위 primary category가 들어 있으며, supplemental category를 사용해 더 구체적인 설명으로 세분화합니다. 각 category는 고유한 [`identifier`](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory/identifier)
에 매핑되며, [`supplementalCategories`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories)
property로 접근해 app usage 관계를 그룹화할 수 있습니다.

이 supplemental category에 접근하려면 이 [table](https://developer.apple.com/download/files/SRSupplementalCategoryTable.zip)
을 사용합니다. table은 identifier와 _representative words_ 집합의 매핑으로 구성되어 있습니다. 예를 들어 Games category 안의 app usage를 추적한다면 _puzzle_, _gameplay_, _addictive_ 같은 representative word를 가진 cluster UUID를 사용해 Games 안의 구체적인 app type과 공통 설명을 추적할 수 있습니다.

[주제](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#topics)

--------------------------------------------------------------------------------------------

### [category 식별하기](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#Identifying-the-category)

[`var identifier: String`](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory/identifier)

supplemental category의 고유 identifier입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#relationships)

----------------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
    
*   [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
    
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
    
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#see-also)

------------------------------------------------------------------------------------------------

### [App 식별하기](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory#Identifying-the-App)

[`var bundleIdentifier: String?`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)

사용 중인 app의 bundle identifier입니다.

[`var reportApplicationIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)

실제 application identifier에 대한 pseudonym입니다.

[`var supplementalCategories: [SRSupplementalCategory]`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories)

app에 대한 추가 정보를 제공하는 category입니다.

현재 페이지: SRSupplementalCategory
