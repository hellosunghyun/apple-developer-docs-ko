---
title: "write(toFile:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.136095+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   write(toFile:metadata:)

instance method

write(toFile:metadata:)
=======================

sound classifier를 file system의 path에 model file로 export합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func write(
        toFile path: String,
        metadata: MLModelMetadata? = nil
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:)#parameters)

----------------------------------------------------------------------------------------------------------------------

`path`

model을 저장할 file system 위치 path입니다.

`metadata`

export한 model file에 포함할 설명 정보입니다.

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:)#discussion)

----------------------------------------------------------------------------------------------------------------------

이 method를 사용하면 sound classifier를 path에 Core ML model로 저장합니다.

이 method는 다음과 같이 동작합니다.

*   path 위치가 directory이면 이름으로 `SoundClassifier.mlmodel`을 사용합니다.
    
*   extension을 제공하지 않으면 `mlmodel`을 extension으로 추가합니다.
    
*   물결표(~)를 home directory path로 바꿉니다.
    
*   중간 directory가 없으면 생성합니다.
    

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:)#see-also)

------------------------------------------------------------------------------------------------------------------

### [Saving a sound classifier](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:)#Saving-a-sound-classifier)

[`func write(to: URL, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:))

sound classifier를 file system의 위치에 model file로 export합니다.

현재 페이지: write(toFile:metadata:)
