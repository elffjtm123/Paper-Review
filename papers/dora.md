---
id: dora
short: "DoRA"
title: "DoRA: Weight-Decomposed Low-Rank Adaptation"
year: 2024
venue: "Liu et al. (NVIDIA / HKUST) / ICML 2024 (Oral)"
category: "Optimization"
tags: ["PEFT", "Magnitude-Direction", "LoRA Improvement", "Zero Overhead"]
pdf: "논문/Optimization/DoRA.pdf"
predecessors: ["lora", "qlora"]
successors: []
---

## 한 줄 요약
사전학습 가중치를 크기(Magnitude)와 방향(Direction)으로 분해해 방향 업데이트에만 LoRA를 적용함으로써, 추론 비용 추가 없이 Full FT에 가까운 학습 패턴을 구현.

## 핵심 메커니즘
- 가중치 분해 분석 결과: Full FT는 크기와 방향 변화가 미세한 음의 상관을 보이지만, LoRA는 강하게 비례(양의 상관)해 표현력이 제한됨.
- W' = m · (W₀ + ΔV) / ||W₀ + ΔV||_c : 스칼라 크기 벡터 m은 직접 학습하고 방향 변화 ΔV = BA만 저랭크로 학습.
- 추론 시 단일 가중치 행렬로 병합 가능해 LoRA와 동일하게 추가 추론 지연 0.

## 기존 대비 차이
LoRA·QLoRA보다 아주 적은 추가 파라미터(m 벡터)만으로 낮은 랭크에서도 일관되게 성능을 높여 Full FT와의 간극을 좁힘.

## 한계 & 연결
학습 시 열별 노름 계산 때문에 순수 LoRA 대비 학습 메모리/속도 오버헤드가 약간 발생(그래디언트 분리 트릭으로 완화).
