---
id: groot-n1
short: "GR00T N1"
title: "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots"
year: 2025
venue: "NVIDIA / arXiv 2025"
category: "VLA"
tags: ["Humanoid", "Dual-System", "DiT", "Flow Matching", "Synthetic Data"]
pdf: "논문/VLA/GR00T-N1.pdf"
predecessors: ["pi-0", "dit", "flow-matching"]
successors: ["smolvla"]
---

## 한 줄 요약
VLM(System 2: 느린 추론) + Diffusion Transformer(System 1: 빠른 운동 제어) 이중 시스템 구조의 오픈 휴머노이드 범용 VLA 파운데이션 모델.

## 핵심 메커니즘
- System 2(Eagle-2 VLM)가 시각·언어를 해석해 잠재 표현을 만들고, System 1(DiT + Flow Matching)이 실시간 연속 모터 행동 생성.
- 실제 로봇 데이터 + 시뮬레이션 합성 궤적 + 인간 영상(잠재 액션 추출)으로 구성된 데이터 피라미드 학습.
- Embodiment별 전용 상태/행동 인코더·디코더를 둬 다양한 휴머노이드·양팔 로봇에 적응.

## 기존 대비 차이
π0와 유사한 VLM+Flow 구조이지만, 휴머노이드 전신·양팔 제어와 인간 비디오·신경망 합성 데이터 피라미드 결합에 특화된 오픈 모델.

## 한계 & 연결
실제 환경 물리 접촉·시각 교란 강건성과 소규모 랩 환경에서의 고속 파인튜닝 비용은 여전히 과제.
