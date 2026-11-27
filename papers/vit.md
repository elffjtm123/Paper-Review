---
id: vit
short: "ViT"
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
year: 2020
venue: "Dosovitskiy et al. (Google) / ICLR 2021"
category: "Vision"
tags: ["Patch Embedding", "Vision Transformer", "Scaling", "CLS Token"]
pdf: "논문/Vision/ViT.pdf"
predecessors: ["transformer", "resnet"]
successors: ["clip", "dino", "dinov2", "siglip", "dit", "palm-e"]
---

## 한 줄 요약
이미지를 16×16 패치 시퀀스로 잘라 선형 투영한 뒤 순수 Transformer 인코더에 그대로 입력해, 대규모 데이터에서 CNN을 능가하는 비전 표준 백본을 확립.

## 핵심 메커니즘
- 이미지를 고정 크기 패치(예: 16×16)로 분할·평탄화해 단어 토큰처럼 취급 + 학습형 1D 위치 임베딩 + [CLS] 토큰.
- CNN 특유의 지역성·평행이동 등변성 귀납 편향(inductive bias)을 거의 넣지 않은 순수 Transformer 구조.
- 소규모 데이터(ImageNet-1K)에선 ResNet보다 약하지만, JFT-300M급 대규모 사전학습 시 CNN을 역전.

## 기존 대비 차이
비전과 언어의 아키텍처 장벽을 허물어 CLIP·SigLIP·DINO·PaLM-E·DiT 등 멀티모달·생성·VLA 통합의 직접적 토대가 됨.

## 한계 & 연결
소량 데이터에서 과적합하기 쉽고, 고해상도 이미지에서는 패치 수 N 증가로 O(N²) 어텐션 비용이 급증.
