---
title: "init(validation:maxIterations:overlapFactor:algorithm:featureExtractionTimeWindowSize:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.158984+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   init(validation:maxIterations:overlapFactor:algorithm:featureExtractionTimeWindowSize:)

initializer

init(validation:maxIterations:overlapFactor:algorithm:featureExtractionTimeWindowSize:)
=======================================================================================

validation dataset, training algorithm, time-window size를 포함하는 sound classifier용 새 training parameter 집합을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+visionOS 1.0+

    init(
        validation: MLSoundClassifier.ModelParameters.ValidationData = __Defaults.validation,
        maxIterations: Int = __Defaults.maximumIterations,
        overlapFactor: Double = __Defaults.overlapFactor,
        algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType = __Defaults.algorithm,
        featureExtractionTimeWindowSize: TimeInterval = __Defaults.defaultVGGishTimeWindow
    )

[parameter](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`validation`

[`MLSoundClassifier.ModelParameters.ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)
 instance로 표현한 validation dataset입니다.

`maxIterations`

training session이 sound classifier를 training할 때 사용할 수 있는 최대 iteration 수입니다.

`overlapFactor`

training session이 audio data에서 연속된 두 window를 분석할 때 사용하는 overlap 비율입니다. 이 비율은 `[0.0, 1.0)` 범위여야 합니다. 값이 클수록 더 많은 training data를 생성하지만 training 시간도 늘어납니다.\
\
기본값은 `0.5`이며, 50% overlap을 의미합니다.\
\
`algorithm`\
\
training session이 sound classifier를 training할 때 사용하는 algorithm입니다.\
\
`featureExtractionTimeWindowSize`\
\
feature-extraction session이 dataset의 audio file에서 읽은 각 audio sample에 사용하는 시간 길이(초)입니다. 값은 `[0.5, 15.0]` 범위여야 합니다.\
\
[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:)#see-also)\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [parameter 만들기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:)#Creating-parameters)\
\
[`init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:))\
\
validation dataset를 포함하는 sound classifier용 새 training parameter 집합을 생성합니다.\
\
[`init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:))\
\
validation dataset와 training algorithm을 포함하는 sound classifier용 새 training parameter 집합을 생성합니다.\
\
현재 페이지: init(validation:maxIterations:overlapFactor:algorithm:featureExtractionTimeWindowSize:)
