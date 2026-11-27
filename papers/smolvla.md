---
id: smolvla
short: "SmolVLA"
title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
year: 2025
venue: "Hugging Face / arXiv 2025"
category: "VLA"
tags: ["Lightweight VLA", "450M", "Async Inference", "Flow Matching", "LeRobot"]
pdf: "논문/VLA/SmolVLA.pdf"
predecessors: ["pi-0", "groot-n1"]
successors: []
---

## 한 줄 요약
커뮤니티 오픈 데이터만으로 학습하고 단일 소비자 GPU·CPU에서도 돌아가는 초경량(450M) Flow Matching VLA + 비동기 추론 스택.

## 핵심 메커니즘
- 경량 VLM(SmolVLM-2)의 앞쪽 레이어 절반만 사용하고 시각 토큰 수를 축소해 연산량 대폭 절감.
- Action Expert에 Self-Attention과 VLM Cross-Attention을 교차 배치(interleaved)해 450M 크기로 Flow Matching 제어.
- 비동기 추론(Asynchronous Inference)으로 액션 청크 실행 중 다음 청크를 미리 계산해 제어 지연 은폐.

## 기존 대비 차이
수십억 파라미터·사내 비공개 데이터에 의존하는 π0/GR00T와 달리, LeRobot 커뮤니티 공개 데이터와 저가 로봇(SO-100 등)에서 바로 쓸 수 있는 경량화.

## 한계 & 연결
초소형 VLM 백본 특성상 복잡한 오픈월드 언어 추론이나 심한 분포 외(OOD) 시각 변화에서는 대형 모델 대비 취약.
