---
id: openvla-oft
short: "OpenVLA-OFT"
title: "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"
year: 2025
venue: "Stanford / RSS 2025"
category: "VLA"
tags: ["Parallel Decoding", "Action Chunking", "Continuous Action", "FiLM"]
pdf: "논문/VLA/OpenVLA-OFT.pdf"
predecessors: ["openvla", "act"]
successors: ["libero-plus", "stablevla"]
---

## 한 줄 요약
OpenVLA에 병렬 디코딩·액션 청킹·연속 L1 회귀·FiLM 언어 조건화를 적용해 추론 속도를 25배+ 높이고 성공률을 대폭 끌어올린 미세조정 레시피.

## 핵심 메커니즘
- 자기회귀 1토큰 생성 대신 빈 토큰을 한 번에 넣는 Parallel Decoding + Action Chunking으로 제어 주기 급상승.
- 256-bin 이산 분류 대신 연속 액션 헤드(L1 loss)로 양자화 오차 제거.
- 다중 시점(손목 카메라)·고유수용감각 입력과 FiLM 기반 언어-시각 결합 추가.

## 기존 대비 차이
기존 OpenVLA의 아키텍처 백본은 유지하면서도 미세조정·디코딩 방식만 바꿔 π0급 LIBERO 성능과 고속 제어를 달성.

## 한계 & 연결
단순 L1 회귀는 다봉 분포 표현이 약하고, CVPR'26 LIBERO-Plus의 시각 교란 환경에서는 강건성 한계가 드러나 혼합 데이터 재학습(OFT+)이 필요.
