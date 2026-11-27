---
id: resnet
short: "ResNet"
title: "Deep Residual Learning for Image Recognition"
year: 2015
venue: "He et al. (Microsoft) / CVPR 2016"
category: "Vision"
tags: ["Skip Connection", "Residual", "Degradation Problem", "Deep CNN"]
pdf: "논문/Vision/ResNet.pdf"
predecessors: ["inception", "batchnorm"]
successors: ["transformer", "clip"]
---

## 한 줄 요약
목표 함수 H(x) 대신 잔차 F(x) = H(x) - x 를 학습하는 항등 지름길 연결(y = F(x) + x)로, 망이 깊어질수록 오히려 학습 오차가 커지는 퇴화 문제를 해결.

## 핵심 메커니즘
- Shortcut(Identity Skip) 연결로 역전파 시 기울기가 소실 없이 앞층까지 직접 흐르는 고속도로 제공.
- 불필요한 층은 F(x)→0(항등 사상)으로 쉽게 수렴할 수 있어 152층 이상 초심층 학습 가능.
- 1×1 → 3×3 → 1×1 Bottleneck 블록으로 깊은 망의 연산량 억제.

## 기존 대비 차이
BatchNorm으로도 못 풀었던 초심층 망의 최적화 퇴화(degradation) 문제를 파라미터 추가 없는 덧셈 연결 하나로 근본 해결 → Transformer 포함 모든 현대 심층망의 필수 요소.

## 한계 & 연결
합성곱 기반 지역 편향이 강해 초거대 데이터 스케일링에서는 전역 어텐션 기반 **ViT**에 주도권을 넘겨줌.
