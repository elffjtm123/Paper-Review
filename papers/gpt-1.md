---
id: gpt-1
short: "GPT-1"
title: "Improving Language Understanding by Generative Pre-Training"
year: 2018
venue: "Radford et al. (OpenAI) / 2018"
category: "Transformer & LLM"
tags: ["Decoder-only", "Pre-training", "Next-Token Prediction", "Fine-tuning"]
pdf: "논문/Transformer & LLM/GPT-1.pdf"
predecessors: ["transformer"]
successors: ["bert", "palm", "llama"]
---

## 한 줄 요약
대규모 비라벨 텍스트에서 Decoder-only Transformer를 다음 토큰 예측으로 비지도 사전학습한 뒤, 소량 라벨 태스크에 미세조정하는 현대 LLM 패러다임의 출발점.

## 핵심 메커니즘
- 12층 Causal Decoder-only Transformer로 왼쪽→오른쪽 언어 모델링(Next-Token Prediction) 사전학습.
- 다운스트림 태스크(분류·추론·QA)의 입력을 특수 토큰 구분 시퀀스로 통일해 아키텍처 변경을 최소화하고 미세조정.
- 미세조정 시 언어모델 보조 손실을 함께 써서 일반화와 수렴 속도 개선.

## 기존 대비 차이
태스크별 전용 모델을 처음부터 학습하던 NLP 관행을 '범용 생성 사전학습 + 태스크 미세조정' 2단계로 전환.

## 한계 & 연결
단방향(왼쪽→오른쪽) 문맥만 보므로 양방향 이해 과제에선 한계 → **BERT**가 양방향 인코더로 보완, 이후 스케일링으로 **PaLM/LLaMA** 발전.
