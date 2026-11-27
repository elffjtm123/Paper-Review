---
id: wavenet
short: "WaveNet"
title: "WaveNet: A Generative Model for Raw Audio"
year: 2016
venue: "van den Oord et al. (DeepMind) / 2016"
category: "Sequence & Audio"
tags: ["Dilated Causal Conv", "Raw Audio", "Autoregressive", "Gated Activation"]
pdf: "논문/Audio & Speech/WaveNet.pdf"
predecessors: ["resnet"]
successors: ["transformer"]
---

## 한 줄 요약
Dilated Causal Convolution으로 RNN 없이도 광범위한 시간 수용야를 확보해, 원시 오디오 파형을 샘플 단위로 자기회귀 생성해 TTS 자연스러움을 혁신한 모델.

## 핵심 메커니즘
- Causal Conv로 미래 시점 누수를 차단하고, dilation(1, 2, 4, 8...)을 지수 확장해 적은 층으로 수천 샘플의 수용야 확보.
- Gated Activation(tanh ⊙ sigmoid) + Residual + Skip Connections로 깊은 파형 생성 안정화.
- μ-law 256구간 양자화 소프트맥스로 연속 오디오 파형의 다봉 분포를 정교하게 모델링.

## 기존 대비 차이
기존 연결/파라메트릭 TTS의 부자연스러움을 딥러닝 원시 파형 직접 생성으로 돌파하고, 시계열에 Dilated Causal Conv(TCN) 패러다임을 전파.

## 한계 & 연결
학습은 병렬이지만 추론은 초당 16,000샘플을 하나씩 자기회귀 생성해야 해 매우 느림(이후 Parallel WaveNet 증류로 해결).
