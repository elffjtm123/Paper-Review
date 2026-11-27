---
id: dit
short: "DiT"
title: "Scalable Diffusion Models with Transformers"
year: 2022
venue: "Peebles & Xie / ICCV 2023"
category: "Generative"
tags: ["Diffusion Transformer", "adaLN-Zero", "Scaling", "ViT"]
pdf: "논문/Generative Model/DiT.pdf"
predecessors: ["ddpm", "vit", "layernorm"]
successors: ["groot-n1"]
---

## 한 줄 요약
확산 모델의 U-Net 백본을 ViT(Transformer)로 대체하고 adaLN-Zero 조건화를 도입해, 연산량(GFlops) 확장에 따라 생성 품질이 일관되게 좋아지는 스케일링 법칙 입증.

## 핵심 메커니즘
- 잠재 공간(VAE latent)을 패치 토큰화해 순수 Transformer 블록으로 디노이징 수행.
- 시간 t와 클래스 조건 c를 LayerNorm의 scale/shift + 잔차 게이트(초기값 0)로 주입하는 **adaLN-Zero**가 가장 우수.
- U-Net의 귀납 편향이 필수가 아님을 보이며 모델 크기·패치 크기 축소에 따른 뚜렷한 FID 스케일링 달성.

## 기존 대비 차이
DDPM 이후 당연시되던 U-Net 백본을 표준 Transformer로 교체해 Sora·Flux·GR00T N1(System 1 DiT) 등 현대 생성·로봇 백본의 표준을 확립.

## 한계 & 연결
고해상도/긴 시퀀스에서는 Self-Attention 연산량이 제곱으로 증가해 잠재 공간 압축(VAE)이나 효율 어텐션에 의존.
