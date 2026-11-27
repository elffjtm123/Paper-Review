---
id: fast
short: "FAST"
title: "FAST: Efficient Action Tokenization for Vision-Language-Action Models"
year: 2025
venue: "Physical Intelligence / RSS 2025"
category: "VLA"
tags: ["Action Tokenization", "DCT", "BPE", "Autoregressive VLA"]
pdf: "논문/VLA/FAST.pdf"
predecessors: ["openvla", "pi-0"]
successors: ["pi-0-5", "wall-oss"]
---

## 한 줄 요약
고주파 로봇 액션 청크에 DCT(이산 코사인 변환) + BPE 압축을 적용해 자기회귀 VLA의 학습 속도와 정밀도를 획기적으로 개선한 액션 토크나이저.

## 핵심 메커니즘
- 기존 차원·스텝별 단순 binning은 고주파 데이터에서 인접 스텝 간 강한 상관관계 때문에 모델이 '이전 값 복사'만 배우는 병목 발생.
- 액션 청크를 DCT 주파수 영역으로 변환해 희소화(양자화)한 뒤 BPE로 가변 길이 압축 토큰 시퀀스 생성.
- 동일 액션 청크를 기존 대비 최대 10배 적은 토큰으로 표현하고, 범용 토크나이저 FAST+ 제공.

## 기존 대비 차이
Flow Matching(π0) 없이도 순수 자기회귀 VLA(π0-FAST)가 π0급 정밀 조작 성능을 내면서 학습 수렴은 최대 5배 빨라짐.

## 한계 & 연결
추론 시 자기회귀 디코딩 자체가 느려 실시간 50Hz 제어에서는 Flow Matching 헤드보다 불리 → **π0.5**에서 FAST(사전학습) + Flow(추론)로 하이브리드 결합.
