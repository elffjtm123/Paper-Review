---
id: real-nvp
short: "Real NVP"
title: "Density Estimation using Real NVP"
year: 2016
venue: "Dinh et al. / ICLR 2017"
category: "Generative"
tags: ["Normalizing Flow", "Affine Coupling", "Exact Likelihood", "Invertible"]
pdf: "논문/Generative Model/RealNVP.pdf"
predecessors: ["vae"]
successors: ["flow-matching"]
---

## 한 줄 요약
Affine Coupling Layer로 역변환과 야코비안 행렬식을 빠르게 계산해 정확한 확률밀도(Exact Likelihood) 추정과 생성을 동시에 수행하는 Normalizing Flow.

## 핵심 메커니즘
- 입력 채널/공간을 절반으로 나눠 한쪽(x1)은 그대로 두고, x1으로 계산한 scale(s)·translation(t)으로 나머지(x2)를 아핀 변환.
- 야코비안이 삼각행렬이 되어 행렬식이 대각 원소 합(exp(∑s))으로 O(D)에 계산되며, s·t 신경망 자체가 가역일 필요 없음.
- 체커보드·채널 마스킹을 교차 적층하고 멀티스케일 구조로 표현력 확보.

## 기존 대비 차이
근사 우도(VAE)나 우도 없음(GAN)과 달리, 변수 변환 공식으로 정확한 로그 우도를 직접 최대화하면서 양방향 1:1 매핑을 유지.

## 한계 & 연결
가역성 제약 때문에 모델 차원 유지가 필요해 표현력·메모리 효율이 떨어짐 → 연속 시간 ODE 기반 **Flow Matching**으로 진화.
