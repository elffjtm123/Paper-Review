---
id: layernorm
short: "LayerNorm"
title: "Layer Normalization"
year: 2016
venue: "Ba, Kiros & Hinton / arXiv 2016"
category: "Optimization"
tags: ["Normalization", "Batch-Independent", "Transformer", "RNN"]
pdf: "논문/Optimization/Layer Normalization.pdf"
predecessors: ["batchnorm", "lstm"]
successors: ["transformer", "dit", "llama"]
---

## 한 줄 요약
배치 축이 아닌 단일 샘플 내부의 특징(feature) 차원 전체에 대해 평균·분산을 정규화해, 배치 크기와 시퀀스 길이에 무관하게 동작하는 정규화 기법.

## 핵심 메커니즘
- 각 토큰/샘플마다 독립적으로 feature 축의 평균과 분산을 계산해 정규화 + 학습 파라미터 (γ, β).
- 학습과 추론 시 동작이 완전히 동일(running statistics 불필요)하며 배치 크기 1에서도 안정적.
- 이후 Transformer의 표준이 되었고, 평균 제거를 생략한 RMSNorm(LLaMA) 및 조건부 adaLN-Zero(DiT)로 진화.

## 기존 대비 차이
BatchNorm이 배치 통계에 의존해 시퀀스·소배치 학습에서 깨지던 문제를 샘플 독립 정규화로 완벽히 해소.

## 한계 & 연결
2D 이미지 CNN에서는 공간/채널별 통계 특성을 살리는 BatchNorm/GroupNorm보다 성능이 다소 떨어질 수 있음.
