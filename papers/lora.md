---
id: lora
short: "LoRA"
title: "LoRA: Low-Rank Adaptation of Large Language Models"
year: 2021
venue: "Hu et al. (Microsoft) / ICLR 2022"
category: "Optimization"
tags: ["PEFT", "Low-Rank", "Zero Inference Latency", "Fine-Tuning"]
pdf: "논문/Optimization/LoRA.pdf"
predecessors: ["transformer", "gpt-1"]
successors: ["qlora", "dora", "openvla"]
---

## 한 줄 요약
사전학습 가중치 W₀는 동결하고, 가중치 변화량 ΔW를 저랭크 행렬 곱 B·A(r ≪ d)로만 학습해 메모리 절감과 추론 지연 0을 동시에 달성한 PEFT 표준.

## 핵심 메커니즘
- h = W₀x + (α/r)BAx : A는 가우시안 초기화, B는 0으로 초기화해 학습 시작 시 원 모델 출력과 정확히 일치.
- 추론 시 W = W₀ + (α/r)BA 로 원본 가중치에 병합(merge)할 수 있어 추가 추론 지연(latency)이 전혀 없음.
- 태스크별 수 MB 크기 어댑터만 교체해 단일 베이스 모델로 다중 작업 서빙 가능.

## 기존 대비 차이
추론 지연을 유발하던 기존 Adapter나 시퀀스 길이를 깎아먹던 Prefix-Tuning의 단점을 저랭크 병합 구조로 깔끔히 극복.

## 한계 & 연결
베이스 모델 자체가 FP16이면 여전히 VRAM 부담이 크고(**QLoRA**), Full FT 대비 가중치 크기·방향 동시 갱신 표현력 격차 존재(**DoRA**).
