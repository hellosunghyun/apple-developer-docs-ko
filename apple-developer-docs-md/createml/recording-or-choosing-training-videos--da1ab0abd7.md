---
title: "Gathering Training Videos for an Action Classifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.150089+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   Gathering Training Videos for an Action Classifier

문서

Gathering Training Videos for an Action Classifier
==================================================

action classifier를 효과적으로 training할 수 있는 고품질 example video를 수집합니다.

[개요](https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos#Overview)

--------------------------------------------------------------------------------------------------------------

classifier가 인식해야 하는 각 action을 사람이 수행하는 모습이 분명히 보이는 고품질 video를 수집해 견고한 action classifier를 만듭니다. 여기에 classifier가 마주칠 수 있는 관련 없는 action video도 함께 수집합니다. 이 video는 관련 없는 action의 _negative class_ 를 만드는 데 사용하며, classifier가 두 유형을 구분하도록 돕습니다.

action classifier를 만드는 일반적인 방법은 [Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)
.

### [각 Action용 Video 수집](https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos#Collect-Videos-for-Each-Action)

action classifier는 사람이 action을 수행하는 example video로 학습합니다. Create ML은 [Vision](https://developer.apple.com/documentation/Vision)
 framework를 사용해 각 video frame에서 _landmark_ 라는 주요 신체 부위를 찾습니다. action classifier는 이 landmark를 frame마다 추적하면서 사람의 움직임을 인식하는 방법을 학습합니다. example video를 녹화하거나 다른 source의 video를 평가할 때는 다음 지침을 적용해 landmark가 분명히 보이도록 합니다.

*   camera를 고정합니다.
    
*   한 번에 한 사람만 촬영합니다.
    
*   사람의 전신이 보이게 촬영합니다.
    
*   환경에 충분한 조명이 있는지 확인합니다.
    
*   사람의 옷이 헐렁하거나 흩날리지 않도록 합니다.
    
*   사람의 옷이 배경과 충분히 대비되도록 합니다.
    
*   사람이 action을 수행할 때 가릴 수 있는 전경 object를 제거합니다.
    
*   한 recording에서 같은 action을 여러 번 수행한다면 반복 사이 시간을 최소화합니다.
    

일반적으로 action classifier는 app을 사용하는 어떤 사람에게도 동작하길 원합니다. 사람이 머리를 드는 방식이나 팔을 두는 방식처럼 classifier가 인식해야 하는 action의 변형을 담은 video를 포함해, model이 자연스러운 변이를 반영하도록 학습시킵니다.

app이 action을 더 일반적으로 인식하거나 다양한 camera 각도에서 인식하길 원한다면, 여러 방향에서 action을 촬영한 example video를 더 추가합니다.

### [Negative Class용 Video 수집](https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos#Collect-Videos-for-a-Negative-Class)

negative class는 action classifier에 중요하지 않은 하나 이상의 action category입니다. negative class는 classifier가 인식해야 하는 action과 app에서 마주칠 수 있는 잠재적 nonaction을 구분하도록 도와줍니다.

classifier가 관찰할 수 있는 관련 없는 nonaction의 example video를 모아 negative class를 만듭니다. 예를 들어 exercise-action classifier의 negative class에는 사람이 frame 안팎으로 걸어 들어오고 나가는 예시를 포함할 수 있습니다. 이런 negative class를 포함하면 action classifier가 걷기를 lunge 같은 exercise로 혼동할 가능성을 줄일 수 있습니다.

시간 길이가 다른 nonaction이나 정적인 nonaction과 동적인 nonaction을 위해 추가 negative class를 만듭니다. 예를 들어 exercise classifier에는 사람이 가만히 서 있거나 의자에 앉아 있는 예시를 포함한 또 다른 정적 action용 negative class가 있을 수 있습니다.

현재 페이지는 Gathering Training Videos for an Action Classifier입니다
