---
title: "Getting motion-activity data from headphones | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.885563+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   Getting motion-activity data from headphones

sample 코드

Getting motion-activity data from headphones
============================================

app이 headphones의 motion-activity 변화를 수신하도록 구성합니다.

[Download](https://docs-assets.developer.apple.com/published/dc6ec1e7e547/GettingMotionActivityDataFromHeadphones.zip)

iOS 18.0+iPadOS 18.0+Mac Catalyst 18.0+Xcode 16.1+

[개요](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones#Overview)

-----------------------------------------------------------------------------------------------------------------------

이 sample app은 현재 motion type이 바뀔 때 `CMHeadphoneActivityManager`를 사용해 update를 요청하는 방법을 보여줍니다. 변화가 발생하면 app은 update 정보를 [`CMMotionActivity`](https://developer.apple.com/documentation/CoreMotion/CMMotionActivity)
 object로 받아 motion 변화의 text 설명을 표시합니다.

### [sample code project 구성](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones#Configure-the-sample-code-project)

이 sample app은 headphone motion update를 사용하므로 Simulator가 아니라 device에서 실행해야 합니다. 이 sample을 실행하려면 다음이 필요합니다.

*   iOS 18 이상이 설치된 iOS device
    
*   AirPods Pro 2 또는 AirPods 4처럼 motion update를 지원하는 headphones
    

[같이 보기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones#see-also)

-----------------------------------------------------------------------------------------------------------------------

### [Activity](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones#Activity)

[`class CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

device에 저장된 motion data에 대한 접근을 관리하는 object입니다.

[`class CMHeadphoneActivityManager`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)

headphone activity service를 시작하고 관리하는 object입니다.

[`class CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

단일 motion update event의 data입니다.

현재 페이지는 Getting motion-activity data from headphones입니다
