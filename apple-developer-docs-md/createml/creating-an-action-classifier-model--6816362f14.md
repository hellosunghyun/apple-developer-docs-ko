---
title: "Creating an Action Classifier Model | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/creating-an-action-classifier-model"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131318+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   Creating an Action Classifier Model

문서

Action Classifier Model 만들기
===================================

사람의 몸동작을 인식하는 machine learning model을 training합니다.

[개요](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Overview)

------------------------------------------------------------------------------------------------------------

_action classifier_ 는 video에서 사람의 몸동작을 식별하는 machine learning model입니다. 예를 들어 운동 동작을 분류하도록 training한 action classifier는 jumping jacks를 하는 사람의 video를 제공하면 "jumping jacks"를 예측할 수 있습니다.

Create ML에서 action classifier를 만들려면 classifier가 인식하고 식별해야 하는 각 action을 사람이 수행하는 example video를 수집합니다. 예를 들어 exercise action classifier를 training하려면 jumping jacks, squats, lunges 같은 여러 운동을 수행하는 사람들의 video를 수집합니다.

![squats와 lunges라고 표시된 두 개의 video file 묶음이 Create ML로 들어가고, 이어서 “Action Classifier”라는 Core ML model file이 생성되는 흐름도입니다.](https://docs-assets.developer.apple.com/published/a2a2cb9e649e38d60cbf42c3d0790baf/creating-an-action-classifier-model-1%402x.png)

Create ML은 training 중 [Vision](https://developer.apple.com/documentation/Vision)
을 사용해 video의 각 frame에서 사람 몸의 중요한 지점인 _landmark_ 를 찾습니다. Action classifier는 시간이 지나면서 이 지점들의 움직임 pattern을 인식하도록 학습합니다. Vision을 사용해 body landmark를 찾는 방법은 [Detecting Human Body Poses in Images](https://developer.apple.com/documentation/Vision/detecting-human-body-poses-in-images)
를 참고합니다.

Create ML developer tool은 action classifier model을 training하고 평가하고 preview하는 데 도움이 됩니다. 각 model마다 training data와 parameter를 조합한 _model source_ 를 구성하면 하나의 project에서 여러 model을 training할 수 있습니다. 원하는 수준의 action classifier를 얻으면 Core ML model file로 export해 Xcode project에 추가합니다.

runtime에 app은 camera 또는 file에서 가져온 일련의 video frame을 분석해 action classifier로 사람의 action을 식별합니다.

![camera 앞에서 jumping jacks를 하는 사람으로 시작해 Vision framework를 거쳐 action classifier로 들어가고, 예측 label인 jumping jacks가 출력되는 흐름도입니다.](https://docs-assets.developer.apple.com/published/152f89bc0bbb977a0c9ed40469167c6c/creating-an-action-classifier-model-2%402x.png)

Create ML developer tool로 action classifier를 training하는 과정은 image classifier 같은 다른 model type과 전반적으로 같은 workflow를 따릅니다([Image Classifier Model 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model)
 참고). 다만 action classifier workflow에는 다음과 같은 중요한 차이점이 있습니다.

*   destination app에 맞춰 action classifier의 frame rate를 구성합니다
    
*   해당 frame rate를 충족하거나 초과하는 video를 확보합니다
    
*   적절한 환경에서 사람이 action을 명확히 수행하는 video를 확보합니다
    
*   관련은 있지만 불필요한 action의 video도 확보합니다
    

### [Frame Rate 선택](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Choose-a-Frame-Rate)

action classifier를 만들기 전에 destination app이 camera 또는 file에서 사용하는 _frame rate_ , 즉 초당 video frame 수를 결정합니다.

action classifier의 frame rate는 destination app의 frame rate와 맞추는 것이 좋습니다. 예를 들어 app이 camera에서 초당 30 frame(fps)으로 video를 가져온다면 action classifier도 30 fps로 구성할 계획을 세웁니다.

### [example action video 수집](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Collect-Example-Action-Videos)

action classifier의 frame rate를 정했으면 training video를 수집합니다. classifier와 destination app의 frame rate는 맞아야 하지만, training video의 frame rate는 classifier의 frame rate 이상이면 됩니다. 예를 들어 30 fps로 구성한 action classifier를 training할 때는 초당 30, 50, 60 frame의 video를 사용할 수 있습니다.

action classifier가 식별해야 하는 각 action마다 최소 50개의 example video를 수집합니다. 각 example video에는 한 사람이 해당 action을 명확하게 수행하는 모습이 보여야 합니다. 여러 사람이 나오는 video에서는 action을 수행하는 사람이 frame에서 가장 크고 두드러지게 보여야 합니다.

추가로 _negative class_ 를 위한 example video도 수집합니다. negative class는 action classifier가 볼 수는 있지만 app에는 관련이 없는 action들의 묶음입니다. Negative class는 관련 없는 action을 관련 있는 action으로 잘못 판단하지 않도록 도와줍니다.

[Action Classifier용 training video 모으기](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier)
에서 고품질 training video를 수집하고 negative class를 만드는 방법을 더 자세히 설명합니다.

### [example video 정리](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Organize-the-Example-Videos)

Create ML developer tool은 여러 종류의 data source를 지원하며, 각 source는 parent folder 안에서 file 배치 방식이 다릅니다. 대표적인 data-source type 두 가지는 다음과 같습니다.

*   label이 있는 folder별로 정리한 single-action video file
    
*   single-action 또는 multiple-action video file과 하나의 annotation file
    

![두 가지 file 배치 방식을 보여 주는 흐름도입니다. 왼쪽에는 Training Data 1이라는 parent folder 안에 Squats, Lunges, Jumping Jacks라는 세 개의 label folder가 있고, 각 folder 옆에는 해당 directory를 가리키는 화살표와 video file icon 묶음이 있습니다. 오른쪽에는 Training Data 2라는 parent folder 안에 annotations.csv, Squats1.mov, Squats2.mov, Jumping Jacks.mov, Exercise montage 1.mov의 5개 file이 있습니다.](https://docs-assets.developer.apple.com/published/c049c29698f004a1ed179f0358ca3ab7/creating-an-action-classifier-model-3%402x.png)

[Action Classifier Data Source 만들기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source)
에서 video file을 이런 배치 중 하나로 정리하는 자세한 방법을 설명합니다.

### [Action Classification project 구성](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Configure-an-Action-Classification-Project)

Xcode > Open Developer Tool > Create ML을 선택해 developer tool을 열고 새 Action Classification project를 만듭니다.

![Action Classification template를 강조한 Create ML의 새 project 대화상자 screenshot입니다.](https://docs-assets.developer.apple.com/published/38c7f28b647dbfccbc2990468c340a44/creating-an-action-classifier-model-4%402x.png)

model source의 Settings tab에 있는 Data section에서 training data source의 parent folder를 Training Data box로 드래그합니다.

![model source의 Data section에서 커서가 Training Data 1이라는 folder를 training data box로 드래그하는 screenshot입니다.](https://docs-assets.developer.apple.com/published/b601f871a91b39358acd52baf7046aad/creating-an-action-classifier-model-5%402x.png)

해당하는 경우 validation 및 testing data source의 folder를 각각 Validation Data와 Testing Data box로 드래그합니다. validation data source를 제공하지 않으면 Create ML이 Training Data data source의 일부를 사용하도록 Validation Data를 자동 구성합니다.

Parameters section의 값을 설정해 action classifier의 model source를 구성합니다. Frame Rate parameter는 destination app의 frame rate와 같은 값으로 설정합니다. 예를 들어 action classifier의 destination app이 초당 30 frame으로 video를 캡처하고 분석한다면 Frame Rate를 30 fps로 설정합니다.

Action Duration은 data source에 있는 대부분의 action을 완료하는 데 걸리는 시간을 기준으로 선택합니다. 예를 들어 training video file의 대다수 action이 약 2초 걸린다면 Action Duration을 2 seconds로 설정합니다.

![model source의 Parameters section에서 Iterations는 80, Frame Rate는 30 FPS, Action Duration은 2 seconds로 설정되고 Horizontal Flip augmentation이 선택된 screenshot입니다.](https://docs-assets.developer.apple.com/published/6c35996d1b5e528e7c54e38cfd989e17/creating-an-action-classifier-model-6%402x.png)

Create ML은 Frame Rate와 Action Duration 설정을 곱해 model의 prediction window 크기, 즉 예측에 필요한 frame 수를 계산합니다. 이 예시에서는 30 fps에 2 seconds를 곱하므로 prediction window 길이는 60 frame입니다.

모든 action이 camera의 왼쪽과 오른쪽 어느 쪽에서도 똑같이 유효하다면 Horizontal Flip augmentation을 활성화해 training data를 사실상 두 배로 늘릴 수 있습니다. Horizontal Flip을 활성화하면 Create ML은 [Vision](https://developer.apple.com/documentation/Vision)
이 분석한 각 video frame의 landmark 위치 output을 좌우 반전한 복사본으로 만듭니다.

### [Action Classifier training](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Train-the-Action-Classifier)

training session을 시작하려면 Train을 클릭합니다. Create ML은 [`VNDetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/Vision/VNDetectHumanBodyPoseRequest)
를 사용해 각 frame에서 사람의 body landmark를 찾는 feature-extraction 단계부터 시작합니다.

feature-extraction 단계는 training data의 크기와 Mac 성능에 따라 시간이 걸릴 수 있습니다. 이 단계가 끝나면 Create ML은 training 단계로 넘어가 landmark output sequence로부터 action을 인식하도록 action classifier를 학습시킵니다. 학습이 진행되는 동안 Create ML은 training iteration에 따른 model accuracy plot을 표시합니다.

![Training Tab에서 action classifier의 training iteration별 accuracy plot 위에 Pause와 Snapshot 버튼이 강조된 screenshot입니다. plot은 두 accuracy가 모두 20% 미만에서 시작해 86 iteration 후 training accuracy 95.9%, validation accuracy 96.7%까지 향상됩니다.](https://docs-assets.developer.apple.com/published/eec07bf4c375b3814a66d3539f0cae29/creating-an-action-classifier-model-7%402x.png)

battery를 아끼는 등 어떤 이유로든 training session을 잠시 중단해야 하면 Pause를 클릭합니다. training을 다시 이어갈 준비가 되면 Resume을 클릭합니다.

training이 끝나기 전에 model의 중간 version을 시험해 보고 싶다면 Snapshot을 클릭합니다. snapshot을 선택한 뒤 Output tab에서 export하면 snapshot으로 Core ML model file을 만들 수 있습니다. Output tab에 대한 자세한 내용은 아래 [Export the Action Classifier](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Export-the-Action-Classifier)
 섹션을 참고합니다.

### [Action Classifier 평가](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Assess-the-Action-Classifier)

Evaluation tab에서 training, validation, testing 단계의 Recall과 Precision metric을 확인해 model의 prediction accuracy를 평가합니다.

![Evaluation tab의 validation data precision 및 recall metric screenshot입니다. Precision column에서는 None class만 76%이고 나머지 class는 모두 100%입니다. recall column에서는 Jumping Jacks와 None class가 100%이고 나머지 class는 90~96% 범위입니다.](https://docs-assets.developer.apple.com/published/b0e16a86bb370138f9c009b1b48eff32/creating-an-action-classifier-model-8%402x.png)

action classifier가 요구 사항을 충족하지 못하면 Train More를 클릭해 model을 더 training합니다. 추가 training iteration으로도 성능이 개선되지 않으면 File > New Model Source를 선택해 다음 둘 중 하나 또는 둘 다를 바탕으로 model을 다시 training할 수 있습니다.

*   새로 만들거나 수정한 training-data source
    
*   다른 parameter
    

더 높은 accuracy의 action classifier가 필요하면 Action Duration parameter를 조정하거나 Horizontal Flip augmentation을 활성화해 봅니다. 특정 action을 잘 식별하지 못한다면 해당 action의 고품질 example video를 더 추가한 data source를 새로 만들거나 수정합니다.

action classifier가 nonaction을 action으로 잘못 식별한다면 그 불필요한 action 예시를 사용해 negative class를 만들거나 보강합니다. negative class를 만드는 방법은 [Action Classifier용 training video 모으기](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier)
를 참고합니다.

새 model source 구성을 마쳤으면 Train을 클릭해 그 설정으로 새로운 action classifier를 만듭니다. 그중 하나의 성능이 만족스러워질 때까지 평가, 조정, training 과정을 반복합니다.

### [Action Classifier preview](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Preview-the-Action-Classifier)

Xcode project에 추가하기 전에 Preview tab을 사용해 action classifier를 빠르게 테스트합니다. video를 드래그한 뒤 Play 버튼을 클릭하면 model의 prediction을 보면서 동작 방식을 시각적으로 확인할 수 있습니다.

![Preview tab에서 jumping jacks를 수행하는 사람의 video file을 재생하는 screenshot입니다. video 아래 prediction label은 Jumping Jacks이며 confidence는 100%입니다.](https://docs-assets.developer.apple.com/published/78af64f158184d826427091ea163ffc7/creating-an-action-classifier-model-9%402x.png)

video file을 드래그하면 Create ML은 action classifier를 사용해 file 전체를 한 번에 분석합니다. video를 재생하면 Create ML이 각 frame에 대한 action classifier의 prediction을 실시간으로 보여 줍니다.

### [Action Classifier export](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Export-the-Action-Classifier)

action classifier를 Core ML file로 저장하려면 Output tab을 선택하고 Get, Xcode, Share 버튼 중 하나를 클릭합니다. training이 완료된 모든 model source와 model training 중 생성한 모든 snapshot에서 model을 export할 수 있습니다.

![Output tab 오른쪽의 Get, Xcode, Share 세 버튼을 강조한 screenshot입니다.](https://docs-assets.developer.apple.com/published/72e5488326ec24c5ab791b2dfa302abb/creating-an-action-classifier-model-10%402x.png)

action classifier를 통합하고 적용하는 example app은 다음 sample code project를 참고합니다.

*   [live video feed에서 human action 감지하기](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed)
    
*   [Building a feature-rich app for sports analysis](https://developer.apple.com/documentation/Vision/building-a-feature-rich-app-for-sports-analysis)
    

[주제](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#topics)

--------------------------------------------------------------------------------------------------------

### [Action Classifier Data Source](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Action-Classifier-Data-Sources)

[Action Classifier용 training video 모으기](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier)

action classifier를 효과적으로 training하는 고품질 example video를 수집합니다.

[Action Classifier Data Source 만들기](https://developer.apple.com/documentation/createml/building-an-action-classifier-data-source)

training video를 action을 설명하는 label folder 여러 개에 나눠 배치하거나, annotation file과 함께 단일 folder에 배치합니다.

[참고 항목](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#see-also)

------------------------------------------------------------------------------------------------------------

### [video model](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model#Video-models)

[live video feed에서 human action 감지하기](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed)

일련의 video frame에서 얻은 사람의 pose data를 action-classification model에 전달해 몸동작을 식별합니다.

[`struct MLActionClassifier`](https://developer.apple.com/documentation/createml/mlactionclassifier)

video로 training해 사람의 몸동작을 분류하는 model입니다.

[`struct MLHandActionClassifier`](https://developer.apple.com/documentation/createml/mlhandactionclassifier)

제공한 사람 손동작 video로 training해 hand action classification model을 생성하는 task입니다.

[`struct MLStyleTransfer`](https://developer.apple.com/documentation/createml/mlstyletransfer)

image의 style을 다른 image 또는 video에 적용하도록 training하는 model입니다.

현재 페이지는 Creating an Action Classifier Model입니다
