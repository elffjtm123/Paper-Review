---
id: palm
short: "PaLM"
title: "PaLM: Scaling Language Modeling with Pathways"
year: 2022
venue: "Google / JMLR 2023"
category: "Transformer & LLM"
tags: ["540B LLM", "Pathways", "SwiGLU", "Multi-Query Attention", "Parallel Block"]
pdf: "논문/Transformer & LLM/PaLM.pdf"
predecessors: ["gpt-1", "rope"]
successors: ["palm-e", "llama"]
---

## 한 줄 요약
Pathways 시스템으로 540B 밀집(dense) Transformer를 6,144 TPU에서 학습해 스케일링에 따른 창발적 추론(Chain-of-Thought)과 효율 아키텍처 개선을 입증한 LLM.

## 핵심 메커니즘
- Parallel Transformer Block(Attention과 FFN을 직렬이 아닌 병렬 계산)으로 대규모 학습 속도 약 15% 가속.
- SwiGLU 활성화 + RoPE + Multi-Query Attention(Key/Value 헤드 공유로 디코딩 메모리 대역폭 절감) 채택.
- 540B 규모에서 Few-shot + Chain-of-Thought 프롬프팅의 불연속적 성능 도약 확인.

## 기존 대비 차이
단순 크기 확장뿐 아니라 병렬 블록·MQA·SwiGLU·RoPE 등 후속 현대 LLM(LLaMA 등)의 핵심 아키텍처 조합을 대규모로 검증.

## 한계 & 연결
540B 모델은 학습·서빙 비용이 막대하며 비공개 → 소형·고효율 오픈 웨이트 **LLaMA**와 체화 확장 **PaLM-E**로 이어짐.
