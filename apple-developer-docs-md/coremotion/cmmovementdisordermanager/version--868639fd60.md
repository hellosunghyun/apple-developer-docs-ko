---
title: "version() | Apple Developer Documentation"
source_url: "https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version()"
section: "Core Motion"
scraped_at: "2026-05-11T03:53:39.894099+00:00"
---

[탐색 건너뛰기](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version()#app-main)

*   [Core Motion](https://developer.apple.com/documentation/coremotion)
    
*   [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)
    
*   version()

type method

version()
=========

movement disorder algorithm의 현재 version을 설명하는 string을 반환합니다.

watchOS 5.0+

    class func version() -> String?

[언급된 문서](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version()#mentions)

------------------------------------------------------------------------------------------------------------------

[Movement disorder algorithm 변경 로그](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

[설명](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version()#Discussion)

------------------------------------------------------------------------------------------------------------------

이 method를 사용해 movement disorder manager가 사용하는 algorithm을 확인합니다. 현재 device가 movement disorder data 수집을 지원하면 이 method는 `<major>.<minor>.<fix>` 형식의 version number string을 반환합니다. [`isAvailable()`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable())
가 [`false`](https://developer.apple.com/documentation/Swift/false)
를 반환하는 경우에는 항상 `nil`을 반환합니다. 현재 version 정보는 [movement disorder algorithm 변경 내역](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)
를 참고합니다.

version이 바뀔 때 알려 주는 test를 설정하려면 현재 version을 예상값과 비교하는 unit test를 만듭니다. 그런 다음 continuous integration을 사용해 새 release마다 이 값을 자동으로 모니터링할 수 있습니다.

    func testForVersionChange() throws {
        let expectedVersion = "1.0.0"
        let currentVersion = CMMovementDisorderManager.version()
        XCTAssertEqual(expectedVersion, currentVersion, "*** The version has changes to \(String(describing: currentVersion)). ***")
    }
    

[참고 항목](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version()#see-also)

--------------------------------------------------------------------------------------------------------------

### [availability 확인](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/version()#Checking-Availablility)

[`class func isAvailable() -> Bool`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable())

현재 device가 movement disorder manager를 지원하는지를 나타내는 Boolean 값입니다.

[`class func authorizationStatus() -> CMAuthorizationStatus`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus())

사용자가 app이 movement disorder data를 모니터링하고 query하도록 허용했는지를 나타내는 값입니다.

현재 페이지는 version()입니다
