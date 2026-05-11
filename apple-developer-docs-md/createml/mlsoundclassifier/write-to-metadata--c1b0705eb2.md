---
title: "write(to:metadata:) | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:)"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.139441+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:)#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   write(to:metadata:)

instance method

write(to:metadata:)
===================

sound classifier를 file system의 위치에 model file로 내보냅니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func write(
        to fileURL: URL,
        metadata: MLModelMetadata? = nil
    ) throws

[Parameters](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:)#parameters)

------------------------------------------------------------------------------------------------------------------

`fileURL`

model을 저장할 file system 위치의 URL입니다.

`metadata`

내보낸 model file에 포함할 설명 정보입니다.

[논의](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:)#discussion)

------------------------------------------------------------------------------------------------------------------

이 method를 사용해 sound classifier를 URL에 Core ML model로 저장합니다.

이 method는 다음과 같이 동작합니다.

*   URL 위치가 directory이면 이름으로 `SoundClassifier.mlmodel`을 사용합니다
    
*   extension을 제공하지 않으면 `mlmodel`을 extension으로 추가합니다
    
*   중간 directory가 없으면 생성합니다
    

[같이 보기](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:)#see-also)

--------------------------------------------------------------------------------------------------------------

### [sound classifier 저장하기](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(to:metadata:)#Saving-a-sound-classifier)

[`func write(toFile: String, metadata: MLModelMetadata?) throws`](https://developer.apple.com/documentation/createml/mlsoundclassifier/write(tofile:metadata:))

sound classifier를 file system 경로에 model file로 내보냅니다.

현재 페이지: write(to:metadata:)
