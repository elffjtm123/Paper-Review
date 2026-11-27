---
id: wall-oss
short: "WALL-OSS"
title: "WALL-OSS: Igniting VLMs toward the Embodied Space"
year: 2025
venue: "X Square Robot / arXiv 2025"
category: "VLA"
tags: ["Embodied Foundation", "Unified CoT", "Action-Vision Alignment", "VLA"]
pdf: "논문/VLA/WALL-OSS.pdf"
predecessors: ["pi-0-5", "openvla", "fast"]
successors: []
---

## 한 줄 요약
일반 VLM을 체화 공간으로 정렬하기 위해 공간·행동 이해 사전학습과 통합 Chain-of-Thought(언어→행동)를 결합한 오픈소스 Embodied Foundation Model.

## 핵심 메커니즘
- 일반 VLM과 로봇 도메인 간 모달리티·분포·목적함수 불일치를 줄이는 대규모 체화 멀티모달 사전학습(Inspiration 단계).
- 이산 액션 토큰 학습으로 언어-행동 정렬을 먼저 맞춘 뒤 Flow Matching 기반 연속 액션 생성(Integration 단계)으로 연결.
- 단일 모델 내에서 공간 추론·서브태스크 계획·저수준 행동을 통합 Chain-of-Thought로 연계.

## 기존 대비 차이
기존 VLA가 VLM 위에 액션 헤드만 얹어 공간 이해와 행동 생성이 괴리되던 문제를, 체화 정렬 사전학습 + 통합 CoT 파이프라인으로 해소 시도.

## 한계 & 연결
현재 읽는 중 — 실제 벤치마크/시각 교란 강건성 및 Heart-Lab 실험 모델(π0.5/OpenVLA-OFT)과의 세부 비교 정리 예정.
