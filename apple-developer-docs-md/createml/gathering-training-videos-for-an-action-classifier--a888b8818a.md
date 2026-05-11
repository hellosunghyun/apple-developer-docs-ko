---
title: "Gathering Training Videos for an Action Classifier | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.133941+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)
    
*   Action Classifier용 training video 수집

Article

Action Classifier용 training video 수집
==================================================

Action classifier를 효과적으로 training할 수 있는 고품질 예시 video를 수집합니다.

[개요](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier#Overview)

---------------------------------------------------------------------------------------------------------------------------

classifier가 인식해야 하는 각 action을 사람이 수행하는 모습이 명확하게 보이는 고품질 video를 수집해 견고한 action classifier를 만듭니다. 여기에 classifier가 실제로 볼 수 있는 관련 없는 action의 video도 함께 수집합니다. 이런 video는 관련 없는 action으로 이루어진 _negative class_ 를 만드는 데 사용하며, classifier가 두 유형을 구분하도록 돕습니다.

Action classifier를 만드는 일반적인 방법은 [Action Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model)
문서를 참고하십시오.

### [각 action용 video 수집](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier#Collect-Videos-for-Each-Action)

Action classifier는 사람이 action을 수행하는 example video로 학습합니다. Create ML은 [Vision](https://developer.apple.com/documentation/Vision)
 framework를 사용해 각 video frame에서 _landmark_ 라고 부르는 주요 신체 부위를 찾습니다. Action classifier는 frame마다 이 landmark를 추적하면서 사람 몸의 움직임을 인식하는 방법을 학습합니다. example video를 촬영하거나 다른 출처의 video를 평가할 때는, 다음 지침을 적용해 landmark가 분명히 보이도록 유지합니다.

*   camera를 고정합니다.
    
*   한 번에 한 사람만 촬영합니다.
    
*   사람의 전신이 들어오도록 촬영합니다.
    
*   주변 환경에 충분한 조명이 있는지 확인합니다.
    
*   사람의 옷이 헐렁하거나 흩날리지 않도록 합니다.
    
*   사람의 옷이 배경과 충분히 대비되도록 합니다.
    
*   action 수행 중 사람을 가릴 수 있는 전경 object를 치웁니다.
    
*   하나의 recording에서 같은 action을 여러 번 수행한다면, 반복 사이 시간을 최소화합니다.
    

일반적으로 action classifier는 app을 사용하는 어떤 사람에게도 동작하길 원합니다. 사람의 머리 위치나 팔의 배치처럼 action에 생기는 자연스러운 variation이 포함된 video를 넣어 model이 이런 차이를 반영하도록 학습시킵니다.

app이 더 일반적인 action을 인식하거나 다양한 camera 각도에서 인식하길 원한다면, 여러 방향에서 action을 담은 example video를 더 추가합니다.

### [negative class용 video 수집](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier#Collect-Videos-for-a-Negative-Class)

negative class는 action classifier에서 중요하지 않은 하나 이상의 action을 묶은 category입니다. negative class는 classifier가 인식해야 하는 action과 app에서 마주칠 수 있는 잠재적 nonaction을 구분하도록 돕습니다.

classifier가 관찰할 수 있는 관련 없는 모든 nonaction의 example video를 수집해 negative class를 만듭니다. 예를 들어 운동 action classifier의 negative class에는 사람들이 frame 안팎으로 걸어 다니는 예시가 들어갈 수 있습니다. 이런 negative class를 포함하면 action classifier가 lunge 같은 운동 action과 walking을 혼동할 가능성이 줄어듭니다.

지속 시간이 다른 nonaction이나 정적인 nonaction과 동적인 nonaction에 대해서는 추가 negative class를 만듭니다. 예를 들어 운동 classifier에는 가만히 서 있거나 의자에 앉아 있는 사람 예시를 포함하는 정적 action용 negative class를 하나 더 둘 수 있습니다.

[같이 보기](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier#see-also)

---------------------------------------------------------------------------------------------------------------------------

### [Action Classifier data source](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier#Action-Classifier-Data-Sources)

[Action Classifier Data Source 구축하기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source)

training video를 action을 설명하는 label별 여러 folder에 정리하거나, annotation file과 함께 하나의 folder에 정리합니다.

현재 페이지는 Action Classifier용 training video 수집입니다.
