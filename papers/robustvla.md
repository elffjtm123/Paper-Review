---
id: robustvla
short: "RobustVLA"
title: "RobustVLA: On Robustness of Vision-Language-Action Model Against Multi-Modal Perturbations"
year: 2026
venue: "ICLR 2026 (arXiv:2510.00037)"
category: "Dataset & Robustness"
tags: ["Multi-Modal Perturbation", "Visual+Language", "Robustness", "ICLR 2026"]
pdf: "논문/Dataset/RobustVLA.pdf"
predecessors: ["openvla", "pi-0", "libero-pro"]
successors: ["stablevla"]
---

## 한 줄 요약
시각 교란뿐 아니라 언어 지시 변형·센서 결함 등 멀티모달 교란 전반에 대한 VLA 강건성을 체계적으로 평가·개선한 ICLR 2026 연구.

## 핵심 메커니즘
- 시각(노이즈·블러·조명·가림) + 언어(패러프레이즈·오타·지시 모호성) + 상태 교란을 복합 평가.
- 기존 VLA의 시각-언어 정렬이 작은 교란에도 쉽게 깨져 잘못된 물체로 오작동하는 메커니즘 분석.
- 강건성 향상을 위한 정규화·데이터/특징 정렬 방어 전략 검증.

## 기존 대비 차이
단일 시각 노이즈에 국한하지 않고 시각·언어 멀티모달 동시 교란의 상호작용까지 본격적으로 다룸.

## 한계 & 연결
시뮬레이션(LIBERO) 중심 평가이며 실제 카메라 ISP 노이즈나 산업 현장 물리 결함과의 괴리는 추가 검증 필요.
