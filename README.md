# Korean Apple Developer Documentation Mirror

Core Motion, SensorKit, Create ML 문서를 한국어 Markdown으로 크롤링한 뒤 정적 HTML 문서 사이트로 빌드한 비공식 아카이브입니다.

## Local Preview

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_docs_site.py
python3 -m http.server 8000 --directory site
```

브라우저에서 `http://localhost:8000`을 열면 됩니다.

## Link Behavior

- 크롤링된 `developer.apple.com/documentation/coremotion`, `sensorkit`, `createml` 하위 문서 링크는 `site/docs/...` 내부 HTML 문서로 이동합니다.
- 크롤링하지 않은 Apple Developer Documentation URL과 asset/download URL은 원본 웹 URL로 이동합니다.
- GitHub Pages project site에서도 깨지지 않도록 내부 링크와 asset 링크는 상대 경로로 생성됩니다.

## GitHub Pages

`.github/workflows/deploy-pages.yml`이 `site/`를 Pages artifact로 업로드합니다.

1. GitHub repo Settings에서 Pages source를 `GitHub Actions`로 설정합니다.
2. `main` 또는 `master` branch에 push합니다.
3. Actions의 `Deploy GitHub Pages` workflow가 `scripts/build_docs_site.py`를 실행하고 `site/`를 배포합니다.

## Rebuild

Markdown을 수정하거나 새로 크롤링한 문서를 반영하려면 다음 명령만 다시 실행하면 됩니다.

```bash
python3 scripts/build_docs_site.py
```
