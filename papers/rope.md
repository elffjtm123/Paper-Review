---
id: rope
short: "RoPE"
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
year: 2021
venue: "Su et al. / Neurocomputing 2024 (arXiv:2104.09864)"
category: "Transformer & LLM"
tags: ["Positional Encoding", "Relative Position", "Rotation Matrix", "LLM Standard"]
pdf: "논문/Transformer & LLM/RoFormer.pdf"
predecessors: ["transformer"]
successors: ["palm", "llama", "transformer-without-pe"]
---

## 한 줄 요약
Query와 Key 벡터를 위치 m에 비례한 각도로 2D 평면 회전시켜, 내적(QK^T)이 자동으로 상대 거리 (m-n)에만 의존하게 만든 현대 LLM 표준 위치 임베딩.

## 핵심 메커니즘
- 임베딩에 위치 벡터를 더하는 대신, 각 어텐션 헤드의 Q·K 쌍을 위치별 회전 행렬 R_m으로 곱해 회전.
- 회전 행렬의 직교성 덕분에 (R_m q)^T (R_n k) = q^T R_{n-m} k 로 절대 위치 변환만으로 상대 위치 정보를 정확히 표현.
- 거리가 멀어질수록 내적 상한이 자연스럽게 감쇠하고, 선형 어텐션·길이 외삽(NTK/YaRN)과 호환.

## 기존 대비 차이
절대 PE의 길이 일반화 한계와 기존 상대 PE의 어텐션 바이어스 오버헤드를 동시에 해결해 LLaMA·PaLM·Qwen 등의 사실상 표준이 됨.

## 한계 & 연결
학습 컨텍스트 길이를 크게 초과할 때는 주파수 스케일링(PI/YaRN) 없이는 외삽 성능이 급락.
