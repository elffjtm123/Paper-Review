---
id: flashattention
short: "FlashAttention"
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
year: 2022
venue: "Dao et al. (Stanford) / NeurIPS 2022"
category: "Optimization"
tags: ["IO-Aware", "Tiling", "Online Softmax", "Exact Attention", "GPU SRAM"]
pdf: "논문/Optimization/FlashAttention.pdf"
predecessors: ["transformer"]
successors: ["pagedattention", "llama"]
---

## 한 줄 요약
GPU의 느린 HBM과 빠른 온칩 SRAM 계층을 고려해 Tiling + Online Softmax + Recomputation으로 근사 없이 정확(Exact) Attention의 메모리 O(N)과 고속화를 달성.

## 핵심 메커니즘
- 거대한 N×N 어텐션 행렬을 HBM에 쓰지 않고, Q·K·V를 작은 블록(tile)으로 나눠 SRAM 안에서 바로 Softmax·V 곱까지 퓨전 연산.
- Online Softmax(블록별 최댓값·분모 보정 통계만 유지)로 전체 행을 한 번에 보지 않고도 정확한 Softmax 계산.
- 역전파 시 N×N 행렬을 저장하는 대신 통계량만으로 SRAM에서 재계산(recomputation)해 HBM 접근 횟수를 획기적으로 축소.

## 기존 대비 차이
품질을 희생하던 근사 어텐션(Linear/Sparse)과 달리 수학적으로 100% 동일한 Exact Attention을 유지하면서 2~4배 가속 + 선형 메모리 O(N) 달성.

## 한계 & 연결
추론 시 길어지는 KV-Cache의 메모리 단편화 관리 문제는 별개 영역 → 서빙 엔진의 **PagedAttention**이 보완.
