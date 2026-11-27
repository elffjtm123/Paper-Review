---
id: dcgan
short: "DCGAN"
title: "Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks"
year: 2015
venue: "Radford et al. / ICLR 2016"
category: "Generative"
tags: ["CNN", "BatchNorm", "Transposed Conv", "Stable GAN"]
pdf: "논문/Generative Model/DCGAN.pdf"
predecessors: ["gan", "cgan", "batchnorm"]
successors: ["ddpm"]
---

## 한 줄 요약
CNN + BatchNorm + Strided/Transposed Conv 설계 가이드라인으로 심층 합성곱 GAN 학습을 안정화하고 잠재 공간 벡터 연산을 보인 기념비적 모델.

## 핵심 메커니즘
- Pooling 제거 → 판별자는 Strided Conv, 생성자는 Fractional-strided(Transposed) Conv로 업샘플링.
- FC 레이어 제거, 생성자·판별자에 BatchNorm 적용, 활성화는 G(ReLU/Tanh)·D(LeakyReLU) 조합.
- 잠재 공간 z에서 의미 벡터 산술(안경 낀 남자 - 남자 + 여자 = 안경 낀 여자) 실증.

## 기존 대비 차이
MLP 기반의 불안정하던 초기 GAN을 이미지 도메인에서 안정적으로 학습되는 Deep CNN 아키텍처 표준으로 정립.

## 한계 & 연결
여전히 고해상도 생성·모드 붕괴 한계가 있고, 생성 과정의 정확한 확률밀도(likelihood) 평가가 불가능.
