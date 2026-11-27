# 지식베이스 CI 초안

`논문_지식베이스` 폴더에 그대로 겹쳐 넣는 구조입니다. 원본 파일은 하나도 바꾸지 않았습니다.

```
ci-draft/
├── .github/workflows/ci.yml   GitHub Actions: 검사 → 빌드 → 결과 확인 → 결과물 업로드
├── .gitignore                 빌드 결과물·개인 기록·실행 부산물 제외
└── scripts/
    ├── check_notes.py         papers/*.md 메타데이터·본문 4칸 + 퀴즈/비교표 JSON 검사
    └── verify_build.py        build.py가 만든 kb_data.json·index.html 확인
```

## 로컬에서 써 보기

```bash
cd ~/Documents/Heart-Lab/논문_지식베이스
python3 scripts/check_notes.py          # 오류 있으면 종료 코드 1
python3 scripts/check_notes.py --strict # 경고까지 실패 처리
python3 build.py && python3 scripts/verify_build.py
```

## check_notes.py가 잡는 것

**오류 (CI 실패)**
- 메타데이터 블록(`---`) 없음, 필수 키 10개 누락, 같은 키 두 번
- `id`가 파일 이름과 다름, 소문자·숫자·하이픈 외 문자, id 중복
- `year`가 따옴표 붙은 문자열이거나 1950~내년 범위 밖
- `category`가 허용 목록 밖 (오타 방지)
- `tags`/`predecessors`/`successors`가 올바른 JSON 목록이 아님 (build.py는 이 경우 조용히 문자열로 넘김)
- `predecessors`/`successors`가 없는 노트를 가리킴
- `## 한 줄 요약 / 핵심 메커니즘 / 기존 대비 차이 / 한계 & 연결` 중 빠졌거나 비었음
- 퀴즈: 필수 칸 누락, id 중복, 없는 논문 참조, `answer`가 보기 범위 밖
- 비교표: 없는 `paperId`, 행 칸 수와 열 수 불일치

**경고 (CI 통과, 로그에 표시)**
- pdf 경로 빈 칸 / 파일 없음 (PDF 확인은 옆에 `논문` 폴더가 있는 Mac에서만, CI에선 건너뜀)
- 선행·후속 연결이 한쪽에만 적힘
- 알 수 없는 키·섹션, 빈 tags, 글머리표 없는 핵심 메커니즘

## 현재 63편 결과

오류 0건, 경고 40건 (단방향 연결 35건, pdf 빈 칸 5건: dinov2, forcevla, openvla-oft, rope, stablevla).

## 추측한 부분 [추측]

| 위치 | 가정 | 바꾸려면 |
|---|---|---|
| `check_notes.py` ALLOWED_CATEGORIES | 지금 쓰는 10개 분야 + build.py의 빈 분야 2개만 허용 | 새 분야를 목록에 추가 |
| `check_notes.py` 연결 검사 | 선행/후속 양방향 기록이 원칙인지 몰라 경고로만 둠 | 원칙이면 `rep.warn` → `rep.error` |
| `check_notes.py` 퀴즈 type/scope | `single_mcq`, `compare` / `single`, `link`만 알려진 값 | 새 유형 추가 시 목록 갱신 |
| `ci.yml` 브랜치 | 기본 브랜치가 `main` | 저장소에 맞게 수정 |
| `ci.yml` Python 3.12 | Mac의 버전을 모름 (표준 라이브러리만 써서 영향 적음) | 원하는 버전으로 |
| `.gitignore` state.json | 개인 복습 기록이라 제외 | 기록도 버전 관리하려면 줄 삭제 |

## .gitignore로 빌드 결과물을 빼도 되는 이유

`server.py`는 시작할 때(613줄)와 `kb_data.json`·`index.html`이 없을 때(72, 356줄) `build()`를 호출합니다. 그래서 새로 받은 저장소에서도 서버를 켜면 바로 만들어집니다. CI는 빌드 결과를 `kb-site` 아티팩트로 14일간 보관합니다.

## 저장소에 붙이는 순서 (아직 하지 않음)

1. GitHub에 빈 저장소 만들기
2. 이 초안의 `.github/`, `.gitignore`, `scripts/`를 `논문_지식베이스/`에 복사
3. `git init && git add . && git commit` → push
4. Actions 탭에서 첫 실행 확인
