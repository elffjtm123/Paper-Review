---
id: llama
short: "LLaMA"
title: "LLaMA: Open and Efficient Foundation Language Models"
year: 2023
venue: "Meta AI / arXiv 2023"
category: "Transformer & LLM"
tags: ["Open Weights", "RMSNorm", "SwiGLU", "RoPE", "Chinchilla Over-training"]
pdf: "논문/Transformer & LLM/LLaMA.pdf"
predecessors: ["gpt-1", "palm", "rope", "layernorm"]
successors: ["openvla", "lora", "qlora", "pagedattention"]
---

## 한 줄 요약
공개 데이터만으로 7B~65B 모델을 Chinchilla 기준보다 훨씬 많은 토큰(1~1.4T)으로 학습해, 13B로 GPT-3 175B를 능가한 오픈소스 LLM 생태계의 기점.

## 핵심 메커니즘
- 추론 비용 최소화를 위해 작은 모델을 더 긴 토큰으로 '과다 학습(over-training)'하는 전략 채택.
- 현대 LLM 표준 레시피 정착: Pre-RMSNorm + SwiGLU FFN + RoPE 위치 임베딩.
- 단일 GPU에서 실행 가능한 7B/13B 가중치 공개로 LoRA·QLoRA·OpenVLA 등 후속 연구 폭발.

## 기존 대비 차이
거대 모델 크기 경쟁(GPT-3 175B, PaLM 540B)에서 '작은 모델 × 대량 고품질 토큰 학습'의 추론 효율 중심 패러다임으로 전환.

## 한계 & 연결
초기 LLaMA 1은 비상업적 연구 라이선스·2k 컨텍스트 제한 → 이후 LLaMA 2/3 및 OpenVLA 백본(Llama 2 7B)으로 계승.
