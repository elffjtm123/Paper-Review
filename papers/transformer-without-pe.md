---
id: transformer-without-pe
short: "NoPE"
title: "Transformer Language Models without Positional Encodings Still Learn Positional Information"
year: 2022
venue: "Haviv et al. / EMNLP 2022 Findings"
category: "Transformer & LLM"
tags: ["NoPE", "Causal Mask", "Implicit Position", "Length Generalization"]
pdf: "논문/Transformer & LLM/Transformer without PE.pdf"
predecessors: ["transformer", "rope"]
successors: []
---

## 한 줄 요약
명시적 위치 인코딩(PE)을 아예 없앤 Causal Transformer도 표준 모델과 동등한 성능을 내며, Causal Attention 마스크 자체로 암묵적 절대 위치를 학습함을 입증.

## 핵심 메커니즘
- PE 없이 학습한 Decoder-only LM의 내부 표현을 프로빙한 결과, 토큰의 절대 위치 정보를 높은 정확도로 복원 가능.
- 원인 가설: Causal Attention에서는 위치 i의 토큰이 정확히 i+1개 이전 토큰만 참조하므로 어텐션 분산/합 구조를 통해 순서를 추론.
- 모델 크기·데이터셋·시퀀스 길이에 걸쳐 일관되게 관찰.

## 기존 대비 차이
Transformer에 위치 인코딩이 절대 필수라는 통념을 깨고, Causal Mask 자체가 강력한 순서 귀납 편향임을 규명.

## 한계 & 연결
초장문 컨텍스트 외삽이나 정밀한 상대 거리 참조에서는 여전히 RoPE 계열 대비 한계가 보고됨.
