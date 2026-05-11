---
title: "init(validation:maxIterations:overlapFactor:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.160413+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.ModelParameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)
    
*   init(validation:maxIterations:overlapFactor:)

initializer

init(validation:maxIterations:overlapFactor:)
=============================================

validation dataset이 포함된 sound classifier용 새 training parameter 집합을 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    init(
        validation: MLSoundClassifier.ModelParameters.ValidationData = .split(strategy: .automatic),
        maxIterations: Int = 25,
        overlapFactor: Double = 0.5
    )

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:)#parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`validation`

[`MLSoundClassifier.ModelParameters.ValidationData`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)
 instance로 표현한 validation dataset입니다.

`maxIterations`

training session이 sound classifier training에 사용할 수 있는 최대 iteration 수입니다.

`overlapFactor`

training session이 audio data의 연속된 두 window를 분석할 때 사용하는 overlap 비율입니다. 비율은 `[0.0, 1.0)` 범위에 있어야 합니다. 값이 클수록 training data는 더 많이 생성되지만 training 시간도 늘어납니다.\
\
기본값은 `0.5`이며, 50% overlap을 의미합니다.\
\
[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:)#see-also)\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Creating parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:)#Creating-parameters)\
\
[`init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:))\
\
validation dataset과 training algorithm이 포함된 sound classifier용 새 training parameter 집합을 생성합니다.\
\
[`init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType, featureExtractionTimeWindowSize: TimeInterval)`](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:))\
\
validation dataset, training algorithm, time-window size가 포함된 sound classifier용 새 training parameter 집합을 생성합니다.\
\
현재 페이지: init(validation:maxIterations:overlapFactor:)
