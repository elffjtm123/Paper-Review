---
id: lstm-forget-gate
short: "LSTM + Forget Gate"
title: "Learning to Forget: Continual Prediction with LSTM"
year: 2000
venue: "Gers, Schmidhuber & Cummins / Neural Computation 2000"
category: "Sequence & Audio"
tags: ["Forget Gate", "Continual Sequence", "Modern LSTM"]
pdf: "논문/Sequence Model/LSTM_with_ForgetGate.pdf"
predecessors: ["lstm"]
successors: ["gru", "bi-lstm"]
---

## 한 줄 요약
원조 LSTM에 이전 셀 상태를 선택적으로 지우는 Forget Gate(f_t)를 추가해, 끝없는 연속 시계열에서 내부 상태를 스스로 리셋할 수 있게 완성한 현대 표준 LSTM.

## 핵심 메커니즘
- c_t = f_t ⊙ c_{t-1} + i_t ⊙ g_t : Forget Gate f_t ∈ (0,1)가 과거 기억의 유지 비율을 동적으로 결정.
- 학습 초기에는 기억을 유지하도록 Forget Gate 편향(bias)을 양수로 초기화하는 실전 팁 제시.
- 외부 리셋 신호 없이도 시퀀스 경계를 스스로 감지해 내부 상태를 초기화.

## 기존 대비 차이
1997년 원조 LSTM이 셀 값을 지우지 못해 연속(continual) 시계열에서 발산·포화하던 결함을 해결해 오늘날 우리가 쓰는 LSTM 공식을 확립.

## 한계 & 연결
게이트 3개(i, f, o)와 두 상태(c, h) 구조로 파라미터·연산이 무거움 → 단순화한 **GRU**, 병렬화 가능한 **Transformer**로 이어짐.
