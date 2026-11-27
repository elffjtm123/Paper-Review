---
id: vae
short: "VAE"
title: "Auto-Encoding Variational Bayes"
year: 2013
venue: "Kingma & Welling / ICLR 2014"
category: "Generative"
tags: ["Latent Variable", "ELBO", "Reparameterization", "KL Divergence"]
pdf: "논문/Generative Model/VAE.pdf"
predecessors: ["autoencoder"]
successors: ["gan", "ddpm", "act"]
---

## 한 줄 요약
잠재 변수를 확률 분포로 모델링하고 ELBO 최적화 + Reparameterization Trick으로 역전파 가능한 생성 모델을 연 변분 오토인코더.

## 핵심 메커니즘
- 인코더가 점 z가 아닌 정규분포 파라미터(μ, σ)를 출력해 잠재 공간을 매끄럽고 연속적으로 형성.
- Reparameterization Trick(z = μ + σ ⊙ ε, ε ~ N(0,I))으로 샘플링 연산을 미분 가능하게 변환.
- 손실함수 = 복원 손실(Likelihood) + 사전분포 N(0,I)와의 KL Divergence 정규화(ELBO 최대화).

## 기존 대비 차이
AutoEncoder의 불연속 잠재 공간을 확률적 구조로 정규화해, 잠재 공간 보간과 신규 샘플 생성이 가능해짐.

## 한계 & 연결
픽셀 단위 가우시안 복원 가정과 KL 제약의 절충으로 생성 이미지가 다소 흐릿(blurry)해지는 경향 → **GAN**, **DDPM**으로 보완.
