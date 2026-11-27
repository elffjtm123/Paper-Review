---
id: gru
short: "GRU"
title: "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation"
year: 2014
venue: "Cho et al. / EMNLP 2014"
category: "Sequence & Audio"
tags: ["Gated RNN", "Update Gate", "Reset Gate", "Lightweight"]
pdf: "논문/Sequence Model/GRU.pdf"
predecessors: ["lstm", "lstm-forget-gate"]
successors: ["transformer"]
---

## 한 줄 요약
LSTM의 셀/은닉 상태를 하나로 합치고 게이트를 2개(Update, Reset)로 줄여, 비슷한 성능을 유지하면서 파라미터와 연산을 간소화한 게이트 순환 유닛.

## 핵심 메커니즘
- Update Gate(z_t): LSTM의 Forget + Input 게이트를 (1-z_t)·h_{t-1} + z_t·h̃_t 로 단일화해 기억 유지·갱신 비율을 동시 제어.
- Reset Gate(r_t): 새로운 후보 상태를 만들 때 과거 정보를 얼마나 무시할지 결정.
- 별도 Cell State와 Output Gate를 없애 파라미터 수 약 25% 절감.

## 기존 대비 차이
LSTM보다 단순하고 소규모 데이터·빠른 학습에서 유리한 경우가 많으며, Seq2Seq 인코더-디코더 프레임워크를 함께 제시.

## 한계 & 연결
초장거리 의존성·복잡한 카운팅에서는 LSTM보다 살짝 약할 수 있고, RNN 고유의 순차 병목 때문에 Transformer에 대체됨.
