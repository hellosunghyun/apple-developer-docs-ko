---
title: "Creating an Image Classifier Model | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/creating-an-image-classifier-model"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.129469+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   Image Classifier Model 만들기

문서

Image Classifier Model 만들기
==================================

image를 분류하는 machine learning model을 training하고 Core ML app에 추가합니다.

[개요](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Overview)

-----------------------------------------------------------------------------------------------------------

_image classifier_ 는 image를 인식하는 machine learning model입니다. image를 입력하면 해당 image의 category label을 반환합니다.

![기린 image에서 image classifier가 Giraffe label을 예측하는 방식을 보여주는 flow diagram입니다.](https://docs-assets.developer.apple.com/published/7c6d96174f8701c5d2402beed64563cc/creating-an-image-classifier-model-1%402x.png)

image classifier는 이미 label이 붙은 image 예시를 많이 보여 주면서 training합니다. 예를 들어 코끼리, 기린, 사자 등의 사진을 모아 동물을 인식하는 image classifier를 training할 수 있습니다.

![동물 image가 Create ML로 들어가고, 그 결과 image classifier Core ML model file이 생성되는 과정을 보여주는 flow diagram입니다.](https://docs-assets.developer.apple.com/published/43b7b6573341efcb1184f5998a570435/creating-an-image-classifier-model-2%402x.png)

image classifier의 training이 끝나면 정확도를 평가하고, 성능이 충분하면 Core ML model file로 저장합니다. 그런 다음 model file을 Xcode project로 가져와 app에서 image classifier를 사용합니다.

### [data 수집하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Gather-Your-Data)

category마다 최소 10장의 image를 사용합니다. 다만 image classifier는 더 다양한 image 집합을 사용할수록 성능이 좋아집니다. 각 category의 image를 여러 각도와 다양한 조명 조건으로 포함하는 것이 좋습니다.

각 category의 image 수를 균형 있게 맞춥니다. 예를 들어 한 category에는 10장만 사용하고 다른 category에는 1000장을 사용하지 마십시오.

image는 JPEG, PNG처럼 Quicktime Player에서 열 수 있는 형식이면 무엇이든 사용할 수 있습니다. 특정 크기일 필요도 없고 모두 같은 크기일 필요도 없습니다. 하지만 최소 299 x 299 pixel 이상인 image를 사용하는 것이 좋습니다.

가능하다면 app에서 실제로 model이 보게 될 상황을 가장 잘 반영하는 image를 모읍니다. 예를 들어 app이 야외 환경에서 device camera로 촬영한 image를 분류한다면, 동일하거나 유사한 camera로 찍은 야외 image를 수집합니다.

### [Training Data 정리하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Organize-Your-Training-Data)

image를 subfolder로 분류해 training dataset을 준비합니다. 각 subfolder에는 그 안에 들어 있는 image category의 이름을 붙입니다. 예를 들어 치타 image에는 모두 `Cheetah` label을 사용할 수 있습니다.

![Training Data라는 folder와 그 안의 subfolder를 보여주는 diagram입니다. 각 subfolder 이름은 포함된 image category의 label을 사용합니다. 예를 들어 치타 image는 모두 Cheetah라는 subfolder에 들어갑니다.](https://docs-assets.developer.apple.com/published/0a419b23cc4238d4b0a2baee09d2f4ea/creating-an-image-classifier-model-3%402x.png)

### [Testing Data 정리하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Organize-Your-Testing-Data)

testing dataset으로 model을 테스트하면 training된 model이 실제 환경에서 얼마나 잘 동작할지 빠르게 확인할 수 있습니다.

dataset에 category당 25장 이상처럼 충분한 image가 있다면, training dataset의 folder 구조를 복제해 testing dataset을 만듭니다. 그런 다음 각 category image의 약 20%를 testing dataset의 대응 category folder로 옮깁니다.

### [Image Classifier Project 만들기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Create-an-Image-Classifier-Project)

Create ML을 사용해 image classifier project를 만듭니다. Xcode를 연 상태에서 Dock의 Xcode icon을 Control-클릭하고 Open Developer Tool > Create ML을 선택합니다. 또는 Xcode menu에서 Open Developer Tool > Create ML을 선택합니다.

Create ML에서 File > New Project를 선택해 model template 목록을 확인합니다. Image Classification을 선택하고 Next를 클릭합니다.

![Create ML project template window의 screenshot입니다. Image Classification template가 선택되어 있으며, 다른 template로 Style Transfer, Action Classification, Sound Classification, Tabular Regression이 포함되어 있습니다.](https://docs-assets.developer.apple.com/published/bcec307ffcea638a98721a2178b9ee77/creating-an-image-classifier-model-4%402x.png)

project의 기본 이름을 더 의미 있는 이름으로 바꿉니다. 필요하다면 이 project에서 생성되는 model에 대해 author 정보나 짧은 description 같은 추가 정보도 입력합니다.

![새 project option window의 screenshot입니다. Project Name, Author, License, Description text field가 있으며, 앞의 세 field에는 각각 Animal Classifier, Maria Ruiz, No license provided 값이 들어 있습니다. Description field에는 동물을 인식하는 image classification machine learning model이라는 설명이 표시됩니다.](https://docs-assets.developer.apple.com/published/37e7674a1b5d8a07422cfdc99d6a9a33/creating-an-image-classifier-model-5%402x.png)

### [Training Session 구성하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Configure-the-Training-Session)

training dataset이 들어 있는 folder를 project window의 Training Data 영역으로 드래그합니다.

![Settings tab의 project window screenshot입니다. 사용자가 Training Data라는 Finder folder를 Training Data 영역으로 드래그하고 있습니다.](https://docs-assets.developer.apple.com/published/1d0270e05db222c3bdcb256eaf8e3893/creating-an-image-classifier-model-6%402x.png)

해당한다면 testing dataset이 들어 있는 folder도 project window의 Testing Data 영역으로 드래그합니다.

![Settings tab의 project window screenshot입니다. 사용자가 Testing Data라는 Finder folder를 Testing Data 영역으로 드래그하고 있습니다. ](https://docs-assets.developer.apple.com/published/32ba5e3473a5edc9088be6314f99b79a/creating-an-image-classifier-model-7%402x.png)

image classifier를 training하기 전에 다음 parameter를 조정할 수 있습니다.

Feature Extractor

_Feature Extractor_ 는 image classifier training session에서 image feature를 추출하는 underlying base model입니다. feature extraction에는 두 가지 option이 있습니다. _Image Feature Print V2_ 는 _Image Feature Print V1_ 보다 output embedding 크기가 작습니다. 그 결과 training 시간이 더 짧아지고, 추출한 feature를 저장하는 데 필요한 memory가 줄어들며, 정확도도 높아질 수 있습니다. 반면 _Image Feature Print V1_ 은 macOS 10.14 이상, iOS 12 이상을 포함한 더 오래된 operating system과 호환됩니다. _Image Feature Print V2_ 는 macOS 14 이상, iOS 17 이상과 호환됩니다.

Iterations

training session에서 사용할 training iteration 수를 알고 있다면 기본값을 변경합니다. 정확한 model을 얻을 수 있을 만큼 충분한 iteration을 포함해야 하며, 너무 일찍 중단하면 정확도가 낮은 model이 될 수 있습니다.

Augmentations

image augmentation option은 일부만 켜거나 전부 켤 수 있습니다. 각 augmentation은 dataset image를 복제한 뒤 transform 또는 filter를 적용하므로, 추가 image를 수집하지 않고도 dataset에 더 많은 다양성을 줄 수 있습니다.

![Settings tab의 project window screenshot입니다. Parameters section이 강조되어 있습니다. Feature Extractor는 Image Feature Print V2로 설정되어 있고, Iterations는 50이며, Augmentations에는 Add Noise, Blur, Crop, Expose, Flip, Rotate라는 6개의 checkbox가 있습니다.](https://docs-assets.developer.apple.com/published/7df3c337506bafe1f56fd2a6671f3e5d/creating-an-image-classifier-model-8%402x.png)

### [Image Classifier Training하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Train-the-Image-Classifier)

Train button을 클릭해 training session을 시작합니다. Create ML은 먼저 training data 일부를 빠르게 분리해 validation dataset을 만듭니다. 다음으로 남은 training image에서 edge, corner, texture, color region과 같은 feature를 추출합니다. Create ML은 이 image feature를 사용해 model을 반복적으로 training하고 validation dataset으로 정확도를 확인합니다.

![Training tab의 project window screenshot입니다. model accuracy와 training iteration 수의 관계를 나타내는 line graph가 보입니다. 선은 전반적으로 100%를 향해 올라가며, 25 iteration 후 training accuracy는 100%, validation accuracy는 97.5%로 끝납니다.](https://docs-assets.developer.apple.com/published/01ed3f16d8fb987b51695b50c63371c4/creating-an-image-classifier-model-9%402x.png)

Create ML은 graph로 진행 상황을 보여 주며, 검은색 선과 회색 선은 각각 training dataset과 validation dataset에서의 model accuracy를 나타냅니다.

### [Model 정확도 평가하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Assess-the-Models-Accuracy)

Create ML이 model training을 마치면 testing dataset을 사용해 model을 테스트합니다. testing이 끝나면 Evaluation tab에서 training, validation, testing accuracy score를 보여 줍니다. model은 training dataset image로 학습했기 때문에 보통 training dataset에서 accuracy score가 더 높습니다. 이 예시에서 image classifier model은 다음을 정확히 식별했습니다.

*   training image의 100 percent
    
*   validation image의 95 percent
    
*   testing image의 97 percent
    

![Evaluation tab의 project window screenshot입니다. testing dataset table에 Class, Item Count, Precision, Recall column이 있습니다. table은 Precision 내림차순으로 정렬되어 있고, 첫 번째 행의 값은 각각 Giraffe, 9, 100%, 100%입니다.](https://docs-assets.developer.apple.com/published/97c4586d7483e9b6020cfb1707ab575a/creating-an-image-classifier-model-10%402x.png)

_Precision_ 은 true positive 수를 true positive와 false positive의 합으로 나눈 값입니다. _Recall_ 은 true positive 수를 true positive와 false negative의 합으로 나눈 값입니다.

evaluation 성능이 충분하지 않다면 더 다양한 dataset으로 새 model을 training해야 할 수 있습니다. 예를 들어 새로운 각도나 새로운 환경에서 추가 image를 수집하거나 image augmentation option을 하나 이상 더할 수 있습니다. model 평가 방법과 model 성능 개선 전략에 대한 자세한 내용은 [model accuracy 개선하기](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)
를 참조하십시오.

### [Model 미리 보기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Preview-the-Model)

Preview tab을 클릭해 model이 이전에 보지 못한 image로 테스트해 봅니다. model prediction을 보려면 Train button 아래 column으로 image file을 드래그합니다.

![Preview tab의 project window screenshot입니다. 코끼리 image를 elephant로 예측하며 confidence는 100%입니다.](https://docs-assets.developer.apple.com/published/ef1d1eea81eeb237b95a654d86f39f33/creating-an-image-classifier-model-11%402x.png)

### [Model 저장하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Save-the-Model)

model 성능이 만족스러우면 file system에 Core ML 형식으로 저장합니다. Output tab에서 다음 방법 중 하나로 model을 저장합니다.

*   Save button을 클릭해 model을 file system에 저장합니다.
    
*   Export button을 클릭해 model을 Xcode에서 엽니다.
    
*   Share button을 클릭해 Mail이나 Messages 같은 방법으로 다른 사람에게 model을 보냅니다.
    
*   model icon을 file을 받을 수 있는 위치 어디로든 드래그합니다.
    

![Output tab의 project window screenshot입니다. 사용자가 Get-button을 클릭한 뒤 model save dialog가 표시됩니다. Get-button icon은 아래쪽 화살표가 들어가는 상자 모양입니다.](https://docs-assets.developer.apple.com/published/7f83e09c032cbc1e776922609f55362a/creating-an-image-classifier-model-12%402x.png)

### [App에 Model 추가하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Add-the-Model-to-Your-App)

마지막 단계는 training한 model을 Xcode project에 추가하는 것입니다. 예를 들어 image classifier model은 [Classifying Images with Vision and Core ML](https://developer.apple.com/documentation/CoreML/classifying-images-with-vision-and-core-ml)
sample의 model을 대체할 수 있습니다.

sample을 다운로드하고 Xcode에서 project를 엽니다. model file을 navigation pane으로 드래그합니다. Xcode는 model을 project에 추가하고 model metadata, operating system availability, class label 등을 보여 줍니다.

![Xcode에서 sample code project를 연 screenshot입니다. editor view에 Animal Classifier model이 표시됩니다.](https://docs-assets.developer.apple.com/published/ebaa8ae6231ff7c7187ac51fe51256c8/creating-an-image-classifier-model-13%402x.png)

code에서 model을 사용하려면 한 줄만 바꾸면 됩니다. 이 project는 `ImagePredictor` class 한 곳에서만 MobileNet model을 instance화합니다.

    // image classifier wrapper class의 instance를 만듭니다.
    let imageClassifierWrapper = try? MobileNet(configuration: defaultConfig)
    

이 줄을 다음처럼 image classification model class를 사용하도록 바꿉니다.

    // image classifier wrapper class의 instance를 만듭니다.
    let imageClassifierWrapper = try? AnimalClassifier(configuration: defaultConfig)
    

두 model은 모두 input으로 image를 받고 output으로 label string을 내보내므로 서로 교체할 수 있습니다. model을 바꿔 끼우면 sample app은 이전과 같은 방식으로 image를 분류하지만, 이제는 사용자의 model과 그에 연결된 label을 사용합니다.

### [Model Training과 평가 자동화하기](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Automate-Model-Training-and-Assessment)

위 섹션에서 설명했듯이 Create ML을 사용하면 적은 code와 적은 machine learning 전문 지식만으로도 유용한 image classifier를 training할 수 있습니다. 하지만 [`MLImageClassifier`](https://developer.apple.com/documentation/createml/mlimageclassifier)
instance를 사용해 model training 과정을 script로 처리할 수도 있습니다. 전체 작업은 동일합니다. data를 준비하고, model을 training하고, 성능을 평가하고, Core ML model file을 저장합니다. 차이는 모든 작업을 programmatically 수행한다는 점입니다.

예를 들어 [`MLImageClassifier.DataSource`](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource)
instance 두 개를 초기화해 하나는 training dataset용으로, 다른 하나는 testing dataset용으로 사용할 수 있습니다. training data source를 사용해 [`init(trainingData:parameters:)`](https://developer.apple.com/documentation/createml/mlimageclassifier/init(trainingdata:parameters:)-4r6hr)
로 image classifier를 초기화합니다. 그런 다음 testing data source와 그 [`evaluation(on:)`](https://developer.apple.com/documentation/createml/mlimageclassifier/evaluation(on:)-9p8mi)
method를 사용하고, 반환된 [`MLClassifierMetrics`](https://developer.apple.com/documentation/createml/mlclassifiermetrics)
instance의 값을 평가합니다.

[참고 항목](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#see-also)

-----------------------------------------------------------------------------------------------------------

### [Image model](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model#Image-models)

[`struct MLImageClassifier`](https://developer.apple.com/documentation/createml/mlimageclassifier)

image를 분류하도록 training하는 model입니다.

[`struct MLObjectDetector`](https://developer.apple.com/documentation/createml/mlobjectdetector)

image 안의 하나 이상의 object를 분류하도록 training하는 model입니다.

[`struct MLHandPoseClassifier`](https://developer.apple.com/documentation/createml/mlhandposeclassifier)

제공한 사람 손 image로 training해 hand pose classification model을 만드는 task입니다.

현재 페이지는 Creating an Image Classifier Model입니다
