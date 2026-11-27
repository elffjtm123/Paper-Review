---
id: batchnorm
short: "BatchNorm"
title: "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift"
year: 2015
venue: "Ioffe & Szegedy / ICML 2015"
category: "Optimization"
tags: ["Normalization", "CNN", "Training Stability", "Scale/Shift"]
pdf: "논문/Optimization/BatchNormalization.pdf"
predecessors: ["inception"]
successors: ["resnet", "dcgan", "layernorm"]
---

## 한 줄 요약
미니배치 단위로 채널별 활성화를 평균 0·분산 1로 정규화하고 학습 파라미터(γ, β)로 복원력을 부여해 깊은 CNN 학습을 비약적으로 안정화·가속.

## 핵심 메커니즘
- 학습 시 미니배치 통계(μ_B, σ_B²)로 정규화 후 학습 가능한 scale γ, shift β 적용(표현력 보존).
- 추론 시에는 학습 중 누적한 이동평균(running mean/var)을 사용해 배치 독립적 출력 보장.
- 더 큰 학습률 허용, 초기값 민감도 감소, 미세한 정규화(regularization) 효과 제공.

## 기존 대비 차이
깊은 신경망에서 활성화 분포 흔들림과 기울기 소실로 학습이 막히던 문제를 간단한 정규화 레이어로 해결해 ResNet·DCGAN의 필수 부품이 됨.

## 한계 & 연결
작은 배치 크기나 가변 길이 시퀀스(RNN/Transformer)에서 통계가 불안정 → **LayerNorm**으로 해결.
