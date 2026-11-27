---
id: bi-lstm
short: "Bi-LSTM"
title: "Framewise Phoneme Classification with Bidirectional LSTM and Other Neural Network Architectures"
year: 2005
venue: "Graves & Schmidhuber / Neural Networks 2005"
category: "Sequence & Audio"
tags: ["Bidirectional", "Past+Future Context", "Speech", "Sequence Labeling"]
pdf: "논문/Sequence Model/Bi-LSTM.pdf"
predecessors: ["lstm", "lstm-forget-gate"]
successors: ["bert", "transformer"]
---

## 한 줄 요약
정방향(과거→현재)과 역방향(미래→현재) 두 LSTM의 은닉 상태를 결합해, 시점 t의 예측에 앞뒤 전체 문맥을 모두 활용하는 양방향 순환 신경망.

## 핵심 메커니즘
- Forward LSTM과 Backward LSTM이 독립적으로 시퀀스를 훑고 각 시점의 은닉 상태를 concat(또는 합산).
- 음소 분류·개체명 인식처럼 뒤 문맥을 봐야 현재 의미가 확정되는 과제에서 단방향 LSTM을 큰 폭으로 능가.
- Full BPTT로 양방향 오차를 동시에 학습.

## 기존 대비 차이
과거 정보만 보던 단방향 LSTM에 미래 문맥을 통합해 시퀀스 태깅·음성인식 성능을 크게 끌어올림(이후 BERT 양방향 문맥의 전신 격).

## 한계 & 연결
전체 시퀀스가 끝날 때까지 기다려야 역방향 계산이 가능해 실시간 스트리밍에는 부적합하며, 순차 연산 병목은 여전.
