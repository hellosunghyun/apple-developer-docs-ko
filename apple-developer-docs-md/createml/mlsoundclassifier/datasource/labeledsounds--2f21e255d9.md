---
title: "labeledSounds() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledsounds()"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.149137+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledsounds()#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
    
*   *   [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier)
        
*   [MLSoundClassifier.DataSource](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)
    
*   labeledSounds()

instance method

labeledSounds()
===============

data source의 label이 지정된 audio file dictionary를 생성합니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.15+visionOS 1.0+

    func labeledSounds() throws -> [String : [URL]]

[반환 값](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledsounds()#return-value)

-----------------------------------------------------------------------------------------------------------------------------

label이 지정된 audio file의 dictionary입니다. 각 dictionary key는 label string이고 값은 audio-file URL 배열입니다.

현재 페이지는 labeledSounds()입니다
