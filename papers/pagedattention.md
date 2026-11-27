---
id: pagedattention
short: "PagedAttention (vLLM)"
title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
year: 2023
venue: "Kwon et al. (UC Berkeley) / SOSP 2023"
category: "Optimization"
tags: ["LLM Serving", "KV Cache", "Virtual Memory", "vLLM", "Throughput"]
pdf: "논문/Optimization/PagedAttention.pdf"
predecessors: ["transformer", "flashattention", "llama"]
successors: []
---

## 한 줄 요약
OS의 가상 메모리·페이징 개념을 LLM 서빙의 KV-Cache에 도입해 메모리 단편화를 거의 0%로 줄이고 서빙 처리량을 2~4배 끌어올린 vLLM 핵심 기술.

## 핵심 메커니즘
- 연속된 거대 메모리 블록을 미리 예약하는 대신, KV-Cache를 고정 크기 블록(페이지)으로 쪼개 비연속 물리 메모리에 동적 할당.
- 논리 블록→물리 블록 매핑 테이블을 둬 요청별 출력 길이를 몰라도 내부/외부 단편화 낭비를 4% 미만으로 축소.
- 동일 프롬프트·빔서치·병렬 샘플링 간 물리 KV 블록 공유(Copy-on-Write)로 메모리 추가 절약.

## 기존 대비 차이
학습/단일 어텐션 커널을 가속한 FlashAttention과 직교하여, 다중 사용자 실시간 LLM 서빙의 최대 병목인 KV-Cache 메모리 낭비를 해결.

## 한계 & 연결
비연속 블록 조회 커널 구현이 필요하며, 초단문·소배치 환경보다는 긴 컨텍스트·고동시성 서빙에서 효과가 극대화됨.
