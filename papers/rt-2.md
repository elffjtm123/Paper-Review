---
id: rt-2
short: "RT-2"
title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
year: 2023
venue: "Google DeepMind / CoRL 2023"
category: "VLA"
tags: ["VLA", "Co-fine-tuning", "Action Tokenization", "Emergent Reasoning"]
pdf: "논문/VLA/RT-2.pdf"
predecessors: ["rt-1", "palm-e"]
successors: ["rt-x", "openvla", "pi-0"]
---

## 한 줄 요약
사전학습 VLM(PaLI-X, PaLM-E)의 출력 텍스트 토큰 일부를 로봇 행동 토큰으로 재정의해 웹 지식을 로봇 제어로 직접 전이한 최초의 VLA.

## 핵심 메커니즘
- 연속 로봇 행동을 256구간 이산 문자열 토큰으로 표현해 VLM의 기존 어휘 공간 안에서 바로 예측.
- 웹 VQA 데이터와 로봇 궤적 데이터를 공동 미세조정(co-fine-tuning)해 VLM의 의미 추론 능력 보존.
- Chain-of-Thought 방식의 중간 추론 후 행동 출력까지 확장 가능.

## 기존 대비 차이
RT-1은 웹 사전학습이 없었고 PaLM-E는 상위 계획만 냈지만, RT-2는 VLM이 직접 저수준 로봇 액션을 출력하며 '멸종한 동물 집기' 같은 창발적 일반화를 달성.

## 한계 & 연결
비공개 초대형 VLM(55B) 기반으로 추론 속도가 느리고(1~3Hz) 폐쇄형 → 오픈소스 **OpenVLA**와 고속 연속제어 **π0**로 발전.
