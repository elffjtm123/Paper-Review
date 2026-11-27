---
id: act
short: "ACT (ALOHA)"
title: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware"
year: 2023
venue: "Stanford / Berkeley / RSS 2023"
category: "Robot Control"
tags: ["Action Chunking", "CVAE", "Temporal Ensemble", "Bimanual", "ALOHA"]
pdf: "논문/robot sim/ACT.pdf"
predecessors: ["vae", "transformer"]
successors: ["openvla-oft", "pi-0"]
---

## 한 줄 요약
저가 양팔 원격조작 시스템(ALOHA)과 Action Chunking + CVAE + Temporal Ensembling으로 누적 오차를 줄여 정밀 양팔 조작을 학습한 핵심 모방학습 알고리즘.

## 핵심 메커니즘
- Action Chunking: 1스텝씩 예측하지 않고 k스텝 행동 묶음을 한 번에 예측해 유효 horizon을 1/k로 단축(누적 오차 억제).
- CVAE(Conditional VAE)로 인간 시연의 다봉성(같은 상태에서 여러 경로)을 잠재변수 z로 흡수.
- Temporal Ensembling: 매 스텝 겹치는 청크 예측들을 지수 가중 평균해 부드럽고 정확한 궤적 실행.

## 기존 대비 차이
단순 스텝별 행동 복제(BC)가 미세 오차 누적으로 정밀 작업(케이블 타이, 배터리 삽입)에서 실패하던 문제를 Action Chunking으로 깔끔히 해결.

## 한계 & 연결
단일 태스크 모방학습이라 언어 지시·다중 작업 일반화가 없음 → Action Chunking 아이디어가 OpenVLA-OFT·π0의 핵심 부품으로 계승.
