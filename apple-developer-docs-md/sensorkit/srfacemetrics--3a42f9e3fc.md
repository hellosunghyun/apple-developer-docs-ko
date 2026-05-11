---
title: "SRFaceMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srfacemetrics"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.029813+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srfacemetrics#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRFaceMetrics

class

SRFaceMetrics
=============

사용자 얼굴에 대한 metric을 나타내는 object입니다.

iOS 17.0+iPadOS 17.0+Mac Catalyst 17.0+

    class SRFaceMetrics

[개요](https://developer.apple.com/documentation/sensorkit/srfacemetrics#overview)

---------------------------------------------------------------------------------------

[`faceMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)
 sensor는 이 class를 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
 type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srfacemetrics#topics)

-----------------------------------------------------------------------------------

### [session 정보 가져오기](https://developer.apple.com/documentation/sensorkit/srfacemetrics#Getting-session-information)

[`var sessionIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/sessionidentifier)

camera session의 identifier입니다.

[`var context: SRFaceMetrics.Context`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/context-swift.property)

camera session 동안의 system context입니다.

[`struct Context`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/context-swift.struct)

camera session 동안의 system context입니다.

[`var version: String`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/version)

system이 face metric과 analytics를 생성할 때 사용하는 algorithm의 version입니다.

### [face analytics 가져오기](https://developer.apple.com/documentation/sensorkit/srfacemetrics#Getting-face-analytics)

[`var faceAnchor: ARFaceAnchor`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/faceanchor)

sensor가 camera 앞에서 감지한 얼굴의 anchor입니다.

[`var partialFaceExpressions: [SRFaceMetricsExpression]`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/partialfaceexpressions)

algorithm이 감지한 부분 face expression입니다.

[`var wholeFaceExpressions: [SRFaceMetricsExpression]`](https://developer.apple.com/documentation/sensorkit/srfacemetrics/wholefaceexpressions)

algorithm이 감지한 전체 face expression입니다.

[`class SRFaceMetricsExpression`](https://developer.apple.com/documentation/sensorkit/srfacemetricsexpression)

facial expression을 나타내는 object입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srfacemetrics#relationships)

-------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srfacemetrics#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [채택 protocol](https://developer.apple.com/documentation/sensorkit/srfacemetrics#conforms-to)

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
    

[참고 항목](https://developer.apple.com/documentation/sensorkit/srfacemetrics#see-also)

---------------------------------------------------------------------------------------

### [face 분석](https://developer.apple.com/documentation/sensorkit/srfacemetrics#Analyzing-faces)

[`var SR_ARKIT_SUPPORTED: Int32`](https://developer.apple.com/documentation/sensorkit/sr_arkit_supported)

SensorKit framework용 SDK에서 ARKit framework를 사용할 수 있는지를 나타내는 flag입니다.

현재 페이지는 SRFaceMetrics입니다
