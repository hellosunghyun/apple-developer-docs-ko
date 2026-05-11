---
title: "Detecting human actions in a live video feed | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.131457+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   live video feed에서 사람 action 감지하기

Sample Code

live video feed에서 사람 action 감지하기
============================================

연속된 video frame에서 사람의 pose data를 action-classification model로 보내 body movement를 식별합니다.

[다운로드](https://docs-assets.developer.apple.com/published/f1a45aa976a1/DetectingHumanActionsInALiveVideoFeed.zip)

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+Xcode 12.3+

[개요](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Overview)

---------------------------------------------------------------------------------------------------------------------

이 sample app은 [Vision](https://developer.apple.com/documentation/Vision)으로 연속된 video frame을 분석하고 action classifier를 적용해 움직임 이름을 예측함으로써 사람의 몸동작(_actions_)을 인식합니다. 이 sample의 action classifier는 다음 세 가지 운동을 인식합니다.

*   점핑잭
    
*   런지
    
*   버피
    

![jumping jacks를 수행하는 사람이 device camera 앞에 서 있는 장면에서 prediction label까지 이어지는 action classifier의 목적을 보여주는 흐름도](https://docs-assets.developer.apple.com/published/75929e2897662f60b99a1231b050d753/detecting-human-actions-1%402x.png)

app은 device camera의 live full-screen video feed 위에 현재 action prediction을 계속 표시합니다. frame에서 한 명 이상의 사람을 인식하면 각 사람 위에 wireframe body pose를 overlay합니다. 동시에 _prominent_ person의 현재 action도 예측하는데, 일반적으로 camera에 가장 가까운 사람입니다.

![sample app의 main view를 보여 주는 다이어그램](https://docs-assets.developer.apple.com/published/7884307fabe284474a34bad3c1e1e742/detecting-human-actions-2%402x.png)

launch 시 app은 device camera를 구성해 video frame을 생성한 뒤, [Combine](https://developer.apple.com/documentation/Combine)으로 연결한 일련의 method에 frame을 전달합니다. 이 method들은 함께 동작해 frame을 분석하고 다음 순서로 action prediction을 만듭니다.

1.  각 frame에서 사람의 body pose를 모두 찾습니다.
    
2.  prominent pose를 분리합니다.
    
3.  prominent pose의 position data를 시간에 따라 누적합니다.
    
4.  누적한 data를 action classifier에 보내 action prediction을 만듭니다.
    

![sample app 내부에서 video frame이 이동하는 경로를 보여주는 흐름도](https://docs-assets.developer.apple.com/published/d60ff302fc0e9dce6cb6b9011e42b408/detecting-human-actions-3%402x.png)

[Sample Code 프로젝트 구성하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Configure-the-Sample-Code-Project)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

이 sample app은 camera를 사용하므로 Simulator에서는 실행할 수 없습니다. iOS 또는 iPadOS device에서 실행해야 합니다.

[Video Capture Session 시작하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Start-a-Video-Capture-Session)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

app의 `VideoCapture` class는 [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession)을 생성해 device camera를 구성하고 video frame을 만들게 합니다.

app이 처음 launch될 때, 또는 사용자가 device를 회전하거나 camera를 전환할 때 video capture는 `configureCaptureSession()` method에서 camera input, frame output, 그리고 둘 사이의 connection을 구성합니다.

    let input = AVCaptureDeviceInput.createCameraInput(position: cameraPosition)
    
    
    let output = AVCaptureVideoDataOutput.withPixelFormatType(kCVPixelFormatType_32BGRA)
    
    
    let success = configureCaptureConnection(input, output)
    return success ? output : nil
    

`createCameraInput(position:frameRate:)` method는 전면 또는 후면 camera를 선택하고, frame rate를 action classifier와 맞도록 구성합니다.

`AVCaptureVideoDataOutput.withPixelFormatType(_:)` method는 특정 pixel format의 frame을 생성하는 [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput)을 만듭니다.

`configureCaptureConnection(_:_:)` method는 capture session의 camera input과 video output 사이 관계를 다음과 같이 구성합니다.

*   video orientation 선택
    
*   video를 수평으로 뒤집을지 결정
    
*   적용 가능한 경우 image stabilization 활성화
    

    if connection.isVideoOrientationSupported {
        // Set the video capture's orientation to match that of the device.
        connection.videoOrientation = orientation
    }
    
    
    if connection.isVideoMirroringSupported {
        connection.isVideoMirrored = horizontalFlip
    }
    
    
    if connection.isVideoStabilizationSupported {
        if videoStabilizationEnabled {
            connection.preferredVideoStabilizationMode = .standard
        } else {
            connection.preferredVideoStabilizationMode = .off
        }
    }
    

이 method는 video output의 [`alwaysDiscardsLateVideoFrames`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput/alwaysDiscardsLateVideoFrames) property를 `true`로 설정해 app이 real time으로 동작하도록 유지하고 frame backlog가 쌓이는 것을 방지합니다.

    // Discard newer frames if the app is busy with an earlier frame.
    output.alwaysDiscardsLateVideoFrames = true
    

capture session 구성과 input/output 연결 방법은 [Setting up a capture session](https://developer.apple.com/documentation/AVFoundation/setting-up-a-capture-session)을 참고합니다.

[Frame Publisher 만들기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Create-a-Frame-Publisher)

-----------------------------------------------------------------------------------------------------------------------------------------------------

video capture는 `createVideoFramePublisher()` method에서 [`PassthroughSubject`](https://developer.apple.com/documentation/Combine/PassthroughSubject)를 생성해 capture session의 frame을 publish합니다.

    // frame을 subscriber에 publish하는 새 passthrough subject를 만듭니다.
    let passthroughSubject = PassthroughSubject<Frame, Never>()
    
    
    // Keep a reference to the publisher.
    framePublisher = passthroughSubject
    

passthrough subject는 [Combine](https://developer.apple.com/documentation/Combine)과 함께 imperative code를 동작하게 맞춰 주는 [`Subject`](https://developer.apple.com/documentation/Combine/Subject)의 구체 구현입니다. 해당 시점에 subscriber가 있으면 [`send(_:)`](https://developer.apple.com/documentation/Combine/Subject/send(_:)) method에 전달한 instance를 즉시 publish합니다.

다음으로 video capture는 output의 [`setSampleBufferDelegate(_:queue:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput/setSampleBufferDelegate(_:queue:)) method를 호출해 자신을 video output의 delegate로 등록하고, capture session에서 video frame을 받습니다.

    // Set the video capture as the video output's delegate.
    videoDataOutput.setSampleBufferDelegate(self, queue: videoCaptureQueue)
    

video capture는 받은 각 frame을 [`send(_:)`](https://developer.apple.com/documentation/Combine/Subject/send(_:)) method에 전달해 `framePublisher`로 전달합니다.

    extension VideoCapture: AVCaptureVideoDataOutputSampleBufferDelegate {
        func captureOutput(_ output: AVCaptureOutput,
                           didOutput frame: Frame,
                           from connection: AVCaptureConnection) {
    
    
            // Forward the frame through the publisher.
            framePublisher?.send(frame)
        }
    }
    

[Publisher Chain 구성하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Build-a-Publisher-Chain)

---------------------------------------------------------------------------------------------------------------------------------------------------

이 sample은 `VideoProcessingChain` class에서 연결된 일련의 [Combine](https://developer.apple.com/documentation/Combine) publisher로 각 video frame과 그 파생 data를 처리합니다.

video capture가 새 frame publisher를 만들 때마다 main view controller에 알리고, main view controller는 그 publisher를 video-processing chain의 `upstreamFramePublisher` property에 할당합니다.

    func videoCapture(_ videoCapture: VideoCapture,
                      didCreate framePublisher: FramePublisher) {
        updateUILabelsWithPrediction(.startingPrediction)
        
        // Build a new video-processing chain by assigning the new frame publisher.
        videoProcessingChain.upstreamFramePublisher = framePublisher
    }
    

property 값이 바뀔 때마다 video-processing chain은 `buildProcessingChain()` method를 호출해 새로운 publisher 데이지 체인을 만듭니다.

![video frame을 소비하고 main view controller에 정보를 생성하는 video-processing chain의 흐름도](https://docs-assets.developer.apple.com/published/ab0288b62b5f7bc9fbf9aeb4f4391de5/build-publisher-chain%402x.png)

이 method는 다음 [`Publisher`](https://developer.apple.com/documentation/Combine/Publisher) method 중 하나를 호출해 각각의 새 publisher를 만듭니다.

*   [`map(_:)`](https://developer.apple.com/documentation/Combine/Publisher/map(_:)-99evh)
    
*   [`compactMap(_:)`](https://developer.apple.com/documentation/Combine/Publisher/compactMap(_:))
    
*   [`scan(_:_:)`](https://developer.apple.com/documentation/Combine/Publisher/scan(_:_:))
    
*   [`filter(_:)`](https://developer.apple.com/documentation/Combine/Publisher/filter(_:))
    

예를 들어 최초 frame publisher를 구독하는 publisher는 [`Publishers.CompactMap`](https://developer.apple.com/documentation/Combine/Publishers/CompactMap)입니다. 이 publisher는 전달받은 각 `Frame`([`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer)의 type alias)을 video-processing chain의 `imageFromFrame(_:)` method를 호출해 [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage)로 변환합니다.

    // upstreamFramePublisher에서 받은 raw video frame을 변환하는
    // publisher-subscriber chain을 만듭니다.
    frameProcessingChain = upstreamFramePublisher
        // ---- Frame (aka CMSampleBuffer) -- Frame ----
    
    
        // Convert each frame to a CGImage, skipping any that don't convert.
        .compactMap(imageFromFrame)
    
    
        // ---- CGImage -- CGImage ----
    
        // frame에서 human body pose를 찾습니다. pose가 없는 경우도 처리합니다.
        .map(findPosesInFrame)
    
    
        // ---- [Pose]? -- [Pose]? ----
    

다음 섹션에서는 chain에 남아 있는 publisher와, 각 publisher가 input을 변환할 때 사용하는 method를 설명합니다.

[각 Frame에서 Body Pose 분석하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Analyze-Each-Frame-for-Body-Poses)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

chain의 다음 publisher는 [`Publishers.Map`](https://developer.apple.com/documentation/Combine/Publishers/Map)입니다. 이전 publisher(compact map)를 구독해 각 [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage)를 받고, video-processing chain의 `findPosesInFrame(_:)` method를 사용해 frame 안의 사람 body pose를 찾습니다. 이 method는 image로 [`VNImageRequestHandler`](https://developer.apple.com/documentation/Vision/VNImageRequestHandler)를 만든 뒤, handler의 [`perform(_:)`](https://developer.apple.com/documentation/Vision/VNImageRequestHandler/perform(_:)) method에 video-processing chain의 `humanBodyPoseRequest` property를 제출해 [`VNDetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/Vision/VNDetectHumanBodyPoseRequest)를 실행합니다.

    // image를 위한 request handler를 만듭니다.
    let visionRequestHandler = VNImageRequestHandler(cgImage: frame)
    
    
    // Vision을 사용해 frame 안의 human body pose를 찾습니다.
    do { try visionRequestHandler.perform([humanBodyPoseRequest]) } catch {
        assertionFailure("Human Pose Request failed: \(error)")
    }
    

request가 완료되면 method는 request의 [`results`](https://developer.apple.com/documentation/Vision/VNDetectHumanBodyPoseRequest/results) property에 있는 각 [`VNHumanBodyPoseObservation`](https://developer.apple.com/documentation/Vision/VNHumanBodyPoseObservation) instance마다 하나씩 포함하는 `Pose` array를 생성해 반환합니다.

    let poses = Pose.fromObservations(humanBodyPoseRequest.results)
    

이 sample의 `Pose` structure는 크게 세 가지 목적을 가집니다.

*   frame 안에서 observation의 area 계산("Isolate A Body Pose" 참고)
    
*   observation의 multiarray 저장("Retrieve the Multiarray" 참고)
    
*   observation을 점과 선으로 이루어진 wireframe으로 그리기("Present the Poses to the User" 참고)
    

[`VNDetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/Vision/VNDetectHumanBodyPoseRequest) 사용에 대한 자세한 내용은 [Detecting Human Body Poses in Images](https://developer.apple.com/documentation/Vision/detecting-human-body-poses-in-images)를 참고합니다.

[Body Pose 분리하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Isolate-a-Body-Pose)

-------------------------------------------------------------------------------------------------------------------------------------------

chain의 다음 publisher는 pose array에서 단일 pose를 고르는 map입니다. video-processing chain의 `isolateLargestPose(_:)` method를 사용하며, 이 method는 pose array의 [`max(by:)`](https://developer.apple.com/documentation/Swift/Array/max(by:)) method에 closure를 전달해 가장 두드러진 pose를 선택합니다.

    private func isolateLargestPose(_ poses: [Pose]?) -> Pose? {
        return poses?.max(by:) { pose1, pose2 in pose1.area < pose2.area }
    }
    

이 closure는 여러 사람이 frame 안에 있을 때 시간이 지나도 일관되게 같은 사람의 pose를 선택할 수 있도록 pose의 area 추정치를 비교합니다.

[Multiarray 가져오기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Retrieve-the-Multiarray)

---------------------------------------------------------------------------------------------------------------------------------------------------

chain의 다음 publisher는 pose의 `multiArray` property에서 [`MLMultiArray`](https://developer.apple.com/documentation/CoreML/MLMultiArray)를 publish하는 map입니다. video processing chain의 `multiArrayFromPose(_:)` method를 사용합니다.

    private func multiArrayFromPose(_ item: Pose?) -> MLMultiArray? {
        return item?.multiArray
    }
    

`Pose` initializer는 [`VNHumanBodyPoseObservation`](https://developer.apple.com/documentation/Vision/VNHumanBodyPoseObservation) parameter에서 observation의 [`keypointsMultiArray()`](https://developer.apple.com/documentation/Vision/VNRecognizedPointsObservation/keypointsMultiArray()) method를 호출해 multiarray를 복사합니다.

    // Save the multiarray from the observation.
    multiArray = try? observation.keypointsMultiArray()
    

[Multiarray Window 모으기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Gather-a-Window-of-Multiarrays)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

chain의 다음 publisher는 [`Publishers.Scan`](https://developer.apple.com/documentation/Combine/Publishers/Scan)입니다. upstream publisher에서 각 multiarray를 받아 두 개의 인자를 사용해 array로 모읍니다.

*   scan publisher의 초기값으로 사용할 빈 multiarray-optional array
    
*   scan publisher transform으로 사용할 video-processing chain의 `gatherWindow(previousWindow:multiArray:)` method
    

    // ---- MLMultiArray? -- MLMultiArray? ----
    
    
    // Gather a window of multiarrays, starting with an empty window.
    .scan([MLMultiArray?](), gatherWindow)
    
    
    // ---- [MLMultiArray?] -- [MLMultiArray?] ----
    

scan publisher는 map과 비슷하게 동작하지만 state도 유지합니다. 다음 scan publisher의 state는 처음에는 비어 있는 multiarray optional array입니다. scan publisher가 upstream publisher에서 multiarray optional을 받을 때마다, 이전 state와 새 multiarray optional을 transform의 인자로 전달합니다.

    private func gatherWindow(previousWindow: [MLMultiArray?],
                              multiArray: MLMultiArray?) -> [MLMultiArray?] {
        var currentWindow = previousWindow
    
    
        // If the previous window size is the target size, it
        // means sendWindowWhenReady() just published an array window.
        if previousWindow.count == predictionWindowSize {
            // Advance the sliding array window by stride elements.
            currentWindow.removeFirst(windowStride)
        }
    
    
        // Add the newest multiarray to the window.
        currentWindow.append(multiArray)
    
    
        // Publish the array window to the next subscriber.
        // currentWindow는 이 method가 upstream publisher에서 다음
        // multiarray를 받을 때 next previousWindow가 됩니다.
        return currentWindow
    }
    

이 method는 다음 작업을 수행합니다.

1.  `previousWindow` parameter를 `currentWindow`로 복사합니다.
    
2.  `currentWindow`가 가득 차 있으면 앞에서 `windowStride` element를 제거합니다.
    
3.  `multiArray` parameter를 `currentWindow` 끝에 추가합니다.
    
4.  `currentWindow`를 반환합니다. 이 값은 scan publisher의 새 state가 되며, 다음 값을 받을 때 `previousWindow`로 다시 전달됩니다.
    

video-processing chain은 window에 `predictionWindowSize` element가 있으면 가득 찬 것으로 간주합니다. window가 가득 차면 이 method는 2단계에서 가장 오래된 element를 제거해 새 element가 들어올 자리를 만들고, 결과적으로 window를 시간축을 따라 앞으로 이동시킵니다.

Exercise Classifier의 `calculatePredictionWindowSize()` method는 model의 [`modelDescription`](https://developer.apple.com/documentation/CoreML/MLModel/modelDescription) property를 확인해 runtime에 prediction window size 값을 결정합니다.

[Window Size 모니터링하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Monitor-the-Window-Size)

---------------------------------------------------------------------------------------------------------------------------------------------------

chain의 다음 publisher는 [`Publishers.Filter`](https://developer.apple.com/documentation/Combine/Publishers/Filter)이며, `gateWindow(_:)` method가 `true`를 반환할 때만 array window를 publish합니다.

    // Only publish a window when it grows to the correct size.
    .filter(gateWindow)
    
    
    // ---- [MLMultiArray?] -- [MLMultiArray?] ----
    

이 method는 window array에 `predictionWindowSize`로 정의한 정확한 개수의 element가 들어 있으면 `true`를 반환합니다. 그렇지 않으면 `false`를 반환하고, filter publisher는 현재 window를 버리고 publish하지 않습니다.

    private func gateWindow(_ currentWindow: [MLMultiArray?]) -> Bool {
        return currentWindow.count == predictionWindowSize
    }
    

이 filter publisher는 upstream scan publisher와 함께 동작해 `windowStride`가 정의한 frame 수마다 한 번씩 multiarray optional array를 publish합니다.

[사람의 Action 예측하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Predict-the-Persons-Action)

----------------------------------------------------------------------------------------------------------------------------------------------------------

chain의 다음 publisher는 multiarray window에서 `ActionPrediction`을 만듭니다. transform으로 `predictActionWithWindow(_:)` method를 사용합니다.

    // Make an activity prediction from the window.
    .map(predictActionWithWindow)
    
    
    // ---- ActionPrediction -- ActionPrediction ----
    

이 method의 input array에는 multiarray optional이 들어 있으며, 각 `nil` element는 [Vision](https://developer.apple.com/documentation/Vision)이 사람 body pose를 찾지 못한 frame을 의미합니다. action classifier는 모든 frame에 대해 유효한 non-`nil` multiarray가 필요합니다. array에서 `nil` element를 제거하기 위해 이 method는 다음 방식으로 `filledWindow`라는 새 multiarray를 만듭니다.

*   `currentWindow`의 유효한 각 element를 복사
    
*   `currentWindow`의 각 `nil` element를 `emptyPoseMultiArray`로 대체
    

    var poseCount = 0
    
    
    // Fill the nil elements with an empty pose array.
    let filledWindow: [MLMultiArray] = currentWindow.map { multiArray in
        if let multiArray = multiArray {
            poseCount += 1
            return multiArray
        } else {
            return Pose.emptyPoseMultiArray
        }
    }
    

empty pose multiarray는 다음 특성을 가집니다.

*   모든 element가 0으로 설정됨
    
*   사람 body-pose observation에서 나온 multiarray와 동일한 [`shape`](https://developer.apple.com/documentation/CoreML/MLMultiArray/shape) property 값을 가짐
    

이 method는 `currentWindow`의 각 element를 순회하면서 non-`nil` element 수를 `poseCount`에 누적합니다.

`poseCount` 값이 너무 낮으면 이 method는 곧바로 `noPersonPrediction` action prediction을 만듭니다.

    // Only use windows with at least 60% real data to make a prediction
    // with the action classifier.
    let minimum = predictionWindowSize * 60 / 100
    guard poseCount >= minimum else {
        return ActionPrediction.noPersonPrediction
    }
    

그렇지 않으면 이 method는 [`init(byConcatenatingMultiArrays:alongAxis:dataType:)`](https://developer.apple.com/documentation/CoreML/MLMultiArray/init(byConcatenatingMultiArrays:alongAxis:dataType:)) initializer를 호출해 multiarray array를 하나의 결합된 multiarray로 병합합니다.

    // Merge the array window of multiarrays into one multiarray.
    let mergedWindow = MLMultiArray(concatenating: filledWindow,
                                    axis: 0,
                                    dataType: .float)
    

이 method는 결합된 multiarray를 action classifier의 `predictActionFromWindow(_:)` helper method에 전달해 action prediction을 생성합니다.

    // Make a genuine prediction with the action classifier.
    let prediction = actionClassifier.predictActionFromWindow(mergedWindow)
    
    
    // Return the model's prediction if the confidence is high enough.
    // Otherwise, return a "Low Confidence" prediction.
    return checkConfidence(prediction)
    

이 method는 prediction을 `checkConfidence(_:)` helper method에 전달해 confidence를 검사합니다. confidence가 충분히 높으면 같은 prediction을 반환하고, 그렇지 않으면 `lowConfidencePrediction`을 반환합니다.

[사용자에게 Prediction 표시하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Present-the-Prediction-to-the-User)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

chain의 마지막 구성 요소는 `sendPrediction(_:)` method를 사용해 prediction을 video-processing chain의 delegate에 알리는 subscriber입니다.

    // Send the action prediction to the delegate.
    .sink(receiveValue: sendPrediction)
    

이 method는 action prediction과 그 prediction이 나타내는 frame 수(`windowStride`)를 video-processing chain의 `delegate`, 즉 main view controller에 전달합니다.

    // Send the prediction to the delegate on the main queue.
    DispatchQueue.main.async {
        self.delegate?.videoProcessingChain(self,
                                            didPredict: actionPrediction,
                                            for: windowStride)
    }
    

main view controller가 action prediction을 받을 때마다 helper method에서 prediction과 confidence로 app UI를 업데이트합니다.

    func videoProcessingChain(_ chain: VideoProcessingChain,
                              didPredict actionPrediction: ActionPrediction,
                              for frameCount: Int) {
    
    
        if actionPrediction.isModelLabel {
            // Update the total number of frames for this action.
            addFrameCount(frameCount, to: actionPrediction.label)
        }
    
    
        // Present the prediction in the UI.
        updateUILabelsWithPrediction(actionPrediction)
    }
    

main view controller는 model에서 온 action label에 대해 `actionFrameCounts` property도 업데이트하며, 사용자가 `Summary` button을 탭하면 나중에 이 값을 Summary View Controller로 전달합니다.

[사용자에게 Pose 표시하기](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed#Present-the-Poses-to-the-User)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

app은 [Vision](https://developer.apple.com/documentation/Vision)이 찾은 frame 위에 pose를 그려 각 human body-pose request의 결과를 시각화합니다. video-processing chain의 `findPosesInFrame(_:)`가 `Pose` instance array를 만들 때마다, 그 pose를 delegate인 main view controller로 보냅니다.

    // Send the frame and poses, if any, to the delegate on the main queue.
    DispatchQueue.main.async {
        self.delegate?.videoProcessingChain(self, didDetect: poses, in: frame)
    }
    

main view controller의 `drawPoses(_:onto:)` method는 먼저 frame을 그려 background로 사용합니다.

    // Draw the camera image first as the background.
    let imageRectangle = CGRect(origin: .zero, size: frameSize)
    cgContext.draw(frame, in: imageRectangle)
    

그다음 이 method는 각 pose의 `drawWireframeToContext(_:applying:)` method를 호출해 pose를 선과 원으로 이루어진 wireframe으로 그립니다.

    // Draw all the poses Vision found in the frame.
    for pose in poses {
        // Draw each pose as a wireframe at the scale of the image.
        pose.drawWireframeToContext(cgContext, applying: pointTransform)
    }
    

main view controller는 완성된 image를 full-screen image view에 할당해 사용자에게 표시합니다.

    // Update the UI's full-screen image view on the main thread.
    DispatchQueue.main.async { self.imageView.image = frameWithPosesRendering }
    

현재 페이지: live video feed에서 사람 action 감지하기
