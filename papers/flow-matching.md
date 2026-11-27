---
id: flow-matching
short: "Flow Matching"
title: "Flow Matching for Generative Modeling"
year: 2022
venue: "Lipman et al. (Meta) / ICLR 2023"
category: "Generative"
tags: ["CNF", "Vector Field", "Optimal Transport", "Straight Paths", "Fast Sampling"]
pdf: "논문/Generative Model/FlowMatching.pdf"
predecessors: ["real-nvp", "ddpm"]
successors: ["pi-0", "pi-0-5", "groot-n1", "smolvla"]
---

## 한 줄 요약
노이즈에서 데이터로 가는 연속 확률 경로의 속도장(vector field)을 시뮬레이션 없이 직접 회귀 학습해, 직선(OT) 궤적과 극소 스텝 고속 샘플링을 구현한 프레임워크.

## 핵심 메커니즘
- Continuous Normalizing Flow(CNF)의 난점이던 ODE 시뮬레이션 학습을 Conditional Flow Matching(CFM) 회귀 손실로 대체.
- Optimal Transport(OT) 직선 보간 경로 x_t = (1-t)x_0 + t x_1 의 목표 속도 u_t = x_1 - x_0 를 직접 예측.
- 확산(Diffusion) 경로를 특수 경우로 포함하면서 더 곧은 궤적 덕분에 5~10스텝 ODE 적분만으로 고품질 생성.

## 기존 대비 차이
Real NVP의 아키텍처 가역성 제약을 없애고, DDPM의 구불구불한 확률 경로·느린 샘플링을 직선 속도장 학습으로 혁신.

## 한계 & 연결
단일 스텝 생성은 아직 증류(distillation)가 필요하나, 10스텝 고속 연속 생성 특성 덕분에 **π0·GR00T·SmolVLA**의 핵심 액션 헤드가 됨.
