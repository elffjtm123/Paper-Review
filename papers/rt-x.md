---
id: rt-x
short: "RT-X (OXE)"
title: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models"
year: 2023
venue: "OXE Collaboration / ICRA 2024"
category: "VLA"
tags: ["Cross-Embodiment", "Dataset", "Scaling", "VLA"]
pdf: "논문/VLA/RT-X.pdf"
predecessors: ["rt-1", "rt-2"]
successors: ["octo", "openvla", "pi-0"]
---

## 한 줄 요약
22종 로봇·60개 데이터셋·100만+ 궤적을 통합한 Open X-Embodiment(OXE) 데이터셋과, 다기종 공동 학습의 긍정적 전이를 입증한 RT-1-X / RT-2-X.

## 핵심 메커니즘
- 서로 다른 로봇의 관측·행동을 표준 포맷(RLDS, 7DoF EEF 델타 등)으로 통일해 단일 데이터셋화.
- RT-1-X(35M)와 RT-2-X(55B)를 다기종 데이터로 학습해 단일 로봇 대비 성공률 향상 검증.
- 로봇 형태가 달라도 타 로봇의 스킬·물체 상호작용 지식이 창발적으로 전이됨을 확인.

## 기존 대비 차이
단일 로봇 플랫폼에 갇혀 있던 RT-1/RT-2를 다기종(cross-embodiment) 패러다임으로 확장해 이후 Octo·OpenVLA·π0의 표준 사전학습 기반을 만듦.

## 한계 & 연결
데이터셋 간 카메라 시점·제어 주파수·좌표계 이질성이 크며, 단순 혼합 시 소규모/고품질 도메인 성능이 희석될 수 있음.
