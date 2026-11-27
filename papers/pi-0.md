---
id: pi-0
short: "Pi-0"
title: "π0: A Vision-Language-Action Flow Model for General Robot Control"
year: 2024
venue: "Physical Intelligence / RSS 2025"
category: "VLA"
tags: ["VLA", "Flow Matching", "Action Expert", "50Hz", "Dexterous"]
pdf: "논문/VLA/Pi-0.pdf"
predecessors: ["rt-2", "openvla", "flow-matching", "siglip"]
successors: ["pi-0-5", "fast", "smolvla", "groot-n1"]
---

## 한 줄 요약
사전학습 VLM(PaliGemma)에 별도 Action Expert를 결합해 Conditional Flow Matching으로 50Hz 연속 정밀 로봇 행동을 생성하는 범용 VLA.

## 핵심 메커니즘
- VLM 백본과 별도 가중치의 Action Expert가 Attention을 공유하는 Mixture-of-Experts(Transfusion 유사) 구조.
- Flow Matching으로 50-step 연속 액션 청크를 10회 적분 스텝 만에 생성해 빨래 개기·박스 조립 같은 고난도 조작 구현.
- 대규모 다기종 사전학습 + 고품질 태스크별 사후학습(post-training) 2단계 파이프라인.

## 기존 대비 차이
이산 토큰 VLA(RT-2, OpenVLA)의 정밀도·주파수 병목을 Flow Matching 연속 액션 청크로 돌파한 현대 VLA 표준 아키텍처.

## 한계 & 연결
고수준 다단계 계획과 미지 가정환경 일반화는 **π0.5**로 확장. (Heart-Lab LIBERO-Plus 실험에서 카메라·센서 노이즈 교란에 민감함을 확인)
