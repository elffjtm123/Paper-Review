---
id: wall-oss
short: "WALL-OSS"
title: "WALL-OSS: Igniting VLMs toward the Embodied Space"
year: 2025
venue: "X Square Robot / arXiv 2509.11766 (2025)"
category: "VLA"
tags: ["Embodied Foundation", "Uni-CoT", "Tightly-coupled MoE", "FAST → Flow Matching", "Embodied VQA"]
pdf: "논문/VLA/WALL-OSS.pdf"
predecessors: ["pi-0", "pi-0-5", "fast", "openvla"]
successors: []
---

## 한 줄 요약
Qwen2.5-VL-3B에 정적 라우팅 MoE(VL FFN / Action FFN)를 붙이고 "체화 VQA + FAST 이산 액션(Inspiration) → Flow Matching 연속 액션(Integration)" 커리큘럼으로 학습해, 지시→추론(CoT)→서브태스크→연속 행동을 한 모델에서 잇는(Uni-CoT) 오픈소스 체화 파운데이션 모델.

## 핵심 메커니즘
- 문제 정의(3가지 간극): ① 모달리티·데이터 규모(액션은 3D·시간 연속이고 텍스트 정렬 데이터가 적음), ② 사전학습 분포(1인칭·어안·자기가림 영상은 웹 이미지와 다름 → VLM이 체화 VQA·공간 추론에 약함), ③ 학습 목적(VLM은 이산 next-token, 액션은 연속 → Diffusion/Flow를 그대로 붙이면 VL 사전지식 붕괴).
- 아키텍처(Fig.2c): RT-2·OpenVLA식 "통합형"(VLM이 액션까지 출력 → 가중치 드리프트로 지시 이해 저하)과 π0식 "분리형"(별도 Action Expert → 언어가 보조 신호로 밀려 지시 결합 약함)의 중간. Self-Attention은 공유하고 FFN만 VL FFN / Action FFN으로 나눔. 라우터는 학습형 top-k가 아닌 정적 라우팅(토큰 종류로 고정 배정).
- Inspiration 단계: 원래 VLM FFN을 재사용해 체화 VQA(공간·진행도·계획)와 FAST(DCT→양자화→BPE) 이산 액션 토큰을 next-token으로 함께 학습(L = λ_VQA·텍스트 NLL + λ_D·FAST 토큰 NLL). "대략적인 행동 감각"을 VLM 출력 공간에 심는 단계.
- Integration 단계: 이산 예측을 Flow Matching 연속 액션으로 교체. Phase 1은 VLM을 얼리고 Action FFN 아래 Flow Head만 학습(속도장 v가 ε − x₀를 회귀), Phase 2는 VLM까지 풀어 공동 최적화.
- Uni-CoT(광의의 CoT): 지시 → 추론(CoT) → 서브태스크 → 연속 행동을 하나의 미분 가능한 모델로 학습. path-drop 목적함수로 중간 단계를 거치거나 건너뛰는(x→a 직행) 경로를 모두 학습해, 추론 시 과제 난이도에 따라 CoT 사용 여부를 스스로 정하고 추론과 실행을 끼워 넣을 수 있음.
- 데이터: 1만 시간 이상. 자체 수집 로봇 데이터(57.5%) + 오픈소스 액션(33.1%, DROID·BC-Z·Bridge·AgiBot 등, 단위·좌표·DoF 템플릿·제어 주기 통일) + 멀티모달 VQA(9.4%, 일반 VQA로 VLM 능력 유지 + 자체 궤적에서 자동 생성한 체화 VQA). 파인튜닝 때도 액션:VQA를 섞어 학습(비-서브태스크 VQA 1:15, 서브태스크 1:100).
- 결과: 체화 VQA에서 베이스 Qwen2.5-VL-3B 대비 Object Grounding 46.1→91.6%, Captioning 57.7→87.6%, Action Planning 59.8→69.0%. 제로샷 지시 pick-place 진행도 85%(본 물체) / 61%(새 물체). Set-Table·Tidy-Bedroom 장기 과제와 Block-Spell·Place-by-Color(글자 "red" 읽고 놓기) 추론 과제에서 π0·Diffusion Policy(평면 지시 및 GPT-4 서브태스크 버전)를 크게 앞섬. 서브태스크·CoT 라벨은 학습 프레임의 1%만으로 충분. Block-Spell 글자 블록 선택 정확도 87%(co-training) vs 26%(WALL-OSS 액션만) vs 9%(π0).

## 기존 대비 차이
π0/π0.5와 같은 "VLM + Flow Matching" 계열이지만, π0가 Action Expert를 느슨하게 붙여 언어를 보조 신호로 쓰는 반면 WALL-OSS는 Attention을 공유한 MoE와 "이산 정렬 먼저, 연속 생성 나중" 커리큘럼으로 언어-행동 결합을 강하게 만듦. π0.5의 FAST co-training + 서브태스크 추론 흐름을 이어받되, 체화 VQA로 VLM의 공간 이해 자체를 끌어올리고 CoT까지 포함한 Uni-CoT를 단일 모델로 학습한다는 점이 핵심. GR00T N1·Hi Robot 같은 계획기/제어기 분리(이중 시스템)는 인터페이스가 미분 불가하고 오차가 누적된다고 보고 이를 하나로 합침. 차이가 가장 크게 드러나는 곳은 정밀 제어보다 지시 이해·추론·장기 과제.

## 한계 & 연결
- 저자 스스로 "정밀 조작은 여전히 π0가 우세"라고 인정. 강점은 추론·지시 이해 쪽이고, Collect-Waste·Pick-Place-Cup 같은 순수 액션 정확도는 π0와 비슷한 수준.
- 평가가 모두 자체 설계 실제 로봇 과제(제3자 블라인드 평가)이고 LIBERO·SimplerEnv 같은 공개 벤치마크 수치가 없어 다른 VLA와 직접 비교가 어려움. Fig.7은 막대그래프뿐이라 과제별 정확한 수치를 읽기 어렵고, 비교 대상도 π0·DP뿐(π0.5·OpenVLA-OFT 없음).
- 시각 교란(블러·조명·가림) 강건성은 학습 때 약한 도메인 랜덤화만 언급되고 따로 측정하지 않음. Heart-Lab의 LIBERO-Plus/StableVLA 축 실험(π0.5 블러 98.2→89.9% 하락)과 같은 방식으로 재보면 의미 있는 비교가 될 것.
- 연결: FAST(이산 토큰), π0(Flow Matching), π0.5(FAST 사전학습 + 서브태스크 추론)의 직접 후속 설계. 오픈소스 코드·체크포인트(github.com/X-Square-Robot/wall-x)가 있어 재현 실험 후보. 체화 CoT 관점에서 ReAct, Gemini Robotics 1.5(ER + VLA)와 비교해 읽기 좋음.
