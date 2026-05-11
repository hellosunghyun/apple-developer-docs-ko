---
title: "Building an Action Classifier Data Source | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133774+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)
    
*   Action Classifier Data Source 만들기

문서

Action Classifier Data Source 만들기
=========================================

action을 설명하는 label별로 training video를 여러 folder에 정리하거나, annotation file과 함께 하나의 folder에 정리합니다.

[개요](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source#Overview)

------------------------------------------------------------------------------------------------------------------

Create ML developer tool은 action classifier용으로 여러 data source type을 지원하며, 각 type마다 file system 구성 방식이 다릅니다. 일반적으로는 다음 두 가지 type 중 하나를 사용합니다.

Label별 folder

single-action video file을 label별 folder로 묶은 collection입니다.

Annotation이 있는 video

annotation file과 함께 single-action 또는 multi-action video file을 하나의 folder에 모은 collection입니다.

예시 video file을 모두 trim했고 각 file이 하나의 action을 한 번 이상 보여 준다면, 어느 data source type이든 사용할 수 있습니다. 반대로 모든 video를 trim하지 않았거나, 하나 이상이 _montage_ video처럼 둘 이상의 서로 다른 action을 담고 있다면 annotated video를 사용해야 합니다.

Create ML API가 지원하는 action-classifier data source type에 대한 자세한 내용은 [`MLActionClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource)
.

action classifier를 만드는 전반적인 방법은 [Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)
.

### [Labeled Folder로 Data Source 만들기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source#Build-a-Data-Source-with-Labeled-Folders)

labeled folder를 담을 parent folder를 만듭니다. 그런 다음 action마다 하나씩 folder를 만들고, folder 이름을 그 action의 label로 사용합니다. 각 예시 video file은 video의 action과 일치하는 label folder에 넣습니다. 예를 들어 data source에 “Jumping Jacks”와 “Squats”라는 folder가 있다면, 해당 action video를 각각 대응하는 folder에 배치합니다.

![labeled directory data source의 파일 구성을 보여 주는 flow diagram입니다. Training Data 1이라는 parent folder 안에 Squats, Lunges, Jumping Jacks라는 세 개의 labeled folder가 있습니다. 각 labeled folder 옆에는 해당 labeled directory를 가리키는 화살표와 함께 video file icon 묶음이 표시됩니다.](https://docs-assets.developer.apple.com/published/f288d165786aefedd400466cf528383e/building-an-action-classifier-data-source-1%402x.png)

각 video file에는 같은 action instance가 둘 이상 들어 있을 수 있지만, 각 instance 사이의 시간 간격은 최소화해야 합니다. action instance 사이에 움직임이 없는 구간이 보이면, video file을 여러 file로 나누고 각 video를 해당 action에 맞게 trim해 그 구간을 제거합니다.

### [Annotated Video로 Data Source 만들기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source#Build-a-Data-Source-with-Annotated-Videos)

folder를 하나 만들고 모든 예시 video file을 그 안에 넣습니다. 그런 다음 CSV 형식(`.csv` 또는 `.txt` 확장자)이나 JSON 형식으로 annotation file을 만듭니다.

![annotated video data source의 파일 구성을 보여 주는 flow diagram입니다. Training Data 2라는 parent folder 안에 annotations.csv, Squats1.mov, Squats2.mov, Jumping Jacks.mov, Exercise montage 1.mov라는 다섯 개의 file이 있습니다.](https://docs-assets.developer.apple.com/published/26472f7c02e0bace57143933dd20e93c/building-an-action-classifier-data-source-2%402x.png)

annotation file의 각 entry에는 다음 category가 있어야 합니다.

`label`

action을 설명하는 이름 또는 label입니다.

`video`

예시 action이 들어 있는 video의 file name 또는 path입니다.

더 큰 video file 안에서 예시 video clip의 시작과 끝을 표시하려면 annotation file에 time index category를 추가할 수도 있습니다.

`start`

video file 안에서 시작 time index입니다.

`end`

video file 안에서 끝 time index입니다.

`start`와 `end` time index는 둘 이상의 서로 다른 action type을 보여 주는 _montage_ video에 사용합니다. annotation file에서 `start` category를 생략하면 Create ML은 모든 entry의 시작 지점을 각 video file의 처음으로 처리합니다. `end` category를 생략하면 Create ML은 모든 video의 끝을 기본값으로 사용합니다.

Create ML은 다음과 같은 여러 time index 형식을 인식합니다.

*   초를 나타내는 integer. 예: `0`, `3`, `5`
    
*   초를 나타내는 floating point number. 예: `0.0`, `3.14`, `60.5`
    
*   분과 초를 나타내는 string. 예: `01:03`
    
*   분, 초, 소수 초를 나타내는 string. 예: `01:03.14`
    
*   시, 분, 초를 나타내는 string. 예: `05:01:03`
    

이 index를 사용해 예시 clip이 video file 안에서 어디서 시작하고 끝나는지 지정합니다. 예를 들어 하나의 video file에 squats와 lunges가 모두 들어 있다면, 아래 CSV file 예시처럼 서로 다른 time index를 사용해 같은 file을 여러 annotation에서 사용할 수 있습니다.

    video, label, start, end
    lunge23.mov, Lunge, 0, 3.1
    squats_13.mov, Squat, 0, 5
    Jumping Jacks 1.mov, Jumping Jacks, 0, 4.7
    Various_Exercises.mov, Lunge, 0.0, 2.2
    Various_Exercises.mov, Lunge, 8:3.2, 8:4.5
    Various_Exercises.mov, Squat, 1:59:5.8, 1:59:7
    Various_Exercises.mov, Squat, 1:59:14, 1:59:15.1
    

JSON 형식의 annotation file을 만들려면 file root에 annotation object array를 만듭니다. 다음 예시는 앞선 CSV file과 동일한 내용을 JSON으로 표현한 것입니다.

     [\
      {\
        "video" : "lunge23.mov",\
        "label" : "Lunge",\
        "start" : 0,\
        "end"   : 3.1\
      },\
      {\
        "video" : "squats_13.mov",\
        "label" : "Squat",\
        "start" : 0,\
        "end"   : 5\
      },\
      {\
        "video" : "Jumping Jacks 1.mov",\
        "label" : " Jumping Jacks",\
        "start" : 0,\
        "end"   : 4.7\
      },\
      {\
        "video" : "Various_Exercises.mov",\
        "label" : "Lunge",\
        "start" : 0.0,\
        "end"   : 2.2\
      },\
      {\
        "video" : "Various_Exercises.mov",\
        "label" : "Lunge",\
        "start" : "8:3.2",\
        "end"   : "8:4.5"\
      },\
      {\
        "video" : "Various_Exercises.mov",\
        "label" : "Squat",\
        "start" : "1:59:5.8",\
        "end"   : "1:59:7"\
      },\
      {\
        "video" : "Various_Exercises.mov",\
        "label" : "Squat",\
        "start" : "1:59:14",\
        "end"   : "1:59:15.1"\
      }\
    ]
    

[같이 보기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source#see-also)

------------------------------------------------------------------------------------------------------------------

### [Action Classifier Data Source](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source#Action-Classifier-Data-Sources)

[Action Classifier용 training video 모으기](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier)

action classifier를 효과적으로 training할 수 있는 고품질 예시 video를 수집합니다.

현재 페이지: Building an Action Classifier Data Source
