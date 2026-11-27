---
id: maia-cria
short: "MAIA (CRIA)"
title: "MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models"
year: 2026
venue: "arXiv:2610.21686 (2026)"
category: "Dataset & Robustness"
tags: ["Anomaly Anticipation", "Contact-Rich", "World Model", "Force-Torque", "CRIA"]
pdf: "논문/Dataset/CIRA(MAIA).pdf"
predecessors: ["surp", "forcevla"]
successors: []
---

## 한 줄 요약
접촉 조작에서 이상(걸림·미끄러짐·과부하)이 발생한 뒤 감지하는 대신, 멀티모달 월드 모델로 행동 실행 전에 이상을 선제 예측·회피하는 프레임워크 및 CRIA 데이터.

## 핵심 메커니즘
- 시각 관측과 계획된 행동으로부터 미래 물리 상호작용(힘/접촉 결과)을 예측하는 Vision-Action 월드 모델.
- 후보 행동들의 이상 위험도를 사전 평가해 가장 저위험 행동을 온라인 선택(Anomaly-aware action selection).
- 서랍·플러그·지퍼·보드 닦기 등 접촉 조작의 정상/이상 시계열과 F/T 신호 분석.

## 기존 대비 차이
기존 이상 탐지가 사고 발생 후 사후(reactive) 경보에 그쳤다면, MAIA는 실행 전 선제(anticipatory) 예측으로 충돌·실패를 예방.

## 한계 & 연결
Heart-Lab Isaac Sim 재현 및 후속 검증에서 힘 분포·이상 지속성·도메인 전이 특성 분석 진행.
