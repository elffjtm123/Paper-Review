---
id: bert
short: "BERT"
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2018
venue: "Devlin et al. (Google) / NAACL 2019"
category: "Transformer & LLM"
tags: ["Encoder-only", "Bidirectional", "MLM", "NSP"]
pdf: "논문/Transformer & LLM/BERT.pdf"
predecessors: ["transformer", "gpt-1"]
successors: ["vilbert", "diffusion-llm"]
---

## 한 줄 요약
입력 토큰 일부를 가리고 맞히는 Masked Language Modeling(MLM)으로 좌우 양방향 문맥을 동시에 사전학습한 Encoder-only Transformer.

## 핵심 메커니즘
- MLM: 입력 토큰의 15%를 마스킹(80% [MASK], 10% 랜덤, 10% 유지)해 양방향 문맥으로 원 토큰 복원.
- NSP(Next Sentence Prediction): 두 문장의 연속성 판별로 문장 쌍 추론(QA, NLI) 능력 학습.
- 토큰 + 세그먼트 + 학습형 위치 임베딩을 합산해 입력.

## 기존 대비 차이
단방향 문맥만 보던 GPT-1과 달리 모든 레이어에서 좌우 양방향 문맥을 깊게 결합해 이해(NLU) 벤치마크를 압도.

## 한계 & 연결
사전학습의 [MASK] 토큰이 미세조정 시엔 안 나오는 불일치가 있고, 자유 텍스트 자기회귀 생성에는 부적합.
