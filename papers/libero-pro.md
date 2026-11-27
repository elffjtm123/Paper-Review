---
id: libero-pro
short: "LIBERO-PRO"
title: "LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization"
year: 2025
venue: "HUST / Tsinghua / arXiv:2510.03827"
category: "Dataset & Robustness"
tags: ["Benchmark", "Memorization", "Fair Evaluation", "VLA"]
pdf: "논문/Dataset/LIBERO-PRO.pdf"
predecessors: ["openvla", "pi-0"]
successors: ["robustvla"]
---

## 한 줄 요약
기존 LIBERO의 높은 점수가 '일반화'가 아니라 초기 배치·궤적 '암기(memorization)' 때문임을 폭로하고, 4축 교란(물체·배치·언어·환경) 공정 평가 체계를 제안.

## 핵심 메커니즘
- 초기 물체 위치·배경·지시문·목표 물체를 변형했을 때 SOTA VLA가 0%대에 가깝게 무너지는 암기 현상 입증.
- 학습 데이터 암기를 차단하고 진정한 시각·언어 grounding 능력을 측정하는 공정 프로토콜 정의.
- 의미 없는 지시문에도 원래 궤적을 그대로 재생하는 '언어 무시' 결함 진단.

## 기존 대비 차이
LIBERO-Plus가 7축 종합 강건성 스펙트럼을 본다면, LIBERO-PRO는 특히 '암기 vs 진짜 이해' 판별과 공정 비교에 초점을 맞춤.

## 한계 & 연결
Heart-Lab에서 π0·π0.5 42,500회 평가로 RobustVLA 및 LIBERO-Plus와 직접 교차 비교 완료.
