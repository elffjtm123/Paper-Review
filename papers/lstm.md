---
id: lstm
short: "LSTM"
title: "Long Short-Term Memory"
year: 1997
venue: "Hochreiter & Schmidhuber / Neural Computation 1997"
category: "Sequence & Audio"
tags: ["RNN", "Cell State", "Constant Error Carousel", "Vanishing Gradient"]
pdf: "논문/Sequence Model/LSTM.pdf"
predecessors: []
successors: ["lstm-forget-gate", "bi-lstm", "gru", "transformer"]
---

## 한 줄 요약
선형 덧셈 경로인 Cell State(CEC)와 Input/Output 게이트를 도입해 기존 RNN의 기울기 소실·폭발을 막고 장거리 시퀀스 기억을 가능케 한 순환망.

## 핵심 메커니즘
- Constant Error Carousel(CEC): 셀 상태가 가중치 곱셈 없이 덧셈으로 흘러 역전파 시 오차가 감쇠 없이 장거리 전달.
- Input Gate가 불필요한 입력 유입을 차단하고, Output Gate가 내부 기억의 외부 노출을 제어.
- 1,000스텝 이상의 지연 시간 과제에서도 기존 RNN이 못 풀던 패턴을 학습.

## 기존 대비 차이
단순 RNN이 매 스텝 tanh·가중치 행렬을 반복 곱하며 기억이 급격히 사라지던 문제를 선형 셀 상태 + 게이트로 해결.

## 한계 & 연결
원조 1997 LSTM에는 오래된 기억을 비우는 Forget Gate가 없어 연속 스트림에서 셀 상태가 무한 누적될 위험 → **LSTM with Forget Gate (2000)**로 완성.
