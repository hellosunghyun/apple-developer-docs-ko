---
title: "isValid | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid"
section: "Create ML"
scraped_at: "2026-05-11T03:53:40.140343+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid#app-main)

*   [Create ML](https://developer.apple.com/documentation/createml)
    
*   [MLRegressorMetrics](https://developer.apple.com/documentation/createml/mlregressormetrics)
    
*   isValid

instance property

isValid
=======

regressor model이 metric을 계산할 수 있었는지를 나타내는 Boolean 값입니다.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 10.14+tvOS 16.0+visionOS 1.0+

    var isValid: Bool { get }

[논의](https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid#discussion)

-------------------------------------------------------------------------------------------------------

training example의 구조와 맞지 않는 data로 evaluation을 수행하려고 하면 metric이 invalid할 수 있습니다.

[참고 항목](https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid#see-also)

---------------------------------------------------------------------------------------------------

### [error 처리](https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid#Handling-errors)

[`var error: (any Error)?`](https://developer.apple.com/documentation/createml/mlregressormetrics/error)

metric이 invalid할 때 존재하는 underlying error입니다.

현재 페이지는 isValid입니다
