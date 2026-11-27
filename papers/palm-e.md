---
id: palm-e
short: "PaLM-E"
title: "PaLM-E: An Embodied Multimodal Language Model"
year: 2023
venue: "Google / ICML 2023"
category: "VLA"
tags: ["Embodied LLM", "Multimodal", "Planning", "ViT", "Positive Transfer"]
pdf: "논문/VLA/PaLM-E.pdf"
predecessors: ["palm", "vit"]
successors: ["rt-2"]
---

## 한 줄 요약
영상(ViT)과 로봇 상태 벡터를 PaLM 언어 임베딩 공간에 직접 투영해 텍스트·센서 통합 시퀀스로 체화 추론과 상위 계획(Planning)을 수행하는 모델.

## 핵심 메커니즘
- 이미지(ViT/OSRT)와 연속 센서 상태를 선형/MLP 프로젝터로 LLM 토큰 차원에 맞춰 자연어 사이에 삽입.
- 대규모 인터넷 VQA·언어 데이터와 로봇 데이터를 공동 학습해 긍정적 전이(positive transfer) 유도.
- PaLM-E는 자연어로 고수준 하위 작업(subtask)을 생성하고 별도 저수준 정책(예: RT-1)이 실행.

## 기존 대비 차이
언어만 다루던 PaLM에 연속 센서 모달리티를 네이티브 토큰으로 결합해, 멀티모달 VQA와 로봇 태스크 플래닝을 한 모델로 통합.

## 한계 & 연결
저수준 로봇 제어 행동을 직접 출력하지 못하고 외부 정책에 의존 → **RT-2**가 액션 토큰 직접 출력으로 해결.
