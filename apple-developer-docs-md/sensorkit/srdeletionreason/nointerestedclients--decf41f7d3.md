---
title: "SRDeletionReason.noInterestedClients | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients"
section: "SensorKit"
scraped_at: "2026-05-11T03:53:40.048084+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients#app-main)

*   [SensorKit](https://developer.apple.com/documentation/sensorkit)
    
*   [SRDeletionReason](https://developer.apple.com/documentation/sensorkit/srdeletionreason)
    
*   SRDeletionReason.noInterestedClients

Case

SRDeletionReason.noInterestedClients
====================================

sensor에 활성 stakeholder가 없음을 나타냅니다.

iOS 14.0+iPadOS 14.0+Mac Catalyst 14.0+

    case noInterestedClients

[논의](https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients#Discussion)

------------------------------------------------------------------------------------------------------------------

특정 sensor에서 recording activity가 없을 때 framework는 이 reason으로 sample을 삭제합니다.

[같이 보기](https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients#see-also)

--------------------------------------------------------------------------------------------------------------

### [Reasons](https://developer.apple.com/documentation/sensorkit/srdeletionreason/nointerestedclients#Reasons)

[`case ageLimit`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/agelimit)

sample이 framework의 보존 한도를 초과했음을 나타냅니다.

[`case lowDiskSpace`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/lowdiskspace)

system의 disk space가 부족함을 나타냅니다.

[`case systemInitiated`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/systeminitiated)

system이 deletion을 요청함을 나타냅니다.

[`case userInitiated`](https://developer.apple.com/documentation/sensorkit/srdeletionreason/userinitiated)

user가 deletion을 요청함을 나타냅니다.

현재 페이지: SRDeletionReason.noInterestedClients
