---
id: ddpm
short: "DDPM"
title: "Denoising Diffusion Probabilistic Models"
year: 2020
venue: "Ho et al. / NeurIPS 2020"
category: "Generative"
tags: ["Diffusion", "Noise Prediction", "U-Net", "Score Matching"]
pdf: "논문/Generative Model/DDPM.pdf"
predecessors: ["vae", "u-net"]
successors: ["dit", "flow-matching", "octo", "diffusion-llm"]
---

## 한 줄 요약
데이터에 점진적으로 가우시안 노이즈를 더하는 Forward 과정과, U-Net으로 주입된 노이즈 ε을 예측해 되돌리는 단순 MSE 손실로 확산 모델 시대를 연 논문.

## 핵심 메커니즘
- Forward 과정은 임의 시점 t의 노이즈 이미지를 닫힌 식 x_t = √ᾱ_t x_0 + √(1-ᾱ_t) ε 로 한 번에 샘플링.
- 복잡한 변분 하한(ELBO)을 '네트워크가 노이즈 ε 자체를 예측하는 단순 L2 손실 L_simple'로 단순화해 품질 급상승.
- Time embedding이 주입된 U-Net 백본으로 T=1000 스텝 순차 디노이징 수행.

## 기존 대비 차이
GAN의 학습 불안정성·모드 붕괴 없이 안정적으로 초고품질·고다양성 이미지를 생성하며 생성모델의 주도권을 확산으로 이동.

## 한계 & 연결
1,000스텝 반복 샘플링으로 추론 속도가 매우 느리고 U-Net 백본의 스케일링 한계 → **DiT**(백본) 및 **Flow Matching**(직선 궤적·고속 샘플링)으로 발전.
