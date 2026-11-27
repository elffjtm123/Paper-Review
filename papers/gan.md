---
id: gan
short: "GAN"
title: "Generative Adversarial Nets"
year: 2014
venue: "Goodfellow et al. / NeurIPS 2014"
category: "Generative"
tags: ["Adversarial", "Minimax Game", "Generator", "Discriminator"]
pdf: "논문/Generative Model/GAN.pdf"
predecessors: ["vae"]
successors: ["cgan", "dcgan"]
---

## 한 줄 요약
가짜를 만드는 생성자(G)와 진짜/가짜를 가리는 판별자(D)의 미니맥스 적대적 게임으로 선명한 샘플을 생성하는 패러다임.

## 핵심 메커니즘
- G는 노이즈 z에서 실제와 구분 안 되는 샘플을 생성하려 하고, D는 진짜 x와 G(z)를 분류(Min-Max 목적함수).
- 이론적 최적점에서 데이터 분포와 생성 분포 사이의 Jensen-Shannon Divergence를 최소화.
- 명시적 확률밀도(likelihood) 계산 없이 한 번의 순전파로 고품질 샘플 생성.

## 기존 대비 차이
VAE의 흐릿한 복원 손실 대신 학습된 판별자 D를 손실함수로 써서 훨씬 날카롭고 사실적인 이미지를 생성.

## 한계 & 연결
학습 불안정, Mode Collapse(다양성 붕괴), 기울기 소실, 제어 불가능성 → **CGAN**, **DCGAN**, 이후 **DDPM**으로 진화.
