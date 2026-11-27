---
id: transformer
short: "Transformer"
title: "Attention Is All You Need"
year: 2017
venue: "Vaswani et al. (Google) / NeurIPS 2017"
category: "Transformer & LLM"
tags: ["Self-Attention", "Multi-Head", "Positional Encoding", "Parallelism"]
pdf: "논문/Transformer & LLM/Transformer.pdf"
predecessors: ["lstm", "bi-lstm", "gru", "layernorm", "resnet"]
successors: ["gpt-1", "bert", "vit", "rope", "flashattention", "rt-1"]
---

## 한 줄 요약
순환(RNN)·합성곱을 완전히 제거하고 Scaled Dot-Product Multi-Head Self-Attention만으로 시퀀스 병렬 학습과 장거리 의존성을 해결한 현대 AI 기반 구조.

## 핵심 메커니즘
- Attention(Q,K,V) = softmax(QK^T / √d_k) V 로 시퀀스 내 임의 두 토큰 간 경로 길이를 O(1)로 단축.
- Multi-Head Attention으로 서로 다른 표현 부분공간을 병렬 참조 + FFN + Residual + LayerNorm.
- 순서 정보가 없으므로 사인/코사인 Positional Encoding을 입력 임베딩에 가산.

## 기존 대비 차이
LSTM/GRU의 순차 계산 병목(병렬화 불가)과 장거리 정보 소실을 동시에 해결해 대규모 사전학습(LLM/VLM/VLA)의 문을 염.

## 한계 & 연결
시퀀스 길이 N에 대해 Attention 메모리·연산이 O(N²) → **FlashAttention**, **PagedAttention**, **RoPE** 등으로 보완.
