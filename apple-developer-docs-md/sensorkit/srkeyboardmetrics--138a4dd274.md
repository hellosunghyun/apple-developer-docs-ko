---
title: "SRKeyboardMetrics | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.024223+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   SRKeyboardMetrics

class

SRKeyboardMetrics
=================

device keyboard의 구성과 사용 패턴입니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    class SRKeyboardMetrics

[개요](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#overview)

-------------------------------------------------------------------------------------------

[`keyboardMetrics`](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)
sensor는 이 class를 자신의 [`sample`](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)
type으로 제공합니다.

[주제](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#topics)

---------------------------------------------------------------------------------------

### [keyboard 구성과 session 확인](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#Inspecting-Keyboard-Configuration-and-Sessions)

[`var duration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/duration)

report가 포괄하는 기간입니다.

[`var keyboardIdentifier: String`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/keyboardidentifier)

keyboard 목록에서 이 keyboard를 식별하는 identifier입니다.

[`var version: String`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/version)

keyboard metrics 버전입니다.

[`var width: Measurement<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/width)

report에 있는 keyboard의 너비(mm)입니다.

[`var height: Measurement<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/height)

report에 있는 keyboard의 높이(mm)입니다.

[`var inputModes: [String]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/inputmodes)

session에서 활성화된 keyboard 언어입니다.

[`var sessionIdentifiers: [String]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers)

sample에 metric을 보고한 keyboard session의 identifier입니다.

### [key 사용량 수치화](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#Quantifying-Key-Use)

[`var totalWords: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalwords)

keyboard에서 입력한 전체 단어 수입니다.

[`var totalAlteredWords: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalalteredwords)

keyboard에서 수정된 전체 단어 수입니다.

[`var totalTaps: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totaltaps)

keyboard의 전체 tap 수입니다.

[`var totalDrags: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totaldrags)

keyboard의 전체 drag 수입니다.

[`var totalDeletes: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totaldeletes)

keyboard의 전체 삭제 수입니다.

[`var totalEmojis: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalemojis)

keyboard의 전체 emoji 수입니다.

[`var totalPaths: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalpaths)

keyboard에서 완료된 전체 path 수입니다.

[`var totalPathTime: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalpathtime)

keyboard에서 path를 완료하는 데 걸린 전체 시간입니다.

[`var totalPathLength: Measurement<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalpathlength)

keyboard에서 완료된 path의 전체 길이입니다.

[`var totalAutoCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalautocorrections)

keyboard의 전체 autocorrection 수입니다.

[`var totalSpaceCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalspacecorrections)

keyboard의 전체 space correction 수입니다.

[`var totalRetroCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalretrocorrections)

keyboard의 전체 retro correction 수입니다.

[`var totalTranspositionCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totaltranspositioncorrections)

keyboard의 전체 transposition correction 수입니다.

[`var totalInsertKeyCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalinsertkeycorrections)

keyboard의 전체 Insert key correction 수입니다.

[`var totalSkipTouchCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalskiptouchcorrections)

keyboard의 전체 skip touch correction 수입니다.

[`var totalNearKeyCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalnearkeycorrections)

keyboard의 전체 near key correction 수입니다.

[`var totalSubstitutionCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalsubstitutioncorrections)

keyboard의 전체 substitution correction 수입니다.

[`var totalHitTestCorrections: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalhittestcorrections)

keyboard의 전체 hit test correction 수입니다.

[`var totalTypingDuration: TimeInterval`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totaltypingduration)

keyboard의 전체 typing 시간입니다.

[`var totalPathPauses: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalpathpauses)

단어의 path를 그리는 동안 발생한 전체 pause 수입니다.

[`var totalPauses: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalpauses)

session 중 발생한 전체 pause 수입니다.

[`var totalTypingEpisodes: Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totaltypingepisodes)

session 중 연속 typing episode의 전체 수입니다.

### [key 사용 타이밍 측정](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#Timing-Key-Use)

[`class ProbabilityMetric`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/probabilitymetric)

발생 가능성을 나타내는 값입니다.

[`var touchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/touchdownup)

모든 key에서 touch down부터 touch up까지의 시간입니다.

[`var touchUpDown: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/touchupdown)

모든 key에서 touch up과 touch down 사이의 시간입니다.

[`var spaceTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetouchdownup)

keyboard의 모든 Space bar event에서 touch down과 touch up 사이의 시간입니다.

[`var deleteTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetouchdownup)

keyboard의 모든 Delete key event에서 touch down과 touch up 사이의 시간입니다.

[`var shortWordCharKeyTouchDownUp: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/shortwordcharkeytouchdownup)

keyboard의 짧은 단어에 있는 모든 문자 key에서 touch down과 touch up 사이의 시간입니다.

[`var touchDownDown: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/touchdowndown)

모든 key에서 touch down과 다음 touch down 사이의 시간입니다.

[`var charKeyToPrediction: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/charkeytoprediction)

문자 key의 touch up과 prediction bar 단어의 touch down 사이의 시간입니다.

[`var shortWordCharKeyToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/shortwordcharkeytocharkey)

짧은 단어에서 문자 key의 touch up과 다음 문자 key의 touch down 사이의 시간입니다.

[`var charKeyToAnyTapKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/charkeytoanytapkey)

문자 key의 touch up과 다음 순차 key의 touch down 사이의 시간입니다.

[`var anyTapToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/anytaptocharkey)

임의의 key의 touch up과 다음 문자 key의 touch down 사이의 시간입니다.

[`var spaceToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetocharkey)

Space bar의 touch up과 다음 문자 key의 touch down 사이의 시간입니다.

[`var charKeyToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/charkeytospacekey)

문자 key의 touch up과 다음 Space bar의 touch down 사이의 시간입니다.

[`var spaceToDeleteKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetodeletekey)

Space bar의 touch up과 다음 Delete key의 touch down 사이의 시간입니다.

[`var deleteToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetospacekey)

Delete key의 touch up과 다음 Space bar의 touch down 사이의 시간입니다.

[`var spaceToSpaceKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetospacekey)

Space bar의 touch up과 다음 Space bar의 touch down 사이의 시간입니다.

[`var spaceToShiftKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetoshiftkey)

Space bar의 touch up과 다음 Shift key의 touch down 사이의 시간입니다.

[`var spaceToPlaneChangeKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetoplanechangekey)

Space bar의 touch up과 다음 plane change key의 touch down 사이의 시간입니다.

[`var spaceToPredictionKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetopredictionkey)

Space bar의 touch up과 prediction bar의 다음 선택 항목 touch down 사이의 시간입니다.

[`var deleteToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetocharkey)

Delete key의 touch up과 다음 문자 key의 touch down 사이의 시간입니다.

[`var charKeyToDelete: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/charkeytodelete)

문자 key의 touch up과 다음 Delete key의 touch down 사이의 시간입니다.

[`var deleteToDelete: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetodelete)

Delete key의 touch up과 다음 Delete key의 touch down 사이의 시간입니다.

[`var deleteToDeletes: [SRKeyboardMetrics.ProbabilityMetric<UnitDuration>]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetodeletes)

단어 전체에 걸쳐 Delete key의 touch up과 다음 Delete key의 touch down 사이의 시간입니다.

[`var deleteToShiftKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetoshiftkey)

Delete key의 touch up과 다음 Shift key의 touch down 사이의 시간입니다.

[`var deleteToPlaneChangeKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetoplanechangekey)

Delete key의 touch up과 다음 plane change key의 touch down 사이의 시간입니다.

[`var anyTapToPlaneChangeKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/anytaptoplanechangekey)

임의의 key의 touch up과 plane change key의 touch down 사이의 시간입니다.

[`var planeChangeToAnyTap: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/planechangetoanytap)

plane change key의 touch up과 다음 순차 key의 touch down 사이의 시간입니다.

[`var charKeyToPlaneChangeKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/charkeytoplanechangekey)

문자 key의 touch up과 다음 plane change key의 touch down 사이의 시간입니다.

[`var planeChangeKeyToCharKey: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/planechangekeytocharkey)

plane change key의 touch up과 임의의 key의 touch down 사이의 시간입니다.

[`var deleteToPath: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletetopath)

Delete key의 touch up과 다음 path의 touch down 사이의 시간입니다.

[`var pathToDelete: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/pathtodelete)

Delete key의 touch up과 연속 path의 touch down 사이의 시간입니다.

[`var spaceToPath: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacetopath)

Space bar의 touch up과 다음 path를 시작하는 touch down 사이의 시간입니다.

[`var pathToSpace: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/pathtospace)

path의 touch up과 다음 Space bar의 touch down 사이의 시간입니다.

[`var pathToPath: SRKeyboardMetrics.ProbabilityMetric<UnitDuration>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/pathtopath)

path의 touch up과 다음 path의 touch down 사이의 시간입니다.

[`var longWordTouchDownUp: [SRKeyboardMetrics.ProbabilityMetric<UnitDuration>]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/longwordtouchdownup)

session의 모든 긴 단어 문자 key에서 touch down과 touch up 사이의 시간입니다.

[`var longWordTouchDownDown: [SRKeyboardMetrics.ProbabilityMetric<UnitDuration>]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/longwordtouchdowndown)

session의 모든 긴 단어 문자 key에서 touch down과 다음 touch down 사이의 시간입니다.

[`var longWordTouchUpDown: [SRKeyboardMetrics.ProbabilityMetric<UnitDuration>]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/longwordtouchupdown)

session의 모든 긴 단어 문자 key에서 touch up과 다음 touch down 사이의 시간입니다.

[`var pathTypingSpeed: Double`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/pathtypingspeed)

session의 QuickType words per minute입니다.

[`var typingSpeed: Double`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/typingspeed)

사용자의 typing 속도(초당 문자 수)입니다.

### [key 사용 측정](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#Measuring-Key-Use)

[`var longWordUpErrorDistance: [SRKeyboardMetrics.ProbabilityMetric<UnitLength>]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/longworduperrordistance)

긴 단어 문자에서 touch up 지점과 의도한 key 중심 사이의 거리입니다.

[`var longWordDownErrorDistance: [SRKeyboardMetrics.ProbabilityMetric<UnitLength>]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/longworddownerrordistance)

긴 단어 문자에서 touch down 지점과 의도한 key 중심 사이의 거리입니다.

[`var upErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/uperrordistance)

touch up 지점과 임의의 key 중심 사이의 거리입니다.

[`var downErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/downerrordistance)

touch down 지점과 임의의 key 중심 사이의 거리입니다.

[`var spaceUpErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spaceuperrordistance)

touch up 지점과 Space bar 오른쪽 centroid 사이의 거리입니다.

[`var spaceDownErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/spacedownerrordistance)

touch down 지점과 Space bar 오른쪽 centroid 사이의 거리입니다.

[`var deleteUpErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deleteuperrordistance)

touch up 지점과 Delete key 중심 사이의 거리입니다.

[`var deleteDownErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/deletedownerrordistance)

touch down 지점과 Delete key 중심 사이의 거리입니다.

[`var shortWordCharKeyUpErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/shortwordcharkeyuperrordistance)

짧은 단어의 문자에서 touch up 지점과 의도한 key 중심 사이의 거리입니다.

[`var shortWordCharKeyDownErrorDistance: SRKeyboardMetrics.ProbabilityMetric<UnitLength>`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/shortwordcharkeydownerrordistance)

짧은 단어의 문자에서 touch down 지점과 의도한 key 중심 사이의 거리입니다.

[`var pathErrorDistanceRatio: [NSNumber]`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/patherrordistanceratio)

의도한 path와 실제 path 사이 error distance 비율의 sample 값입니다.

### [sentiment 추론](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#Inferring-Sentiment)

[`func wordCount(for: SRKeyboardMetrics.SentimentCategory) -> Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/wordcount(for:))

report에서 지정한 sentiment에 해당하는 입력 단어 수를 제공합니다.

[`func emojiCount(for: SRKeyboardMetrics.SentimentCategory) -> Int`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/emojicount(for:))

report에서 지정한 sentiment에 해당하는 입력 emoji 수를 제공합니다.

[`enum SentimentCategory`](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sentimentcategory)

framework가 사용자 입력을 분석해 판단한 감정 상태입니다.

[관계](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#relationships)

-----------------------------------------------------------------------------------------------------

### [상속](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#inherits-from)

*   [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
    

### [준수하는 protocol](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#conforms-to)

*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
    
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
    
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
    
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
    
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
    
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
    

[관련 항목](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#see-also)

-------------------------------------------------------------------------------------------

### [data 해석](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics#Interpreting-data)

[`class SRAmbientLightSample`](https://developer.apple.com/documentation/sensorkit/srambientlightsample)

사용자 환경의 주변광 양입니다.

[`class SRDeviceUsageReport`](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)

사용자가 device, 특정 Apple app 또는 웹사이트를 사용하는 빈도와 상대적 duration입니다.

[`class SRMediaEvent`](https://developer.apple.com/documentation/sensorkit/srmediaevent)

image나 video 같은 media object에 대한 사용자 상호작용입니다.

[`class SRMessagesUsageReport`](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)

일정 기간 동안의 사용자 Messages app activity를 설명하는 object입니다.

[`class SRPhoneUsageReport`](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)

일정 기간 동안의 사용자 전화 activity를 설명하는 object입니다.

[`class SRVisit`](https://developer.apple.com/documentation/sensorkit/srvisit)

사용자의 일상 이동 루틴에서의 진행 상황입니다.

[`class SRWristDetection`](https://developer.apple.com/documentation/sensorkit/srwristdetection)

착용자의 손목에 있는 watch의 구성입니다.

현재 페이지는 SRKeyboardMetrics입니다
