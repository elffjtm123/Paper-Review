---
id: autoencoder
short: "AutoEncoder"
title: "Reducing the Dimensionality of Data with Neural Networks"
year: 2006
venue: "Hinton & Salakhutdinov / Science 2006"
category: "Generative"
tags: ["Representation", "Bottleneck", "Reconstruction", "Encoder-Decoder"]
pdf: "논문/Generative Model/Autoencoders.pdf"
predecessors: []
successors: ["vae", "u-net"]
---

## 한 줄 요약
입력을 저차원 병목(latent code)으로 압축했다가 다시 복원(reconstruction)하도록 학습해 비선형 데이터 표현을 추출하는 신경망의 원형.

## 핵심 메커니즘
- Encoder가 고차원 입력 x를 저차원 잠재벡터 z로 압축하고, Decoder가 z에서 원본 x̂를 복원(MSE/BCE 손실).
- 병목 차원 제약으로 데이터의 핵심 구조만 남기도록 강제(비선형 PCA 역할).
- 사전학습(RBM 등)으로 심층 인코더-디코더 최적화 난제 돌파.

## 기존 대비 차이
선형 변환에 국한된 PCA와 달리 다층 비선형 변환으로 복잡한 매니폴드 구조를 훨씬 효율적으로 압축.

## 한계 & 연결
잠재 공간이 연속·정규화되어 있지 않아 임의의 z를 샘플링해 새 데이터를 생성하기 어려움 → **VAE**로 발전.
