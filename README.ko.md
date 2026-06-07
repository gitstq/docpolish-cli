# 🎉 DocPolish-CLI

🦞 Lightweight Markdown Document Intelligent Beautification Engine | 轻量级Markdown文档智能美化引擎

## ✨ 핵심 기능

- ✨ Smart Markdown formatting
- ✨ Document structure analysis
- ✨ AI content polishing
- ✨ Multi-language README generation
- ✨ Zero-dependency core
- 🚀 **제로 의존성** - 순수 Python 구현, 추가 의존성 불필요
- 🎨 **스마트 포맷팅** - Markdown 형식 문제 자동 수정
- 🤖 **AI 강화** - GLM-5.1 통합으로 콘텐츠 다듬기 및 번역
- 🌍 **다국어 지원** - 원클릭 다국어 README 생성
- 📊 **문서 분석** - 문서 구조 및 품질 심층 분석

## 🚀 빠른 시작

### 요구사항

- Python 3.8+
- pip

### 설치

```bash
pip install docpolish
```

### 기본 사용법

```bash
# Markdown 문서 포맷팅
docpolish format README.md

# 문서 구조 분석
docpolish analyze document.md

# AI 콘텐츠 다듬기
docpolish polish README.md --style professional

# 다국어 README 생성
docpolish readme --project-name "MyProject" --lang ko,en
```

## 📖 상세 사용 가이드

### 포맷 명령

```bash
# 포맷하고 원본 파일 덮어쓰기
docpolish format README.md

# 새 파일에 출력
docpolish format README.md -o README_formatted.md

# 확인만 하고 수정하지 않음
docpolish format README.md --check

# 변경 사항 차이 표시
docpolish format README.md --diff
```

### 분석 명령

```bash
# 텍스트 형식 분석
docpolish analyze document.md

# JSON 형식 출력
docpolish analyze document.md --json
```

### AI 다듬기

```bash
# 전문가 스타일 다듬기
docpolish polish README.md --style professional

# 간단한 스타일 다듬기
docpolish polish README.md --style simple

# API 키 지정
docpolish polish README.md --api-key YOUR_API_KEY
```

### 번역 기능

```bash
# 한국어로 번역
docpolish translate README.md --target ko

# 영어로 번역
docpolish translate README.md --target en
```

## 💡 설계 철학 및 로드맵

### 설계 철학

DocPolish는 개발자가 Markdown 문서를 작성하고 유지 관리할 때 직면하는 형식 불일치, 레이아웃 혼란, 다국어 유지 관리의 어려움을 해결하기 위해 설계되었습니다. 지능형 형식 수정 및 AI 강화 기능을 통해 문서 작성이 효율적이 됩니다.

### 기술 선택

- **순수 Python 구현**: 제로 의존성 코어로 크로스 플랫폼 호환성 보장
- **정규 표현식 엔진**: 효율적인 텍스트 구문 분석 및 포맷팅
- **GLM-5.1 통합**: 강력한 중국어 이해 및 생성 기능
- **모듈화 아키텍처**: 확장 및 유지 관리가 용이

### 로드맵

- [ ] v1.1.0 - 더 많은 Markdown 확장 구문 지원 (GFM, CommonMark)
- [ ] v1.2.0 - 실시간 미리보기 기능 추가
- [ ] v1.3.0 - 사용자 정의 포맷팅 규칙 지원
- [ ] v2.0.0 - Web UI 인터페이스

## 📦 패키징 및 배포 가이드

### 소스에서 설치

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### 릴리스 패키지 빌드

```bash
python -m build
```

### 로컬 패키지 설치

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 기여 가이드

Issue와 Pull Request를 환영합니다!

### 커밋 규약

- `feat:` 새 기능
- `fix:` 버그 수정
- `docs:` 문서 업데이트
- `refactor:` 코드 리팩토링

### 개발 워크플로우

1. 이 저장소를 Fork
2. 기능 브랜치 생성 (`git checkout -b feat/amazing-feature`)
3. 변경사항 커밋 (`git commit -m 'feat: add amazing feature'`)
4. 브랜치 푸시 (`git push origin feat/amazing-feature`)
5. Pull Request 생성

## 📄 라이선스

이 프로젝트는 [MIT](LICENSE) 라이선스 하에 공개되어 있습니다.

---

<p align="center">Made with ❤️ by Lobster AI</p>
