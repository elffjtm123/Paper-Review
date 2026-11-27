---
id: stablevla
short: "StableVLA"
title: "StableVLA: Towards Robust Vision-Language-Action Models without Extra Data"
year: 2026
venue: "ICML 2026 (arXiv:2605.18287)"
category: "VLA"
tags: ["Visual Robustness", "Information Bottleneck", "ImageNet-C", "VLA"]
pdf: "논문/VLA/StableVLA.pdf"
predecessors: ["openvla-oft", "libero-plus", "robustvla"]
successors: []
---

## 한 줄 요약
경량 VLA-Adapter(0.5B)에 Fused Information Bottleneck(IB) Adapter를 결합해 ImageNet-C 강도 3~5 시각 교란에서도 높은 성공률을 유지하는 강건 VLA.

## 핵심 메커니즘
- Fused IB-Adapter로 시각 특징에서 태스크와 무관한 노이즈·교란 정보를 압축·차단하고 핵심 상태 정보만 통과.
- 0.5B급 경량 VLA-Adapter 백본 위에서 동작해 연산 부담을 억제하면서 시각 결함 방어.
- LIBERO 4개 스위트 × ImageNet-C 18~19종 × Severity 3~5 대규모 프로토콜에서 클린 성능 유지 + 교란 강건성 대폭 향상.

## 기존 대비 차이
단순 데이터 증강만으로 교란에 대응하던 기존 접근과 달리, 정보 병목(IB) 어댑터 구조로 미지 시각 손상에도 일관된 안정성을 확보.

## 한계 & 연결
현재 Heart-Lab에서 111,500회 공식 프로토콜 완전 재현 진행 중(S5 Long은 45.3%로 고강도·장거리 교란에선 여전히 하락폭 존재).
