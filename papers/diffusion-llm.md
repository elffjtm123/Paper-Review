---
id: diffusion-llm
short: "LLaDA (Diffusion LLM)"
title: "Large Language Diffusion Models (LLaDA)"
year: 2025
venue: "Renmin Univ. / Ant Group / arXiv:2502.09992"
category: "Transformer & LLM"
tags: ["Masked Diffusion", "Non-Autoregressive", "Bidirectional LLM", "8B"]
pdf: "논문/Transformer & LLM/Diffusion LLM.pdf"
predecessors: ["ddpm", "bert", "llama"]
successors: []
---

## 한 줄 요약
자기회귀(ARM) 없이 Masked Diffusion만으로 8B LLM을 처음부터 사전학습·SFT해 Llama 3 8B급 성능과 역방향 추론 우위를 보인 확산 언어모델.

## 핵심 메커니즘
- Forward: 시퀀스 토큰을 비율 t∈[0,1]로 무작위 마스킹; Reverse: 양방향 Transformer가 마스킹된 토큰을 반복 예측·언마스킹.
- 자기회귀의 왼쪽→오른쪽 제약이 없는 양방향 모델이라 'Reversal Curse(역방향 시 구절 회상 실패)'를 자연스럽게 극복.
- 생성 가능 우도 하한을 직접 최적화하며 2.3T 토큰 규모에서 LLM 스케일링·ICL·지시 따르기 입증.

## 기존 대비 차이
BERT형 마스크 예측을 연속 비율 확산 프레임워크로 확장해, LLM의 핵심 능력(스케일링·대화·추론)이 자기회귀만의 전유물이 아님을 증명.

## 한계 & 연결
KV-Cache를 그대로 쓰기 어려워 추론 속도·가변 길이 생성 최적화가 진행 중(이후 Discrete Diffusion VLA로도 아이디어 확산).
